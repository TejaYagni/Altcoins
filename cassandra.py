from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect()
create_keyspace = "CREATE KEYSPACE IF NOT EXISTS altcoins_keyspace" \
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

create_type_data = "CREATE TYPE IF NOT EXISTS data_type ("\
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
create_table_altcoins = """

CREATE TABLE altcoins(
   txid varchar,
   type varchar,
   data data_type,
   PRIMARY KEY TXID
   )

"""
print(session.execute(create_keyspace))
print(session.execute("use altcoins_keyspace"))
print(session.execute(create_type_inputs))
print(session.execute(create_type_outputs))
print(session.execute(create_type_data))
print(session.execute(create_table_altcoins))