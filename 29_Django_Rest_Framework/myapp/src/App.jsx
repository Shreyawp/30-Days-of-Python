import { useState } from 'react'
import './App.css'
import { AuthProvider } from './AuthContext';
import { Login } from "./components/Login";
import { Dashboard } from "./components/Dashboard";
import { BrowserRouter, Routes, Route, Link } from "react-router";

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <AuthProvider>
        <BrowserRouter>

        <Link to='/login'>Login</Link>
        <Link to='/dashboard'>Dashboard</Link>

          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </>
  )
}

export default App;
