import React from "react";
import ReactDOM from "react-dom";

var xhr = new XMLHttpRequest();

class Map extends React.Component {
  render() {
    return (<div id = 'map-pane'> map goes here! </div>);
  }
}

class TranscriptBox extends React.Component {
  render() {
    return (<div id = 'transcript-box'> transcript </div>);
  }
}

class AlertStack extends React.Component {
  constructor(props) {
    super(props);
    this.state = {stack: [0], serverData: props.serverData};
  }

  render() {
    return (<div id = 'alert-stack'> alerts {this.state.stack} {this.state.serverData} </div>);
  }
}

class SwitchForm extends React.Component {
  render() {
    return (<div id = 'switchform'> switchboard form </div>);
  }
}

class AlertPusher extends React.Component {
  render() {
    return (<div id = 'alert-pusher'> alert pusher </div>);
  }
}

class TranscriptDetailed extends React.Component {
  render() {
    return (<div id = 'transcript-detail'> detailed transcript </div>);
  }
}

class AlertEditor extends React.Component {
  render() {
    return (<div id = 'alert-editor'> alert editor </div>);
  }
}

function Header(props) {
  return (<div id='header'> <h1> Command Center {props.page} </h1>
  <button disabled={props.page=='Home'} onClick={props.onClick} value='Home'> Home </button>
  <button disabled={props.page=='Switchboard'} onClick={props.onClick} value='Switchboard'> Switchboard </button>
  <button disabled={props.page=='Validation'} onClick={props.onClick} value='Validation'> Validation </button>
  <button disabled={props.page=='Analytics'} onClick={props.onClick} value='Analytics'> Analytics </button>
  </div>);
}

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.handleNav = props.handleNav;
    this.state = {serverData: props.serverData};
  }

  render() {return (<div>
    <Header page='Home' onClick={this.handleNav}/>
    <Map />
    <AlertStack serverData={this.state.serverData} />
    <TranscriptBox />
    </div>
  );}
}

class Switchboard extends React.Component {
  constructor(props) {
    super(props);
    this.handleNav = props.handleNav;
  }

  render() {return(<div>
    <Header page='Switchboard' onClick={this.handleNav}/>
    <SwitchForm />
    </div>
  );}
}

class Validation extends React.Component {
  constructor(props) {
    super(props);
    this.handleNav = props.handleNav;
  }

  render() {return(<div>
    <Header page='Validation' onClick={this.handleNav}/>
    <AlertPusher />
    <TranscriptDetailed />
    <AlertEditor />
    </div>
  );}
}

class Analytics extends React.Component {
  constructor(props) {
    super(props);
    this.handleNav = props.handleNav;
  }

  render() {return(<div>
    <Header page='Analytics' onClick={this.handleNav}/>
    </div>
  );}
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {currentPage: 'Home', test: 0, alertNum: 0};
    this.switchPage = this.switchPage.bind(this);
    this.handleGetReq = this.handleGetReq.bind(this);
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
    fetch('http://localhost:5000/update/')
          .then(function(response) {
                  return response.json();

          })
          .then(function(myJson) {
                  console.log(JSON.stringify(myJson));

          });
   }

  render() {
    switch(this.state.currentPage) {
      case 'Home':
        return (<Home handleNav={this.switchPage} serverData={this.state.alertNum}/>);
        break;
      case 'Switchboard':
        return(<Switchboard handleNav={this.switchPage}/>);
        break;
      case 'Validation':
        return(<Validation handleNav={this.switchPage}/>);
        break;
      case 'Analytics':
        return(<Analytics handleNav={this.switchPage}/>);
        break;
      default:
        return (<Home handleNav={this.switchPage}/>);
        break;
    }
  }

  handleGetReq() {
    if (xhr.readyState == 4 && xhr.status == 200) {
        this.setState({alertNum: xhr.response});
    }
  }
}



ReactDOM.render(<App />, document.getElementById('root'));
