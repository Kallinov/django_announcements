# django-announcements

django-announcements is a Django app that allows the administrator
to add and view announcements that a developer can receive in the code.
That is also possible to disable announcements on client-side.

Quick start
-----------

1. Add "announcements" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = [
        ...,
        "django_announcements",
    ]
    ```

2. Include the announcements URLconf in your project urls.py like this::

```
    path("announcements/", include("django_announcements.urls")),
```

3. Run ```python manage.py migrate``` to create the models.

4. Start the development server and visit the admin to create an announcements.

5. Visit the ```/announcements/page1``` URL to see active announcements.
