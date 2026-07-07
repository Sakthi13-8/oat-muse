# 🌿 Oat Muse – Full-Stack Skincare E-Commerce Website

## Overview

Oat Muse is a full-stack skincare e-commerce web application developed as a final-year Computer Science Engineering project. The application provides a seamless online shopping experience where users can browse products, manage their shopping cart, complete checkout, and place orders.

The project demonstrates the integration of frontend technologies, backend development using Flask, database management, and cloud deployment.

---

## Live Demo

🔗 **Website:** https://oat-muse.onrender.com

---

## Features

* Responsive and modern user interface
* Dynamic product loading using Flask API
* Shopping cart with add and remove functionality
* Checkout page with customer information form
* Order confirmation page
* SQLite database integration for order storage
* Session-based cart management
* Fully deployed using Render

---

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### Version Control

* Git
* GitHub

### Deployment

* Render

---

## Project Structure

```text
Oat Muse/
│
├── app.py
├── database.py
├── requirements.txt
├── schema.sql
│
├── templates/
│   ├── index.html
│   ├── cart.html
│   ├── checkout.html
│   ├── success.html
│   └── orders.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
└── README.md
```

---

## Application Workflow

1. User visits the homepage.
2. Products are loaded dynamically through a Flask API.
3. User adds products to the shopping cart.
4. Cart items are managed using Flask sessions.
5. User proceeds to checkout and enters customer details.
6. Order information is stored in the SQLite database.
7. A success page confirms the order placement.

---

## Database

The application uses an SQLite database to store customer order information.

Stored details include:

* Customer Name
* Email
* Phone Number
* Address
* Order Total
* Order Date

---

## Key Learning Outcomes

* Full-stack web application development
* Flask routing and backend logic
* REST API development
* Database integration with SQLite
* Session management
* Git and GitHub version control
* Cloud deployment using Render

---

## Future Enhancements

* User Authentication
* Product Search
* Wishlist
* Online Payment Gateway
* Admin Dashboard
* Product Categories and Filters

---
