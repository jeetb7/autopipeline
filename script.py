import psycopg2,uuid
from flask import Flask,jsonify,request

app=Flask(__name__)
hostname= 'localhost'
username='postgres'
database='travel_booking'
port_id= 5436
pwd= 'admin123'
try:
    id=uuid.uuid4
    conn=psycopg2.connect(


        host=hostname,
        user=username,
        database=database,
        password=pwd,
        port=port_id

)
    curr=conn.cursor()
    create_table="""CREATE TABLE IF NOT EXISTS "public"."User" (
    "user_id" varchar PRIMARY KEY,
    "username" varchar not null,
    "password" varchar not null
    );

    CREATE TABLE IF NOT EXISTS "public"."Flights" (
    "flight_id" varchar PRIMARY KEY,
    "user_id" varchar REFERENCES "public"."User" ("id"),
    "flight_name" varchar not null,
    "flight_number" varchar NOT NULL,
    "origin" varchar NOT NULL,
    "destination" varchar NOT NULL,
    "departure_date" DATE NOT NULL,
    "departure_time" TIME NOT NULL,
    "arrival_date" DATE NOT NULL,
    "arrival_time" TIME NOT NULL,
    "price" FLOAT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS "public"."Hotels" (
    "hotel_id" VARCHAR PRIMARY KEY,
    "user_id" VARCHAR REFERENCES "public"."User" ("id"),
    "name" VARCHAR NOT NULL,
    "Location" VARCHAR NOT NULL,
    "Checkin_date" DATE NOT NULL,
    "Checkin_time" TIME NOT NULL,
    "Checkout_date" DATE NOT NULL,
    "Checkout_time" TIME NOT NULL,
    "price" FLOAT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS "public"."Car_rentals" (
    "carrental_id" VARCHAR PRIMARY KEY,
    "user_id" varchar REFERENCES "public"."User" ("id"),
    "car_type" VARCHAR NOT NULL,
    "Location" VARCHAR NOT NULL,
    "pickup_date" DATE NOT NULL,
    "pickup_time" TIME NOT NULL,
    "price" FLOAT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS "public"."Bookings" (
    "id" varchar PRIMARY KEY,
    "user_id" varchar REFERENCES "public"."User" ("id"),
    "flight_id" VARCHAR REFERENCES "public"."Flights" ("flight_id"),
    "carrental_id" VARCHAR REFERENCES "public"."Car_rentals" ("id"),
    "hotel_id" VARCHAR REFERENCES "public"."Hotels" ("hotel_id")
    );

    CREATE TABLE IF NOT EXISTS "public"."Reviews" (
    "service_id" VARCHAR PRIMARY KEY,
    "user_id" varchar REFERENCES "public"."User" ("id"),
    "service_type" VARCHAR NOT NULL,
    "rating" INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    "comment" TEXT
    );"""
    curr.execute(create_table)
    curr.execute()
    
    conn.commit()

    conn.close()
    
except (Exception,psycopg2.DatabaseError)as error:
        print(f"Error:{str(error)}")


        
if __name__=='__main__':
    app.run(host='0.0.0.0',port=1781)
