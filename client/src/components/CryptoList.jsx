import React, { useState } from "react";
import InfoBoard from "./InfoBoard.jsx";
import axios from "axios";
import styles from "../../css/cryptolist.css";

export default function CryptoList() {
  const [state, setState] = useState({
    cryptos: [
      { ticker: "BTC-USD" },
      { ticker: "AVAX-USD" },
      { ticker: "DOGE-USD" },
      { ticker: "ETH-USD" },
      { ticker: "LTC-USD" },
    ],
    data: null,
    analysis: [],
  });
  const { cryptos, data } = state;

  const getDescription = (id) => {
    axios
      .get(`/api/crypto/${id}/`)
      .then(({ data }) => {
        setState({ ...state, data });
      })
      .catch((e) => console.log(e));
  };

  const getAnalysis = (id) => {
    axios
      .get(`/analysis/${id}/`)
      .then(({ data }) => {
        setState({ ...state, analysis: [...state.analysis, data] });
      })
      .catch((e) => console.log(e));
  };

  const handleClick = async (id, e) => {
    await getDescription(id);
    await getAnalysis(id);
    console.log(state.analysis);
  };

  const list = cryptos.map((crypto, index) => (
    <div
      key={index}
      className="dropdown-item"
      onClick={(e) => handleClick(index + 1, e)}
    >
      {crypto.ticker}
    </div>
  ));
  return (
    <>
      <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
        {list}
      </div>
      {data && <InfoBoard data={data} />}
    </>
  );
}
