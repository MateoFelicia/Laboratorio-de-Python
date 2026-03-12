const grid = document.getElementById("grid");
const buscador = document.getElementById("buscador");
const carrito = [];
const contadorCarrito = document.getElementById("contador-carrito");
const carritoIcono = document.querySelector(".carrito-icono");
const carritoDropdown = document.getElementById("carrito-dropdown");
const filtroCategoria = document.getElementById("filtro-categoria");


const productos = [
    {
        titulo: "PROYECTOR ASTRONAUTA",
        imagen: "https://images.unsplash.com/photo-1591449235870-2d8491bf51ff?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8UHJveWVjdG9yJTIwYXN0cm9uYXV0YXxlbnwwfHwwfHx8MA%3D%3D",
        precio: 50000,
        fecha_de_lote: 1,
        categoria: "decoracion"
    },
    {
        titulo: "AURICULARES GAMER",
        imagen: "https://plus.unsplash.com/premium_photo-1679177183750-0eda63444b24?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8YXVyaWN1bGFyZXMlMjBnYW1lcnxlbnwwfHwwfHx8MA%3D%3D5",
        precio: 35000,
        fecha_de_lote: 2,
        categoria: "perifericos"
    },
    {
        titulo: "MOUSE GAMER",
        imagen: "https://images.unsplash.com/photo-1727417453138-7d8efdd70fb3?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW91c2UlMjBnYW1lcnxlbnwwfHwwfHx8MA%3D%3D",
        precio: 20000,
        fecha_de_lote: 3,
        categoria: "perifericos"
    },
    {
        titulo: "TECLADO MECÁNICO RGB",
        imagen: "data:image/jpeg;base64,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suJi47VGJfwLhlEnh/EJVMXsRv8A/n2s1S/Bd5ysNiXBzmBxDHPzFoNnEEwT0xK6rHhObs4p6Nn0ngCf+qUP0uh++VR+2vc/A2hb8tP+6PdI/Vq0OU8m5XvADF42u3E4UNqDmwx1I1BTc1zXEioxzt0yDlIMe21Wrkpnn1Dko2jG/gKpPS3aOFaO4td71nONVvqyS/6t/wCSJTjvT5+hipyT7RndwNQdu0MKT3gBSlVtq1yf6ibx4Pn6ElDkp2hG/s+q4/2dpYRo7i0qso1n7Ml8rf8Akit0aVuSfaM7mAqNHXtHCuPeGhTGNW3WkuT/AFMaGo5J9peQv9fwqm1TiuT8zKam31Wl71fxRo/kk2nwwLx247DH4KUqm9rl6kJVd7XJ/qI6nJJtbhgyO3F4c/xBXV95eKlvf3zMt5JNq8cGfXMOP4k1Ianua5eo+qTankR9cw/zIu0WnxXL1M/VJtTyJ3ruG+KtoRapxXL1NHcke1eGDPreHP8AErRcL9ZPn6Flm3v75mPqi2t5H+1Yf51dujui/mX6SdTH1RbW8j/asP8AOq3hwfP0JMfVFtbyP9qw/wDiJeHB8/QFgcl+2vJqnr1D/EUXhwfP0J0Mv5M9tkZXYZxadQcVhzPnzqrtuCsRfVJtXyJ3rmG+ZT1eH19DTNT4PmvIyeSXafkD/XsL8U0+/wDRfNh/5ZfMv0Gn1S7V8id65hvnVSmanwfP0N/ql2n5A/17C/FToaZsP/LL5l+gjPJJtbyJ3reG+dQZN0+D5+hkcku1fIXeuYb51DvuLRlS3xfzL9Jn6pdqcMC/13DfMq2lx+nqWc6G6Mr/ANy/SZPJPtU3dgnk/puG+ZLPd3epPSUpO81Jv+5fpYHJPtYeLgnjp/nmG+dTZ7+71I6SnF3gpLj1l+lD6pdqeQv9dw3zKLS4/T1JzYf+SXzL9B9Vyc8lmNpYylXxNIUKdF4qGa7Kj3uZdgaKZIAzRJPCVNtbspKpHJlira32393Diz3pWMQgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCA//2Q==",
        precio: 45000,
        fecha_de_lote: 4,
        categoria: "perifericos"
    },
    {
        titulo: "MONITOR 24'' GAMER",
        imagen: "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf",
        precio: 180000,
        fecha_de_lote: 5,
        categoria: "monitores"
    },
    {
        titulo: "SILLA GAMER",
        imagen: "https://media.istockphoto.com/id/2198864501/photo/game-zone-with-gamer-chair-on-dark-3d-background-night-room-interior-with-computer-on-table.webp?a=1&b=1&s=612x612&w=0&k=20&c=T0vKdVhCLFdxVSmyZH-JgVbIqY2AvCHxCP2oM7V5xLQ=",
        precio: 220000,
        fecha_de_lote: 6,
        categoria: "muebles"
    },
    {
        titulo: "WEBCAM HD",
        imagen: "https://images.unsplash.com/photo-1626581795188-8efb9a00eeec?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8d2ViY2FtJTIwaGR8ZW58MHx8MHx8fDA%3D",
        precio: 30000,
        fecha_de_lote: 7,
        categoria: "streaming"
    },
    {
        titulo: "MICRÓFONO STREAMING",
        imagen: "https://images.unsplash.com/photo-1671063064510-bbcc56fa79e5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bWljcm9mb25vJTIwc3RyZWFtfGVufDB8fDB8fHww",
        precio: 70000,
        fecha_de_lote: 8,
        categoria: "streaming"
    },
    {
        titulo: "PARLANTES BLUETOOTH",
        imagen: "https://plus.unsplash.com/premium_photo-1683141496040-eeef9702269f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGFybGFudGVzfGVufDB8fDB8fHww",
        precio: 40000,
        fecha_de_lote: 9,
        categoria: "audio"
    },
    {
        titulo: "SMARTWATCH",
        imagen: "https://images.unsplash.com/photo-1660844817855-3ecc7ef21f12?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c21hcnR3YXRjaHxlbnwwfHwwfHx8MA%3D%3D",
        precio: 95000,
        fecha_de_lote: 10,
        categoria: "gadgets"
    },
    {
        titulo: "TABLET ANDROID",
        imagen: "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0",
        precio: 150000,
        fecha_de_lote: 11,
        categoria: "dispositivos"
    },
    {
        titulo: "CARGADOR INALÁMBRICO",
        imagen: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQDxAPDw8PEA8PDw8PEBAPDw8PDw8OFRUWFhURFRYYHSggGBolHRUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0NGw4NGislHyUrOC0rLTctMisrKysyKzc4LSsrNzcyLjEtLSs3Ky04Ky0rLS0rKzcuKysuKys4KysrK//AABEIAOcA2gMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAAAgEDBAYHBQj/xABEEAACAQMABwUDCQUGBwEAAAAAAQIDBBEFBhIhMUFhEyJRcZEHMoEUI0JSYnKCobFjksHR8BUzU6Ky4TRzg5PCw/EX/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAH/xAAWEQEBAQAAAAAAAAAAAAAAAAAAARH/2gAMAwEAAhEDEQA/AOsaH05b3UNuhVjNL3kt04dJRe9fE9OMjiGlNVNI6PqdpQdS5hDLi4y7K+gukl3ay9G/A9nVn2mt/N3SdXY3TlGPZ3NLk+1ovHXLWOHMDrCZKZ5uitLULmHaUKsakN2XF74trOzKL3xfRpMz1IC3JJXknIDgLknIEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVVaUZLEkmvBrJqOtGoNred5w2asfcqwk6daD5bNRb/AIPKNzIwBwe+0BpPRlTtabqV4xz89QSp3cY8cTpru1Y+XHmjZNWfadGa2bpKaW6VajFqUH+1pcYvqvQ6dWoRmsSSa6ml60ezu2un2sE6dde7WpPs6y/FwmukgNqsNI0q8FUo1IVIP6UJJrPg/B9GZakcIudH6U0VUdRdpUhHjcWscVFH9vb8JLjvWVzNt1a9ptKrFfKdnG5fKKClKnnwnD3oP18kgOmZJTMOzvadWCqUpwqQlvjOElKL8mjJUgLCciZJTAbJJCZIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEYIaGADHuLaE1iUU/DxXk+Roes/s2oV5OvQ2qFx/i0MQnL78fdqLz39ToeCGgOBTjpPRE3OSl2afeuLaLlSkl/j0H7vDik8csG7aue0ijVjFXOzTzhKvSbnbyfXnB9HnHNo3+6s4VFiUU+vNfE55rL7MqU5SrWknbVnvcqMVsz6VKXuzXlhgb/AG91GcVKEoyjJZUotSjJeKa4l6mfP89I32ianZVqnybtdtQq0ZbdtWa3SexJZpzWVva8j29Fe0W8t0vlGxd0XwnmNOvs+KlFbM/ik+oHZ1IbJzmHtYscZdK8z4dnRf8A7D3NA69WN5JU6dV06r4Uq67Kcukd7jJ9E2wNqyTkpVQZSAtyGRMkpgOBCZIAAAAAAAAAAAAAAAAAKmTkVMnIDAGQACGiQAUhoYhga/rXqzb39F0q9OMnxhNrvQl4prejhOseqH9m3NKnUqfN1XWdNyeE0lHdnhnvH0o0al7QdT6ek7ZU5d2rSk50Z+DaxKL8U93ogOF1rWUeWc+rX8fgY7WeOPLkZmlNB6R0Y3GpB1aK5NOUcePQwKmkaVXYjDFKpOag+12tinn6TlFNtZ6MDbNAe0O7sko1J/KKC+hWk+0ivsVN7+DyvI6/qxrHTvreNxTjVpqTacK0dmaeE/Jpppprc8nKNHarW1pCFzdOV5OcoqDpUqlxRTb3OEaaltJfWe7dwT3G20e3hXU4VoxoqGOyVJqbnn3nPa4fZ2QOjQqFiZqGgtZ6devO1U4zrUobc9jLUVlLEnwUt/DOeiNqpMC9DIRDpgSAAAAAAAAAAAAAAAAVE5AgB8k5EJTAcBQAYhhkgAIaJADEu7KFWLjUipR8GjnunfZRbVasa1Fuk1LacY4Sk+XL+R00hoDiV3q9pHRknOi5TpN5lsrahL78ODfXj4YPI0ld6S0jPsKEXb0EodpOntw2pOKbTm+9jOe7H4s+gnTT4oxI6JoKW1GnFPpw9OQGhezvU+Ng3UScqk4qEpyyu7ueIx5LcuOWdEpoaNFIsUQISGROCQAAAAAAAAAAAAAAAAA5fqp7TYzioXbctjuSrRjipCS3YrUsZT8l8DolpeUq0FUpVI1IS4Sg1KL+KNN1r9n9C5fax2qVdLu3NHEayXhNcKkej/I586ukdD1NubcaecO5oRcrWp4K4o8ab5Z67muIHesgaPq3r/QuFGFxs0KkktmW0pW1XPBwn9HlufjhORucagFxORFInID5AQlMBgAnAEATggAAjJIE5DJAAMBGAAkBQAYBScgSBGSQAAAAAAARow73R0KqeVhtNZxxXg1zM5kAck1k9nGw5VbFxoSk25UmnKzqvrHjSfWPoeLofWm/sJO1qR7OSi9i3uvnKb5KdvNNbUc47qfwzvO5yj8UafrpqPbX9PvwaqQy6coPE4N4zs+i3PwAwNC+0a3niF4vktXhl7UqEuqljMfKSXmzbrLSdGstqjVp1Y+NOpGa/Jnzzf6Gq2Vz8luKu3CpDapTm3HacXjZTfCXT/6Y8aFShNzhOpGaaalFuE6fk1vXrgD6YVQtjI4/qx7R6scU75OpHgrinFdovvwW6XnHD6M3+etNnClGrK4p7ElmGy9uc+iit+fhuA2VMY51f+0CrPKtKChH/EuO9L4U4vC+Lfka9e6Suq/9/c1Zp8YqXZ0/3Y4XqB1e90za0d1W4owf1ZVI7X7vE8mvrvYR4VJ1PuUqn6tJHMo0IrgkvgNsoDfantBtvo0LmXwpR/8AIq//AESlyta379M0ZxIwBvsfaJR521deUqb/AIoyaWv9m/ejXh504v8A0yZzdoVxA63ba2WNThcwi/2ilT/1JHr0LiFRbVOcZrxhJSXqjhbiFKpKD2oSlCS4ShJxfqgO8EYOSaP10vaOE6irR+rWW0/3lh/mzbdEa/21XEa8ZW8nzb26T/Et6+K+IG3YIIo1YzipQlGUXvUotSi10aHAUCWhWA2SRMk5AYCMhkAZAwuAASSHYrA1TXfVShpGhsVId+PehNbpxfRnG9IaHvbB7M4u6tovCe9VaS/VfofQ93UjCMpzkowhFylJ7lGK4tnItY9Mz0hWxBbFrB4isYlU+1L+XL1yGr0rZTeYJpbm3JJfDC3Z6o9e0sYx34y+bfEzKNsorCRcoAIo4BjtCtAKQxiAEYrGZACsVjCsBWK0MyGBW0VyRdIVgZWiNOXFnLao1GlnvU5d6nLzj/Fbzp2rGt1C8Sg/mrhLfSk90usHz8uJyOUSnacWpRbjKLTi08NNc0wPoQU1HUXW35VHsK7SuILdLh2sfHz/AK89vwBAE4AAAgkBgAgCCGiSu7rxpU51Ze7ThOpL7sU2/wBAOee0bTDqVFYUn3YuMq7XOphSjD8KcZec4/VPDt7ZQiklwMXRcpVpuvU9+qlVln61X5xr4ObXkkepNAY8kIyyQjAVitDEMBGQxmKArFGxngm34JNvxKll+KT4PDXX6S5pfyb5AtarGONp4zuSw3KT6Jb38Ap1FKKlF5i+DMR2G1tKWzsy95b6jf4nj802uTRk06MY+7FJtJNpJSljhl8wGYozFAVisZigKymoi9lUwKKF3OhUjVpvEoNNb8Z8U/66nctXNLxu7eFVPfhbXLisp45ZXo01yOD3XA3P2WaWcJdi33ZTnTS8MxdWH5xrfvgdZyDYilklsCcgKSA7BEgAHha8VHHR13jnRcfhJqL/AFPdPH1qt3Vsrqmt7lQqYXjJLKXqkBzPRUVvxwaUl91pNfk0ZlVHl6v3ClGPil2cujhhL/JsfHJ7VeAGBJFbL5opkgEYrY4rAVkEshgNOcXCMXBbUXLvrCbTw0m8Z3PPPmUv+vF9RmKwFFYzIYCMVjMVgQxWMxWArKqhZIoqSAw7uW5mTqjdOnWjJc7u0S8k5qX5SXqeZpCthFmreXcW8OSqKs/N4aXlsQpy/GwPoa0rZSMls8XRNXMUexFgOiSESBaAABDKa63PyLmJUW4DjNPRkbfSNa2cthVsK3k3iG1lukn6yhnq+h7VGWcwmnGcW4yi9zjJcUzN9oOg+2h2kF85Ty4/ajzia/ojTCu9mnWmqd9BKEKk3swu4rcqdR/RqrgpP3uD34Aza9IxJxPQdZNuE4unUjiM4y3SUueVyKqtEJLsYDQrMiVMplEKrkKx2hWAjFY7FYCMgZisBWKxmIwIYjJkympUwAVJGBd3CSZF3dpczw7i4c8vOIp4b47/AAS5vp64W8ArVdttvfBPes42nygvPD8km+Rsupdu5VXVlve/fjGZPe30/wBzVqEXOSjFdEuOE+Lb5vcsvouSSOm6q6P2IxSX+/UDfdELuo9ymeTo+GEj1YAXICIkgWgAAQxWOKwPO0hb7UWjk+uOrsoylVpre/ejjdL/AHOyzjk8jSmjlUTTQHI9G60pqNG+jOpGC2YVotK7oL6uXuqR+zL1PdpTlsOpRnG6oLjOin2kP+ZSfeg/VdTA1p1T3uUVh8muJpTqXFrPaTnGUeFSm5Qkvit4HQ6d5Tmsprf1JlFPgafR1tVT/iqUK0udaHzFx5ylHuzf3kZ9HSdCX91dOD+pdQ2cf9SGYv0QHtyplUomIrmvjKgqkfrUZwqp+jz+RVPSyj78ZQ+/Fx/UDNaEaMP+16b5oWWlIeIGWxGzBnpWHiYtTTEeTA9SUimdVHk1NIzfCMseOGl6mDWvJPjOEfxbX+nK9QPYuL2K5nlXGkW3iKbfHC3vHj5HmVryC5ym+vdXonn/ADGHVvpS7sdyznZSSWeTwuL68eoGZXrrjN7T+rF934yXH4epRGUqkkks8ljcorw6Imz0dUqPflZ9Tc9BavYxlAV6taGxiTWW8ZZ0nQ9nhIxtFaMxjcbLaW2AMu2hgzYFdKBkQQEobAEgOAAAEMkAEaK5wyXitAeVe2MZp5RpunNVozy0jokomPVoJgcD0xqe021H4rczWrnRNam9zf4kfR13ouMuKNe0hqzCWe6gOD7deDzsyT8YN5/Ivp6xXMN3a1V0k2/1OnXuqC34ieNcapvwfoBpVTWGrJ5lJN9Yr+BW9Ny8If8Abh/I2irqo/qL91FD1V/Zr0A116alyUF5Qiv0Elpmr9aS8m0jZo6rfYXoX0tVn9RL4IDSnd1J8NpvoNC1rT5NeZ0Khqu+a/I9S11YS5Ac3tdAzlxy/JGx6M1Z+zj9TfrTV9L6J7NtohLkBqmjNAKOO6bRY6LS5HrULFLkZ9K3SAxba1wehSp4HhTLYxAiMSxIEhkAJEggAYAAAAAAAAAFZDQ5GAKpQKZ0cmUQ0B51S0T5GJU0dF8j2nERwA1+pomL5IploaPgbI6YrpAa3/Y0fAeOiI+BsPZB2QHhw0ZHwMiFgvA9RUhlTAwIWi8C+NAylAlQApjTLFEdRGwAqQwYJSAhIkklICCcEgAAAAAAAAAAAAAARggAAMEYAADBGAACMBgAAnAYIACcE4IACSQAAAAAlIkAAAAAP//Z",
        precio: 18000,
        fecha_de_lote: 12,
        categoria: "accesorios"
    }
];


function crearCard(producto) {

    const card = document.createElement("div");
    card.classList.add("card");

    const titulo = document.createElement("h3");
    titulo.textContent = producto.titulo;

    const imagen = document.createElement("img");
    imagen.src = producto.imagen;
    imagen.alt = producto.titulo;

    const precio = document.createElement("p");
    precio.textContent = `$${producto.precio.toLocaleString()}`;

    // Botón
    const boton = document.createElement("button");
    boton.textContent = "Agregar al carrito";

    boton.addEventListener("click", function () {
        agregarAlCarrito(producto);
    });

    card.appendChild(imagen);
    card.appendChild(titulo);
    card.appendChild(precio);
    card.appendChild(boton);

    return card;
}

// Render
function renderProductos() { //renderiza los productos en el DOM
    grid.innerHTML = "";
    productos.forEach(producto => {
        grid.appendChild(crearCard(producto));
    });
}



function filtrarProductos() {
    const texto = buscador.value.toLowerCase();
    const categoria = filtroCategoria.value;

    const productosFiltrados = productos.filter(producto => {

        const coincideTexto = producto.titulo.toLowerCase().includes(texto);

        const coincideCategoria =
            categoria === "todos" || producto.categoria === categoria;

        return coincideTexto && coincideCategoria;
    });

    grid.innerHTML = "";

    productosFiltrados.forEach(producto => {
        grid.appendChild(crearCard(producto));
    });
}

buscador.addEventListener("input", filtrarProductos);
filtroCategoria.addEventListener("change", filtrarProductos);


function agregarAlCarrito(producto) {
    carrito.push(producto);
    actualizarCarrito();
    renderCarrito();
}

function actualizarCarrito() {
    contadorCarrito.textContent = carrito.length;
}

carritoIcono.addEventListener("click", function () {
    if (carritoDropdown.style.display === "block") {
        carritoDropdown.style.display = "none";
    } else {
        carritoDropdown.style.display = "block";
    }
});


function renderCarrito() {
    carritoDropdown.innerHTML = "";
    if (carrito.length === 0) {
        carritoDropdown.innerHTML = "<p>Carrito vacío</p>";
        return;
    }

    let total = 0;

    carrito.forEach(producto => {
        const item = document.createElement("p");
        item.textContent = `${producto.titulo} - $${producto.precio}`;
        carritoDropdown.appendChild(item);
        total += producto.precio;
    });

    const totalElemento = document.createElement("p");

    totalElemento.textContent = `Total: $${total.toLocaleString()}`;
    totalElemento.style.fontWeight = "bold";

    carritoDropdown.appendChild(totalElemento);
}

renderProductos();