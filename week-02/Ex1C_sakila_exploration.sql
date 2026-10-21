/*
a) The actor tables stores perosnal information about actors: actor_id, first_name, last_name, last_update, with actor_id being the PK.
b) The film tables stores information related to films such as: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update.
c) The film_actor table contains colums fot both actor_id and film_id.
d) The rental table includes records of movie rental transactions such as: rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update.
e) The inventory table tracks copies of movies available across store loacations such as: inventory_id, film_id, store_id, last_update.
f) to find the names of the films rented on specific data, you need three tables: rental, inventory, and films, they are related becasue the rental connects to inventory using inventory_id and inventory connects to films using film_id.
*/

SELECT rental_date FROM rental;
SELECT inventory_id FROM inventory;
SELECT title FROM film;
