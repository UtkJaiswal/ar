import http.server
import socketserver
import os

# --- Configuration ---
# Get the port from the environment variable provided by the deployment platform (e.g., Render, Heroku).
# Default to 8000 for local development if the PORT variable isn't set.
PORT = int(os.environ.get('PORT', 8000))

# --- Server Setup ---

# This handler will serve files from the directory it's run from.
Handler = http.server.SimpleHTTPRequestHandler

# --- Create and Run the Server ---
# We create a standard TCPServer. The deployment platform will handle HTTPS.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("=====================================================================")
    print(f"  HTTP server starting on port: {PORT}")
    print("  This server is ready for deployment on a platform that handles SSL.")
    print("=====================================================================")

    try:
        # Start the server and keep it running.
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        pass