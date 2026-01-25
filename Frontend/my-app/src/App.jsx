import './App.css'
import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SubmitGrievance from './pages/SubmitGrievance'

function App() {
  return (
    <Router>
      <div className='App'>
        {/* Navigation here */}
      </div>
      <Routes>
        
        <Route path="/" element={<SubmitGrievance />} />
      </Routes>
    </Router>
  )
}

export default App