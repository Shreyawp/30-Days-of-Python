import { createContext } from 'react';

export const AuthContext = createContext(null);

export const AuthProvider = ({children}) => {
    const [user, setuser] = useState(null);

    const login = async (username, password) => {
        try {
            const reponse = await fetch('http://localhost:8000/auth/token/login/', {
                method: "POST",
                headers: {
                    'Context-Type': 'application/json',
                },
                body: JSON.stringify({username, password})
            })

            if (!response.ok) {
                throw new Error('Login Failed');
            }

            const data = await response.json();
            console.log(data)
        } catch (error) {
            console.error('Login failed', error);
            return false;
        }
    }

    return (
        <AuthContext.Provider value={{user}}>
            {children}
        </AuthContext.Provider>
    )
}