import React from "react";
import { List, Header } from "semantic-ui-react";

export const Wikis = ({ wikis }) => {
  return (
    <List>
      {wikis.map((wiki) => {
        return (
          <li key={wiki.id}>
            <h1>{wiki.title}</h1>
            <h3>{wiki.link}</h3>
          </li>
        );
      })}
    </List>
  );
};
