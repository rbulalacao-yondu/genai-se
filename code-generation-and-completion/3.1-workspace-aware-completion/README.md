# Copilot Multi‑file Demo

This miniature Express project is **not** meant to run in production.  
It exists solely to demonstrate how GitHub Copilot reads surrounding files to craft context‑aware completions.

## How to use

1. Ensure the **GitHub Copilot** extension and **Copilot Chat** are enabled in VS Code (or your IDE of choice).  
2. Open `routes/project.js`.  
3. Place your cursor on the blank line under the comment and start typing:
   ```js
   router.get('/');
   ```
   – Pause. Copilot should immediately suggest the full asynchronous handler that:
   * Queries `Project.find({})`
   * Wraps with `try/catch`  
   * Mirrors the error response style used in **routes/user.js**
4. Press <kbd>Tab</kbd> to accept, or cycle alternatives with <kbd>Alt</kbd> + <kbd>[</kbd>/<kbd>]</kbd>.
