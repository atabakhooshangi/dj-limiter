import time
from django.core.cache import cache
from django.http import JsonResponse
from django.conf import settings


class RateLimitingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = getattr(settings, 'RATE_LIMIT', 100)
        self.time_window = getattr(settings, 'TIME_WINDOW', 60)

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        cache_key = f"rl:{client_ip}"
        request_data = cache.get(cache_key, (0, time.time()))
        request_count, first_request_time = request_data

        if time.time() - first_request_time > self.time_window:
            request_count = 1
            first_request_time = time.time()
        else:
            request_count += 1

        cache.set(cache_key, (request_count, first_request_time), timeout=self.time_window)

        if request_count > self.rate_limit:
            return JsonResponse({"error": "Rate limit exceeded"}, status=429)

        response = self.get_response(request)
        return response
