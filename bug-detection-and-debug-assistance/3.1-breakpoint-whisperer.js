// loop_demo.js
function processTotals(totals) {
    for (let i = 0; i < totals.length; i++) {
      const t = totals[i];
      // imagine we only want to pause when t < 0
      console.log(`Index ${i}:`, t);
    }
  }
  
  processTotals([5, 2, -3, 8, -1, 7]);