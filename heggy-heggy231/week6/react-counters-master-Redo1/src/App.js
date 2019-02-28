import React, { Component } from "react";
import Header from "./Header";
// get my CounterList access
import CounterList from "./CounterList";

class App extends Component {

  state = {
    counter: 0,
  }

  increaseCount = () => {
    let counter = this.state.counter + 1;

    this.setState({
      counter
    });
  }

  decreaseCount = () => {
    let counter = this.state.counter -1;

    this.setState({
      counter
    });
  }

  render() {
    return (
      <div className="App">
        <Header 
        increaseFunction = {
  // presentational components (header b/c it has no state) behavior by passing callback functions (this.increaseCount) to header as props
          this.increaseCount
        } 

        decreaseFunction = {
  // presentational components (header b/c it has no state) behavior by passing callback functions (this.increaseCount) to header as props
          this.decreaseCount
        }
        />
        {/* passing 5 to counterList */}
        <CounterList appdata =
        // put into obj with key value counters: 5  
        {
          {appCounters: this.state.counter}
        } />

      </div>
    );
  }
}

// remember to export making it public
export default App;