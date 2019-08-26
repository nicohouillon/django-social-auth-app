# Django Social Auth App
<!-- badges -->
<a href="https://www.gnu.org/licenses/gpl-3.0.pt-br.html"><img src="https://img.shields.io/badge/licence-GPL3-green.svg"/></a>

 Simple application that implements integration between Django and Github, using the python lib [social-auth-app-django](https://github.com/python-social-auth/social-app-django) and allow users to add tags on their repositories, classifing and filtering them by categories.

 This project is a `test app`, that serve as a boilerplate for projects that use Django Social Authentication.

---

# How to run the project

## Django - service 'web'

### Setup database and user

Before running the Django service it's necessary to migrate models to database:

```sh
sudo docker-compose run --rm web python manage.py migrate
```

If you want to, you can create a super user by running:
```sh
sudo docker-compose run --rm web python manage.py createsuperuser
```

### Setup GitHub OAuth application

As this application is configures to used Github Authentication, you need to set a oauth application on GitHub. To know how to do it, follow this reference link: [How to config Github Oauth application?](https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html).

After that, get you `Client ID` and `Client Secret` keys and add it respectively on env variables, at docker-compose:

```yml
- SOCIAL_AUTH_GITHUB_KEY=<SET YOUR KEY VALUE HERE>
- SOCIAL_AUTH_GITHUB_SECRET=<SET YOUR GITHUB SECRET HERE>
```

The `ALLOWED_HOSTS` variable must be setted according to your domains configs.

```yml
ALLOWED_HOSTS=localhost
```

**Do not share your secrets in a public way!**

If you do not want to use GitHub authentication, you need to properly configure another provide and comment the following lines, at file 'setting.py':
```python
'social_core.backends.github.GithubOAuth2',

---------------

SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET')
```



### Execution
To run the Django service, start the container:
```sh
sudo docker-compose up -d web
```

You can access the site by default at the url `http://localhost:8000`.

# How to contribute

We'll be very happy to having your contribution :)

The process is simple:

- Write a new issue describing the feature you want to work on (or look for issue with the labels `help-wanted` or `good-first-issue`);
- Write your code, tests and documentation
- Open a `pull request` describing the changes you've made;
- DONE! Now you only need to wait for a review and feedback on your code.

Read the [Contribution Guide](./docs/CONTRIBUTING.md) for more information.

# License

All this project is developed and are available under LICENSE [GPL3](https://github.com/MatheusMiranda/django-social-auth-app/blob/master/LICENSE)

You can see the dependency list [here](https://libraries.io/github/MatheusMiranda/django_social_auth_app)
