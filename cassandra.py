from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect()
create_keyspace = "CREATE KEYSPACE IF NOT EXISTS altcoins" \
                  " WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':1};"
create_type_inputs = "CREATE TYPE IF NOT EXISTS inputs_type("\
                    "previous_txid varchar"\
                    "type varchar"\
                    "address varchar"\
                    "amount float"\
                    "script varchar"\
                    "input_no int;"
create_type_outputs = "CREATE TYPE IF NOT EXISTS outputs_type("\
                    "type varchar"\
                    "address varchar"\
                    "amount float"\
                    "script varchar"\
                    "output_no int;"

create_type_date = "CREATE TYPE IF NOT EXISTS data ("\
                    "txid varchar,"\
                    "confirmations boolean,"\
                    "block_hash varchar"\
                    "block_no int"\
                    "block_time timestamp"\
                    "received_at timestamp"\
                    "network_fee float"\
                    "amount_received float"\
                    "is_green boolean"\
                    "inputs set<frozen<inputs_type>>"\
                    "outputs set<frozen<outputs_type>>"
create_table_transport = """

CREATE TABLE altcoins(
   head_rt_version double PRIMARY KEY,
   head_time_stamp timestamp,  
   head_user_data varchar,
   id varchar,
   is_deleted Boolean,
   trip_id bigint,
   route_id int,
   start_date date,
   schedule_relationship int,
   vehicle_id int,
   vehicle_label int,
   latitude double,
   longitude double,
   bearing int,
   odometer float,
   speed float,
   current_stop_sequence int,
   current_status int,
   vehicle_time_stamp timestamp,
   vehicle_congestion_level int
   )

"""
print(session.execute(create_keyspace))
print(session.execute("use Transport_keyspace"))
print(session.execute(create_table_transport))