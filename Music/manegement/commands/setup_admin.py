from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Tạo tài khoản admin superuser nếu chưa tồn tại'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('ADMIN_USERNAME', 'admin')
        email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
        password = os.environ.get('ADMIN_PASSWORD', 'Admin123!')
        
        # Kiểm tra nếu admin đã tồn tại
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Đã tạo tài khoản admin thành công! Username: {username}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'⚠️ Tài khoản admin "{username}" đã tồn tại, bỏ qua tạo mới')
            )