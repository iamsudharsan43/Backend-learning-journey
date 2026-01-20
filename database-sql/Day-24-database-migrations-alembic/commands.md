# Alembic Commands Reference

## Install Alembic
pip install alembic

## Initialize Alembic
alembic init alembic

## Create a migration
alembic revision --autogenerate -m "message"

## Apply migrations
alembic upgrade head

## Rollback migration
alembic downgrade -1

## Check current version
alembic current

## Migration history
alembic history
