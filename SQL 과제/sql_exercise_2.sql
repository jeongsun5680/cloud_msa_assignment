/**
3번 부서 월급의 평균ㅡ 최고, 최저, 인원수를 구하여 출력하라
**/
select department_id, max(salary) as 최고, min(salary) as 최저, count(emp_id) as 인원수 from employees where department_id=3;

/**
각 부서별 급여의 평균, 최고, 최저, 인원수를 구하여 출력하라.
**/
select d.department_name, avg(e.salary) as 평균, max(e.salary) as 최고, min(e.salary) as 최저, count(e.emp_id) as 인원수 from employees e, departments d where e.department_id = d.department_id group by e.department_id;

/**
각 부서별 같은 업무를 하는 사람의 인원수를 구하여 부서번호, 업무명, 인원수를 출력하라.
**/
select department_id, job_id, count(emp_id) as 인원수 from employees group by department_id, job_id order by department_id desc;

/**
같은 업무를 하는 사람의 수가 4명 이상인 업무와 인원수를 출력하라.
**/
select job_id, count(emp_id) as 인원수 from employees group by job_id;

/**
각 부서별 평균월급, 전체월급, 최고월급, 최저월급,을 구하여 평균월급이 많은순으로 출력하라.
**/
select d.department_name as 부서명, avg(e.salary) as 평균월급, sum(e.salary) as 전체월급, max(e.salary) as 최고월급, min(e.salary) as 최저월급 from employees e, departments d where e.department_id=d.department_id group by e.department_id order by 평균월급 desc;

/**
 부서번호, 부서명, 이름, 급여를 출력하라.
**/
select d.department_id, d.department_name, e.first_name, e.salary from employees e, departments d where e.department_id=d.department_id;

/**
이름이 혜림인 사원의 부서명을 출력하라.
**/
select e.first_name, d.department_name from employees e, departments d where e.department_id=d.department_id and e.first_name like '혜림';

/**
employees테이블에 있는 employee_id와 manager_id를 이용하여 서로의 관계를 다음과 같이 출력하라
'smith'의 매니저는 'ford'이다.
**/
select a.first_name as 직원, b.first_name as 매니저 from employees a JOIN employees b ON a.manager_id=b.emp_id;

/**
정선의 직무와 같은 직무를 갖는 사람의 이름, 부서명, 급여, 직무를 출력하라.
**/
select A.first_name as 이름, C.department_name as 부서명, A.salary as 급여, A.job_id as 직무 from employees A, (select job_id from employees where first_name='정선') B, departments C where A.job_id=B.job_id and A.department_id=C.department_id;

/**
전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하라.
평균급여 4850000
**/
select A.emp_id, A.first_name, C.department_name, A.hire_date, A.salary from employees A, (select avg(salary) as balance from employees) B, departments C where A.salary>=B.balance and A.department_id=C.department_id;

/**
1번 부서사람들 중에서 4번 부서의 사원과 같은 업무를 하는 사원의 사원번호, 이름, 부서명, 입사일을 출력하라.
**/
select A.emp_id as 사원번호 , A.first_name as 이름, C.department_name as 부서명, A.hire_date as 입사일 from employees A, (select job_id from employees where department_id=4) B, departments C where A.department_id=1 and A.job_id=B.job_id and A.department_id=C.department_id;


/**
급여가 3번 부서의 최고 급여보다 높은 사원의 사원번호, 이름, 급여를 출력하라.
**/
select A.emp_id as 사원번호, A.first_name as 이름, A.salary as 급여 from employees A, (select max(salary) as salary from employees where department_id=3) B where A.salary>B.salary;