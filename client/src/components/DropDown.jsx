import React, { useState } from "react";
import CryptoList from "./CryptoList.jsx";

export default function DropDown({ cryptos, data, handleClick }) {
  return (
    <div className="dropdown show">
      <div
        className="btn btn-secondary dropdown-toggle"
        id="dropdownMenuLink"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        Currencies
      </div>
      <CryptoList handleClick={handleClick} data={data} cryptos={cryptos} />
    </div>
  );
}
