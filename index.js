const fs = require('fs');
const { fakerES: faker } = require('@faker-js/faker');


let objects = new Array(100).fill({}).map((_) => {
  const type = faker.helpers.arrayElement(['student', 'professor'])
  const firstName = faker.person.firstName();
  const lastName = faker.person.lastName();
  const obj = {
    id: faker.string.uuid(),
    firstName,
    lastName,
    email: faker.internet.email({
      firstName,
      lastName,
      allowSpecialCharacters: false,
      provider: type === 'student' ? 'correo.unimet.edu.ve' : 'unimet.edu.ve',
    }),
    username: faker.internet.userName(),
    type,
  };
  if (type === 'student') {
    obj.major = faker.helpers.arrayElement([
      'Ingeniería Civil',
      'Ingeniería Eléctrica',
      'Ingeniería Mecánica',
      'Ingeniería de Producción',
      'Ingeniería Química',
      'Ingeniería de Sistemas',
      'Contaduría Publica',
      'Economía Empresarial',
      'Ciencias Administrativas',
      'Psicología',
      'Matematicas Industriales',
      'Idiomar Modernos',
      'Educación',
      'Derecho',
      'Estudios Liberales'
    ]);
  } else {
    obj.department = faker.helpers.arrayElement([
      'Banca, Contabilidad y Auditoría',
      'Economía',
      'Gerencia y Emprendimiento',
      'Finanzas',
      'Mercadeo',
      'Ciencias de la Educación',
      'Ciencias del Comportamiento',
      'Desarrollo Integral',
      'Humanidades',
      'Física',
      'Inglés',
      'Lingüística',
      'Matemáticas',
      'Química',
      'Estudios Internacionales',
      'Estudios Jurídicos',
      'Estudios Políticos',
      'la Construcción y Desarrollo Sustentable',
      'Energía y Automatización',
      'Producción Industrial',
      'Gestión de Proyectos y Sistemas',
    ]);
  }
  return obj;
});

const ids = objects.map((obj) => obj.id);

objects = objects.map((obj) => {
  obj.following = faker.helpers.arrayElements(ids, {min: 3, max: 15}).filter((id) => id !== obj.id);
  return obj;
})

fs.writeFileSync('./users.json', JSON.stringify(objects, null, 2));

const posts = new Array(1000).fill({}).map((_) => {
  const type = faker.helpers.arrayElement(['photo', 'video']);
  const obj = {
    publisher: faker.helpers.arrayElement(ids),
    type,
    caption: faker.word.words({ count: { min: 10, max: 75 } }),
    date: faker.date.past(),
    tags: faker.word.words({ count: { min: 1, max: 5 } }).split(' '),
  };
  if (type === 'photo') {
    obj.multimedia = {
      type,
      url: faker.image.urlPicsumPhotos(),
    };
  } else {
    obj.multimedia = {
      type,
      url: faker.helpers.arrayElement([
        'https://youtu.be/0bnSwzT7CX8?si=PriJ2uAVYwMgrH_6',
        'https://youtu.be/s07kXl58qWM?si=iJcS8F4FAM7psZZO',
        'https://youtu.be/40UQGZ1jgA4?si=XERwuMDaKWyGiFQZ',
        'https://youtu.be/e1JbzSvuIdY?si=JOq3tmylEPuPUwm6',
        'https://youtu.be/04mmSIDwmeg?si=IXKfHyIaioqPA8_-',
        'https://youtu.be/WN-92Cfrk4o?si=hQBY5i1Qs2mkS-ct',
      ]),
    };
  }
  return obj;
});

fs.writeFileSync('./posts.json', JSON.stringify(posts, null, 2));
