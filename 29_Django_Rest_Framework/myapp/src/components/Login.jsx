import React, { useContext } from 'react';
import { AuthContext } from '../AuthContext';

export const Login = () => {
    const {user} = useContext(AuthContext)

    return (
        <div>
            <h2>Login</h2>

        </div>
    );
}

export default Login;