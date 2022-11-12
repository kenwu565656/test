SELECT o.owner_id, o.owner_name, count(DISTINCT c.category_id) AS different_category_count
FROM owner AS o, article AS a, category_article_mapping AS c
WHERE a.owner_id = o.owner_id
AND a.owner_id = c.article_id
GROUP BY a.owner_id
ORDER BY count(DISTINCT c.category_id) DESC;