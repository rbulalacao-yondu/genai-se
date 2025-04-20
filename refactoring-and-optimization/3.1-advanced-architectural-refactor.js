import { Router } from 'express';
import { Pool } from 'mysql2/promise';
import { body, param, validationResult } from 'express-validator';

const router = Router();
const db: Pool = /* … createConnection … */;

/* GET /orders/:id */
router.get(
  '/:id',
  param('id').isInt().withMessage('ID must be numeric'),
  async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    try {
      const [rows] = await db.query(
        'SELECT * FROM orders WHERE id = ?',
        [req.params.id]
      );
      if (!rows.length) return res.status(404).send('Not found');
      res.json(rows[0]);
    } catch (err) {
      console.error(err);
      res.status(500).send('DB error');
    }
  }
);

/* POST /orders */

router.post(
  '/',
  body('customerId').isInt(),
  body('items').isArray({ min: 1 }),
  body('total').isFloat({ gt: 0 }),
  async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) return res.status(400).json({ errors: errors.array() });

    const { customerId, items, total } = req.body;
    const conn = await db.getConnection();
    await conn.beginTransaction();
    try {
      const [result] = await conn.query(
        'INSERT INTO orders (customer_id,total) VALUES (?,?)',
        [customerId, total]
      );
      const orderId = (result as any).insertId;

      for (const item of items) {
        await conn.query(
          'INSERT INTO order_items (order_id,product_id,qty,price) VALUES (?,?,?,?)',
          [orderId, item.productId, item.qty, item.price]
        );
      }

      await conn.commit();
      res.status(201).json({ id: orderId });
    } catch (e) {
      await conn.rollback();
      console.error(e);
      res.status(500).send('DB error');
    } finally {
      conn.release();
    }
  }
);

export default router;
