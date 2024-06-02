const fs = require('fs');
const dayjs = require('dayjs');
const { fakerES: faker } = require('@faker-js/faker');
const roundes = require('./rounds.json');

const teamNames = new Set();

roundes.rounds.forEach((round) => {
  round.matches.forEach((match) => {
    teamNames.add(`${match.team1.code}_${match.team1.name}_${match.group}`);
    teamNames.add(`${match.team2.code}_${match.team2.name}_${match.group}`);
  });
});

const teams = Array.from(teamNames).map((team) => {
  const [code, name, group] = team.split('_');
  return {
    id: faker.string.uuid(),
    code,
    name,
    group: String(group).replace('Group ', ''),
  };
});


const stadiumInfo = [
  {
    name: 'Estadio Olímpico de Berlín',
    city: 'Berlín',
    capacity: [100, 20],
  },
  {
    name: 'Allianz Arena',
    city: 'Munich',
    capacity: [100, 20],
  },
  {
    name: 'Signal Iduna Park',
    city: 'Dortmund',
    capacity: [100, 20],
  },
  {
    name: 'MHPArena',
    city: 'Stuttgart',
    capacity: [100, 20],
  },
  {
    name: 'Veltins-Arena',
    city: 'Gelsenkirchen',
    capacity: [100, 20],
  },
  {
    name: 'Volksparkstadion',
    city: 'Hamburgo',
    capacity: [100, 20],
  },
  {
    name: 'Deutsche Bank Park',
    city: 'Fráncfort del Meno',
    capacity: [100, 20],
  },
  {
    name: 'Estadio Rhein Energie',
    city: 'Colonia',
    capacity: [100, 20],
  },
  {
    name: 'Red Bull Arena',
    city: 'Leipzig',
    capacity: [100, 20],
  },
  {
    name: 'Merkur Spiel-Arena',
    city: 'Düsseldorf',
    capacity: [100, 20],
  },
];

function generateProduct() {
  return {
    name: faker.commerce.productName(),
    quantity: faker.number.int({ min: 15, max: 15000 }),
    price: faker.commerce.price(),
    stock: faker.number.int({min: 100, max: 500}),
    adicional: faker.helpers.arrayElement([
      `alcoholic`,
      `non-alcoholic`,
      `package`,
      `plate`,
    ]),
  };
}

function generateRestaurants() {
  const products = [];
  for (let i = 0; i < faker.number.int({min: 10, max: 20}); i++) {
    products.push(generateProduct());
  }
  return {
    name: faker.company.name(),
    products,
  };
}

const stadiums = stadiumInfo.map((stadium) => {
  let restaurants = [];
  for (let i = 0; i < faker.number.int({ min: 1, max: 10 }); i++) {
    restaurants.push(generateRestaurants());
  }
  return {
    id: faker.string.uuid(),
    name: stadium.name,
    city: stadium.city,
    capacity: [faker.number.int({ min: 10, max: 1000 }), faker.number.int({min: 10, max: 500})],
    restaurants,
  };
});

const matches = roundes.rounds.flatMap((round) =>
  round.matches.map((match) => {
    const team1 = teams.find((team) => team.code === match.team1.code);
    const team2 = teams.find((team) => team.code === match.team2.code);
    return {
      id: faker.string.uuid(),
      number: match.num,
      home: team1,
      away: team2,
      date: match.date,
      group: match.group,
      stadium_id: faker.helpers.arrayElement(stadiums).id,
    };
  })
);

fs.writeFileSync('teams.json', JSON.stringify(teams, null, 2));
fs.writeFileSync('matches.json', JSON.stringify(matches, null, 2));
fs.writeFileSync('stadiums.json', JSON.stringify(stadiums, null, 2));
