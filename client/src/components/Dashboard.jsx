import React, { Fragment } from "react";
import CryptoList from "./CryptoList.jsx";
import styles from "../../css/dashboard.css";

export default function Dashboard(props) {
  return (
    <Fragment>
      <div className={styles.dashboardContainer}>
        <div>
          <h4>news</h4>
          <CryptoList />
        </div>
        <h4>simple daily return</h4>
        <h4>daily log return</h4>
        <h4>beta</h4>
      </div>
    </Fragment>
  );
}
