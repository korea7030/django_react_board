import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from "mobx-react";
import rootStore from "../src/stores/rootStore";

// import './index.css';
import App from './App';

ReactDOM.render(
    <Provider {...rootStore} >
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </Provider>, 
    document.getElementById('root')
  
);