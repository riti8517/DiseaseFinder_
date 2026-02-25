#!/bin/bash
# Kill any existing processes
pkill -f "vite" 2>/dev/null
pkill -f "uvicorn" 2>/dev/null
pkill -f "docker-java-app" 2>/dev/null
pkill -f "ngrok" 2>/dev/null
sleep 2

# Re-download ngrok if missing
if [ ! -f /tmp/ngrok ]; then
  echo "Downloading ngrok..."
  curl -sL https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz -o /tmp/ngrok.tgz
  tar -xzf /tmp/ngrok.tgz -C /tmp
fi

# Start servers
echo "Starting Java backend..."
java -jar /home/titi/workingdir3/DiseaseFinder_/web_backend/target/docker-java-app-symptomfinder.jar > /tmp/java-backend.log 2>&1 &

echo "Starting Python backend..."
cd /home/titi/workingdir3/DiseaseFinder_/web_frontend/web_frontend/src/backend
uvicorn main:app --reload --port 8000 > /tmp/python-backend.log 2>&1 &

echo "Starting Vite frontend..."
cd /home/titi/workingdir3/DiseaseFinder_/web_frontend/web_frontend
npx vite --host 0.0.0.0 --port 5173 > /tmp/vite.log 2>&1 &

echo "Waiting for servers to start..."
sleep 6

# Start ngrok
echo "Starting ngrok tunnel..."
/tmp/ngrok http 5173 > /tmp/ngrok.log 2>&1 &
sleep 6

# Print the public URL
echo ""
echo "==============================="
PUBLIC_URL=$(curl -s http://localhost:4040/api/tunnels | python3 -c "import json,sys; d=json.load(sys.stdin); print([t['public_url'] for t in d['tunnels'] if 'https' in t['public_url']][0])" 2>/dev/null)
echo "PUBLIC URL: $PUBLIC_URL"
echo "==============================="
echo "Share this link with anyone!"
