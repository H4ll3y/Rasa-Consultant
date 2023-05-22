﻿USE ChatBot_Rasa
GO

INSERT INTO Major(Id, Name, Alias)
VALUES
    ('IT', N'Công nghệ thông tin', 'CNTT'),
    ('CS', N'Khoa học máy tính', 'KHMT');

INSERT INTO Subject(Id_Major, Id, Name, Credit, Condition_Subject, Condition_Term, Term, Year, Semester, Alias)
VALUES
    ('IT', 'ML111', N'Triết học Mác-Lênin', 2, NULL, NULL, 1, 1, 1, N'Triết'),
    ('IT', 'ML112', N'Kinh tế chính trị và CNXH khoa học', 3, 'ML111', NULL, 1, 1, 2, NULL),
	('IT', 'ML202', N'Tư tưởng Hồ Chí Minh', 2, 'ML112', NULL, 1, 2, 1, N'Tư tưởng'),
	('IT', 'ML203', N'Đường lối cách mạng của Đảng CS Việt Nam', 3, 'ML202', NULL, 1, 1, 3, NULL),
	('IT', 'CS101', N'Công dân số', 2, NULL, NULL, 1, 1, 1, NULL),
	('IT', 'MA101', N'Logic, suy luận toán học và kỹ thuật đếm', 3, NULL, NULL, 1, 1, 1, NULL),
	('IT', 'CS100', N'Tin đại cương', 2, NULL, NULL, 1, 1, 1, NULL),
	('IT', 'NA151', N'Khoa học môi trường', 2, NULL, NULL, 1, 1, 3, NULL),
	('IT', 'EC101', N'Kinh tế học đại cương', 3, NULL, NULL, 1, 2, 1, NULL),
	('IT', 'VL101', N'Tiếng Việt thực hành', 2, NULL, NULL, 1, 1, 1, NULL),
	('IT', 'SH131', N'Pháp luật đại cương', 2, NULL, NULL, 1, 1, 2, NULL),
	('IT', 'GE101', N'Tiếng Anh sơ cấp 1', 2, NULL, NULL, 1, 1, 1, NULL),
	('IT', 'GE102', N'Tiếng Anh sơ cấp 2', 2, 'GE101', NULL, 1, 1, 2, NULL),
	('IT', 'GE103', N'Tiếng Anh sơ cấp 3', 2, 'GE102', NULL, 1, 1, 3, NULL),
	('IT', 'GE201', N'Tiếng Anh sơ trung cấp 1', 2, 'GE103', NULL, 1, 2, 1, NULL),
	('IT', 'GE202', N'Tiếng Anh sơ trung cấp 2', 2, 'GE201', NULL, 1, 2, 2, NULL),
	('IT', 'GE205', N'Tiếng Anh sơ trung cấp 3', 2, 'GE202', NULL, 1, 2, 3, NULL),
	('IT', 'GE301', N'Tiếng Anh trung cấp 1', 2, 'GE205', NULL, 1, 3, 1, NULL),
	('IT', 'GE303', N'Tiếng Anh trung cấp 2', 2, 'GE301', NULL, 1, 3, 2, NULL),
	('IT', 'GE305', N'Tiếng Anh trung cấp 3', 2, 'GE303', NULL, 1, 3, 3, NULL),
	('IT', 'GF101', N'Tiếng Pháp 1', 2, NULL, NULL, 1, 3, 2, NULL),
	('IT', 'GF102', N'Tiếng Pháp 2', 2, 'GF101', NULL, 1, 3, 3, NULL),
	('IT', 'GJ101', N'Tiếng Nhật 1', 2, NULL, NULL, 1, 3, 2, NULL),
	('IT', 'GJ102', N'Tiếng Nhật 2', 2, 'GJ101', NULL, 1, 3, 3, NULL),
	('IT', 'GZ101', N'Tiếng Trung 1', 2, NULL, NULL, 1, 3, 2, NULL),
	('IT', 'GZ102', N'Tiếng Trung 2', 2, 'GZ101', NULL, 1, 3, 3, NULL),
	('IT', 'GI101', N'Tiếng Ý 1', 2, NULL, NULL, 1, 3, 2, NULL),
	('IT', 'GI102', N'Tiếng Ý 2', 2, 'GI101', NULL, 1, 3, 3, NULL),
	('IT', 'GK101', N'Tiếng Hàn 1', 2, NULL, NULL, 1, 3, 2, NULL),
	('IT', 'GK102', N'Tiếng Hàn 2', 2, 'GK101', NULL, 1, 3, 3, NULL),
	('IT', 'PG100', N'Giáo dục thể chất', 4, NULL, NULL, 1, 1, 1, NULL),
	('IT', 'PG121', N'Giáo dục quốc phòng', 4, NULL, NULL, 1, 1, 1, NULL),

	('IT', 'MA103', N'Số và cấu trúc đại số', 3, 'MA101', NULL, 2, 1, 3, NULL),
	('IT', 'MA110', N'Giải tích 1', 3, 'MA101', NULL, 2, 2, 1, NULL),
	('IT', 'MA111', N'Giải tích 2', 3, 'MA110', NULL, 2, 2, 2, NULL),
	('IT', 'MA120', N'Đại số tuyến tính', 3, 'MA101', NULL, 2, 1, 2, NULL),
	('IT', 'MA231', N'Xác xuất thống kê', 4, 'MA120, CS101', NULL, 2, 2, 3, NULL),
	('IT', 'MI201', N'Toán rời rạc', 3, 'CS122', NULL, 2, 2, 1, NULL),
	('IT', 'CF212', N'Cấu trúc dữ liệu', 3, 'CS122', NULL, 2, 2, 2, NULL),
	('IT', 'CS110', N'Kỹ thuật số', 2, 'MA101', NULL, 2, 1, 2, NULL),
	('IT', 'CS121', N'Ngôn ngữ lập trình', 3, 'CS100', NULL, 2, 1, 2, NULL),
	('IT', 'CS122', N'Lập trình hướng đối tượng', 3, 'CS121', NULL, 2, 1, 3, NULL),
	('IT', 'CS212', N'Kiến trúc máy tính', 3, 'CS110, CS122', NULL, 2, 1, 3, NULL),
	('IT', 'CS315', N'Nguyên lý hệ điều hành', 3, 'CS212', NULL, 2, 2, 3, NULL),
	('IT', 'IS222', N'Cơ sở dữ liệu', 3, 'CS121, MA103', NULL, 2, 2, 2, NULL),
	('IT', 'NW212', N'Mạng máy tính', 2, 'CS212', NULL, 2, 2, 1, NULL),

	('IT', 'IS314', N'Hệ thống thông tin', 3, 'IS222', NULL, 3, 3, 2, NULL),
	('IT', 'IS322', N'Hệ quản trị cơ sở dữ liệu', 2, 'IS222', NULL, 3, 3, 3, NULL),
	('IT', 'IS329', N'Dữ liệu lớn', 2, 'IS222', NULL, 3, 3, 3, NULL),
	('IT', 'IS332', N'Phân tích thiết kế hướng đối tượng', 3, 'CS122, IS222', NULL, 3, 3, 1, NULL),
	('IT', 'IS334', N'Quản lý dự án hệ thống thông tin', 3, 'IS314', NULL, 3, 3, 3, NULL),
	('IT', 'MI322', N'Trí tuệ nhân tạo và công nghệ tri thức', 3, 'MI201, CF212', NULL, 3, 3, 1, NULL),
	('IT', 'SE302', N'Công nghệ phần mềm', 2, 'IS322', NULL, 3, 3, 2, NULL),
	('IT', 'CS311', N'Lập trình ứng dụng di động', 2, 'CS122', NULL, 3, 3, 1, NULL),
	('IT', 'IT320', N'Lập trình Python', 3, 'MA120, CF212', NULL, 3, 3, 2, NULL),
	('IT', 'IT332', N'Internet of Things', 2, 'SE302', NULL, 3, 4, 1, 'IOT'),
	('IT', 'IT333', N'Công nghệ Web', 3, 'NW212', NULL, 3, 3, 3, NULL),
	('IT', 'IT380', N'Dự án Công nghệ thông tin', 2, 'IS314', NULL, 3, 4, 1, NULL),
	
	('IT', 'CF211', N'Phân tích và thiết kế thuật toán', 2, 'CS121', NULL, 4, 4, 0, NULL),
	('IT', 'CS223', N'Lập trình Java', 3, 'CS122', NULL, 4, 4, 0, NULL),
	('IT', 'CS224', N'Lập trình .Net', 3, 'IS222', NULL, 4, 4, 0, NULL),
	('IT', 'CS320', N'Học máy', 3, 'MA231', NULL, 4, 4, 0, NULL),
	('IT', 'CS325', N'Lập trình PHP', 3, 'IS222', NULL, 4, 4, 0, NULL),
	('IT', 'IS324', N'Phân tích cơ sở dữ liệu', 3, 'IS322', NULL, 4, 4, 0, NULL),
	('IT', 'IS424', N'Lập trình cơ sở dữ liệu', 3, 'IS322', NULL, 4, 4, 0, NULL),
	('IT', 'SE312', N'Kiểm thử và đảm bảo chất lượng phần mềm', 3, 'SE302', NULL, 4, 4, 0, NULL),
	('IT', 'MI312', N'Đồ họa', 2, 'CS122, MA120', NULL, 4, 4, 0, NULL),
	('IT', 'MI414', N'Giao diện người máy', 2, 'MI312', NULL, 4, 4, 0, NULL),

	('IT', 'IP404', N'Thực tập ngành CNTT', 2, NULL, 100, 5, 4, 0, N'Thực tập'),
	('IT', 'IT499', N'KLTN ngành CNTT', 6, NULL, 120, 5, 4, 0, N'Khoá luận'),
	('IT', 'IS484', N'CĐTN: Cơ sở dữ liệu', 6, 'IS322', 110, 5, 4, 0, N'Chuyên đề'),
	('IT', 'SE487', N'CĐTN: CĐTN: Phát triển phần mềm', 6, 'SE302', 110, 5, 4, 0, N'Chuyên đề');

Use ChatBot_Rasa
GO
SELECT Name FROM Subject WHERE Subject.Id = 'CS100'