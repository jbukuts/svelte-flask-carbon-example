<script>
  import { Button } from "carbon-components-svelte";

  let randomNum = null;

  const getRandomNum = () => {
    fetch("/api/rand").then(async (v) => {
      const res = await v.json();
      randomNum = res.num;
    });
  };
</script>

<Button kind="primary" on:click={getRandomNum}>
  {randomNum ? `random number is ${randomNum}` : "click to get a random number"}
</Button>
