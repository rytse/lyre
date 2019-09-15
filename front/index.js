import React from "react";
import ReactDOM from "react-dom";

var xhr = new XMLHttpRequest();

function Map(props) {
  return (<div id = 'map-pane'> map goes here! </div>);
}

function TranscriptBox(props) {
  return (<div id = 'transcript-box'> transcript </div>);
}

function Alert(props) {
  return (<div id='alert'> {props.title} <button> Action </button> </div> );
}

function AlertStack(props) {
  // console.log(props.serverData);
  const items = props.serverData.map((e) => <li key={e}> <Alert title={e}/> </li>);
  return (<div id = 'alert-stack'> <ul> {items} </ul> </div>);
}

function SwitchForm(props) {
  return (<div id = 'switchform'> switchboard form </div>);
}

function AlertPusher(props) {
  return (<div id = 'alert-pusher'> alert pusher </div>);
}

function TranscriptDetailed(props) {
  return (<div id = 'transcript-detail'> detailed transcript </div>);
}

function AlertEditor(props) {
  return (<div id = 'alert-editor'> alert editor </div>);
}

function Header(props) {
  return (<div id='header'> <h1> Command Center {props.page} </h1>
  <button disabled={props.page=='Home'} onClick={props.onClick} value='Home'> Home </button>
  <button disabled={props.page=='Switchboard'} onClick={props.onClick} value='Switchboard'> Switchboard </button>
  <button disabled={props.page=='Validation'} onClick={props.onClick} value='Validation'> Validation </button>
  <button disabled={props.page=='Analytics'} onClick={props.onClick} value='Analytics'> Analytics </button>
  </div>);
}

function Home(props) {
  // console.log(props.serverData);
  return (<div>
    <Header page='Home' onClick={props.handleNav}/>
    <Map />
    <AlertStack serverData={props.serverData['alerts']} />
    <TranscriptBox />
    </div>
  );
}

function Switchboard(props) {
  return(<div>
    <Header page='Switchboard' onClick={props.handleNav} serverData={props.serverData}/>
    <SwitchForm />
    </div>
  );
}

function Validation(props) {
  return(<div>
    <Header page='Validation' onClick={props.handleNav} serverData={props.serverData}/>
    <AlertPusher />
    <TranscriptDetailed />
    <AlertEditor />
    </div>
  );
}

function Analytics(props) {
  return(<div>
    <Header page='Analytics' onClick={props.handleNav} serverData={props.serverData}/>
    </div>
  );
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {currentPage: 'Home', test: 0, serverData: {'alerts': ['alert1', 'alert2'], 'disasters':['disaster1']}};
    this.switchPage = this.switchPage.bind(this);
    this.setState = this.setState.bind(this);
  }

  switchPage(e) {
    this.setState({currentPage: e.target.value});
  }

  componentDidMount() {
    this.timerID = setInterval(() => this.updateTest(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  updateTest() {
    var setState = this.setState;
    var sData = this.state.serverData;
    fetch('http://localhost:5000/update/')
      .then(function(response) {
        return response.json();
      })
      .then(function(myJson) {
        console.log("asdf");
        console.log(myJson);
        // console.log(typeof(setState));
        setState({serverData: Object.assign({}, myJson)});
      })
      // .catch(function() {console.log("Error")});
      // console.log(this.state.serverData);
   }

  render() {
    // console.log(this.state.serverData);
    switch(this.state.currentPage) {
      case 'Home':
        return (<Home handleNav={this.switchPage} serverData={this.state.serverData}/>);
        break;
      case 'Switchboard':
        return(<Switchboard handleNav={this.switchPage} serverData={this.state.serverData}/>);
        break;
      case 'Validation':
        return(<Validation handleNav={this.switchPage} serverData={this.state.serverData}/>);
        break;
      case 'Analytics':
        return(<Analytics handleNav={this.switchPage} serverData={this.state.serverData}/>);
        break;
      default:
        return (<Home handleNav={this.switchPage} serverData={this.state.serverData}/>);
        break;
    }
  }
}

ReactDOM.render(<App />, document.getElementById('root'));
