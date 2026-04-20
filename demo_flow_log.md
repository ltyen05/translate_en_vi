# 📋 NHẬT KÝ LUỒNG DỊCH THUẬT RAG (FULL FLOW)

**Thời gian thực hiện**: 2026-04-21 00:04:06
**Thời gian xử lý AI**: 27.59 giây

## 1. 📥 ĐẦU VÀO (USER INPUT)
```text
Ménière's disease is a chronic disorder of the inner ear that primarily affects hearing and balance. It is characterized by episodes of vertigo, tinnitus, hearing loss, and a feeling of fullness in the ear. The exact cause of the disease is not well understood, but it is believed to be related to an accumulation of fluid, known as endolymph, in the inner ear. This fluid buildup can interfere with the normal signals between the ear and the brain, leading to the symptoms mentioned above. Diagnosis typically involves a combination of clinical evaluation, hearing tests, and vestibular function tests. Imaging studies, such as MRI, may also be used to rule out other potential causes of the symptoms. Treatment options for Ménière's disease aim to manage the frequency and severity of episodes. These can include lifestyle modifications, such as a low-salt diet, and medications to control vertigo and nausea. In more severe cases, medical procedures like intratympanic steroid injections or surgery may be considered for the patient.
```

## 2. 🔍 NGỮ CẢNH TRUY XUẤT (RAG CONTEXT)
```text
[NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]
- Tiếng Anh: Meniere Disease (Meniere's Disease; Endolymphatic Hydrops) By Mickie Hamiter, MD, New York Presbyterian Columbia Reviewed / Revised May 2023 View Patient Education Symptoms and Signs Diagnosis Treatment Key Points Meniere disease is an inner ear disorder that causes vertigo, nausea, fluctuating sensorineural hearing loss, and tinnitus.
  Nghĩa: Bệnh Meniere (Bệnh Meniere, sũng nước mê nhĩ) Theo Lawrence R. Lustig, MD, Columbia University Medical Center and New York Presbyterian Hospital Đánh giá về mặt y tế Thg6 2021 | đã sửa đổi Thg9 2022 Triệu chứng và Dấu hiệu Chẩn đoán Điều trị Những điểm chính Bệnh Meniere là rối loạn tai trong gây ra chóng mặt, mất thính giác về nghe kém tiếp nhận dao động và ù tai.
- Tiếng Anh: Treatment of Meniere Disease Symptom relief with antiemetics, antihistamines, or benzodiazepines Diuretics and low-salt diet Rarely vestibular ablation by medications or surgery Meniere disease tends to be self-limited.
  Nghĩa: Điều trị Bệnh Meniere Giảm triệu chứng bằng thuốc chống nôn, thuốc kháng histamine, hoặc benzodiazepine Thuốc lợi tiểu và chế độ ăn ít muối Hiếm khi huỷ diệt tiền đình bằng thuốc hoặc phẫu thuật Bệnh Meniere có xu hướng tự giới hạn.
- Tiếng Anh: Patients with symptoms suggesting Meniere disease should have an and an MRI (with gadolinium enhancement) of the central nervous system with attention to the internal auditory canals to exclude other causes.
  Nghĩa: Bệnh nhân có triệu chứng gợi ý bệnh Meniere nên đo thính lực đồ và chụp MRI (có tiêm đối quang từ) của nội sọ với sự chú ý đến các tai trong để loại trừ các nguyên nhân khác.
- Tiếng Anh: Diagnosis of Meniere Disease Clinical evaluation Audiogram and gadolinium-enhanced MRI to rule out other causes The diagnosis of Meniere disease is made clinically.
  Nghĩa: Chẩn đoán Bệnh Meniere Đánh giá lâm sàng Thính lực đồ và MRI tiêm đối quang từ để loại trừ các nguyên nhân khác Chẩn đoán bệnh Meniere được dựa vào lâm sàng.
- Tiếng Anh: Although bilateral Meniere disease can occur, bilateral symptoms increase the likelihood of an alternate diagnosis (eg, vestibular migraine).
  Nghĩa: Mặc dù có thể xảy ra bệnh Meniere hai bên nhưng các triệu chứng hai bên sẽ làm tăng khả năng xảy ra chẩn đoán thay thế (ví dụ như migraine tiền đình).
- Tiếng Anh: The absence of concomitant tinnitus or hearing loss is a hallmark of vestibular neuronitis and helps distinguish it from Meniere disease as well as labyrinthitis.
  Nghĩa: Sự vắng mặt của chứng ù tai hoặc mất thính giác đồng thời là dấu hiệu của viêm thần kinh tiền đình và giúp phân biệt nó với Bệnh Meniere cũng như viêm mê nhĩ.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.

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
- Tiếng Anh: Meniere Disease (Meniere's Disease; Endolymphatic Hydrops) By Mickie Hamiter, MD, New York Presbyterian Columbia Reviewed / Revised May 2023 View Patient Education Symptoms and Signs Diagnosis Treatment Key Points Meniere disease is an inner ear disorder that causes vertigo, nausea, fluctuating sensorineural hearing loss, and tinnitus.
  Nghĩa: Bệnh Meniere (Bệnh Meniere, sũng nước mê nhĩ) Theo Lawrence R. Lustig, MD, Columbia University Medical Center and New York Presbyterian Hospital Đánh giá về mặt y tế Thg6 2021 | đã sửa đổi Thg9 2022 Triệu chứng và Dấu hiệu Chẩn đoán Điều trị Những điểm chính Bệnh Meniere là rối loạn tai trong gây ra chóng mặt, mất thính giác về nghe kém tiếp nhận dao động và ù tai.
- Tiếng Anh: Treatment of Meniere Disease Symptom relief with antiemetics, antihistamines, or benzodiazepines Diuretics and low-salt diet Rarely vestibular ablation by medications or surgery Meniere disease tends to be self-limited.
  Nghĩa: Điều trị Bệnh Meniere Giảm triệu chứng bằng thuốc chống nôn, thuốc kháng histamine, hoặc benzodiazepine Thuốc lợi tiểu và chế độ ăn ít muối Hiếm khi huỷ diệt tiền đình bằng thuốc hoặc phẫu thuật Bệnh Meniere có xu hướng tự giới hạn.
- Tiếng Anh: Patients with symptoms suggesting Meniere disease should have an and an MRI (with gadolinium enhancement) of the central nervous system with attention to the internal auditory canals to exclude other causes.
  Nghĩa: Bệnh nhân có triệu chứng gợi ý bệnh Meniere nên đo thính lực đồ và chụp MRI (có tiêm đối quang từ) của nội sọ với sự chú ý đến các tai trong để loại trừ các nguyên nhân khác.
- Tiếng Anh: Diagnosis of Meniere Disease Clinical evaluation Audiogram and gadolinium-enhanced MRI to rule out other causes The diagnosis of Meniere disease is made clinically.
  Nghĩa: Chẩn đoán Bệnh Meniere Đánh giá lâm sàng Thính lực đồ và MRI tiêm đối quang từ để loại trừ các nguyên nhân khác Chẩn đoán bệnh Meniere được dựa vào lâm sàng.
- Tiếng Anh: Although bilateral Meniere disease can occur, bilateral symptoms increase the likelihood of an alternate diagnosis (eg, vestibular migraine).
  Nghĩa: Mặc dù có thể xảy ra bệnh Meniere hai bên nhưng các triệu chứng hai bên sẽ làm tăng khả năng xảy ra chẩn đoán thay thế (ví dụ như migraine tiền đình).
- Tiếng Anh: The absence of concomitant tinnitus or hearing loss is a hallmark of vestibular neuronitis and helps distinguish it from Meniere disease as well as labyrinthitis.
  Nghĩa: Sự vắng mặt của chứng ù tai hoặc mất thính giác đồng thời là dấu hiệu của viêm thần kinh tiền đình và giúp phân biệt nó với Bệnh Meniere cũng như viêm mê nhĩ.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.

[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]
- 'Ménière s disease': Bệnh Ménière (Lĩnh vực: medical_glossary)

* Văn bản nguồn: Ménière's disease is a chronic disorder of the inner ear that primarily affects hearing and balance. It is characterized by episodes of vertigo, tinnitus, hearing loss, and a feeling of fullness in the ear. The exact cause of the disease is not well understood, but it is believed to be related to an accumulation of fluid, known as endolymph, in the inner ear. This fluid buildup can interfere with the normal signals between the ear and the brain, leading to the symptoms mentioned above. Diagnosis typically involves a combination of clinical evaluation, hearing tests, and vestibular function tests. Imaging studies, such as MRI, may also be used to rule out other potential causes of the symptoms. Treatment options for Ménière's disease aim to manage the frequency and severity of episodes. These can include lifestyle modifications, such as a low-salt diet, and medications to control vertigo and nausea. In more severe cases, medical procedures like intratympanic steroid injections or surgery may be considered for the patient.
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
- Tiếng Anh: Meniere Disease (Meniere's Disease; Endolymphatic Hydrops) By Mickie Hamiter, MD, New York Presbyterian Columbia Reviewed / Revised May 2023 View Patient Education Symptoms and Signs Diagnosis Treatment Key Points Meniere disease is an inner ear disorder that causes vertigo, nausea, fluctuating sensorineural hearing loss, and tinnitus.
  Nghĩa: Bệnh Meniere (Bệnh Meniere, sũng nước mê nhĩ) Theo Lawrence R. Lustig, MD, Columbia University Medical Center and New York Presbyterian Hospital Đánh giá về mặt y tế Thg6 2021 | đã sửa đổi Thg9 2022 Triệu chứng và Dấu hiệu Chẩn đoán Điều trị Những điểm chính Bệnh Meniere là rối loạn tai trong gây ra chóng mặt, mất thính giác về nghe kém tiếp nhận dao động và ù tai.
- Tiếng Anh: Treatment of Meniere Disease Symptom relief with antiemetics, antihistamines, or benzodiazepines Diuretics and low-salt diet Rarely vestibular ablation by medications or surgery Meniere disease tends to be self-limited.
  Nghĩa: Điều trị Bệnh Meniere Giảm triệu chứng bằng thuốc chống nôn, thuốc kháng histamine, hoặc benzodiazepine Thuốc lợi tiểu và chế độ ăn ít muối Hiếm khi huỷ diệt tiền đình bằng thuốc hoặc phẫu thuật Bệnh Meniere có xu hướng tự giới hạn.
- Tiếng Anh: Patients with symptoms suggesting Meniere disease should have an and an MRI (with gadolinium enhancement) of the central nervous system with attention to the internal auditory canals to exclude other causes.
  Nghĩa: Bệnh nhân có triệu chứng gợi ý bệnh Meniere nên đo thính lực đồ và chụp MRI (có tiêm đối quang từ) của nội sọ với sự chú ý đến các tai trong để loại trừ các nguyên nhân khác.
- Tiếng Anh: Diagnosis of Meniere Disease Clinical evaluation Audiogram and gadolinium-enhanced MRI to rule out other causes The diagnosis of Meniere disease is made clinically.
  Nghĩa: Chẩn đoán Bệnh Meniere Đánh giá lâm sàng Thính lực đồ và MRI tiêm đối quang từ để loại trừ các nguyên nhân khác Chẩn đoán bệnh Meniere được dựa vào lâm sàng.
- Tiếng Anh: Although bilateral Meniere disease can occur, bilateral symptoms increase the likelihood of an alternate diagnosis (eg, vestibular migraine).
  Nghĩa: Mặc dù có thể xảy ra bệnh Meniere hai bên nhưng các triệu chứng hai bên sẽ làm tăng khả năng xảy ra chẩn đoán thay thế (ví dụ như migraine tiền đình).
- Tiếng Anh: The absence of concomitant tinnitus or hearing loss is a hallmark of vestibular neuronitis and helps distinguish it from Meniere disease as well as labyrinthitis.
  Nghĩa: Sự vắng mặt của chứng ù tai hoặc mất thính giác đồng thời là dấu hiệu của viêm thần kinh tiền đình và giúp phân biệt nó với Bệnh Meniere cũng như viêm mê nhĩ.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.

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
Dịch câu này: Ménière's disease is a chronic disorder of the inner ear that primarily affects hearing and balance. It is characterized by episodes of vertigo, tinnitus, hearing loss, and a feeling of fullness in the ear. The exact cause of the disease is not well understood, but it is believed to be related to an accumulation of fluid, known as endolymph, in the inner ear. This fluid buildup can interfere with the normal signals between the ear and the brain, leading to the symptoms mentioned above. Diagnosis typically involves a combination of clinical evaluation, hearing tests, and vestibular function tests. Imaging studies, such as MRI, may also be used to rule out other potential causes of the symptoms. Treatment options for Ménière's disease aim to manage the frequency and severity of episodes. These can include lifestyle modifications, such as a low-salt diet, and medications to control vertigo and nausea. In more severe cases, medical procedures like intratympanic steroid injections or surgery may be considered for the patient.<|im_end|>
<|im_start|>assistant

```

## 4. 📤 KẾT QUẢ ĐẦU RA (AI TRANSLATION)
**Dịch sang tiếng Việt**:

> Bệnh Meniere là một rối loạn mãn tính của tai trong chủ yếu ảnh hưởng đến nghe và cân bằng. Bệnh được đặc trưng bởi các cơn chóng mặt, ù tai, mất thính lực và cảm giác đầy tai. Cái gọi là nguyên nhân chính xác của bệnh chưa được hiểu rõ, nhưng được cho là liên quan đến sự tích tụ của chất lỏng, được gọi là endolymph, trong tai trong. Sự tích tụ chất lỏng này có thể làm gián đoạn các tín hiệu bình thường giữa tai và não, dẫn đến các triệu chứng được nêu trên. Chẩn đoán thường bao gồm sự kết hợp của đánh giá lâm sàng, các bài kiểm tra nghe và các bài kiểm tra chức năng tiền đình. Các nghiên cứu hình ảnh, như MRI, cũng có thể được sử dụng để loại trừ các nguyên nhân tiềm năng khác của triệu chứng. Các lựa chọn điều trị cho bệnh Meniere nhằm quản lý tần suất và mức độ nghiêm trọng của các cơn. Những điều này có thể bao gồm các thay đổi lối sống, như chế độ ăn ít muối, và thuốc để kiểm soát chóng mặt và buồn nôn. Trong các trường hợp nặng hơn, các thủ thuật y khoa như tiêm steroid qua màng nhĩ hoặc phẫu thuật có thể được xem xét cho bệnh nhân.
