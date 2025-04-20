# Copilot Chat Refactor Demo

This single‑file example (`legacy.js`) contains a deliberately
convoluted callback‑hell function **getUserOrderStatuses**.

## How to demo

1. Open `legacy.js` in VS Code with **GitHub Copilot Chat** enabled.
2. Select the entire body of `getUserOrderStatuses` (lines 15‑55).
3. In the Copilot Chat panel, ask:
   ```
   Refactor this function to use async/await,
   extract helper functions where logical,
   and add proper error handling with try/catch.
   ```
4. Copilot Chat will propose a diff‑style patch or complete new code:
   * Converts nested callbacks into `await` calls.
   * Uses `Promise.all` for parallelisation of shipments.
   * Keeps existing sorting logic but in a cleaner style.
5. Accept the suggestion and show the diff side‑by‑side.

### Pro tip
After accepting, you can follow‑up in chat:
> "Add JSDoc comments and TypeScript‑style typings to the new function."
