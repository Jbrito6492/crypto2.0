import React, { Fragment } from "react";
import DropDown from "./DropDown.jsx";
import DashboardHook from "../hooks/Dashboard";
import styles from "../../css/dashboard.css";

export default function Dashboard(props) {
  const { state, handleClick } = DashboardHook();
  const { analysis } = state;
  console.log("data board", analysis);
  return (
    <Fragment>
      {analysis && (
        <div className={styles.dashboardContainer}>
          <h4>news</h4>
          <h4>simple return</h4>
          {analysis.simple_return}
          <h4>beta</h4>
          {analysis.beta}
        </div>
      )}
      <DropDown
        handleClick={handleClick}
        cryptos={state.cryptos}
        data={state.data}
      />
    </Fragment>
  );
}
