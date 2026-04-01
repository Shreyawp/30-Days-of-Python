import { useState } from 'react'
import './App.css'
import { Login } from "./components/Login"
import { AuthProvider } from './AuthContext';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <AuthProvider>
        <Login />
      </AuthProvider>
    </>
  )
}

export default App;
