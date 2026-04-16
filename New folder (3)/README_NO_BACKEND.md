# Chess Game - No Backend Version

A **pure HTML/JavaScript chess game** that runs entirely in the browser with no server required!

## Files

- `index.html` - Single-player chess game (AI opponent)
- `multiplayer.html` - Multiplayer chess game (play with friends)
- Uses `chess.js` library from CDN for game logic

## How to Use

### Option 1: Open Locally
1. Double-click any `.html` file in your file explorer
2. Or open it in your browser: `file:///path/to/file.html`

### Option 2: Host on Netlify (FREE)
1. Go to **netlify.com** → Sign up
2. Drag & drop your `.html` files into Netlify
3. Done! Your games are live at `https://your-site.netlify.app`

### Option 3: Host Anywhere
- Upload `.html` files to any web hosting service
- No special configuration needed
- Works on any static hosting (GitHub Pages, Vercel, etc.)

## 🎮 Game Modes

### Single Player (`index.html`)
- Play against AI with random moves
- Perfect for practicing chess

### Local Multiplayer (`multiplayer.html`)
- Play with someone on the same device
- Take turns clicking moves
- Great for learning with friends/family

### Online Multiplayer (`multiplayer.html`)
- Play with friends on different devices
- Real-time connection using WebRTC
- No server required!

## 🎯 How to Play with Friends Online

### Step-by-Step Guide:

1. **Both players open `multiplayer.html`** in their browsers

2. **Player 1 (Host) creates a room:**
   - Select "Online Multiplayer" mode
   - Click "Create Room"
   - A room code will be generated (e.g., "A1B2C3")
   - Tell your friend the room code

3. **Player 2 (Join) connects:**
   - Select "Online Multiplayer" mode
   - Enter the room code from Player 1
   - Click "Join Room"

4. **Exchange connection info:**
   - Player 1 will see a popup with connection offer
   - Copy the offer text and send it to Player 2
   - Player 2 pastes the offer and clicks OK
   - Player 2 will get an answer - copy and send back to Player 1
   - Player 1 pastes the answer

5. **Start playing!**
   - Connection status will show "Connected! Game ready"
   - Take turns making moves
   - The game automatically switches turns

### Alternative: Share Direct Link
- After creating a room, click "Copy Game Link"
- Send the link to your friend
- They can join directly without entering the room code

## Features

- ✅ **No backend required** - runs entirely in browser
- ✅ **Multiple game modes** - AI, local, online multiplayer
- ✅ **Real-time online play** - WebRTC peer-to-peer connection
- ✅ **Move validation** - only legal moves allowed
- ✅ **Visual feedback** - green dots for moves, red for captures
- ✅ **Game over detection** - checkmate, stalemate, etc.
- ✅ **Beautiful UI** - responsive design with Unicode pieces
- ✅ **Offline playable** - works without internet (except for chess.js CDN)

## How It Works

- **chess.js** handles all game logic (moves, validation, AI)
- **JavaScript** manages the UI and user interactions
- **WebRTC** enables direct browser-to-browser communication for online play
- **No server** - everything runs client-side

## Browser Compatibility

Works in all modern browsers:
- Chrome, Firefox, Safari, Edge
- Mobile browsers (iOS Safari, Chrome Mobile)
- Requires JavaScript and WebRTC support

## Troubleshooting

### Pieces not showing?
- Ensure internet connection for chess.js CDN
- Or download chess.js locally and update the script tag

### Online multiplayer not connecting?
- Make sure both players are using modern browsers
- Check that you're copying/pasting the connection info correctly
- Try refreshing and creating a new room
- WebRTC requires both players to be online simultaneously

### Game not loading?
- Check browser console for errors (F12)
- Make sure JavaScript is enabled

### Mobile issues?
- The game is responsive but touch controls may need adjustment

## Why No Backend?

**Advantages:**
- ✅ Instant loading
- ✅ No hosting costs
- ✅ Works offline
- ✅ No server maintenance
- ✅ Easy to share (single file)
- ✅ Direct peer-to-peer connection

**Limitations:**
- ❌ No game saving
- ❌ No advanced AI
- ❌ No user accounts
- ❌ No statistics
- ❌ Online play requires manual connection setup

## Next Steps

If you want advanced features like:
- Automatic matchmaking
- Game saving
- Better AI
- User accounts
- Chat during games

Then you'd need to add a backend server (see `NETLIFY_DEPLOYMENT.md` for full-stack version).

## License

Free to use and modify! 🎉