/**
 * legacy.js
 *
 * This file simulates a "callback‑hell" style function
 * that fetches user info, then orders, then iterates over
 * each order to fetch shipment status. It mixes error handling,
 * callback nesting, and mutable state — perfect to ask Copilot
 * Chat to refactor into async/await.
 */

const db = require('fake-db'); // assume SDK with callback APIs

function getUserOrderStatuses(userId, callback) {
  db.getUser(userId, function(err, user) {
    if (err) return callback(err);
    if (!user) return callback(new Error('User not found'));

    db.getOrdersForUser(user.id, function(err, orders) {
      if (err) return callback(err);

      let results = [];
      let pending = orders.length;
      if (pending === 0) return callback(null, results);

      orders.forEach(function(order) {
        db.getShipmentStatus(order.shipmentId, function(err, status) {
          if (err) {
            // Continue on error but record it
            results.push({ orderId: order.id, error: err.message });
          } else {
            results.push({ orderId: order.id, status: status });
          }
          pending -= 1;
          if (pending === 0) {
            // Sort by orderId before returning
            results.sort(function(a, b) {
              return a.orderId - b.orderId;
            });
            callback(null, results);
          }
        });
      });
    });
  });
}

module.exports = { getUserOrderStatuses };

// Example invocation for manual testing (uncomment to try)
/*
getUserOrderStatuses(42, function(err, statuses) {
  if (err) {
    console.error('ERROR:', err);
  } else {
    console.log('Order statuses:', statuses);
  }
});
*/
