# Multi-Level Cloud Cache Optimization using DAA

## 📌 Project Overview

This project implements a **Multi-Level Cloud Cache Optimization Algorithm** that intelligently decides whether data should be stored at:

* Edge Cache
* Regional Cache
* Central Cloud Cache

The objective is to **minimize a weighted combination of:**

* Latency
* Bandwidth Usage
* Energy Consumption

Unlike traditional cache systems that optimize only latency, this project provides a **multi-objective, algorithm-driven, and capacity-aware cache placement strategy** using Design and Analysis of Algorithms (DAA).

This architecture is inspired by real-world CDN systems used in organizations like Amazon Web Services and Google Cloud Platform.

---

## 🎯 Objectives

* Optimize cache placement across Edge, Regional, and Cloud levels
* Minimize total latency, bandwidth, and energy
* Improve cache hit ratio
* Compare performance with traditional LRU and LFU
* Provide mathematically optimized cache placement using DAA

---

## 🧠 Algorithms Used

| Algorithm              | Purpose                            |
| ---------------------- | ---------------------------------- |
| Greedy                 | Fast cache placement approximation |
| Dynamic Programming    | Optimal cache placement            |
| 0/1 Knapsack           | Capacity-aware optimization        |
| Dijkstra Shortest Path | Network cost optimization          |
| LRU                    | Traditional cache comparison       |
| LFU                    | Traditional cache comparison       |

---

## 🏗️ Project Structure

```
cache-allocation/
│
├── member1_network_graph/
│   ├── graph_model.py
│   ├── cost_functions.py
│   ├── shortest_path.py
│   └── latency_analysis.ipynb
│
├── member2_cache_optimization/
│   ├── cache_placement.py
│   ├── knapsack.py
│   ├── lru_lfu_comparison.py
│   ├── hit_ratio_analysis.py
│   └── performance_metrics.py
│
├── member3_simulation/
│   ├── request_generator.py
│   ├── simulation_engine.py
│   ├── result_collector.py
│   ├── plots.py
│   └── report_final.docx
│
├── data/
│   ├── content_list.json
│   ├── network_topology.json
│   └── requests.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone or Download

```
git clone <repository_url>
cd cache-allocation
```

---

### Step 2: Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### Step 3: Install Requirements

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the main file:

```
python main.py
```

---

## 📊 Performance Metrics Measured

The system evaluates:

* Total Latency
* Total Bandwidth Consumption
* Total Energy Consumption
* Cache Hit Ratio
* Cache Efficiency

---

## 📈 Expected Results

The optimized cache placement provides:

* Reduced latency
* Reduced energy consumption
* Reduced bandwidth usage
* Improved hit ratio

Compared to:

* LRU
* LFU
* Non-optimized caching

---

## 💡 Innovation and Contribution

This project introduces:

* Multi-objective optimization
* Capacity-aware cache placement
* Pure algorithm-based optimization (no ML dependency)
* Adjustable priority weights (Latency, Bandwidth, Energy)
* Mathematical performance guarantees

---

## 📂 Dataset

Located in:

```
data/
```

Contains:

* Content list
* Network topology
* Request patterns

---

## 👨‍💻 Team Responsibilities

| Member   | Responsibility                        |
| -------- | ------------------------------------- |
| Member 1 | Network graph modeling                |
| Member 2 | Cache optimization algorithms         |
| Member 3 | Simulation and performance evaluation |

---

## 🌍 Real-World Applications

* Content Delivery Networks (CDN)
* Cloud Storage Optimization
* Edge Computing Systems
* Video Streaming Platforms
* Smart Cloud Infrastructure

---

## 🚀 Future Improvements

* Machine Learning-based prediction
* Real-time cache updates
* Integration with live cloud systems
* Reinforcement Learning optimization

---

## 📚 Technologies Used

* Python
* NumPy
* Matplotlib
* JSON
* Graph Algorithms

---

## 📜 Conclusion

This project demonstrates an efficient and scalable multi-level cache optimization framework using classical algorithms. It significantly improves cloud system performance while reducing energy and bandwidth consumption, making it suitable for modern cloud and edge computing environments.

