export default function getStudentIdsSum(listStudents) {
  let list = null;
  if (Array.isArray(listStudents)) {
    list = listStudents.reduce(
      (accumulator, student) => accumulator + student.id,
      0
    );
  }
  return list;
}
