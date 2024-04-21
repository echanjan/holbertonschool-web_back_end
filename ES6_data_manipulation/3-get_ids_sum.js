export default function getStudentIdsSum(listStudents) {
  let list = null;
  if (Array.isArray(listStudents)) {
    temp = listStudents.reduce(
      (acumulator, student) => acumulator + student.id,
      0
    );
  }
  return list;
}
