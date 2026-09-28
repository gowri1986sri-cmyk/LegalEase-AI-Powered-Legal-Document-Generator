# PHASE 3 – PROJECT DESIGN

## Project Title

LegalEaseAI – AI-Powered Legal Document Generator

## 1. Introduction

The project design phase defines the architecture, modules, workflow, user interface and data flow of the LegalEaseAI application.

LegalEaseAI is designed as a web-based application that accepts legal document requirements from the user and generates a structured legal document using Generative AI.

## 2. System Architecture

The LegalEaseAI application consists of the following main components:

User
   ↓
HTML/CSS Frontend
   ↓
Jinja2 Templates
   ↓
FastAPI Backend
   ↓
Input Validation
   ↓
Prompt Creation
   ↓
Generative AI Model
   ↓
Generated Legal Document
   ↓
Result Page
   ↓
Download / Save

## 3. Architecture Components

### 3.1 Frontend

The frontend is developed using:

- HTML
- CSS
- Jinja2

It provides the interface through which the user enters the required information.

### 3.2 Backend

FastAPI is used as the backend framework.

The backend manages:

- HTTP requests
- Form submission
- Input validation
- AI communication
- Response processing
- Result display

### 3.3 Template Engine

Jinja2 is used to create dynamic HTML pages.

The main templates are:

- index.html
- result.html

### 3.4 AI Layer

The Generative AI model receives the prepared prompt and generates the requested legal document.

### 3.5 Static Files

CSS files are stored in the static folder and are used to style the application.

## 4. Project Structure

```text
LegalEaseAI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css