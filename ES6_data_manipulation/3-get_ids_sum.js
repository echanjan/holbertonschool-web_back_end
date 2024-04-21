export default function getStudentIdsSum(getListStudents) {
  return getListStudents.reduce((acumulador, ids) => acumulador + ids.id, 0);
}
