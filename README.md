# ITrack – Job Tracking Web App

ITrack is a Django-based web application designed to help students and job seekers **track job opportunities they are interested in**, without losing links, context, or application status.

The app separates **externally sourced job listings** from **user-owned tracked jobs**, allowing users to browse available roles and selectively save the ones they care about to a personal dashboard.

---

## ✨ Features

### 🔐 Authentication

* User registration and login
* Each user has a **private dashboard** (no shared data)

### 📋 Scraped Jobs Feed

* Jobs are ingested from **public, static job listing pages** using a web scraper
* Scraped jobs are stored separately from user data
* Users can browse all available scraped jobs

### ⭐ Interest Tracking

* Users can mark a job as **Interested**
* Interested jobs are copied to the user’s dashboard
* Each user only sees jobs they personally selected

### 📊 Personal Dashboard

* Displays jobs the user is tracking
* Jobs are ordered by creation date
* Serves as the main “home page” after login

---

## 🏗️ Architecture Overview

The system is intentionally split into two layers:

### 1. ScrapedJob (External Data)

* Represents jobs sourced from public websites
* Shared across all users
* Read-only from the user’s perspective

### 2. Job (User Data)

* Represents jobs a user is personally interested in
* Linked directly to a `User`
* Created when a user clicks **Interested**

This separation ensures:

* Clean data ownership
* No mutation of external data
* Easy extensibility for new scraping sources

---

## 🕷️ Web Scraping

### Design Choices

* Scraping is implemented as a **Django management command**
* This keeps scraping logic separate from request/response handling
* Scraping is **manually triggered**, not automatic

### Why this approach?

* Avoids blocking web requests
* Respects rate limits
* Makes failures isolated and debuggable

### Ethical Considerations

* Only **publicly accessible pages with static HTML** are scraped
* Platforms that prohibit scraping (e.g., LinkedIn, Indeed) are intentionally excluded
* The scraper is modular and source-agnostic

---

## ⚙️ Tech Stack

* **Backend:** Django
* **Database:** SQLite (development)
* **Frontend:** Django Templates + CSS
* **Scraping:** `requests`, `BeautifulSoup`
* **Auth:** Django built-in authentication

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd ITrack
```

### 2. Create and activate a virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the scraper

```bash
python manage.py scrape_jobs
```

### 7. Start the server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 🧪 Example User Flow

1. User logs in
2. User visits **Scraped Jobs** page
3. User clicks **Interested** on a job
4. Job appears on the user’s dashboard
5. User can now track that opportunity

---

## 🔮 Future Improvements

* Application status updates (Applied / Rejected)
* Notes per job
* Multiple scraping sources
* Background scraping (Celery / cron)
* Deployment to production environment

---

## 📌 Motivation

ITrack was built to solve a common student problem: job listings are scattered across platforms, easily lost, and difficult to track over time. This project focuses on **clean backend architecture**, **data ownership**, and **real-world constraints** such as ethical scraping and system reliability.

---

## 🧑‍💻 Author

**Gabriel**
BS Computer Science, Ateneo de Manila University
