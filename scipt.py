import psycopg2
from flask import Flask,jsonify,request
from Myservice import DocumentManager
app=Flask(__name__)
hostname= 'localhost'
username='postgres'
database='doc_manager'
port_id= 5436
pwd= 'admin123'
try:
   
    conn=psycopg2.connect(


        host=hostname,
        user=username,
        database=database,
        password=pwd,
        port=port_id

)
    curr=conn.cursor()
    create_users= '''
    CREATE TABLE IF NOT EXISTS "public"."Documents"(
        "id" SERIAL PRIMARY KEY,
        "title" varchar not null,
        "content" text not null,
        "created at" TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        "updated_at" TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    )
'''
    scripts='''

ALTER TABLE "public"."Documents"
ALTER COLUMN "updated_at" SET DATA TYPE TIMESTAMP WITHOUT TIME ZONE,
ALTER COLUMN "updated_at" SET DEFAULT CURRENT_TIMESTAMP;


ALTER TABLE "public"."Documents"
ADD COLUMN id_new VARCHAR(255);

UPDATE "public"."Documents"
SET id_new = CAST(id AS VARCHAR);

ALTER TABLE "public"."Documents"
DROP COLUMN id;

ALTER TABLE "public"."Documents"
RENAME COLUMN id_new TO id;

ALTER TABLE "public"."Documents"
ADD PRIMARY KEY (id);
'''
    curr.execute(scripts)
    
    conn.commit()

    conn.close()
    
except Exception as Error:
    print(Error)
@app.route("/post",methods=["POST"])
def insertDocumemnt():
        data=request.get_json()
        doc=DocumentManager()
        code,msg= doc.insertDocument(data)
        if code==0:
             return {"code":0,"msg":"success"}
        else:
             return {"code":1,'msg':"Failed"}
       
@app.route("/getdocs",methods=["GET"])
def getDocumemnts():
        id=request.args.get('id')
        manager=DocumentManager()
        details=  manager.fetchDocumentById(id)
        if not details:
              return jsonify({-1:"Please enter a valid id that existed in database"})
        else:
              return jsonify(details)
         
@app.route("/update",methods=["PUT"])
def updateDocumemnts():
        data=request.get_json()
        id=request.args.get('id')
        docs=DocumentManager()
        code,msg=  docs.updateDocument(id,data)
        if code==0:
             return {"code":0,"msg":"success"}
        else:
             return {"code":1,'msg':msg}

@app.route("/deletedoc",methods=["DELETE"])
def deleteDocumemnt():
        id=request.args.get('id')
        code,msg=  DocumentManager().deleteDocument(id)
        if code==0:
             return {"code":0,"msg":"success"}
        else:
             return {"code":1,'msg':"Failed"}

        
            

if __name__=='__main__':
     app.run(host='0.0.0.0',port=1786)


    