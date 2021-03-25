import React, { useState } from "react";
import CryptoList from "./CryptoList.jsx";

export default function DropDown(props) {
  const [state, setState] = useState({});

  const handleSubmit = (e) => {};

  return (
    <div className="dropdown show">
      <div
        className="btn btn-secondary dropdown-toggle"
        href="#"
        role="button"
        id="dropdownMenuLink"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        Currencies
      </div>
      <CryptoList />
    </div>
  );
}
