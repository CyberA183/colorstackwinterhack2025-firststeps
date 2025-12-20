import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
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
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        {error && <p style={{ color: "red" }}>{error}</p>}
        {!error && (message ? <p>{message}</p> : <p>Loading data...</p>)}

        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
