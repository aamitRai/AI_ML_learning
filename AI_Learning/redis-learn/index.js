// index.js
import express from "express";
import axios from "axios";
import { createClient } from "redis";

const app = express();
const PORT = 3000;

// Redis client
const redisClient = createClient();
redisClient.on("error", (err) => console.error("Redis Client Error", err));
await redisClient.connect();

// Route: fetch GitHub user
app.get("/user/:username", async (req, res) => {
  const { username } = req.params;

  try {
    // 1. Check Redis cache
    const cached = await redisClient.get(username);
    if (cached) {
      return res.json({ source: "cache", data: JSON.parse(cached) });
    }

    // 2. Fetch from GitHub API
    const response = await axios.get(`https://api.github.com/users/${username}`);

    // 3. Save to Redis with 60 sec expiry
    await redisClient.setEx(username, 60, JSON.stringify(response.data));

    return res.json({ source: "api", data: response.data });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Something went wrong" });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
