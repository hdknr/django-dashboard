import React from 'react';
import { ApolloProvider } from '@apollo/react-hooks';
import { client } from '../graphql/client'
import { Header, Main } from '../Layouts';
import { BrowserRouter as Router } from 'react-router-dom';
import './index.css';
import './App.css';


const App: React.FunctionComponent = () => {
  return (
    <div className="App">
      <ApolloProvider client={ client }>
        <Router>
          <Header />
          <Main />
        </Router>
      </ApolloProvider>
    </div >
  );
}

export default App;
