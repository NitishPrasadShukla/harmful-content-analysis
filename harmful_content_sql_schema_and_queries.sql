
CREATE TABLE comments (
    comment_id INT PRIMARY KEY,
    user_id INT,
    comment_text TEXT,
    category VARCHAR(50),
    severity_score INT
);

-- Category distribution
SELECT category, COUNT(*) AS total_comments, AVG(severity_score) AS avg_severity
FROM comments
GROUP BY category
ORDER BY total_comments DESC;

-- High-risk users
WITH user_stats AS (
    SELECT
        user_id,
        COUNT(*) AS total_comments,
        SUM(CASE WHEN severity_score > 0 THEN 1 ELSE 0 END) AS harmful_comments
    FROM comments
    GROUP BY user_id
)
SELECT
    user_id,
    total_comments,
    harmful_comments,
    CAST(harmful_comments AS FLOAT) / total_comments AS harmful_ratio
FROM user_stats
WHERE total_comments >= 5
ORDER BY harmful_ratio DESC, harmful_comments DESC
LIMIT 20;

-- Harmful vs Safe
SELECT
    CASE WHEN severity_score = 0 THEN 'safe' ELSE 'harmful' END AS harm_bucket,
    COUNT(*) AS total
FROM comments
GROUP BY harm_bucket;

-- Top harmful categories
SELECT category, COUNT(*) AS total
FROM comments
WHERE severity_score > 0
GROUP BY category
ORDER BY total DESC;
