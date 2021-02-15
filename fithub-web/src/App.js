import React from 'react';
import './App.css';

import {ExercisesList, Search} from './exercises'





function App() {
  
  return (
    <div className="App">
      <Search />
        
        <div>
          <ExercisesList />
        </div>
        
    </div>
  );
}

export default App;
