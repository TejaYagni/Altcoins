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
    output_no int
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
CREATE TYPE IF NOT EXISTS altcoins_keyspace.data_type (
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
   type varchar,
   data frozen<data_type> PRIMARY KEY
   );

"""

create_type_datatype2 = """
CREATE TYPE IF NOT EXISTS altcoins_keyspace.data_type2 (
    nonce bigint,
    network text,
    merkle_root text,
    block_no bigint,
    block_hash text,
    difficulty float,
    confirmations int,
    time bigint,
    previous_block_hash text,
    version bigint, 
    cbvalue float,
    ismainchain boolean,
    txs set<text>
);

"""

create_table_altcoins2 = """
CREATE TABLE IF NOT EXISTS altcoins_keyspace.altcoins2 (
    data frozen<data_type2> PRIMARY KEY,
    type text
)
"""
print(session.execute(create_keyspace))
print(session.execute("use altcoins_keyspace"))
print(session.execute(create_type_inputs))
print(session.execute(create_type_outputs))
print(session.execute(create_type_data))
print(session.execute(create_table_altcoins))
print(session.execute(create_type_datatype2))