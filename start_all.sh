#!/bin/bash
# Kill any existing processes
pkill -f "vite" 2>/dev/null
pkill -f "uvicorn" 2>/dev/null
pkill -f "docker-java-app" 2>/dev/null
pkill -f "cloudflared" 2>/dev/null
pkill -f "ngrok" 2>/dev/null
sleep 2

# Re-download cloudflared if missing from /tmp
if [ ! -f /tmp/cloudflared ]; then
  echo "Downloading cloudflared..."
  curl -sL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o /tmp/cloudflared
  chmod +x /tmp/cloudflared
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

# Start Cloudflare tunnel (for mysymptoms.info)
echo "Starting Cloudflare tunnel for mysymptoms.info..."
nohup /tmp/cloudflared tunnel --config /home/titi/.cloudflared/config.yml run mysymptoms > /tmp/cf-tunnel.log 2>&1 &
sleep 5

# Check if tunnel connected
if grep -q "Registered tunnel connection" /tmp/cf-tunnel.log 2>/dev/null; then
  echo ""
  echo "==============================="
  echo "LIVE AT: https://mysymptoms.info"
  echo "==============================="
else
  echo ""
  echo "WARNING: Cloudflare tunnel failed to connect."
  echo "Try again or check logs: cat /tmp/cf-tunnel.log"
fi
