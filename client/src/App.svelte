<script>
  import svelteLogo from "./assets/svelte.svg";
  import RandomNum from "./lib/RandomNum.svelte";
</script>

<main>
  <div>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Svelte + Carbon UI + Flask</h1>

  <p>
    Simple example page that uses a Svelte front-end SPA with Carbon UI to
    interact with a Python Flask REST API
  </p>

  <p>Click button below to get a random number from a REST API</p>

  <div class="card">
    <RandomNum />
  </div>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
</style>
