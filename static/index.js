async function handleSubmit(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch('/submit', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    const resultDiv = document.getElementById('result');
    if (result.status === 'success') {
        resultDiv.innerText = result.message;
        resultDiv.style.display = 'block';
        Swal.fire({
            icon: 'success',
            title: '¡Éxito!',
            text: 'Las fechas se han subido correctamente a Firebase.',
        });
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: result.message,
        });
    }
}
