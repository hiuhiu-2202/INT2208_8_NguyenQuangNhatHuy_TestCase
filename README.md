# Phân tích lớp tương đương và giá trị biên cho các biến đầu vào

Theo kỹ thuật kiểm thử hộp đen, mỗi biến đầu vào được chia thành các **lớp tương đương** hợp lệ và không hợp lệ. Mỗi lớp tương đương đại diện cho một tập giá trị mà hệ thống xử lý tương đồng【4†L90-L94】. Đồng thời, kỹ thuật **giá trị biên** tập trung vào các giá trị ngay sát mép của các lớp này (giá trị biên, giá trị biên ±1, v.v.)【5†L256-L264】 để phát hiện lỗi thường tiềm ẩn tại biên. Áp dụng cho các biến theo ràng buộc đề bài như sau:

- **Tuổi (age):** Giá trị hợp lệ là số nguyên từ 18 đến 65. 
  - *Lớp hợp lệ:* [18, 65] (toàn bộ các giá trị nguyên trong khoảng này đều được coi tương đương)【4†L90-L94】.
  - *Lớp không hợp lệ:* Giá trị < 18 hoặc > 65, và giá trị không phải số nguyên.  
  - *Giá trị kiểm thử gợi ý:* ta chọn các giá trị biên và trung gian đại diện: **17** (invalid), **18** (min hợp lệ), **19** (hợp lệ), **64** (hợp lệ), **65** (max hợp lệ), **66** (invalid). Các giá trị 18 và 65 là biên của miền; 17, 66 là biên ngoài giới hạn【5†L256-L264】.

- **Thu nhập (income):** Giá trị hợp lệ là số thực (làm tròn 1 chữ số thập phân) từ 5.0 đến 500.0 (triệu VNĐ). 
  - *Lớp hợp lệ:* [5.0, 500.0].
  - *Lớp không hợp lệ:* Giá trị < 5.0 hoặc > 500.0, hoặc không đúng định dạng số thực (độ dài thập phân).  
  - *Giá trị kiểm thử gợi ý:* **4.9** (invalid dưới 5.0), **5.0** (min hợp lệ), **5.1** (hợp lệ), **499.9** (hợp lệ), **500.0** (max hợp lệ), **500.1** (invalid trên 500.0). Chọn giá trị biên ±0.1 và giá trị giữa cũng nhằm đảm bảo phủ các kịch bản biên【5†L256-L264】.

- **Điểm tín dụng (credit_score):** Giá trị hợp lệ là số nguyên từ 300 đến 850. 
  - *Lớp hợp lệ:* [300, 850].
  - *Lớp không hợp lệ:* Giá trị < 300 hoặc > 850, hoặc không phải số nguyên.  
  - *Giá trị kiểm thử gợi ý:* **299** (invalid), **300** (min hợp lệ), **301** (hợp lệ), **849** (hợp lệ), **850** (max hợp lệ), **851** (invalid). Tương tự, chọn các giá trị ở biên và sát biên【5†L256-L264】.

Việc chia thành lớp hợp lệ/không hợp lệ như trên cho phép giảm thiểu số lượng testcase bằng cách chọn đại diện từ mỗi lớp【4†L90-L94】【4†L103-L107】. Sau đó, áp dụng phân tích giá trị biên để thêm các giá trị cạnh vùng nhằm phát hiện lỗi tại mép của miền giá trị【5†L256-L264】.

# Bảng quyết định cho logic nghiệp vụ phê duyệt khoản vay

Bảng quyết định (Decision Table) sẽ liệt kê tất cả các kết hợp điều kiện đầu vào và hành động (kết quả) tương ứng【8†L82-L90】【10†L1-L4】. Các điều kiện và kết quả của hệ thống được tóm tắt như sau:

- **Điều kiện 1 – Rủi ro tín dụng (từ credit_score):** High (300–500), Medium (501–700), Low (701–850).
- **Điều kiện 2 – Thu nhập:** <15 (triệu) hoặc ≥15 (triệu).
- **Điều kiện 3 – Hình thức lao động (employment):** C (Contract) hoặc F (Freelance).
- **Kết quả:** APPROVE, MANUAL REVIEW, hoặc REJECT.

Từ các quy tắc nghiệp vụ đề bài, ta có bảng quyết định như sau:

| Rủi ro tín dụng | Thu nhập (triệu) | Employment | Kết quả      |  
|-----------------|------------------|------------|-------------|  
| High (300–500)  | bất kỳ           | C/F        | **REJECT**  |  
| Medium (501–700)| < 15             | C/F        | **REJECT**  |  
| Medium (501–700)| ≥ 15             | C          | **APPROVE** |  
| Medium (501–700)| ≥ 15             | F          | **MANUAL**  |  
| Low (701–850)   | < 15             | C          | **MANUAL**  |  
| Low (701–850)   | < 15             | F          | **REJECT**  |  
| Low (701–850)   | ≥ 15             | C          | **APPROVE** |  
| Low (701–850)   | ≥ 15             | F          | **MANUAL**  |  

- Theo quy tắc: **High Risk** luôn dẫn đến REJECT, không phụ thuộc thu nhập hay hình thức lao động.  
- Nếu **thu nhập < 15** triệu:
  - Freelance (F) hoặc Rủi ro trung bình (Medium) cũng đều bị **REJECT**. 
  - Chỉ trường hợp kết hợp **Low Risk** và **hợp đồng (C)** mới là **MANUAL REVIEW**.
- Nếu **thu nhập ≥ 15** triệu và rủi ro là Medium/Low:
  - Employment = C → **APPROVE**.
  - Employment = F → **MANUAL REVIEW**.  
- Tất cả các kết hợp điều kiện trên được thể hiện trong bảng trên. Việc liệt kê đầy đủ các điều kiện và giá trị có thể của chúng đảm bảo không bỏ sót bất kỳ kịch bản kiểm thử nào【10†L1-L4】.

# Rút gọn bảng quyết định và kịch bản kiểm thử tối thiểu

Dựa vào bảng trên, ta có thể rút gọn số kịch bản cần kiểm thử bằng cách kết hợp các điều kiện cho ra kết quả giống nhau. Tổng cộng có 8 kịch bản tối thiểu đại diện cho tất cả các trường hợp kết quả (APPROVE, MANUAL, REJECT):

1. **REJECT (High Risk):** Credit score trong khoảng 300–500 (ví dụ 400), bất kể income, employment. Kết quả luôn *REJECT*.  
2. **REJECT (Medium, thu nhập <15):** Credit score trong 501–700 (ví dụ 600), income = 10 triệu (<15), employment bất kỳ. Kết quả *REJECT*.  
3. **APPROVE (Medium, thu nhập ≥15, C):** Credit score 501–700 (ví dụ 650), income = 20 triệu (≥15), employment = C. Kết quả *APPROVE*.  
4. **MANUAL (Medium, thu nhập ≥15, F):** Credit score 501–700 (ví dụ 650), income = 20 triệu, employment = F. Kết quả *MANUAL REVIEW*.  
5. **MANUAL (Low, thu nhập <15, C):** Credit score 701–850 (ví dụ 750), income = 10 triệu, employment = C. Kết quả *MANUAL REVIEW*.  
6. **REJECT (Low, thu nhập <15, F):** Credit score 701–850 (ví dụ 750), income = 10 triệu, employment = F. Kết quả *REJECT*.  
7. **APPROVE (Low, thu nhập ≥15, C):** Credit score 701–850 (ví dụ 800), income = 20 triệu, employment = C. Kết quả *APPROVE*.  
8. **MANUAL (Low, thu nhập ≥15, F):** Credit score 701–850 (ví dụ 800), income = 20 triệu, employment = F. Kết quả *MANUAL REVIEW*.  

Mỗi kịch bản trên đảm bảo bao phủ tất cả các tổ hợp điều kiện đầu vào quan trọng và xuất ra mỗi kết quả nghiệp vụ một lần. Bằng cách này, bộ testcase tối thiểu vẫn đáp ứng được yêu cầu kiểm thử toàn bộ các quy tắc nghiệp vụ đã cho【10†L1-L4】.

**Nguồn tham khảo:** Tổng hợp từ tài liệu về kỹ thuật phân vùng tương đương, giá trị biên và bảng quyết định【4†L90-L94】【5†L256-L264】【8†L82-L90】【10†L1-L4】. Các kỹ thuật này giúp xác định hiệu quả bộ giá trị kiểm thử cần thiết.