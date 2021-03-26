import React, { Fragment } from "react";
import DropDown from "./DropDown.jsx";
import styles from "../../css/dashboard.css";

export default function Dashboard(props) {
  return (
    <Fragment>
      <div className={styles.dashboardContainer}>
        <h4>news</h4>
        <h4>simple return</h4>
        <h4>log return</h4>
        <h4>beta</h4>
      </div>
      <DropDown />
    </Fragment>
  );
}
