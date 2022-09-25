import React, {useState, useEffect} from 'react'
import './App.css';
import MainPage from './MainPage';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";



function App() {
  const [data, setData] = useState({});

  // useEffect(() => {
  //     fetch("/").then(
  //       res => res.json()
  //       ).then(
  //         data => {
  //             setData(data)
  //             console.log(data)
  //         }
  //       )
  // }, []);
  return (
      <div className="App">
        <MainPage/>
      </div>
  );
}

export default App;
