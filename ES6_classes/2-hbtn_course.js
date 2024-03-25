class HolbertonCourse {
  constructor(name, length, students) {
    // Verificar el tipo de los atributos durante la creación del objeto
    if (typeof name !== 'string') {
      throw new Error('El nombre debe ser una cadena de caracteres.');
    }
    if (typeof length !== 'number') {
      throw new Error('La longitud debe ser un número.');
    }
    if (!Array.isArray(students)) {
      throw new Error('Los estudiantes deben ser un array de cadenas de caracteres.');
    }

    // Almacenar cada atributo en una versión con guión bajo (underscore)
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter y setter para el atributo 'name'
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new Error('El nombre debe ser una cadena de caracteres.');
    }
    this._name = value;
  }

  // Getter y setter para el atributo 'length'
  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new Error('La longitud debe ser un número.');
    }
    this._length = value;
  }

  // Getter y setter para el atributo 'students'
  get students() {
    return this._students;
  }

  set students(value) {
    if (!Array.isArray(value)) {
      throw new Error('Los estudiantes deben ser un array de cadenas de caracteres.');
    }
    this._students = value;
  }
}

module.exports = HolbertonCourse;
