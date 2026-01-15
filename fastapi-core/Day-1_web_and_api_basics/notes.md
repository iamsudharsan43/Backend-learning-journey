# Day 1 – How the Web Works & What is an API

## What is the Web?
The web works using a **client–server model**.
- Client: Browser / Mobile app
- Server: Backend application
- Communication happens using HTTP

## What is HTTP?
HTTP (HyperText Transfer Protocol) is a rule that defines how data is sent between client and server.

Common HTTP methods:
- GET – fetch data
- POST – send data
- PUT – update data
- DELETE – remove data

## What is an API?
API (Application Programming Interface) is a way for two software systems to communicate.

In backend development:
- API exposes data
- Frontend consumes data
- API usually sends and receives JSON

## Example
A frontend requests:
GET /expenses

Backend responds:
{
  "total": 12000
}

## Why APIs are important for backend developers
- Most companies use APIs
- Frontend, mobile apps, and other services depend on APIs
- APIs allow separation of frontend and backend

## What I learned today
- How the web works using client-server architecture
- What HTTP is and why it is important
- What an API is and its role in backend development
