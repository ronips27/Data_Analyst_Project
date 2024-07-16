use hr;

select * from hr_data;

describe hr_data;

select birthdate from hr_data;

set sql_safe_updates = 0;

update hr_data set birthdate = case
	when birthdate like '%/%' then date_format(str_to_date(birthdate, '%m/%d/%y'),'%Y-%m-%d')
    when birthdate like '%-%' then date_format(str_to_date(birthdate, '%m/%d/%y'),'%Y-%m-%d')
    else null
end;

alter table hr_data
modify column birthdate date;


select hire_date from hr_data;

describe hr_data;

alter table hr_data add column age int;

update hr_data set hire_date = case
	when hire_date like '%/%' then date_format(str_to_date(hire_date, '%m/%d/%y'),'%Y-%m-%d')
    when hire_date like '%-%' then date_format(str_to_date(hire_date, '%m/%d/%y'),'%Y-%m-%d')
    else null
end;



update hr_data 
set age = timestampdiff(YEAR, birthdate, curdate());

select * from hr_data;

select min(age) as youngest, max(age) as oldest from hr_data;

-- Quest

select * from hr_data;

-- 1. what is the gender breakdown of employees in the company?
select gender, count(*) as count from hr_data group by gender; 
-- 2. what is the race / ethnicity breakdown of employees in the company?
select 
	case 
		when age >= 18 and age <= 24 then '18-24'
        when age >= 25 and age <= 34 then '25-34'
        when age >= 35 and age <= 44 then '35-44'
        when age >= 45 and age <= 54 then '44-54'
        when age >= 55 and age <= 64 then '55-64'
		else '65+'
	end as age_group, gender,
    count(*) as count from hr_data group by age_group, gender order by age_group, gender;
select race, count(*) as count from hr_data group by race;
-- 3. what is the age distribution of employees in the company?
select age, count(*) as count from hr_data group by age;
select min(age) as youngest, max(age) as oldest from hr_data;
select 
	case 
		when age >= 18 and age <= 24 then '18-24'
        when age >= 25 and age <= 34 then '25-34'
        when age >= 35 and age <= 44 then '35-44'
        when age >= 45 and age <= 54 then '44-54'
        when age >= 55 and age <= 64 then '55-64'
		else '65+'
	end as age_group,
    count(*) as count from hr_data group by age_group order by age_group;
-- 4. how many employees work at headquarters versus remote locations?
select location, count(*) from hr_data group by location;
-- 5. what is average length of employement for employees who have been terminated?
select 
	round(avg(datediff(term_date, hire_date))/365) as avg_length_work
from hr_data;
	
-- 6. how does the gender distribution vary across departments and job titles?
select department, gender, count(*) as count from hr_data group by department, gender;

-- 7. what is the distribution of job titles across the company?
select jobtitle, count(*) as count from hr_data group by jobtitle order by count desc;

-- 8. which department has the highest turnover rate?
select department,
	total_count,
    terminated_count,
    terminated_count/total_count as termination_rate
from (
	select department,
    count(*) as total_count,
    sum(case when term_date <= curdate() then 1 else 0 end) as terminated_count
    from hr_data
    where age >= 18
    group by department) as subquery
    order by termination_rate desc;

-- 9. what is the distribution of employees across locations by city and state?
select location_state, count(*) as count
from hr_data
group by location_state order by count desc;

-- 10. how has the employee count changed over time based on hire and term dates/
select 
	year,
    hires,
    termination,
    hires - termination as net_change,
    round(((hires - termination)/hires*100),2) as net_change_precent
from(
	select 
		year(hire_date) as year,
        count(*) as hires,
        sum(case when term_date <= curdate() then 1 else 0 end) as termination
        from hr_data
        group by year(hire_date)
        ) as subquery
order by year asc; 

-- 11. what is the tenure distribution for each department?
select department, round(avg(datediff(term_date, hire_date)/365),0) as avg_tenure from hr_data where term_date <= curdate() group by department

