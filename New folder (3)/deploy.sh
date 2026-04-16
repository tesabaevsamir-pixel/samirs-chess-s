#!/bin/bash
# Deploy to Netlify
# Make sure you have netlify-cli installed: npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy the frontend
netlify deploy --prod --dir=. --functions=functions
