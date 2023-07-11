create database APIGNews;
USE APIGNews;

CREATE TABLE `user` (
  `id` smallint(3) UNSIGNED NOT NULL PRIMARY KEY,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password` blob NOT NULL,
  `fullname` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'ThunderGer', 0x98fb67ca8f459f49841208bd4261bceb, 'Luis Gerardo Baeza');

DELIMITER //
CREATE PROCEDURE sp_addUser(IN pUsername VARCHAR(20), IN pPassword VARCHAR(20), IN pFullname VARCHAR(50))
BEGIN
    INSERT INTO user (username, password, fullname)
    VALUES (pUsername, AES_ENCRYPT(pPassword, SHA2('B!1w8*NAt1T^%kvhUI*S^_', 512)), pFullname);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_verifyIdentity(IN pUsername VARCHAR(20), IN pPassword VARCHAR(20))
BEGIN
	SELECT USER.id, USER.username, USER.fullname 
	FROM user USER 
    WHERE 1 = 1 
    AND USER.username = pUsername 
	AND CAST(AES_DECRYPT(USER.password, SHA2('B!1w8*NAt1T^%kvhUI*S^_', 512)) AS CHAR(30)) = pPassword;
END //
DELIMITER ;