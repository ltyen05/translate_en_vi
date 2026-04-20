# 📋 NHẬT KÝ LUỒNG DỊCH THUẬT RAG (FULL FLOW)

**Thời gian thực hiện**: 2026-04-21 00:05:39
**Thời gian xử lý AI**: 30.55 giây

## 1. 📥 ĐẦU VÀO (USER INPUT)
```text
Ménière's disease represents a sophisticated and often debilitating chronic condition of the inner ear that manifests through a complex array of physiological disturbances primarily impacting both auditory perception and vestibular equilibrium in affected individuals. This pathological state is clinically recognized by recurrent, unpredictable episodes of intense rotational vertigo, which are frequently accompanied by significant nausea and vomiting, alongside fluctuating sensorineural hearing loss that may eventually progress to permanent impairment over time. Furthermore, patients often experience distressing tinnitus, characterized by a persistent ringing or roaring sound, combined with a profound sense of aural pressure or fullness within the affected ear, all of which contribute to a substantial reduction in the patient's overall functional capacity and quality of life. While the precise underlying etiology of Ménière's disease remains elusive to modern medical science, contemporary research suggests that the condition is inherently linked to an abnormal accumulation of endolymphatic fluid within the labyrinthine compartments of the inner ear, a phenomenon commonly referred to as endolymphatic hydrops. This mechanical distension is thought to interfere with the critical transduction of acoustic and balance signals between the peripheral sensory organs and the central nervous system, thereby triggering the hallmark symptomatic manifestations of the disorder.
```

## 2. 🔍 NGỮ CẢNH TRUY XUẤT (RAG CONTEXT)
```text
[NGỮ CẢNH TRI THỨC (STRATEGIC CONTEXT)]
- Tiếng Anh: Meniere Disease (Meniere's Disease; Endolymphatic Hydrops) By Mickie Hamiter, MD, New York Presbyterian Columbia Reviewed / Revised May 2023 View Patient Education Symptoms and Signs Diagnosis Treatment Key Points Meniere disease is an inner ear disorder that causes vertigo, nausea, fluctuating sensorineural hearing loss, and tinnitus.
  Nghĩa: Bệnh Meniere (Bệnh Meniere, sũng nước mê nhĩ) Theo Lawrence R. Lustig, MD, Columbia University Medical Center and New York Presbyterian Hospital Đánh giá về mặt y tế Thg6 2021 | đã sửa đổi Thg9 2022 Triệu chứng và Dấu hiệu Chẩn đoán Điều trị Những điểm chính Bệnh Meniere là rối loạn tai trong gây ra chóng mặt, mất thính giác về nghe kém tiếp nhận dao động và ù tai.
- Tiếng Anh: Fluctuating unilateral hearing loss accompanied by aural fullness, tinnitus, and vertigo also suggests Meniere syndrome.
  Nghĩa: Nghe kém một bên dao động kèm theo đầy tai, ù tai và chóng mặt cũng gợi ý hội chứng Meniere.
- Tiếng Anh: Two of the most common specific causes are disorders of the inner ear: benign paroxysmal positional vertigo and Meniere disease.
  Nghĩa: Hai trong số các nguyên nhân cụ thể nhất là rối loạn của tai trong: chóng mặt kịch phát tư thế lành tính và Bệnh Meniere.
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: The absence of concomitant tinnitus or hearing loss is a hallmark of vestibular neuronitis and helps distinguish it from Meniere disease as well as labyrinthitis.
  Nghĩa: Sự vắng mặt của chứng ù tai hoặc mất thính giác đồng thời là dấu hiệu của viêm thần kinh tiền đình và giúp phân biệt nó với Bệnh Meniere cũng như viêm mê nhĩ.
- Tiếng Anh: It can be the result of vestibular neuronitis, migraine with vertigo, Meniere disease, head trauma or inner ear surgery.
  Nghĩa: Tình trạng này có thể là kết quả của viêm dây thần kinh tiền đình, đau nửa đầu kèm theo chóng mặt, bệnh Meniere, chấn thương đầu hoặc sau phẫu thuật tai trong.
- Tiếng Anh: Although bilateral Meniere disease can occur, bilateral symptoms increase the likelihood of an alternate diagnosis (eg, vestibular migraine).
  Nghĩa: Mặc dù có thể xảy ra bệnh Meniere hai bên nhưng các triệu chứng hai bên sẽ làm tăng khả năng xảy ra chẩn đoán thay thế (ví dụ như migraine tiền đình).
- Tiếng Anh: In Meniere disease, pressure and volume changes in the labyrinthine endolymph affect inner ear function.
  Nghĩa: Trong bệnh Meniere, sự thay đổi áp lực và thể tích của nội dịch mê nhĩ ảnh hưởng đến chức năng tai trong.

[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]
- 'Ménière s disease': Bệnh Ménière (Lĩnh vực: medical_glossary)
- 'Tinnitus': Ù tai (Lĩnh vực: medical_glossary)

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
- Tiếng Anh: Fluctuating unilateral hearing loss accompanied by aural fullness, tinnitus, and vertigo also suggests Meniere syndrome.
  Nghĩa: Nghe kém một bên dao động kèm theo đầy tai, ù tai và chóng mặt cũng gợi ý hội chứng Meniere.
- Tiếng Anh: Two of the most common specific causes are disorders of the inner ear: benign paroxysmal positional vertigo and Meniere disease.
  Nghĩa: Hai trong số các nguyên nhân cụ thể nhất là rối loạn của tai trong: chóng mặt kịch phát tư thế lành tính và Bệnh Meniere.
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: The absence of concomitant tinnitus or hearing loss is a hallmark of vestibular neuronitis and helps distinguish it from Meniere disease as well as labyrinthitis.
  Nghĩa: Sự vắng mặt của chứng ù tai hoặc mất thính giác đồng thời là dấu hiệu của viêm thần kinh tiền đình và giúp phân biệt nó với Bệnh Meniere cũng như viêm mê nhĩ.
- Tiếng Anh: It can be the result of vestibular neuronitis, migraine with vertigo, Meniere disease, head trauma or inner ear surgery.
  Nghĩa: Tình trạng này có thể là kết quả của viêm dây thần kinh tiền đình, đau nửa đầu kèm theo chóng mặt, bệnh Meniere, chấn thương đầu hoặc sau phẫu thuật tai trong.
- Tiếng Anh: Although bilateral Meniere disease can occur, bilateral symptoms increase the likelihood of an alternate diagnosis (eg, vestibular migraine).
  Nghĩa: Mặc dù có thể xảy ra bệnh Meniere hai bên nhưng các triệu chứng hai bên sẽ làm tăng khả năng xảy ra chẩn đoán thay thế (ví dụ như migraine tiền đình).
- Tiếng Anh: In Meniere disease, pressure and volume changes in the labyrinthine endolymph affect inner ear function.
  Nghĩa: Trong bệnh Meniere, sự thay đổi áp lực và thể tích của nội dịch mê nhĩ ảnh hưởng đến chức năng tai trong.

[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]
- 'Ménière s disease': Bệnh Ménière (Lĩnh vực: medical_glossary)
- 'Tinnitus': Ù tai (Lĩnh vực: medical_glossary)

* Văn bản nguồn: Ménière's disease represents a sophisticated and often debilitating chronic condition of the inner ear that manifests through a complex array of physiological disturbances primarily impacting both auditory perception and vestibular equilibrium in affected individuals. This pathological state is clinically recognized by recurrent, unpredictable episodes of intense rotational vertigo, which are frequently accompanied by significant nausea and vomiting, alongside fluctuating sensorineural hearing loss that may eventually progress to permanent impairment over time. Furthermore, patients often experience distressing tinnitus, characterized by a persistent ringing or roaring sound, combined with a profound sense of aural pressure or fullness within the affected ear, all of which contribute to a substantial reduction in the patient's overall functional capacity and quality of life. While the precise underlying etiology of Ménière's disease remains elusive to modern medical science, contemporary research suggests that the condition is inherently linked to an abnormal accumulation of endolymphatic fluid within the labyrinthine compartments of the inner ear, a phenomenon commonly referred to as endolymphatic hydrops. This mechanical distension is thought to interfere with the critical transduction of acoustic and balance signals between the peripheral sensory organs and the central nervous system, thereby triggering the hallmark symptomatic manifestations of the disorder.
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
- Tiếng Anh: Fluctuating unilateral hearing loss accompanied by aural fullness, tinnitus, and vertigo also suggests Meniere syndrome.
  Nghĩa: Nghe kém một bên dao động kèm theo đầy tai, ù tai và chóng mặt cũng gợi ý hội chứng Meniere.
- Tiếng Anh: Two of the most common specific causes are disorders of the inner ear: benign paroxysmal positional vertigo and Meniere disease.
  Nghĩa: Hai trong số các nguyên nhân cụ thể nhất là rối loạn của tai trong: chóng mặt kịch phát tư thế lành tính và Bệnh Meniere.
- Tiếng Anh: Key Points Meniere disease typically causes vertigo with nausea and vomiting, unilateral tinnitus, and chronic, progressive hearing loss.
  Nghĩa: Những điểm chính Bệnh Meniere thường gây chóng mặt với buồn nôn và nôn ói, ù tai một bên, và nghe kém tiến triển.
- Tiếng Anh: Symptoms and Signs of Meniere Disease Patients with Meniere disease have sudden attacks of vertigo that usually last for 20 minutes to 12 hours; rarely, the attacks last up to 24 hours.
  Nghĩa: Triệu chứng và dấu hiệu của bệnh Meniere Bệnh nhân có các cơn chóng mặt thường kéo dài từ 1 đến 6 giờ, nhưng có thể (ít) kéo dài đến 24 giờ, thường là buồn nôn và nôn.
- Tiếng Anh: Inner ear disorders include Benign paroxysmal positional vertigo Drug-induced ototoxicity Herpes zoster oticus Meniere disease Purulent labyrinthitis Vestibular neuronitis Vestibular schwannoma Inside the Ear
  Nghĩa: Các rối loạn tai trong bao gồm Chóng mặt kịch phát tư thế lành tính Ngộ độc tai trong do thuốc Zona tai Bệnh Meniere Viêm mê nhĩ mủ Viêm dây thần kinh tiền đình u xơ thần kinh tiền đình Bên trong tai
- Tiếng Anh: The absence of concomitant tinnitus or hearing loss is a hallmark of vestibular neuronitis and helps distinguish it from Meniere disease as well as labyrinthitis.
  Nghĩa: Sự vắng mặt của chứng ù tai hoặc mất thính giác đồng thời là dấu hiệu của viêm thần kinh tiền đình và giúp phân biệt nó với Bệnh Meniere cũng như viêm mê nhĩ.
- Tiếng Anh: It can be the result of vestibular neuronitis, migraine with vertigo, Meniere disease, head trauma or inner ear surgery.
  Nghĩa: Tình trạng này có thể là kết quả của viêm dây thần kinh tiền đình, đau nửa đầu kèm theo chóng mặt, bệnh Meniere, chấn thương đầu hoặc sau phẫu thuật tai trong.
- Tiếng Anh: Although bilateral Meniere disease can occur, bilateral symptoms increase the likelihood of an alternate diagnosis (eg, vestibular migraine).
  Nghĩa: Mặc dù có thể xảy ra bệnh Meniere hai bên nhưng các triệu chứng hai bên sẽ làm tăng khả năng xảy ra chẩn đoán thay thế (ví dụ như migraine tiền đình).
- Tiếng Anh: In Meniere disease, pressure and volume changes in the labyrinthine endolymph affect inner ear function.
  Nghĩa: Trong bệnh Meniere, sự thay đổi áp lực và thể tích của nội dịch mê nhĩ ảnh hưởng đến chức năng tai trong.

[THUẬT NGỮ CẦN LƯU Ý (GLOSSARY)]
- 'Ménière s disease': Bệnh Ménière (Lĩnh vực: medical_glossary)
- 'Tinnitus': Ù tai (Lĩnh vực: medical_glossary)
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
Dịch câu này: Ménière's disease represents a sophisticated and often debilitating chronic condition of the inner ear that manifests through a complex array of physiological disturbances primarily impacting both auditory perception and vestibular equilibrium in affected individuals. This pathological state is clinically recognized by recurrent, unpredictable episodes of intense rotational vertigo, which are frequently accompanied by significant nausea and vomiting, alongside fluctuating sensorineural hearing loss that may eventually progress to permanent impairment over time. Furthermore, patients often experience distressing tinnitus, characterized by a persistent ringing or roaring sound, combined with a profound sense of aural pressure or fullness within the affected ear, all of which contribute to a substantial reduction in the patient's overall functional capacity and quality of life. While the precise underlying etiology of Ménière's disease remains elusive to modern medical science, contemporary research suggests that the condition is inherently linked to an abnormal accumulation of endolymphatic fluid within the labyrinthine compartments of the inner ear, a phenomenon commonly referred to as endolymphatic hydrops. This mechanical distension is thought to interfere with the critical transduction of acoustic and balance signals between the peripheral sensory organs and the central nervous system, thereby triggering the hallmark symptomatic manifestations of the disorder.<|im_end|>
<|im_start|>assistant

```

## 4. 📤 KẾT QUẢ ĐẦU RA (AI TRANSLATION)
**Dịch sang tiếng Việt**:

> Bệnh Meniere đại diện cho một tình trạng mãn tính phức tạp và thường gây mất khả năng hoạt động của tai trong, biểu hiện qua một loạt các rối loạn sinh lý ảnh hưởng chủ yếu đến cả nhận thức về âm thanh và cân bằng của tai trong ở các cá nhân bị ảnh hưởng. Trạng thái bệnh lý này được chẩn đoán lâm sàng bởi các cơn chóng mặt xoay mạnh liên tục và không dự đoán được, thường đi kèm với buồn nôn và nôn nghiêm trọng, cùng với mất thính giác về nghe tiếp nhận dao động có thể tiến triển thành mất thính giác vĩnh viễn theo thời gian. Ngoài ra, bệnh nhân thường trải qua cảm giác ù tai gây khó chịu, đặc trưng bởi tiếng kêu hoặc tiếng vang liên tục, kết hợp với cảm giác áp lực hoặc đầy tai trong ảnh hưởng đến tai, tất cả những điều này góp phần làm giảm đáng kể khả năng hoạt động tổng thể và chất lượng cuộc sống của bệnh nhân. Mặc dù nguyên nhân cơ bản của bệnh Meniere vẫn là một bí ẩn đối với khoa học y học hiện đại, các nghiên cứu hiện đại cho thấy tình trạng này có liên quan đến sự tích tụ bất thường của dịch endolymphatic trong các phần tử của tai trong, một hiện tượng thường được gọi là endolymphatic hydrops. Sự căng cơ học này được cho là can thiệp vào quá trình chuyển đổi quan trọng của tín hiệu âm thanh và cân bằng giữa các cơ quan cảm nhận ngoại vi và hệ thần kinh trung ương, từ đó gây ra các triệu chứng đặc trưng của bệnh.
