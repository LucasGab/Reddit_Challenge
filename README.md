# OnaRoll reddit project

Tutorial to the reddit project

## Goal

The goal of the project are to get the information of top posts on reddit, and
run a process that on each run need:

1. New posts from the last program execution,
2. Posts that are no longer within the top 75 posts, and
3. Posts that had a vote count change and by how much.

## Enviroment

The project was build with Python 3.8.10. Create a new virtualenv and run:

```bash
make install
```

## Run the script

To run the proccess to get the reports, use:

```bash
make run_process
```

## Server

The project is a flask server. To run the server run:

```bash
make run
```

The server has the swagger documentation and the endpoint to get the saved reddit posts.

## Tests

## Future work

The project can have some improvements:

1. Increase reliability and the error handling
2. Increase features and tests suitecase
