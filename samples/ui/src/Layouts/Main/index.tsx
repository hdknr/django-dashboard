import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Top } from '../../Pages';

export const Main: React.FunctionComponent = () => {
    return (
        <div className="App-Main">
            <Router>
                <Route path="" exact component={Top} />
            </Router>
        </div>);
};
