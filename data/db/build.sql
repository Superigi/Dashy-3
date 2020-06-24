CREATE TABLE IF NOT EXISTS exp(
    UserID interger PRIMARY KEY,
    XP interger DEFAULT 0,
    Level interger DEFAULT 0,
    XpPLock text DEFAULT CURRENT_TIMESTAMP
);