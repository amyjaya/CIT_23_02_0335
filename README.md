# CIT_23_02_0335
# Multi-Service Docker Web Application

**Registration Number:** CIT-23-02-0335  
**Course:** CCS3308 - Virtualization and Containers  

##  Application Overview
This project is a **Docker-based multi-service web application** with:
- **User Registration & Message Board** (Flask web service)
- **Admin Dashboard** to view stats & reset data (Flask admin service)
- **Redis** database with **persistent volume** for data storage

The system allows users to:
- Register with name, email, and message
- View a shared message board
- Track per-user visit count and last visit timestamp

The Admin dashboard provides:
- Total user count
- Total messages
- Latest user details
- Top visitors list
- Reset button to clear all data

---

##  Deployment Requirements
- **Docker** (version 20+ recommended)  
- **Docker Compose**  
- **Git**  
- Web browser (Chrome, Firefox, or similar)

---

##  Services & Ports
| Service | Description           | Port (Host:Container) |
|---------|----------------------|-----------------------|
| Web     | Flask User Interface | 5000:5000             |
| Admin   | Flask Admin Dashboard| 8000:6000 *(example)* |
| Redis   | Data store           | 6379:6379             |

---

##  Network and Volume Details
- **Network:** Automatically created by Docker Compose to link containers.
- **Volume:** `redis_data` — stores all Redis database data persistently.

---

##  Container Configuration
### **Web Service**
- Built from `Dockerfile.web`
- Runs Flask app (`web/app.py`)
- Connects to Redis via service name `redis`

### **Admin Service**
- Built from `Dockerfile.admin`
- Runs Flask app (`admin/admin.py`)
- Connects to Redis via service name `redis`

### **Redis Service**
- Uses official `redis:7` image
- Configured with Append-Only File (`--appendonly yes`) for persistence
- Stores data in named volume `redis_data`

---

##  Container List
1. **web** — User registration, message board, visit tracking
2. **admin** — Admin dashboard, reset function
3. **redis** — Data storage for users and messages

---

## Instructions

# Create application resources
./prepare-app.sh
Preparing app ...

# Run the application
./start-app.sh
Starting app ...
Web app: http://localhost:5000
Admin dashboard: http://localhost:8000

# Open browser and interact with the application
# Submit registration form and view messages

# Pause application
./stop-app.sh
Stopping app ...

# Delete all application resources
./remove-app.sh
Removed app.

