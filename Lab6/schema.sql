DROP TABLE IF EXISTS dishware_item;

CREATE TABLE dishware_item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    price FLOAT NOT NULL,
    weight_in_g FLOAT NOT NULL,
    country_origin TEXT NOT NULL,
    brand TEXT NOT NULL,
    code INTEGER NOT NULL,
    name TEXT NOT NULL,
    category TEXT NOT NULL
);