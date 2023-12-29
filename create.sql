CREATE TABLE Olympics
(
  olymp_year INT NOT NULL,
  city VARCHAR(25) NOT NULL,
  PRIMARY KEY (olymp_year)
);

CREATE TABLE Athlete
(
  athlete_name VARCHAR(100) NOT NULL,
  country VARCHAR(3) NOT NULL,
  gender VARCHAR(5) NOT NULL,
  athlete_id INT NOT NULL,
  PRIMARY KEY (Athlete_id)
);

CREATE TABLE Sport
(
  sport VARCHAR(30) NOT NULL,
  discipline VARCHAR(30) NOT NULL,
  sport_event VARCHAR(60) NOT NULL,
  sport_id INT NOT NULL,
  PRIMARY KEY (sport_id)
);

CREATE TABLE Medal
(
  medal_type VARCHAR(6) NOT NULL,
  medal_id INT NOT NULL,
  sport_id INT NOT NULL,
  olymp_year INT NOT NULL,
  athlete_id INT NOT NULL,
  PRIMARY KEY (Medal_id),
  FOREIGN KEY (sport_id) REFERENCES Sport(sport_id),
  FOREIGN KEY (olymp_year) REFERENCES Olympics(olymp_year),
  FOREIGN KEY (athlete_id) REFERENCES Athlete(Athlete_id)
);