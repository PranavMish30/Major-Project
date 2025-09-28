# Indoor Navigation System Using Wi-Fi RSSI

## Overview

This project implements an **indoor navigation system** that estimates the position of a user inside a building using **Wi-Fi RSSI (Received Signal Strength Indicator)** values. Unlike GPS, which does not work well indoors, this system leverages Wi-Fi signals from multiple access points to provide **accurate indoor localization**.

---

## Features

- Real-time indoor location estimation using RSSI values from Wi-Fi access points.
- Support for multiple floors or large indoor environments.
- Uses a **fingerprinting-based localization approach** (or trilateration, depending on implementation).
- Provides the **shortest path** from the current location to a specified destination.
- Handles multiple equally optimal paths.

---

## Technologies Used

- **Python 3.x** – core programming language.
- **Wi-Fi RSSI scanning** – collection of signal strength values from nearby access points.
- **Pandas / NumPy** – data processing and matrix computations.
- **Dijkstra’s Algorithm** – shortest path computation on the indoor graph.
- **Matplotlib / Plotly** (optional) – visualization of indoor maps and paths.
- **Excel / CSV** – storage of reference points, RSSI fingerprints, and adjacency matrices.

---

## System Architecture

1. **Data Collection**  
   - Collect RSSI values at multiple reference points in the indoor environment.  
   - Each location is associated with a **name** and a **unique identifier** (e.g., BSSID of AP or location code).

2. **Fingerprint Database / Graph**  
   - Locations and distances between them are stored in an **adjacency matrix**.  
   - Each vertex corresponds to a location, and edges correspond to the distance or estimated travel cost.

3. **Localization**  
   - Compare live RSSI values with the fingerprint database to estimate the **current location**.

4. **Pathfinding**  
   - Use **Dijkstra’s algorithm** to compute the **shortest path** from the current location to a desired destination.

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/PranavMish30/Major-Project.git
   cd Major-Project