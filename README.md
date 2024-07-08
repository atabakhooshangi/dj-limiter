
# DJ-Limiter

A simple and configurable rate limiting middleware for Django applications to control the rate at which requests are processed.

## Features

- Configurable request limits and time windows.
- Easy integration with existing Django projects.
- Uses Django's caching framework for tracking request counts.

## Installation

You can install the package using pip:

```bash
pip install dj-limiter
```

Or if you are using Poetry:

```bash
poetry add dj-limiter
```

## Usage

### Adding the Middleware

Add the middleware to your Django settings by updating the `MIDDLEWARE` list in your `settings.py` file:

```python
MIDDLEWARE = [
    # ... other middleware ...
    'dj_limiter.middleware.RateLimitingMiddleware',
]
```

### Configuring Rate Limits

Configure the rate limiting parameters in your `settings.py`:

```python
# Maximum number of requests allowed within the time window
RATE_LIMIT = 100

# Time window in seconds
TIME_WINDOW = 60
```

### Example

Here's an example of how to configure and use the middleware in a Django project:

1. Install the package:

    ```bash
    pip install dj-limiter
    ```

2. Update your `settings.py` to include the middleware and configure the rate limits:

    ```python
    MIDDLEWARE = [
        # ... other middleware ...
        'dj_limiter.middleware.RateLimitingMiddleware',
    ]

    RATE_LIMIT = 100
    TIME_WINDOW = 60
    ```

3. Run your Django server and test the rate limiting by making multiple requests from the same client. Once the rate limit is exceeded, the middleware will return a `429 Rate Limit Exceeded` response.

## Development

### Setting Up the Development Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/dj-limiter.git
    cd dj-limiter
    ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.