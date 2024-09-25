import uuid
import psycopg2
from flask import Flask, jsonify,request


class TravelBooking:
    def connection(self, hostname='localhost', username='postgres', database='travel_booking', port_id=5436, pwd='admin123'):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname=database,
                user=username,
                password=pwd,
                host=hostname,
                port=port_id
            )
            
            return conn
        except Exception as e:
            
            return None
    
    def registerUser(self,data):
        data = request.get_json()
        user_id=str(uuid.uuid4())
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}),
        try:
            con=self.connection()
            cursor = con.cursor()
            insert_script="""INSERT INTO "public"."User" ("user_id","username", "password") VALUES (%s, %s)"""
            cursor.execute(insert_script, (user_id,username, password))
            con.commit()
            cursor.close()
            con.close()
            return jsonify({'message': 'User registered successfully'}),
        except (Exception,psycopg2.DatabaseError)as error:
            print(f"Error:{str(error)}")
    def loginUser(self,data):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}),
        try:
            conn=self.connection()
            cursor = conn.cursor()
            login_script="""SELECT * from "public"."User" (username, password) where "username"=%s, "password"=%s)"""
            cursor.execute(login_script, (username, password))
            user=cursor.fetchone
            if user :
                return ("User logged in Successfully")
            else :
                return("Invalid Credentials")
            conn.commit()
            cursor.close()
            conn.close()
            
        except (Exception,psycopg2.DatabaseError)as error:
            print(f"Error:{str(error)}")
        
    def insertFlightsDtls(self,data):
        
        

        try:
                con=self.connection()
                cur=con.cursor()
                flight_id=str(uuid.uuid4())
                user_id=data.get('user_id')
                flight_name=data.get('flight_name')
                destination=data.get('destination')
                departure_date=data.get("departure_date")
                arrival_date=data.get("arrival_date")
                arrival_time=data.get('arrival_time')
                departure_time=data.get('departure_time')
                price=data.get('price')
                print("Flight details:")
                print("Flight name:",flight_name)
                print("Flight destination:", destination)
                cur.execute('''Select "flight_id" from "public"."Flights" where ("flightname"=%s AND "flightdestination"=%s)''',(flight_name,destination))
                row=cur.fetchone()
                if row:
                    flightnumber=row[0]
                
                else:
                    raise Exception("Flight not found")
                print(flightnumber)
                

                
                cur.execute('''Insert INTO "public"."Flights"("flight_id","user_id,"flight_name","destination","departure_date","arrival_date","departure_time","arrival_time") VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',(flight_id,user_id,flight_name,destination,departure_date,arrival_date,arrival_time,departure_time,price))

                
                con.commit()
                cur.close()
                return 0, "Flight details inserted successfully"
        except(Exception,psycopg2.DatabaseError)as error:
                
                print(error)
                return 1, str(error)
        finally:
                if con is not None:
                    con.close()
                    print("Database connection got closed ")
    def insertHotelDtls(self,data):
        connection=self.connection()
        try:
            cur=connection.cursor()
            hotel_id=str(uuid.uuid4())
            user_id=data.get("user_id")
            name=data.get('name')
            Location=data.get('Location')
            Checkin_date=data.get('Checkin_date')
            Checkin_time=data.get('Checkin_time')
            Checkout_date=data.get('Checkout_date')
            Checkout_time=data.get('Checkout_time')
            price=data.get('price')
            cur.execute('''Insert INTO "Hotels"("hotel_id","user_id","name","Location","Checkin_time","Checkin_date","Checkout_date","Checkout_time","price") values(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(hotel_id,user_id,name,Location,Checkin_time,Checkin_date,Checkout_date,Checkout_time,price))
            
            connection.commit()
            cur.close()
            return 0,"Success"
        except(Exception,psycopg2.DatabaseError)as error:
            print(error)
            return -1,str(error)
        finally:
            if connection is not None:
                connection.close()

    def insertcarRentalDtls(self,data):
        
        try:
            cont=self.connection
            cur=cont.cursor()
            carrental_id=str(uuid.uuid4())
            user_id=data.get('user_id')
            car_type=data.get('car_type')
            Location=data.get('Location')
            
            pickup_time=data.get('pickup_time')
            price=data.get('price')
            
            
            cur.execute('Insert INTO "public"."Car_rentals"("carrental_id","user_id","car_type","Location","pickup_time","price") Values(%s,%s,%s,%s,%s,%s,)',(carrental_id,user_id,car_type,Location,pickup_time,price))
            
           
            cont.commit()
            cur.close()
            return 0,"Success"
        except(Exception,psycopg2.DatabaseError)as error:
            print(error)
            return -1,str(error)
        finally:
            if cont is not None:
                cont.close()    
    
    def getFlight(self,data):
        connn=self.connection()
        try:
            curs=connn.cursor
            user_id=data.get('user_id')
            get_script="""SELECT * FROM "public"."Flights WHERE ("user_id=%s")"""
            curs.execute(get_script(user_id))
            
            flights=curs.fetchall()
            return(flights)
        except (Exception,psycopg2.DatabaseError)as error:
            print(f"Error:{str(error)}")
            connn.close
            
            
    def bookFlight(self,data):
        data = request.get_json()
        
        con=self.connection()
        try:
            
            cur=con.cursor()
            flightBookingId=str(uuid.uuid4())
           
            flightdestination=data.get('flightdestination')
            flightname=data.get('flightname')
            userId=data.get('user_id')
            arrivaltime=data.get('arrival_time')
            departuretime=data.get('departure_time')
           
            numberofperson=data.get('numberofperson')
            isfoodincluded=data.get('isfoodincluded')
            fare=data.get('fare')
            print("Flight details:")
            print("Flight name:", flightname)
            print("Flight destination:", flightdestination)
            cur.execute('''Select "flightnumber" from "flight" where ("flightname"=%s AND "flightdestination"=%s)''',(flightname,flightdestination))
            row=cur.fetchone()
            if row:
                flightnumber=row[0]
               
            else:
                raise Exception("Flight not found")
            print(flightnumber)
           
           
            cur.execute('''Insert INTO "flight_bookings"("flightbooking_id","flightnumber","user_id","arrival_time","departure_time","numberofperson","isfoodincluded","fare") VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',(flightBookingId,flightnumber,userId,arrivaltime,departuretime,numberofperson,isfoodincluded,fare))
           
 
           
            con.commit()
            cur.close()
            return 0, "Flight details inserted successfully"
        except(Exception,psycopg2.DatabaseError)as error:
            print(error)
            return 1, str(error)
        finally:
            if con is not None:
                con.close()
                print("Database connection got closed ")
 

        
    def bookCar(self,data):
        data = request.get_json()
        user_id=data.get('user_id')
        carrental_id=data.get('carrental_id')
        con=self.connection()
        try:
            curr=con.cursor()
            insert_script="""INSERT into "public"."Bookings"("user_id","carrental_id")"""
            curr.execute(insert_script,(user_id,carrental_id))
            con.commit()
            return("Car booked Successfully")
        except (Exception,psycopg2.DatabaseError) as error:
            print(f"Error:{str(error)}")
            curr.close()

    def getHotel(self):
        connn=self.connection
        try:
            curs=connn.cursor()
            get_script="""SELECT * FROM "public"."Hotels"""
            curs.execute(get_script)
            connn.commit()
            hotels=curs.fetchall()
            return(hotels)
        except (Exception,psycopg2.DatabaseError)as error:
            print(f"Error:{str(error)}")
            curs.close()
    def bookHotel(self,data):
        data = request.get_json()
        user_id=data.get('user_id')
        hotel_id=data.get('hotel_id')
        con=self.connection()
        try:
            curr=con.cursor
            insert_script="""INSERT into "public"."Bookings"("user_id","hotel_id")"""
            curr.execute(insert_script,(user_id,hotel_id))
            con.commit()
            return("Hotel booked Successfully")
        except (Exception,psycopg2.DatabaseError)as error:
            print(f"Error:{str(error)}")
            curr.close()
    def review(self,data):
        data = request.get_json()
        user_id=data.get('user_id')
        service_type=data.get('service_type')
        service_id=data.get('service_id')
        rating=data.get('rating')
        comment=data.get('comment')
        cont=self.connection()
        try:
            crs=cont.cursor()
            table_name=" "
            if service_type=="Flights":
                table_name="Flights"
            elif service_type=="Hotels":
                table_name="Hotels"
            elif service_type=="Car Rentals":
                table_name="Car_rentals"
            else:
                return("Invalid Service Type")
            crs.execute("""SELECT * FROM "public"."Reviews" WHERE "service_id=%s""",(service_id,))
            service=crs.fetchone()
            if not service:
                return("Error!")
        
            insert_script=("""INSERT INTO "public"."Reviews"('user_id','service_type','service_id','rating','comment') VALUES(%s,%s,%s,%s,%s) """)
            crs.execute(insert_script,(user_id,service_type,service_id,rating,comment,))
            return("Reviews added successfully!")
        except (Exception,psycopg2.DatabaseError)as error:
            print(f"Error:{str(error)}")
        
        
        



