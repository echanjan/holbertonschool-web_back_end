# ES6 Classes

Este proyecto es un ejemplo básico de cómo utilizar las clases de ES6 en JavaScript. Las clases de ES6 proporcionan una sintaxis más clara y orientada a objetos para trabajar con objetos y herencia en JavaScript.

## Instalación

No se requiere ninguna instalación especial para utilizar este proyecto. Simplemente clona el repositorio y empieza a trabajar con los archivos de código fuente.

## Uso

Puedes utilizar las clases proporcionadas en este proyecto como base para construir tus propias aplicaciones JavaScript que requieran la creación de objetos con propiedades y métodos.

## Ejemplos

A continuación, se muestra un ejemplo básico de cómo utilizar las clases proporcionadas en este proyecto:

```javascript
// Importar la clase
import { Car } from './Car';

// Crear una nueva instancia de Car
const myCar = new Car('Toyota', 'V6', 'Blue');

// Obtener la marca del coche
console.log(myCar.brand); // Output: Toyota

// Clonar el coche
const clonedCar = myCar.cloneCar();

// Mostrar la marca del coche clonado
console.log(clonedCar.brand); // Output: Toyota
