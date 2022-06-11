CREATE KEYSPACE wikipedia WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE wikipedia;

CREATE TABLE domains_data (
    id text,
    domain text,
    page text,
    PRIMARY KEY ((domain), page)
);


CREATE TABLE pages_users (
    id text,
    user_id text,
    user_name text,
    page text,
    creation_timestamp timestamp,
    PRIMARY KEY ((user_id), creation_timestamp)
);


CREATE TABLE pages_data (
    page_id text,
    page text,
    PRIMARY KEY ((page_id))
);
