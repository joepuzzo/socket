#!/bin/bash

set -e

CONTROLLER="js"  # Default controller

# Parse command line arguments
for arg in "$@"; do
  case $arg in
    --controller=py)
      CONTROLLER="py"
      shift
      ;;
    --controller=js)
      CONTROLLER="js"
      shift
      ;;
  esac
done

echo "Starting $CONTROLLER controller..."

if [ "$CONTROLLER" == "py" ]; then
  npm run start-py-controller &
else
  npm run start-js-controller &
fi
PID1=$!

echo "Starting JS client..."
npm run start-js-client &
PID2=$!

echo "Starting Python client..."
npm run start-py-client &
PID3=$!

# Define a function to kill all the processes when this script exits
cleanup() {
  echo "Cleaning up..."
  kill $PID1 $PID2 $PID3 2>/dev/null
}

# Call the cleanup function when the script exits
trap cleanup EXIT

# Wait for all processes to finish
wait $PID1 $PID2 $PID3
