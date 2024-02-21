import React from 'react';
import AsyncSelect from 'react-select/async';



export function LoadWikis () {
    const [wikis, setWikis] = React.useState([]);
    React.useEffect(() => {
        fetch('/get_wiki_name').then(response => 
            response.json().then(data => {
            //console.log(data);
            setWikis(data.wikis);
        })
    );
    }, []);
    return wikis;
}

var options = [
    { value: 'jack', label: 'Jack' },
    { value: 'john', label: 'John' },
    { value: 'three', label: 'Three' },
  ];


export const AutoCompleteBar = () => {
    const handleChange = (selectedOption)=> {
        console.log("handleChange",selectedOption);
    };
    const loadOptions = (searchValue, callback) => {
        setTimeout(() => {
        const filteredOptions = options.filter((option) =>
            option.label.toLowerCase().includes(searchValue.toLowerCase())
        );
        console.log('loadOptions', searchValue, filteredOptions);
        console.log("options",options);
        callback(filteredOptions);
        }, 0)
    
        };
  return <AsyncSelect loadOptions={loadOptions} onChange={handleChange} />;
};