function onSubmit() {
    let age = document.getElementById('age').value;
    if (age < 18) {
        alert('Вы слишком молоды для такого...')
        return false
    } else {
        return true
    }
}
