# Asynchronous Posts Fetcher

This Python project fetches posts from a public API (`https://jsonplaceholder.typicode.com`) using asynchronous requests. It retrieves 77 posts and stores them in a local JSON file (`data.json`) using `aiohttp` and `asyncio`.

## Features

- **Asynchronous HTTP Requests**: The code fetches posts concurrently using `aiohttp` and `asyncio`.
- **JSON Storage**: All posts are stored in a formatted JSON array within the `data.json` file.

## Requirements

- Python 3.7+
- `aiohttp` library