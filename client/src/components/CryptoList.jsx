import React from "react";
import InfoBoard from "./InfoBoard.jsx";
import styles from "../../css/cryptolist.css";

export default function CryptoList({ cryptos, data, handleClick }) {
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
