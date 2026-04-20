# 📋 NHẬT KÝ LUỒNG DỊCH THUẬT RAG (FULL FLOW)

**Thời gian thực hiện**: 2026-04-20 23:56:40
**Thời gian xử lý AI**: 13.66 giây

## 1. 📥 ĐẦU VÀO (USER INPUT)
```text
The patient presented with persistent vertigo and hearing loss. Upon examination, a diagnosis of Meniere's disease was suspected, and an intratympanic steroid injection was recommended to alleviate the symptoms.
```

## 2. 🔍 NGỮ CẢNH TRUY XUẤT (RAG CONTEXT)
```text
[NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]
- Tiếng Anh: Fluctuating unilateral hearing loss accompanied by aural fullness, tinnitus, and vertigo also suggests Meniere syndrome.
  Nghĩa: Nghe kém một bên dao động kèm theo đầy tai, ù tai và chóng mặt cũng gợi ý hội chứng Meniere.
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Patients with marked hearing loss or severe vertigo are evaluated by an otolaryngologist as soon as possible.
  Nghĩa: Bệnh nhân có dấu nghe kém hoặc nghiêm trọng chóng mặt được đánh giá bởi một chuyên gia về tai mũi họng càng sớm càng tốt.
- Tiếng Anh: Vestibular neurectomy (an intracranial procedure) relieves vertigo in about 95% of patients and usually preserves hearing.
  Nghĩa: Phẫu thuật cắt dây thần kinh tiền đình (thủ thuật nội sọ) làm giảm chóng mặt ở khoảng 95% bệnh nhân và thường bảo quản thính giác.
- Tiếng Anh: To prevent permanent vestibuloauditory damage, symptoms of hearing loss, tinnitus, or vertigo require urgent referral to an otolaryngologist.
  Nghĩa: Để dự phòng tổn thương tiền đình thính giác vĩnh viễn, cần chuyển chuyên khoa tai mũi họng khi bệnh nhân có nghe kém, ù tai hoặc chóng mặt.
- Tiếng Anh: It can be the result of vestibular neuronitis, migraine with vertigo, Meniere disease, head trauma or inner ear surgery.
  Nghĩa: Tình trạng này có thể là kết quả của viêm dây thần kinh tiền đình, đau nửa đầu kèm theo chóng mặt, bệnh Meniere, chấn thương đầu hoặc sau phẫu thuật tai trong.
- Tiếng Anh: Diagnosis of Meniere Disease Clinical evaluation Audiogram and gadolinium-enhanced MRI to rule out other causes The diagnosis of Meniere disease is made clinically.
  Nghĩa: Chẩn đoán Bệnh Meniere Đánh giá lâm sàng Thính lực đồ và MRI tiêm đối quang từ để loại trừ các nguyên nhân khác Chẩn đoán bệnh Meniere được dựa vào lâm sàng.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: The injection can be repeated in 4 weeks if vertigo persists without hearing loss.
  Nghĩa: Tiêm có thể được lặp lại trong 4 tuần nếu chóng mặt vẫn tồn tại mà không có nghe kém.

[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]
- 'Ménière s disease': Bệnh Ménière (Lĩnh vực: medical_glossary)

```

## 3. 🧠 PROMPT CUỐI CÙNG (FINAL PROMPT TO AI)
```text
<|im_start|>system
Bạn là một hệ thống dịch đa ngôn ngữ cấp chuyên gia, được tối ưu cho dịch theo ngữ cảnh (context-aware) và theo lĩnh vực (domain-aware) sử dụng Retrieval-Augmented Generation (RAG).

---

## MỤC TIÊU

Dịch văn bản đầu vào một cách chính xác, đảm bảo:
* Đúng thuật ngữ chuyên ngành
* Phù hợp ngữ cảnh
* Tự nhiên trong ngôn ngữ đích

---

## CẤU TRÚC ĐẦU VÀO

Bạn sẽ nhận được các thông tin sau:
* Lĩnh vực: Đa lĩnh vực
* Từ điển thuật ngữ: Xem danh sách bên dưới
* Ngữ cảnh truy xuất (RAG): [NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]
- Tiếng Anh: Fluctuating unilateral hearing loss accompanied by aural fullness, tinnitus, and vertigo also suggests Meniere syndrome.
  Nghĩa: Nghe kém một bên dao động kèm theo đầy tai, ù tai và chóng mặt cũng gợi ý hội chứng Meniere.
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Patients with marked hearing loss or severe vertigo are evaluated by an otolaryngologist as soon as possible.
  Nghĩa: Bệnh nhân có dấu nghe kém hoặc nghiêm trọng chóng mặt được đánh giá bởi một chuyên gia về tai mũi họng càng sớm càng tốt.
- Tiếng Anh: Vestibular neurectomy (an intracranial procedure) relieves vertigo in about 95% of patients and usually preserves hearing.
  Nghĩa: Phẫu thuật cắt dây thần kinh tiền đình (thủ thuật nội sọ) làm giảm chóng mặt ở khoảng 95% bệnh nhân và thường bảo quản thính giác.
- Tiếng Anh: To prevent permanent vestibuloauditory damage, symptoms of hearing loss, tinnitus, or vertigo require urgent referral to an otolaryngologist.
  Nghĩa: Để dự phòng tổn thương tiền đình thính giác vĩnh viễn, cần chuyển chuyên khoa tai mũi họng khi bệnh nhân có nghe kém, ù tai hoặc chóng mặt.
- Tiếng Anh: It can be the result of vestibular neuronitis, migraine with vertigo, Meniere disease, head trauma or inner ear surgery.
  Nghĩa: Tình trạng này có thể là kết quả của viêm dây thần kinh tiền đình, đau nửa đầu kèm theo chóng mặt, bệnh Meniere, chấn thương đầu hoặc sau phẫu thuật tai trong.
- Tiếng Anh: Diagnosis of Meniere Disease Clinical evaluation Audiogram and gadolinium-enhanced MRI to rule out other causes The diagnosis of Meniere disease is made clinically.
  Nghĩa: Chẩn đoán Bệnh Meniere Đánh giá lâm sàng Thính lực đồ và MRI tiêm đối quang từ để loại trừ các nguyên nhân khác Chẩn đoán bệnh Meniere được dựa vào lâm sàng.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: The injection can be repeated in 4 weeks if vertigo persists without hearing loss.
  Nghĩa: Tiêm có thể được lặp lại trong 4 tuần nếu chóng mặt vẫn tồn tại mà không có nghe kém.

[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]
- 'Ménière s disease': Bệnh Ménière (Lĩnh vực: medical_glossary)

* Văn bản nguồn: The patient presented with persistent vertigo and hearing loss. Upon examination, a diagnosis of Meniere's disease was suspected, and an intratympanic steroid injection was recommended to alleviate the symptoms.
* Ngôn ngữ nguồn: English
* Ngôn ngữ đích: Vietnamese

---

## NGUYÊN TẮC CỐT LÕI

### 1. ƯU TIÊN LĨNH VỰC (CAO NHẤT)
* Luôn ưu tiên nghĩa theo lĩnh vực hơn nghĩa thông thường
* Nếu một thuật ngữ có trong từ điển → BẮT BUỘC dùng chính xác
* Không được đơn giản hóa hoặc thay đổi thuật ngữ chuyên ngành

---

### 2. TUÂN THỦ THUẬT NGỮ
* Phải sử dụng đúng từ điển thuật ngữ đã cung cấp
* Nếu có nhiều nghĩa:
  1. Ưu tiên theo lĩnh vực
  2. Sau đó theo ngữ cảnh
  3. Cuối cùng mới đến nghĩa phổ thông
* Không tự tạo thuật ngữ mới

---

### 3. SỬ DỤNG NGỮ CẢNH (RAG)
* Dùng [NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]
- Tiếng Anh: Fluctuating unilateral hearing loss accompanied by aural fullness, tinnitus, and vertigo also suggests Meniere syndrome.
  Nghĩa: Nghe kém một bên dao động kèm theo đầy tai, ù tai và chóng mặt cũng gợi ý hội chứng Meniere.
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Patients with marked hearing loss or severe vertigo are evaluated by an otolaryngologist as soon as possible.
  Nghĩa: Bệnh nhân có dấu nghe kém hoặc nghiêm trọng chóng mặt được đánh giá bởi một chuyên gia về tai mũi họng càng sớm càng tốt.
- Tiếng Anh: Vestibular neurectomy (an intracranial procedure) relieves vertigo in about 95% of patients and usually preserves hearing.
  Nghĩa: Phẫu thuật cắt dây thần kinh tiền đình (thủ thuật nội sọ) làm giảm chóng mặt ở khoảng 95% bệnh nhân và thường bảo quản thính giác.
- Tiếng Anh: To prevent permanent vestibuloauditory damage, symptoms of hearing loss, tinnitus, or vertigo require urgent referral to an otolaryngologist.
  Nghĩa: Để dự phòng tổn thương tiền đình thính giác vĩnh viễn, cần chuyển chuyên khoa tai mũi họng khi bệnh nhân có nghe kém, ù tai hoặc chóng mặt.
- Tiếng Anh: It can be the result of vestibular neuronitis, migraine with vertigo, Meniere disease, head trauma or inner ear surgery.
  Nghĩa: Tình trạng này có thể là kết quả của viêm dây thần kinh tiền đình, đau nửa đầu kèm theo chóng mặt, bệnh Meniere, chấn thương đầu hoặc sau phẫu thuật tai trong.
- Tiếng Anh: Diagnosis of Meniere Disease Clinical evaluation Audiogram and gadolinium-enhanced MRI to rule out other causes The diagnosis of Meniere disease is made clinically.
  Nghĩa: Chẩn đoán Bệnh Meniere Đánh giá lâm sàng Thính lực đồ và MRI tiêm đối quang từ để loại trừ các nguyên nhân khác Chẩn đoán bệnh Meniere được dựa vào lâm sàng.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: The injection can be repeated in 4 weeks if vertigo persists without hearing loss.
  Nghĩa: Tiêm có thể được lặp lại trong 4 tuần nếu chóng mặt vẫn tồn tại mà không có nghe kém.

[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]
- 'Ménière s disease': Bệnh Ménière (Lĩnh vực: medical_glossary)
 để:
  * Làm rõ nghĩa
  * Đảm bảo tính nhất quán
* Nếu ngữ cảnh mâu thuẫn với kiến thức chung → ưu tiên ngữ cảnh

---

### 4. CHẤT LƯỢNG BẢN DỊCH
* Bản dịch phải:
  * Đúng nghĩa
  * Tự nhiên, trôi chảy
  * Đúng ngữ pháp
* Giữ nguyên tone (technical / formal / neutral)

---

### 5. GIỮ NGUYÊN CẤU TRÚC
* Bảo toàn:
  * Format (markdown, bullet, code…)
  * Số, đơn vị, ký hiệu
* Không thay đổi cấu trúc trừ khi cần thiết

---

### 6. XỬ LÝ MƠ HỒ
Nếu câu hoặc từ mơ hồ:
* Ưu tiên dùng context
* Sau đó dùng domain
* Nếu vẫn chưa rõ:
  * Chọn nghĩa hợp lý nhất theo lĩnh vực
  * Không hỏi lại
  * Không suy diễn thêm

---

### 7. NGĂN NGỪA LỖI
KHÔNG được:
* Bịa nội dung
* Thêm giải thích
* Dịch từng từ nếu làm sai nghĩa
* Bỏ qua cách diễn đạt chuyên ngành

---

### 8. CHIẾN LƯỢC FALLBACK
* Thiếu terminology → suy luận theo domain + context
* Thiếu context → dựa vào domain
* Thiếu cả hai → dịch trung tính nhưng chính xác

---

### 9. RÀNG BUỘC OUTPUT
* Chỉ trả về bản dịch
* Không giải thích
* Không thêm tiền tố như "Bản dịch:"

---

## GỢI Ý LĨNH VỰC (DEFAULT)

* IT: ưu tiên chính xác kỹ thuật (API, model, pipeline…)
* Y tế: ưu tiên chính xác lâm sàng
* Pháp lý: ưu tiên formal và chặt chẽ

---

## KIỂM TRA CUỐI

* Đúng thuật ngữ?
* Đúng ngữ cảnh?
* Đúng lĩnh vực?
* Tự nhiên?

Nếu đạt tất cả → xuất bản dịch.
<|im_end|>
<|im_start|>user
Dịch câu này: The patient presented with persistent vertigo and hearing loss. Upon examination, a diagnosis of Meniere's disease was suspected, and an intratympanic steroid injection was recommended to alleviate the symptoms.<|im_end|>
<|im_start|>assistant

```

## 4. 📤 KẾT QUẢ ĐẦU RA (AI TRANSLATION)
**Dịch sang tiếng Việt**:

> Bệnh nhân có triệu chứng chóng mặt và nghe kém kéo dài. Sau khi khám, chẩn đoán nghi ngờ hội chứng Meniere và được chỉ định tiêm steroid vào tai giữa để giảm triệu chứng.
