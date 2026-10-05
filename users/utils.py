from django.core.cache import cache

def save_confirmation_code(user_id, code):
    # сохраняем код с TTL 5 минут
    cache.set(f"confirm:{user_id}", code, timeout=300)

def check_confirmation_code(user_id, code):
    saved_code = cache.get(f"confirm:{user_id}")
    if saved_code and saved_code == code:
        # удаляем после использования
        cache.delete(f"confirm:{user_id}")
        return True
    return False
