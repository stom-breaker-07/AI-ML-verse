-- 1. Retrieve all transactions where the payment method is Credit Card.
select * from transaction where Payment_Method = "Credit Card" ;

-- 2. Find items where the fat content is “Low Fat” and the brand is “ITC”.
select * from items where Item_Fat_Content = "Low Fat" and Brand = "ITC" ;

-- 3. Get all outlets established before the year 2000.
select * from outlets where  Outlet_Establishment_Year<2000 ;

-- 4. Show transactions where the unit price is greater than 200.
select * from transaction where Unit_Price > 200 ;

-- 5. Display all outlets located in Tier 3 cities with competitors present.
select * from outlets where  Outlet_Location_Type = "Tier 3";

-- 6. Find all transactions where the units sold are more than 3 and the unit margin is less than 50. 
select * from transaction where Units_Sold > 3 and Unit_Margin < 50 ;

-- 7. List all items belonging to Soft Drinks or Frozen Foods. 
select * from items where Item_Type = "Soft Drinks" or Item_Type = "Frozen Foods" ;

-- 8. Show all outlets whose average income level is between 40,000 and 55,000.
select * from outlets where Average_Income_Level between 40000 and 55000 ;

-- 9. Retrieve all transactions made in the year 2023. 
select * from transaction where year(str_to_date(Transaction_Date,'%d-%m-%Y')) = 2023 ;

-- 10. Find all items whose names contain the word “Energy”.
select * from items where Item_Name like "%Energy%" ;