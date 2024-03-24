class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== "string") {
      throw new Error("Deben ser cadenas");
    }
    this._code;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== "string") {
      throw new Error("Deben ser cadenas");
    }
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

export default Currency;
