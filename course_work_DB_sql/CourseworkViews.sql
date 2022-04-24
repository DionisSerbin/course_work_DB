use course_work;

create or replace view PlacePlaceCuisineView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, p.placeID, c.cuisineID from Place as p LEFT JOIN PlaceCuisines as c on p.placeID = c.placeID;

create or replace view PlacePlaceMetroView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, p.placeID, m.metroID from Place as p LEFT JOIN PlaceMetros as m on p.placeID = m.placeID;

create or replace view PlacePlaceAddressView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, p.placeID, a.addressID from Place as p LEFT JOIN PlaceAddresses as a on p.placeID = a.placeID;

create or replace view PlacePlaceAtmosphereView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, p.placeID, a.atmosphereID from Place as p LEFT JOIN PlaceAtmospheres as a on p.placeID = a.placeID;

create or replace view PlacePlaceLeisureView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, p.placeID, l.leisureID from Place as p LEFT JOIN PlaceLeisures as l on p.placeID = l.placeID;

create or replace view PlacePlaceFitView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, p.placeID, f.fitID from Place as p LEFT JOIN PlaceFits as f on p.placeID = f.placeID;

create or replace view PlacePlaceFormatView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, p.placeID, f.formatID from Place as p LEFT JOIN PlaceFormats as f on p.placeID = f.placeID;

create or replace view PlaceCuisinesView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, c.cuisineName, placeID, p.cuisineID from PlacePlaceCuisineView as p LEFT JOIN Cuisine as c on p.cuisineID = c.cuisineID;

create or replace view PlaceMetrosView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, m.metroName, placeID, p.metroID from PlacePlaceMetroView as p LEFT JOIN Metro as m on p.metroID = m.metroID;

create or replace view PlaceAddressesView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, a.addressName, placeID, p.addressID  from PlacePlaceAddressView as p LEFT JOIN Address as a on p.addressID = a.addressID;

create or replace view PlaceAtmospheresView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, a.atmosphereName, placeID, p.atmosphereID from PlacePlaceAtmosphereView as p LEFT JOIN Atmosphere as a on p.atmosphereID = a.atmosphereID;

create or replace view PlaceLeisuresView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, l.leisureName, placeID, p.leisureID from PlacePlaceLeisureView as p LEFT JOIN Leisure as l on p.leisureID = l.leisureID;

create or replace view PlaceFitsView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, f.fitName, placeID, p.fitID from PlacePlaceFitView as p LEFT JOIN Fit as f on p.fitID = f.fitID;

create or replace view PlaceFormatsView as select placeDescription, placeName,
                                placeDogFriendly, placeURL,
                                placePhoto, averageCheck, f.formatName, placeID, p.formatID from PlacePlaceFormatView as p LEFT JOIN Format as f on p.formatID = f.formatID;

create or replace view PlaceView as select p.placeID, p.placeDescription, p.placeName,
                                p.placeDogFriendly, p.placeURL,
                                p.placePhoto, p.averageCheck, c.cuisineName,
                                m.metroName, ad.addressName, at.atmosphereName,
                                l.leisureName, fi.fitName, fo.formatName
                                from Place as p LEFT JOIN PlaceCuisinesView as c on p.placeID = c.placeID
                                LEFT JOIN PlaceMetrosView as m on p.placeID = m.placeID
                                LEFT JOIN PlaceAddressesView as ad on p.placeID = ad.placeID
                                LEFT JOIN PlaceAtmospheresView as at on p.placeID = at.placeID
                                LEFT JOIN PlaceLeisuresView as l on p.placeID = l.placeID
                                LEFT JOIN PlaceFitsView as fi on p.placeID = fi.placeID
                                LEFT JOIN PlaceFormatsView as fo on p.placeID = fo.placeID;

create or replace view UserFavouritesView as select u.userID, u.userName, f.placeID
                                from User as u LEFT JOIN Favourite as f on u.userID = f.userID;

create or replace view UserFavouritesPlacesView as select u.userID, u.userName, u.placeID,
                                p.averageCheck, p.placeDogFriendly, p.placePhoto,
                                p.placeURL, p.placeDescription, p.placeName, p.adminID
                                from UserFavouritesView as u LEFT JOIN Place as p on u.placeID = p.placeID

