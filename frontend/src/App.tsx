import { useState, useEffect } from 'react'
import { Routes, Route } from 'react-router-dom'
import Home from '@pages/Home'
import About from '@pages/About'
import NoPage from '@pages/NoPage'
import Login from '@pages/Login'
import Register from '@pages/Register'
import '@css/App.css'

function App() {

  const [message, setMessage] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
        fetch("/api/hello")
            .then(res => {
                    if (!res.ok) throw new Error("Network response was not ok")
                    return res.json()
                })
            .then(data => setMessage(data.message))
            .catch(error => {
                    console.error(error)
                    setError("Failed to load data")
                })
      }, []);

  return (
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/about" element={<About />}/>
        <Route path="/login" element={<Login />}/>
        <Route path="/register" element={<Register />}/>
        {/*Route for unknown paths (404 Page)*/}
        <Route path="*" element={<NoPage />}/>
      </Routes>
  )
}

export default App
