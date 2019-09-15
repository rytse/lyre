import React from "react";
import ReactDOM from "react-dom";

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
  render() {
    return (<div id = 'alert-stack'> alerts </div>);
  }
}

function Header() {
  return (<div id='header'> header, nav </div>);
}

function App() {
  return (<div> <Header />
      <Map />
      <AlertStack />
      <TranscriptBox />
      hi
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
