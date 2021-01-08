-- 부분 쿼리 실행 : Ctrl+Enter
-- 전체 테이블 데이터
select * from employees;

-- 부서번호가 3번인 부서의 사람 중 사원번호, 이름, 월급을 출력하라
select emp_id, first_name, salary from employees where department_id=3;

-- 사원번호가 dt1001101인 사람 중 이름, 입사일, 부서 번호를 출력하라.
select first_name, hire_date, department_id from employees where emp_id='dt1001101';

-- 이름이 소희인 사람의 모든 정보를 출력하라.
select * from employees where first_name = '소희';

-- 입사일이 2020-09-07인 사원의 이름, 부서번호, 월급을 출력하라.
select first_name, department_id, salary from employees where hire_date='2020-09-07';

-- 직무가 SI가 아닌 사람의 모든 정보를 출력하라.
select * from employees where job_id!=1;

-- 입사일이 2020-09-07 이후에 입사한 사원의 정보를 출력하라.
select * from employees where hire_date>='2020-09-07';

-- 부서번호 1번을 제외한 모든 사람의 이름, 사원번호, 부서번호를 출력하라.
select first_name, emp_id, department_id from employees where department_id!=1;

-- 메일이 c로 시작하는 사원의 사원번호, 이름, 입사일, 부서번호를 출력하라.
SELECT emp_id, first_name, hire_date, department_id from employees where email Like 'c%';

-- 메일이 r로 시작하고 r로 끝나는 사원의 모든 정보
SELECT * from employees where email Like 'r%r@%';

/**
employees 테이블에서 이름, 급여, 상여, 총액을 구하여 총액 많은 순서로 출력하라 단 상여금이 NULL인 사람은 제외
무슨 뜻인지 모르겠습니당...
*/

/**
3번 부서의 모든 사람들에게 급여의 13%를 보너스로 지불하기로 하였다. 이름, 급여, 보너스금액, 부서번호를 출력하라.
**/
select first_name, salary, salary*0.13 as bonus, department_id from employees;

/**
3번 부서의 연봉을 계산하여 이름, 부서번호, 급여, 연봉을 출력하라. 단 연말에 급여의 150%를 보너스로 지급한다.
   -- 연봉 = sal*12+(sal*1.5)
**/
select first_name, department_id, salary, salary*12+(salary*1.5) as bonus from employees;

/**
부서번호가 2인 부서의 시간당 임금을 계산하여 출력하라. 단 1달의 근무일수는 12일이고 1일 근무시간은 5시간이다.
출력양식은 이름, 급여, 시간당 임금(소수이하 1번째 자리에서 반올림)을 출력하라.
   -- 시급 = sal/일수/시간  -> sal/ 12/5 
   -- round(m, n) m을 소수점 n자리에서 반올림 
**/
select department_id, first_name, salary, round(salary/12/5, 1) as time_salary from employees where department_id=2;

/**
급여가 400부터 500사이의 사람은 급여의 5%를 회비로 지불하기로 하였다. 이를 이름, 급여, 회비(-2자리에서 반올림)를 출력하라.
	-- 회비  = sal * 0.05	
	-- -2자리에서 반올림 : 정수 2번째 자리에서 반올림.. 100단위로  
**/
select first_name, salary, round(salary*0.05, 2) as dues from employees where salary between 4000000 and 5000000;

/**
입사일부터 지금까지의 날짜수를 출력하라. 부서번호, 이름, 입사일, 현재일, 근무일수(소수점이하절삭), 근무년수,
 근무월수(30일 기준)를 출력하라.
	-- 지금 날짜 : sysdate 
	-- 근무 일수 : 현재날짜 - 입사일 = sysdate - hire_date  -> 날짜 - 날짜 : 일수 나옴
	-- 근무 년수 : to_char(sysdate,'YYYY')-to_char(hiredate,'YYYY')
	-- 근무 월수 : 근무일수 / 1달(30일)
**/
-- select department_id, first_name, hire_date, to_char(sysdate(),'YYYYmmdd'), sysdate()-hire_date as 근무일수, to_char(sysdate(),'YYYY')-to_char(hire_date, 'YYYY') as 근무년수, (sysdate()-hire_date)/30 as 근무월수 from employees;
select department_id, first_name, hire_date, date_format(sysdate(), '%Y-%m-%d') as 현재날자, TO_DAYS(sysdate())-TO_DAYS(hire_date) as 근무일수, date_format(sysdate(),'%Y')-date_format(hire_date, '%Y') as 근무년수, round((TO_DAYS(sysdate())-TO_DAYS(hire_date))/30,0) as 근무월수 from employees;
/**
입사일로부터 오늘까지의 일수를 구하여 이름, 입사일, 근무일수를 출력하라.
--round(sysdate-hiredate,0) 근무일수
**/
select first_name, hire_date, round(TO_DAYS(sysdate())-TO_DAYS(hire_date),0) as 근무일수 from employees;

/**
입사일을 2012년 7월 5일의 형태로 이름, 입사일을 출력하라.
	-- 날짜 형시 앞에 fm 은 선행 '0'을 표현하지 않는다는 뜻.. 
	-- 'fmYYYY"년" MM"월" DD"일' 
**/
select first_name, date_format(hire_date, '%Y년 %c월 %e일') from employees;

/**
이름(first_name)의 글자수가 6자이상인 사람의 이름을 앞에서 3자만 구하여 소문자로 이름만을 출력하라.
	-- substr(str, position, length) : str 문자를 positin 부터 length길이 만큼 표현
	-- lower(str)  소문자 변환
	-- length(str)  str의 길이
    전부 한글이름이라 패스..
**/


/**
4번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하라
**/
select max(salary) as 최고, min(salary) as 최저, avg(salary) as 평균, count(emp_id) as 인원수 from employees where department_id=4;

/**
각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하라.
**/
select department_id, max(salary) as 최고, min(salary) as 최저, avg(salary) as 평균, count(emp_id) as 인원수 from employees group by department_id;

/**
각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하라.
**/
select department_id, job_id, first_name, count(emp_id) as 인원수 from employees group by department_id, job_id order by department_id;

/**
같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하라.
**/
select job_id, count(emp_id) as 인원수 from employees group by job_id;

/**
각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하라.
**/
select department_id, avg(salary) as 평균월급, sum(salary) as 전체월급, max(salary) as 최고월급, min(salary) as 최저월급 from employees group by department_id order by 평균월급 desc;