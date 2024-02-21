import React from 'react';
import AsyncSelect from 'react-select/async';



export function LoadWikis () {
    const [wikis, setWikis] = React.useState([]);
    React.useEffect(() => {
        fetch('/get_wikis').then(response => 
            response.json().then(data => {
            //console.log(data);
            setWikis(data.wikis);
        })
    );
    }, []);
    console.log("these are", wikis);
    return wikis;
}

const options = LoadWikis().title;




export const AutoCompleteBar = () => {
    LoadWikis();
    const handleChange = (selectedOption)=> {
        console.log("handleChange",selectedOption);
    };
    
    const loadOptions = (searchValue, callback) => {
        setTimeout(() => {
        const filteredOptions = options.filter((option) =>
            option.label.toLowerCase().includes(searchValue.toLowerCase())
        );
        console.log('loadOptions', searchValue, filteredOptions);
        callback(filteredOptions);
        }, 0)
    
        };
  return <AsyncSelect loadOptions={loadOptions} onChange={handleChange} />;
};