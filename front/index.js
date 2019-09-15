import React from "react";
import ReactDOM from "react-dom";

var xhr = new XMLHttpRequest();

function Map(props) {
  const cy = 38.975;
  const cx = 77.159;
  const fire = 'https://i7.pngguru.com/preview/751/826/536/black-triangle-computer-icons-symbol-arrow-triangle.jpg';
  const pol = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAS1BMVEUAAP99ff+MjP+bm/+rq/+4uP+2tv+pqf+Kiv+Bgf/Z2f90dP94eP/8/P/z8//k5P/Pz//IyP+ysv+Rkf+Vlf+goP+urv+kpP+Ojv/Q7Co7AAABmUlEQVR4nO3dS04DMRAG4e5kJm8eCUng/ieFBQvEhgip1apxfb7AX0tLlhxPzy+H1/N5nufLNE3b9be31U+7/Lf96k/X9QNu0wPu82+bQ1xi2Y4xdU8olgMUvndPKJax7p5QzEI+C/ks5LOQz0K+EQqv3ROKZay6JxSzkM9CPgv5LOSzkM9CPgv5LOSzkM9CPgv5LOSzkM9CPgv5RijcdU8oll9n2Szks5DPQj4L+Szks5DPQj4L+Szks5DPQj4L+Szks5DPQj4L+Szks5DPQr6MffeEYiO8GFr+qy8L6Szks5DPQj4L+Szks5DPQj4L+Szks5DPQj4L+Szks5DPQj4L+Szks5Av46N7QrER/pmxkM5CPgv5LOSzkM9CPgv5LOSzkM9CPgv5LOSzkM9CPgv5LOSzkG+Ewlv3hGIZ2+4JxTKm7gnFLOSzkM9CPgv5LOSzkM9CPgv5LOSzkM9CPgv5LOSzkM9CPgv5LOTLuHdPKJax6Z5QLGPunlDMQj4L+Szks5DPQj4L+SzkG6Fw6TfgUxyOuWSn+RNFSAfbc4zH5wAAAABJRU5ErkJggg==';
  const guard = 'https://cdn3.iconfinder.com/data/icons/flatastic-10-2/256/trafficlight_green-512.png';
  const dis = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Red_star.svg/2000px-Red_star.svg.png';
  // const fire_locs = [[(props.fire_locs['u1'][x]-cx)/cx, -(props.fire_locs['u1'][y]-cy)/cy],
  //   [(props.fire_locs['u2'][x]-cx)/cx, -(props.fire_locs['u2'][y]-cy)/cy],
  //   [(props.fire_locs['u3'][x]-cx)/cx, -(props.fire_locs['u3'][y]-cy)/cy],
  //   [(props.fire_locs['u4'][x]-cx)/cx, -(props.fire_locs['u4'][y]-cy)/cy],
  //   [(props.fire_locs['u5'][x]-cx)/cx, -(props.fire_locs['u5'][y]-cy)/cy]];

  var element = (<div id = 'map-pane'> <img id='fu1' src={fire} /> <img id='fu2' src={fire} /> <img id='fu3' src={fire} />
    <img id='fu4' src={fire} /> <img id='fu5' src={fire} /> <img id='pu1' src={pol} /> <img id='pu2' src={pol} />
    <img id='pu3' src={pol} /> <img id='pu4' src={pol} /> <img id='pu5' src={pol} /> <img id='gu1' src={guard} />
    <img id='gu2' src={guard} /> <img id='gu3' src={guard} /> <img id='gu4' src={guard} /> <img id='gu5' src={guard} />
    </div>);
  return (element);
}

function TranscriptBox(props) {
  return (<div id = 'transcript-box'> <h2> Transcript </h2> </div>);
}

function Alert(props) {
  return (<div id='alert'> {props.title} <button onClick={props.handleDispatch} value={props.title}> Dispatch </button> </div> );
}

function AlertStack(props) {
  // console.log(props.serverData);
  const items = props.serverData.map((e) => props.display[props.serverData.indexOf(e)] && <li key={e}> <Alert title={e} handleDispatch={props.handleDispatch}/> </li>);
  return (<div id = 'alert-stack'> <h2> Alerts </h2> <ul> {items} </ul> </div>);
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
    <Map fire={props.serverData['fire_locs']} pol={props.serverData['police_locs']} guard={props.serverData['guard_locs']} dis={props.serverData['disasters']}/>
    <AlertStack serverData={props.serverData['alerts']} handleDispatch={props.handleDispatch} display={props.display['alerts']} />
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
    this.state = {currentPage: 'Home', test: 0, serverData: {'alerts': [], 'disasters':[],
      'fire-locs': [], 'police-locs': [], 'guard-locs': [], 'dispatches': [], 'transcript': []},
      display: {'alerts': [], 'disasters': []}};
    this.switchPage = this.switchPage.bind(this);
    this.setState = this.setState.bind(this);
    this.dispatch = this.dispatch.bind(this);
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
    var sDisp = this.state.display;
    fetch('http://localhost:5000/update/')
      .then(function(response) {
        return response.json();
      })
      .then(function(myJson) {
        console.log(myJson);
        // console.log(typeof(setState));
        var tempData = Object.assign({}, sDisp);
        var i;
        if (sData['alerts'].length < myJson['alerts'].length) {
          for (i=0; i<myJson['alerts'].length-sData['alerts'].length; i++) {tempData['alerts'].push(true);}}
        if (sData['disasters'].length < myJson['disasters'].length) {
          for (i=0; i<myJson['disasters'].length-sData['disasters'].length; i++) {tempData['disasters'].push(true);}}
        setState({display: Object.assign({}, sDisp)});
        setState({serverData: Object.assign({}, myJson)});
      })
      // .catch(function() {console.log("Error")});
      // console.log(this.state.serverData['alerts']);
   }

   dispatch(e) {
     var tempData = Object.assign({}, this.state.display);
     tempData['alerts'][this.state.serverData['alerts'].indexOf(e.target.value)] = false;
     this.setState({display: Object.assign({}, tempData)});
     //TODO push request to server to remove alert
   }

  render() {
    // console.log(this.state.serverData);
    switch(this.state.currentPage) {
      case 'Home':
        return (<Home handleNav={this.switchPage} serverData={this.state.serverData}
          handleDispatch={this.dispatch} display={this.state.display}/>);
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
