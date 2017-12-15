from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect()
create_keyspace = "CREATE KEYSPACE IF NOT EXISTS altcoins_keyspace" \
                  " WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':1};"
create_type_inputs = """
CREATE TYPE IF NOT EXISTS altcoins_keyspace.inputs_type (
    previous_txid text,
    type text,
    address text,
    amount float,
    script text,
    input_no int,
    previous_output_no int,
    confirmed boolean,
    confirmations int,
    unconfirmedinput boolean,
    doublespenttxid bigint
);
"""
create_type_outputs = """
CREATE TYPE IF NOT EXISTS altcoins_keyspace.outputs_type (
    type text,
    address text,
    amount float,
    script text,
    output_no int
);
"""

create_type_data = """
CREATE TYPE altcoins_keyspace.data_type (
    txid text,
    confirmations int,
    block_hash text,
    block_no int,
    block_time bigint,
    received_at bigint,
    network_fee float,
    amount_received float,
    is_green boolean,
    inputs set<frozen<inputs_type>>,
    outputs set<frozen<outputs_type>>,
    network text
);
"""
create_table_altcoins = """

CREATE TABLE IF NOT EXISTS altcoins(
   txid varchar PRIMARY KEY ,
   type varchar,
   data frozen<data_type>
   );

"""
print(session.execute(create_keyspace))
print(session.execute("use altcoins_keyspace"))
print(session.execute(create_type_inputs))
print(session.execute(create_type_outputs))
print(session.execute(create_type_data))
print(session.execute(create_table_altcoins))