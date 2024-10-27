const BotonCarrito = document.querySelector('.container-cart-icon');
const MenuDesplegable = document.querySelector('.container-cart-products');

BotonCarrito.addEventListener('click', () => {
    MenuDesplegable.classList.toggle('hidden-cart');
});

/*==================================================================*/ 

const InformacionCarrito = document.querySelector('.cart-product');
const FilaProducto = document.querySelector('.row-product');

const ListaProductos = document.querySelector('.container-items');

let ListaCompras = [];

const ValorTotal = document.querySelector('.total-pagar');

const CantidadProductos = document.querySelector('#contador-productos');

/*==================================================================*/ 

ListaProductos.addEventListener('click', e => {
    if(e.target.classList.contains('btn-add-cart')){
        const Producto = e.target.parentElement;

        const InformacionProducto = {
            quantity: 1,
            title: Producto.querySelector('h2').textContent,
            price: Producto.querySelector('p').textContent,
        };

        const existe = ListaCompras.some(Producto => Producto.title === InformacionProducto.title);
        if(existe){
            const Productos = ListaCompras.map(Producto => {
                if(Producto.title === InformacionProducto.title){
                    Producto.quantity++;
                    return Producto;
                } else{
                    return Producto;
                }
            });
            ListaCompras = [...Productos];
        } else{
            ListaCompras = [...ListaCompras, InformacionProducto];
        }

        showHTML();
    }
});

/*==================================================================*/ 

FilaProducto.addEventListener('click', (e) => {
    if(e.target.classList.contains('icon-close')){
        const Producto = e.target.parentElement;
        const title = Producto.querySelector('p').textContent;

        ListaCompras = ListaCompras.filter(
            Producto => Producto.title !== title
        );

        showHTML();
    }
});

/*==================================================================*/ 

const showHTML = () => {
    FilaProducto.innerHTML = '';

    let Total = 0;
    let TotalProductos = 0;

    ListaCompras.forEach(Producto => {
        const containerProduct = document.createElement('div');
        containerProduct.classList.add('cart-product');

        containerProduct.innerHTML = `
            <div class="info-cart-product">
                <span class="cantidad_producto-carrito">${Producto.quantity}</span>
                <p class="titulo-producto-carrito">${Producto.title}</p>
                <span class="precio-producto-carrito">${Producto.price}</span>
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="icon-close">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
            </svg>
        `;

        FilaProducto.append(containerProduct);

        Total += Producto.quantity * parseFloat(Producto.price.slice(1)); 
        TotalProductos += Producto.quantity;
    });

    ValorTotal.innerText = `$${Total}`; 
    CantidadProductos.innerText = TotalProductos;

    document.querySelector('#total-input').value = Total; 
};

/*==================================================================*/ 

document.querySelector('#realizar-pedido').addEventListener('click', () => {
    const MontoPagar = document.querySelector('.total-pagar').textContent.trim();
    document.querySelector('#pedido-form').submit(); 
});