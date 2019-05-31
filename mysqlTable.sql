use miniproject;

create table t_disease
(name varchar(50) , 
description varchar(100),
primary key(name) );

create table t_medicine
(name varchar(100) ,
drug varchar(200) ,
type varchar(30) ,
primary key(name) );

create table t_store
(store_id int(11) not null auto_increment,
name varchar(100),
email varchar(254),
phone int(10),
city varchar(30),
location varchar(200),
pincode int(10),
primary key(store_id) );

create table t_symptom
(symptom_id int(11) not null auto_increment,
name varchar(40),
primary key(symptom_id)
);

create table t_disease_symptoms
(name varchar(50) ,
symptom_id int(11),
foreign key(symptom_id) references t_symptom(symptom_id) on delete cascade,
foreign key(name) references t_disease(name) on delete cascade);

create table t_medicine_stores
(name varchar(100) ,
store_id int(11),
foreign key(name) references t_medicine(name) on delete cascade,
foreign key(store_id) references t_store(store_id) on delete cascade);

create table t_disease_medicines
(disease_id varchar(40) , 
medicine_id varchar(40),
foreign key(medicine_id) references t_medicine(name) on delete cascade,
foreign key(disease_id) references t_disease(name) on delete cascade);