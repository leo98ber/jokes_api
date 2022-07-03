# jokes_api
Project consuming apis generating jokes about chuck norrys in flask

This project is a simple REST api made with flask and pymongo

The reason why mongoDB was selected is due to several reasons. Easy to save data, lack of structured information for the database, it is a more efficient database and with high compatibility with flask. SQLs are discarded because DJANGO is far superior when it comes to using them in REST APIs. As a last reason at the personal level of the developer and in view of the short time granted, this database was selected.

The project consists of 3 main app files, where the entire response structure of the server is; utils where the standard functions to process the data are defined and consts where relevant variables are stored.

the other files are used to configure and define the vertebrae of the project