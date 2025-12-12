-- Задание 1
SELECT
  c."login",
  COUNT(o."id") AS "inDelivery_count"
FROM "Couriers" c
LEFT JOIN "Orders" o
  ON o."courierId" = c."id"
AND o."inDelivery" = true
GROUP BY c."login"
ORDER BY "inDelivery_count" DESC, c."login";

-- Задание 2
SELECT
    "track",
    CASE
        WHEN "finished" = true THEN 2
        WHEN "cancelled" = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders"
ORDER BY "track";
