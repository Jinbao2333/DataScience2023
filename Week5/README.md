1. 使用微软 SQL 数据库，并使用 Microsoft SQL Server Management Studio 工作台作为操作程序。
2. 使用 Windows 身份验证直接登录数据库。
3. 完成，已创建新表格。
4. 

```sql
SELECT * FROM [user] WHERE age BETWEEN 20 AND 30;
```

5.  

```sql
DELETE FROM [user] WHERE name LIKE '%zhang%';
```

6.  

```sql
SELECT AVG(age) as average_age FROM [user];
```

7.  

```sql
SELECT * FROM [user] WHERE age BETWEEN 20 AND 30 AND name LIKE '%zhang%' ORDER BY age DESC;
```

8. 完成，已创建新表格。 

```sql
-- 创建 team 表
CREATE TABLE team (
    id INT PRIMARY KEY,
    teamName VARCHAR(255) NOT NULL
);
-- 创建 score 表，设置外键关系
CREATE TABLE score (
    id INT PRIMARY KEY,
    teamid INT,
    userid INT,
    score INT,
    FOREIGN KEY (teamid) REFERENCES team(id),
    FOREIGN KEY (userid) REFERENCES [user](id)
);
```

9.  

```sql
SELECT u.*
FROM [user] u
JOIN score s ON u.id = s.userid
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU' AND u.age < 20;
```

10.  

```sql
SELECT t.teamName, COALESCE(SUM(s.score), 0) AS totalScore
FROM team t
LEFT JOIN score s ON t.id = s.teamid
WHERE t.teamName = 'ECNU'
GROUP BY t.teamName;
```
