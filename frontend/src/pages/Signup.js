import React, { useState } from 'react';
import "./SignUp.css";


const SignUp = ({showPopup, handleClose, handleSignup}) => {
    const [username, setUsername] = useState('');
    const [statusText, setStatusText] = useState('');
    const [signupSuccessful, setSignupSuccessful] = useState(false);

    const handleUsernameChange = (event) => {
        setUsername(event.target.value);
    }

    const handleSubmit = (event) => {
        console.log(signupSuccessful);
        event.preventDefault();
        if (!signupSuccessful){
            handleSignup(username);

            const requestOptions = {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    name: username
                }),
            };
            fetch('/signup', requestOptions)
            .then(response => response.json())
            .then(res => {
                console.log(res);
                setStatusText(res["message"]);
                if (res["isError"] === false){
                    setSignupSuccessful(true);
                } else {
                    setSignupSuccessful(false);
                }
            })
        }

        // handleClose();
    }

    return (
        <>
            {showPopup && (
            <div className="popup">
                <div className="popup-inner">
                <h2>Sign Up</h2>
                <form onSubmit={handleSubmit}>
                    <label>
                    Username:
                    <input type="text" value={username} onChange={handleUsernameChange} />
                    </label>
                    <p>{statusText}</p>
                    <button type="submit">Sign Up</button>
                </form>
                <button onClick={handleClose}>Close</button>
                </div>
            </div>
            )}
        </>
    );

}

export default SignUp;
