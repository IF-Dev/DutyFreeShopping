create table brand
(
  brand_id   int auto_increment comment '品牌ID'
    primary key,
  brand_name varchar(100)   null comment '品牌名称',
  brand_info varchar(10000) null comment '其他信息，或许之后api会用到'
);

create table product
(
  product_id       bigint auto_increment comment '主键，自增'
    primary key,
  name             varchar(500)   null comment '商品名称',
  brand_id         int            null comment 'FK到brand brand_id',
  description      varchar(10000) null comment '描述',
  product_category varchar(1000)  null comment '类别，大部分网站都有这个信息，先放一个字段',
  keywords         varchar(10000) null comment '用来匹配爬虫结果和product的关键词',
  constraint product_brand_brand_id_fk
    foreign key (brand_id) references brand (brand_id)
);

create table shop
(
  shop_id   int            not null
    primary key,
  shop_name varchar(1000)  null comment '免税店名称',
  shop_info varchar(10000) null comment '免税店信息',
  shop_url  varchar(1000)  null comment '免税店链接'
);

create table result
(
  record_id   bigint auto_increment comment '爬虫结果ID
'
    primary key,
  update_time datetime default CURRENT_TIMESTAMP not null comment '写入时间，默认current timestamp',
  price       double                             null comment '价格',
  currency    char(3)                            null comment '货币三字代码',
  product_id  bigint                             null comment '外键',
  shop_id     int                                null comment '外键',
  url         varchar(10000)                     null comment '信息的网址',
  info        varchar(10000)                     null comment '其他信息',
  constraint result_product_product_id_fk
    foreign key (product_id) references product (product_id),
  constraint result_shop_shop_id_fk
    foreign key (shop_id) references shop (shop_id)
);

create table test_tobedelete
(
  id int(11) unsigned auto_increment
    primary key
);

