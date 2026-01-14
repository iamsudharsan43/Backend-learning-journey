# Day 12 – Logging & Debugging

## What is logging?
Logging is the process of recording events that happen in an application.
Logs help developers understand:
- What happened
- When it happened
- Why it happened

## Why print() is bad in production
- No log levels
- No timestamps
- Hard to filter
- Not suitable for servers

## What is logging used for?
- Debugging errors
- Monitoring performance
- Tracking user actions
- Investigating production issues

## Log Levels (VERY IMPORTANT)
- DEBUG → detailed internal info (development only)
- INFO → normal application flow
- WARNING → something unexpected but not broken
- ERROR → something failed
- CRITICAL → system is unusable

## Logging vs Debugging
- Debugging → during development
- Logging → always running (dev + prod)

## Best practices
- Use logging module
- Never log secrets
- Log meaningful messages
- Use proper log levels

## What I learned today
- Difference between print and logging
- How log levels work
- How backend systems track behavior
