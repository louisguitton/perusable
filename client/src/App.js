import React, { useState } from 'react';

import './App.css';

import { Col, Container, Row } from 'react-bootstrap';
import axios from 'axios';

import ResultList from './components/ResultList';
import Search from './components/Search';

function App() {
  const [results, setResults] = useState([]);

  const search = async (country, points, query) => {
    try {
      const response = await axios({
        method: 'get',
        url: 'http://localhost:8003/api/v1/catalog/wines/',
        params: {
          query: query,
          country: country,
          points: points
        }
      });
      setResults(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Container className='pt-3'>
      <h1>Perusable</h1>
      <p className='lead'>
        Use the controls below to peruse the wine catalog and filter the results.
      </p>
      <Row>
        <Col lg={4}>
          <Search search={search} />
        </Col>
        <Col lg={8}>
          <ResultList results={results} />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
