import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './pages';
import CreateGame from './pages/CreateGame';
import SignUp from './pages/Signup';

function App() {
return (
	<Router>
	{/* <Navbar /> */}
	<Routes>
		<Route exact path='/' element={<Home />} />
		<Route path='/create-game' element={<CreateGame/>} />
		<Route path='/sign-up' element={<SignUp/>} />
	</Routes>
	</Router>
);
}

export default App;
