import { StrictMode } from 'react' // Change this
import { createRoot } from 'react-dom/client' // Modern way to import createRoot
import App from './App.jsx'
import './index.css'

// Use the imported named functions directly
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)