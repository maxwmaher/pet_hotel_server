CREATE TABLE owners
(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(50)
);

CREATE TABLE pets
(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(50),
    "breed" VARCHAR(50),
    "color" VARCHAR(50),
    "checked_in" BOOLEAN DEFAULT false,
    "owner_id" INT REFERENCES "owners"
);
