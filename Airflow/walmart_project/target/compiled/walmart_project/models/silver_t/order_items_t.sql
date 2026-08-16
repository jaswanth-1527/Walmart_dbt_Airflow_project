
SELECT 
* ,current_timestamp() as processed_at
FROM `walmart`.`bronze1`.`order_items`



    WHERE updated_timestamp > (SELECT COALESCE(MAX(updated_timestamp), '1900-01-01') FROM `walmart`.`silver_t`.`order_items_t`)
