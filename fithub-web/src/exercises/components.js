import React, {useEffect, useState} from 'react';
import {loadExercises} from '../lookup'

class Search extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log(this.state.value)
  }

  render() {
    return (
      <div className='row mb-3'>
        <div className='col-md-4 mx-auto col-10'>
            <form className='form' onSubmit={this.handleSubmit}>
                <textarea className='form-control' name='search' placeholder='search...' onChange={this.handleChange}></textarea>
                <button type='submit' className='btn btn-primary' >search</button>
            </form>
        </div>
      </div>
    );
  }
}



export function ExercisesList(props){
    const [exsercises, setExercises] = useState([])
    useEffect(() => {
      const myCallback = (response, status) => {
        if (status === 200){
          setExercises(response.response)
        } else {
          alert('there was an error')
        }
      }
      loadExercises(myCallback)
      
    }, [])
    return exsercises.map((item, index)=>{
      return <Exercise exercise={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}/>
    })
  }

export function Exercise(props){
    const {exercise} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className} >
      <p key={props.index}>{exercise.name} - {exercise.description}</p>
    </div>
  }

export default Search