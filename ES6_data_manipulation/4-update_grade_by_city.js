export default function updateStudentGradeByCity(ListStudents, city, newGrades) {
  if (!Array.isArray(ListStudents) || typeof city !== 'string' || !Array.isArray(newGrades)) {
    throw new Error('Parámetros no inválidos.');
  }

  return ListStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const newGradeObj = newGrades.find((grade) => grade.studentId === student.id);
      const grade = newGradeObj ? newGradeObj.grade : 'N/A';
      return { ...student, grade };
    });
}
