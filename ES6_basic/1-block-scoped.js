export default function taskBlock(trueOrFalse) {
  let task = false; // Cambiado de var a let
  let task2 = true; // Cambiado de var a let

  if (trueOrFalse) {
    task = false; // No se necesita declarar nuevamente con let o const
    task2 = true; // No se necesita declarar nuevamente con let o const
  }

  return [task, task2];
}
