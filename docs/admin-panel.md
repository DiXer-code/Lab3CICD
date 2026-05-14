# Django admin panel

Before creating an admin user, apply database migrations:

```bash
docker compose exec web python manage.py migrate
```

Create a superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

Open the admin panel at:

```text
http://localhost:8000/admin/
```

The admin panel is used to manage menu categories and dishes without writing SQL manually.
