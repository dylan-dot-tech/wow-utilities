# bnet-api

## Dependencies

- [Python 3.9+](https://www.python.org/downloads/)
  - [Requests](https://pypi.org/project/requests/)
- [Battle.net API Access](https://develop.battle.net/)
  - `client_id`
  - `client_secret`

## Setup

### Virtual Environment

1. Create a `venv` virtual environment, if not exists, via:

```sh
python -m venv venv
```

2. Edit the virtual environment `activate` script via:

```sh
nano venv/bin/activate
```

3. Set the virtual environment variables by adding the following lines to your `activate` script, substituting your unique [Battle.net](https://develop.battle.net/) `client_id` and `client_secret`:

```sh
export BNET_CLIENT_ID=XXXXXXXXXXXXXXXXXXXX
export BNET_CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXX
```

4. Save and exit.
5. Activate the virtual environment via:

```sh
source venv/bin/activate
```

6. Install dependencies via:

```sh
python -m pip install requests
```
