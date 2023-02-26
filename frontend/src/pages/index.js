import React, { useState } from 'react';
import SignUp from './Signup';

const Home = () => {
    const [showPopup, setShowPopup] = useState(false);
    const [username, setUsername] = useState('');

    const updateUsername = (newUsername) => {
        setUsername(newUsername);
    }

    return (
        <div>
            <h1>Home</h1>
            <button onClick={() => setShowPopup(true)}>Open Popup</button>
            <SignUp
                showPopup={showPopup}
                handleClose={() => setShowPopup(false)}
                handleSignup={updateUsername}
            />
            {username && <p>Username: {username}</p>}
        </div>
);
};

export default Home;
