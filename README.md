# Svelte + Carbon UI + Flask Example

This repo contains a simple example of integrating a Python back-end with a JS front-end using IBM's UI library.

Using:

- Flask
- Svelte
- Carbon UI

## Design

For the design of this application the Flask backend

This means that after the static assets of the Svelte front-end have been built

Lastly, the top-level `package.json` exists to facilitate a simpler DX while working. It uses an [NPM workspace]() to easily call scripts that the front-end client contains.

## Getting started

Begin by running

```bash
npm install
```

This will install all of the dependencies for both the Svelte front-end and the Python backend

> Please note the `preinstall` script in the top level `package.json` in this repository. If this command, or any other python related command, fails you may need to add an alias to your shell config.

After installing all the dependencies you can run

```bash
npm run dev
```

With this, the development application should now be live at `http://localhost:5000/`

Any changes made to the client application should result in an automatic rebuild, however, if viewing the webpage you will need to refresh to see changes.

## Deployment

A simple `Dockerfile` as well as a bash script to build an image has also been included in this repository if you wish to deploy via Docker.

The `Docker` file will copy only what's needed to deploy the app (the `/client/dist` folder, `server.py`, and `requirements.txt`) and expose the default port Flask uses.

the default image name that will be generated is `flask-svelte-carbon-image`.
