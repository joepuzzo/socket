import io from "socket.io-client";

// Create connection to the controller
const controllerConnectionString = `http://localhost:3000/js`;
const controllerSocket = io(controllerConnectionString);

setInterval(() => {
  console.log("js sending pulse");
  controllerSocket.emit("pulse");
}, 5000);

controllerSocket.on("connect", () => {
  console.log("js is connected to controller");
});

controllerSocket.on("disconnect", () => {
  console.log("js is disconnected from controller");
});
