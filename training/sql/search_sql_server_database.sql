use YourDataBaseName

select * from INFORMATION_SCHEMA.COLUMNS 
where COLUMN_NAME like '%ColumnName%'
and TABLE_NAME like '%TableName%'
order by TABLE_NAME
