import React from "react";
import styles from "../../static/css/dashboard.css";

export default function Dashboard(props) {
  return (
    <div className={styles.dashboardContainer}>
      <div>news</div>
      <div>simple daily return</div>
      <div>daily log return</div>
      <div>beta</div>
    </div>
  );
}
