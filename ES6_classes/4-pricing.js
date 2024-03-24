import Currency from "./3-currency.js";

class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== "number") {
      throw new Error("La cantidad debe ser un número");
    }
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new Error("La moneda debe ser una instancia de Currency");
    }
    this._currency = value;
  }

  displayFullPrice() {
    return '${this._amount} ${this._currency.name} (${this._currency.code})';
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== "number" || typeof conversionRate !== "number") {
        throw new Error("La cantidad y la tasa de conversión deben ser números");
    }
    return amount * conversionRate;
  }
}

export default Pricing;
