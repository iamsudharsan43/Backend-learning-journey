# Day 11 – Environment Variables & Configuration

## What are environment variables?
Environment variables are values stored outside the source code.
They are used to store:
- Secrets
- Configuration values
- Environment-specific settings

Examples:
- Database URL
- Secret keys
- Debug mode

## Why NOT hardcode values?
Hardcoding secrets is dangerous because:
- Code is pushed to GitHub
- Anyone can see secrets
- Security risk in production

## Development vs Production
Different environments need different values:
- Development → debug enabled
- Production → debug disabled
- Different databases

Environment variables solve this problem.

## How Python accesses environment variables
Using:
import os
os.getenv("VARIABLE_NAME")

## Common backend usage
- SECRET_KEY
- DATABASE_URL
- DEBUG
- API_KEYS

## What I learned today
- Why environment variables are important
- How to read environment variables in Python
- How professional backends manage configuration
