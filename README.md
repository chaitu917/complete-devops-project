# Complete DevOps CI/CD Project

## Project Overview

This project demonstrates a complete DevOps CI/CD workflow using:

- Linux
- Git
- Jenkins
- Docker
- Docker Compose
- Ansible
- Nginx

## Application

The application is a Python Flask web application.

## Current Deployment

Application Container:
complete-devops-app

Docker Image:
complete-devops-app:1.0

Application Port:
5001

Container Port:
5000

Health Check:
/health

## Architecture

Git
  |
  v
Jenkins
  |
  v
Docker Build
  |
  v
Docker Container
  |
  v
Nginx
  |
  v
Web Application
