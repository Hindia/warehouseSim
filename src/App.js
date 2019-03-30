import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {

    return (
     <div className="App">
        {
        this.state.items.map(((item, index) =>
          <tr><th key={`${item.id}${index}`}>

                <td>{item.id}</td> <td>{item.itemName}</td>

          </th></tr>
          //<tr><td>{item.itemName}</td></tr>
        ))
        }
      </div>
    );
  }

  constructor(props){
        super(props);
        this.state={
            items:[]
        }
  }
   componentDidMount(){
       fetch('items.json')
    .then(response => {
      return response.json();
    })
    .then(d => {
      this.setState({ items: d });
      console.log("state", this.state.items)
    })
    .catch(error => console.log(error))

    }
}

export default App;
