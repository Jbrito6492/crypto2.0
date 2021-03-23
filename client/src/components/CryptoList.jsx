import React, { useState } from "react";
import styles from "../../css/cryptolist.css";

export default function CryptoList() {
  const [state, setState] = useState({
    cryptos: [
      { name: "BTC-USD" },
      { name: "ETH-USD" },
      { name: "AVAX-USD" },
      { name: "LTC-USD" },
      { name: "DOGE-USD" },
    ],
  });
  const list = state.cryptos.map((crypto, index) => (
    <div key={index}>{crypto.name}</div>
  ));
  return <div className={styles.cryptoList}>{list}</div>;
}
