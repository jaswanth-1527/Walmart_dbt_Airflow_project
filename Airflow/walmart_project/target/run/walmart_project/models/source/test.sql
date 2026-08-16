
  
  
  
  create or replace view `walmart`.`dbt_schema`.`test`
  
  as (
    SELECT * FROM `walmart`.`bronze1`.`orders`
  )
