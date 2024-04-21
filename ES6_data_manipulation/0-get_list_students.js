export default function getListStudents() {
  const matriz = [
    ['Guillaume", 1, "San Francisco'],
    ['James", 2, "Columbia'],
    ['Serena", 5, "San Francisco'],
  ];

  const result = matriz.map((item) => {
    return {
      id: item[1],
      firstname: item[0],
      location: item[2],
    };
  });
  return result;
}
