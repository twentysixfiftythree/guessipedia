import React from 'react';
import { List,Header } from 'semantic-ui-react';

export const Wikis = ({ wikis }) => {
    return (
        <List>
            {wikis.map(wiki => {
                return (
                    <List.Item key={wiki.id}>
                        <Header>{wiki.title}</Header>
                        <List.Description>{wiki.link}</List.Description>
                    </List.Item>
                )
            })}
        </List>

    );
};