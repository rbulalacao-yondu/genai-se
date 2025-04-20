import fetch from 'node-fetch';

/**
 * Fetches user data from a remote API.
 * Always performs a network request – slow & wasteful if
 * called repeatedly with the same userId.
 */
export async function getUserData(userId) {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/users/${userId}`
  );

  if (!response.ok) {
    throw new Error(`Failed to fetch user ${userId}: ${response.status}`);
  }

  return response.json();
}