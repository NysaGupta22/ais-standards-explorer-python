const search = document.getElementById('search'), filter = document.getElementById('filter');

function filterCards() {
  const q = search.value.toLowerCase(), v = filter.value;
  document.querySelectorAll('.standard').forEach(c => {
    c.style.display = c.dataset.text.includes(q) && (v === 'all' || c.dataset.ready === v) ? 'block' : 'none';
  });
}

search.addEventListener('input', filterCards);
filter.addEventListener('change', filterCards);
