docker pull postgres:latest
docker run --name etl-database -e POSTGRES_PASSWORD=root -d -p 5432:5432 postgres:latest

sleep 5

IP_ADDRESS=$(cat ip_address.txt)
echo "Using IP address: $IP_ADDRESS"

docker run -it --network=host postgres psql -h "$IP_ADDRESS" -U postgres -c "CREATE DATABASE \"etl-database\";"

echo "Downloading CSV"
python3 jobs_etl/job_1.py
echo "CSV Downloaded"

echo "Transferring data..."
python3 jobs_etl/job_2.py

docker pull metabase/metabase:latest
docker run -d -p 3000:3000 --name metabase metabase/metabase
