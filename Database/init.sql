create database duty_free
  with owner postgres;

create table spider.product
(
  product_id       bigserial    not null
    constraint product_pk
      primary key,
  product_name     varchar(255) not null,
  brand            varchar(255) not null,
  description      text,
  product_category text,
  keywords         text[]
);

alter table spider.product
  owner to postgres;

create table spider.result
(
  record_id  bigserial not null
    constraint result_pk
      primary key,
  time       timestamp default now(),
  price      double precision,
  currency   char(3),
  product_id bigint,
  shop_id    integer,
  url        text,
  info       text
);

alter table spider.result
  owner to postgres;

