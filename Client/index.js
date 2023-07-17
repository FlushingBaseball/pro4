import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import './index.css';
import App from './App';
// import reportWebVitals from './reportWebVitals';

// const { createRoot } = ReactDOM
const root = document.getElementById('root')

createRoot(root).render(<BrowserRouter><App /></BrowserRouter>)

// ReactDOM.render(
//   <BrowserRouter>
//     <App />
//   </BrowserRouter>,
//   document.getElementById('root')
// );
