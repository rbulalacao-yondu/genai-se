app.post('/login', async (req, res) => {
    const { user, pass } = req.body;
    const result = await db.query(
      `SELECT * FROM accounts WHERE user = '${user}' AND pass = '${pass}'`
    );
    …
  });