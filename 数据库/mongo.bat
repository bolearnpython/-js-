mkdir C:\data\db
mkdir C:\data\log
echo log>>C:\data\log\mongod.log
echo systemLog:>>C:\MongoDB\mongod.cfg
echo     destination: file>>C:\MongoDB\mongod.cfg
echo     path: C:\data\log\mongod.log>>C:\MongoDB\mongod.cfg
echo storage:>>C:\MongoDB\mongod.cfg
echo     dbPath: C:\data\db>>C:\MongoDB\mongod.cfg
"C:/mongodb/bin/mongod.exe" --config "C:\mongodb\mongod.cfg" --install
net start MongoDB