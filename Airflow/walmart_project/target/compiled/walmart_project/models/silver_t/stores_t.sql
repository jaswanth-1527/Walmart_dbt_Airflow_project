
SELECT 
* ,current_timestamp() as processed_at
FROM `walmart`.`bronze1`.`stores`



    WHERE updated_timestamp > (SELECT COALESCE(MAX(updated_timestamp), '1900-01-01') FROM `walmart`.`silver_t`.`stores_t`)
