import React, { useState } from "react";

export default function InfoBoard({ data }) {
  const { ticker, current_price, name, description } = data;

  return (
    <>
      <div>{ticker}</div>
      <div>${current_price}</div>
      <div>{name}</div>
      <div>{description}</div>
    </>
  );
}
