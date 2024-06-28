const textGenForm = document.querySelector('.text-gen-form');

const translateText = async (text) => {
    const inferResponse = await fetch(`infer_t5?input=${text}`);
    const inferJson = await inferResponse.json();

    return inferJson.output;
};

textGenForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const textGenInput = document.getElementById('text-gen-input');
  const textGenParagraph = document.querySelector('.text-gen-output');

  try {
    textGenParagraph.textContent = await translateText(textGenInput.value);
  } catch (err) {
    console.error(err);
  }
});