import React, { useState } from "react";
import axios from "axios";

export default function DashboardHook() {
  const [state, setState] = useState({
    cryptos: [
      { ticker: "BTC-USD" },
      { ticker: "AVAX-USD" },
      { ticker: "DOGE-USD" },
      { ticker: "ETH-USD" },
      { ticker: "LTC-USD" },
    ],
    data: null,
    analysis: null,
  });

  const getDescription = (id) => {
    return axios
      .get(`/api/crypto/${id}/`)
      .then(({ data }) => data)
      .catch((e) => console.log(e));
  };

  const getAnalysis = (id) => {
    return axios
      .get(`/analysis/${id}/`)
      .then(({ data }) => data)
      .catch((e) => console.log(e));
  };

  const handleClick = async (id, e) => {
    e.preventDefault();
    const data = await getDescription(id);
    const analysis = await getAnalysis(id);
    setState({ ...state, data, analysis });
  };

  return { state, handleClick }

}