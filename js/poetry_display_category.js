// https://reactjs.org/docs/add-react-to-a-website.html
'use strict';

const e = React.createElement;

class DisplayCategory extends React.Component {
  constructor(props) {
    super(props);
    this.state = { display: 0 };
  }

  render() {
    if (this.state.display == 0) {
      return 'Categories';
    }

    return e(
      'button',
      { onClick: () => this.setState({ display: 1 }) },
      'Display a category'
    );
  }
}

const domContainer = document.querySelector('#display_category_container');
ReactDOM.render(e(DisplayCategory), domContainer);