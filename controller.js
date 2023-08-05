import express from "express";
import http from "http";

// For new version
import { Server } from "socket.io";

const app = express();
const server = http.createServer(app);

// For new version
const io = new Server(server);

// Create io with namespace robot
const robotio = io.of("/js");
// Initialize listeners
robotio.on("connection", (socket) => {
  console.log("js connected");

  socket.on("pulse", () => {
    console.log("js Pulse");
  });

  socket.on("disconnect", () => {
    console.log("js disconnected");
  });
});

// Create io with namespace "py"
const cameraio = io.of("/py");
// Initialize listeners
cameraio.on("connection", (socket) => {
  console.log("py connected");

  socket.on("pulse", () => {
    console.log("py pulse");
  });

  socket.on("disconnect", () => {
    console.log("py disconnected");
  });
});

server.listen(3000, () => {
  console.log("listening on *:3000");
});
