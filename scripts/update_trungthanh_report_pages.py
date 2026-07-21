from __future__ import annotations

from pathlib import Path


ROOT = Path(r"C:\Users\admin\source\repos\Talent-Graph-AI\FCAJ-workshop-trungthanh")


FILES: dict[str, str] = {
    "content/_index.vi.md": """---
title: "Báo cáo thực tập"
date: 2026-04-17
weight: 1
chapter: false
---

# Báo cáo thực tập

### Thông tin sinh viên

&emsp; **Họ và tên:** Nguyễn Trung Thành

&emsp; **MSSV:** 2280618931

&emsp; **Lớp:** 22DTHH3

&emsp; **Ngành:** Công nghệ thông tin

&emsp; **Chuyên ngành:** Công nghệ phần mềm

&emsp; **Email:** trungthanh070104@gmail.com

&emsp; **Đơn vị thực tập:** Công ty TNHH Amazon Web Services Viet Nam

&emsp; **Cán bộ hướng dẫn tại đơn vị thực tập:** Nguyễn Gia Hưng - hunggia@amazon.com

&emsp; **Giảng viên theo dõi tại trường:** Trần Văn Hùng - hungtran3028@gmail.com

&emsp; **Thời gian ghi nhận tiến độ:** 17/04/2026 - 12/07/2026

![Ảnh đại diện của bạn](images/Thanh.png)

### Tổng quan quá trình thực tập

Trong 12 tuần thực tập, tôi tập trung vào hai nhóm nội dung chính: xây dựng nền tảng kiến thức AWS và triển khai dự án Workshop **Vertex IntervAI / Talent Graph AI**. Giai đoạn đầu giúp tôi làm quen với AWS Console, AWS CLI, IAM, S3, EC2, VPC, Lambda và API Gateway. Giai đoạn sau tập trung vào thiết kế kiến trúc, phát triển backend serverless, tích hợp Amazon Bedrock, lưu trữ dữ liệu bằng S3/DynamoDB và hoàn thiện các luồng phỏng vấn AI.

| Giai đoạn | Thời gian | Nội dung chính | Kết quả nổi bật |
| --- | --- | --- | --- |
| Nền tảng AWS | 17/04/2026 - 17/05/2026 | Console/CLI, IAM, S3, EC2, VPC, Lambda, DynamoDB, API Gateway, Bedrock | Nắm được các dịch vụ AWS cốt lõi và cách kết hợp trong ứng dụng serverless |
| Mở rộng dịch vụ | 18/05/2026 - 21/06/2026 | SQS/SNS, CloudFront, Route 53, ECS, ALB, RDS, CloudWatch, Security, Cost Optimization | Củng cố khả năng thiết kế hệ thống scalable, reliable và observable |
| Dự án Vertex IntervAI | 22/06/2026 - 12/07/2026 | Kiến trúc dự án, Lambda backend, S3/DynamoDB, Bedrock, API Gateway, Cognito, profile, interview flow | Hoàn thiện MVP với các luồng upload CV, phân tích AI, phỏng vấn AI, kết quả và profile |

### Nội dung báo cáo

1. [Worklog](1-Worklog/)
2. [Proposal](2-Proposal/)
3. [Các bài blogs đã đăng](3-BlogsPosted/)
4. [Các events đã tham gia](4-EventParticipated/)
5. [Workshop](5-Workshop/)
6. [Tự đánh giá](6-Self-evaluation/)
7. [Chia sẻ, đóng góp ý kiến](7-Feedback/)
""",
    "content/_index.md": """---
title: "Internship Report"
date: 2026-04-17
weight: 1
chapter: false
---

# Internship Report

### Student Information

&emsp; **Full name:** Nguyễn Trung Thành

&emsp; **Student ID:** 2280618931

&emsp; **Class:** 22DTHH3

&emsp; **Major:** Information Technology

&emsp; **Specialization:** Software Engineering

&emsp; **Email:** trungthanh070104@gmail.com

&emsp; **Internship organization:** Amazon Web Services Viet Nam Company Limited

&emsp; **Company mentor:** Nguyễn Gia Hưng - hunggia@amazon.com

&emsp; **University supervisor:** Trần Văn Hùng - hungtran3028@gmail.com

&emsp; **Progress period:** 17/04/2026 - 12/07/2026

![Your profile picture](images/Thanh.png)

### Internship Overview

During the 12-week internship, my work focused on two main areas: building AWS foundations and developing the **Vertex IntervAI / Talent Graph AI** workshop project. The first phase covered AWS Console, AWS CLI, IAM, S3, EC2, VPC, Lambda, and API Gateway. The later phase focused on architecture design, serverless backend implementation, Amazon Bedrock integration, S3/DynamoDB data storage, and the completion of AI interview workflows.

| Phase | Period | Main focus | Key outcome |
| --- | --- | --- | --- |
| AWS foundations | 17/04/2026 - 17/05/2026 | Console/CLI, IAM, S3, EC2, VPC, Lambda, DynamoDB, API Gateway, Bedrock | Built a practical understanding of core AWS services and serverless integration |
| Service expansion | 18/05/2026 - 21/06/2026 | SQS/SNS, CloudFront, Route 53, ECS, ALB, RDS, CloudWatch, Security, Cost Optimization | Strengthened system design skills for scalable, reliable, and observable workloads |
| Vertex IntervAI project | 22/06/2026 - 12/07/2026 | Project architecture, Lambda backend, S3/DynamoDB, Bedrock, API Gateway, Cognito, profile, interview flow | Completed an MVP covering CV upload, AI analysis, AI interview, results, and profile |

### Report Contents

1. [Worklog](1-Worklog/)
2. [Proposal](2-Proposal/)
3. [Blogs Posted](3-BlogsPosted/)
4. [Events Participated](4-EventParticipated/)
5. [Workshop](5-Workshop/)
6. [Self-evaluation](6-Self-evaluation/)
7. [Sharing and Feedback](7-Feedback/)
""",
    "content/6-Self-evaluation/_index.vi.md": """---
title: "Tự đánh giá"
date: 2026-07-12
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

Trong quá trình thực tập tại **Công ty TNHH Amazon Web Services Viet Nam** từ **17/04/2026** đến **12/07/2026**, tôi có cơ hội hệ thống hóa kiến thức cloud và áp dụng vào dự án **Vertex IntervAI / Talent Graph AI**. Nội dung thực tập bắt đầu từ các dịch vụ nền tảng như IAM, S3, EC2, VPC, Lambda, API Gateway, DynamoDB, CloudWatch; sau đó mở rộng sang ECS, ALB, RDS, security, cost optimization và các dịch vụ AI/ML như Amazon Bedrock.

Ở giai đoạn dự án, tôi tham gia thiết kế kiến trúc tổng thể, phát triển các Lambda function chính, tích hợp S3 để lưu CV, DynamoDB để quản lý metadata, Amazon Bedrock để phân tích CV và chấm điểm phỏng vấn, đồng thời hỗ trợ kết nối frontend React với API Gateway. Nhờ đó, tôi hiểu rõ hơn cách triển khai một ứng dụng serverless theo hướng có khả năng mở rộng, dễ quan sát và có cơ chế fallback khi dịch vụ gặp sự cố.

### Kết quả đạt được

| Nhóm năng lực | Minh chứng từ tiến độ | Tự đánh giá |
| --- | --- | --- |
| Kiến thức AWS nền tảng | Hoàn thành các tuần học IAM, S3, EC2, VPC, Lambda, API Gateway, DynamoDB, CloudWatch | Tốt |
| Thiết kế kiến trúc | Tham gia thiết kế High-level Architecture cho Vertex IntervAI, đề xuất các thành phần backend/serverless | Tốt |
| Phát triển backend | Triển khai và tối ưu các luồng upload_cv, analyze_cv, create_interview, submit_answer, profile | Tốt |
| Tích hợp AI | Ứng dụng Amazon Bedrock vào phân tích CV, tạo câu hỏi và đánh giá câu trả lời | Khá |
| Kiểm thử và vận hành | Thực hiện test tích hợp, kiểm tra CloudWatch Logs, rà soát CORS/IAM/fallback | Khá |
| Làm việc nhóm | Tham gia họp nhóm, cập nhật worklog/proposal, phối hợp frontend/backend | Tốt |
| Tài liệu hóa | Chuẩn bị worklog, proposal, diagram kiến trúc và tài liệu demo | Tốt |

### Điểm mạnh

* Có khả năng tự học nhanh các dịch vụ AWS mới và liên hệ chúng với bài toán thực tế.
* Chủ động ghi nhận tiến độ, cập nhật tài liệu và theo dõi các đầu việc theo từng tuần.
* Nắm được luồng triển khai serverless từ frontend, API Gateway, Lambda đến S3/DynamoDB/Bedrock.
* Biết kiểm tra lỗi ở mức tích hợp thông qua logs, API response, quyền IAM và cấu hình CORS.
* Có tinh thần phối hợp nhóm tốt trong giai đoạn thiết kế kiến trúc, backend và chuẩn bị demo.

### Điểm cần cải thiện

* Cần tiếp tục luyện tập triển khai production hoàn chỉnh, đặc biệt ở CI/CD, bảo mật API và kiểm thử tự động.
* Cần cải thiện thêm khả năng ước lượng thời gian cho các task có nhiều phụ thuộc như voice flow, Cognito và IAM.
* Cần viết tài liệu kỹ thuật theo hướng chuẩn hóa hơn để người khác có thể tái triển khai dễ dàng.

### Định hướng sau thực tập

Sau kỳ thực tập, tôi muốn tiếp tục đào sâu về AWS Serverless, kiến trúc ứng dụng AI, observability và bảo mật cloud. Dự án Vertex IntervAI là nền tảng tốt để tôi phát triển thêm năng lực thiết kế hệ thống, tích hợp AI vào sản phẩm thực tế và hoàn thiện kỹ năng phát triển phần mềm theo quy trình chuyên nghiệp.
""",
    "content/6-Self-evaluation/_index.md": """---
title: "Self-Assessment"
date: 2026-07-12
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

During my internship at **Amazon Web Services Viet Nam Company Limited** from **17/04/2026** to **12/07/2026**, I had the opportunity to strengthen my cloud knowledge and apply it to the **Vertex IntervAI / Talent Graph AI** project. The internship started with core AWS services such as IAM, S3, EC2, VPC, Lambda, API Gateway, DynamoDB, and CloudWatch, then expanded into ECS, ALB, RDS, security, cost optimization, and AI/ML services such as Amazon Bedrock.

During the project phase, I contributed to high-level architecture design, backend Lambda implementation, S3 CV storage, DynamoDB metadata management, Amazon Bedrock integration for CV analysis and interview scoring, and React frontend integration through API Gateway. This helped me understand how to build a serverless application that is scalable, observable, and resilient through fallback mechanisms.

### Outcomes Achieved

| Competency | Evidence from progress | Self-rating |
| --- | --- | --- |
| AWS foundations | Completed learning and practice for IAM, S3, EC2, VPC, Lambda, API Gateway, DynamoDB, and CloudWatch | Good |
| Architecture design | Joined the High-level Architecture design for Vertex IntervAI and proposed backend/serverless components | Good |
| Backend development | Implemented and optimized upload_cv, analyze_cv, create_interview, submit_answer, and profile flows | Good |
| AI integration | Applied Amazon Bedrock to CV analysis, question generation, and interview answer evaluation | Fair |
| Testing and operations | Ran integration tests, checked CloudWatch Logs, and reviewed CORS/IAM/fallback behavior | Fair |
| Teamwork | Joined team meetings, updated worklog/proposal, and coordinated frontend/backend work | Good |
| Documentation | Prepared worklog, proposal, architecture diagrams, and demo documentation | Good |

### Strengths

* Able to learn new AWS services quickly and connect them to real project requirements.
* Proactive in tracking progress, updating documentation, and organizing weekly tasks.
* Understands the serverless flow from frontend, API Gateway, and Lambda to S3/DynamoDB/Bedrock.
* Can investigate integration issues through logs, API responses, IAM permissions, and CORS settings.
* Works well with the team during architecture design, backend implementation, and demo preparation.

### Areas for Improvement

* Continue practicing production deployment, especially CI/CD, API security, and automated testing.
* Improve time estimation for tasks with many dependencies such as voice flow, Cognito, and IAM.
* Write more standardized technical documentation so others can reproduce the deployment more easily.

### Direction After the Internship

After the internship, I plan to continue learning AWS Serverless, AI application architecture, observability, and cloud security. Vertex IntervAI is a strong foundation for improving my system design ability, integrating AI into practical products, and strengthening professional software development skills.
""",
    "content/7-Feedback/_index.vi.md": """---
title: "Chia sẻ, đóng góp ý kiến"
date: 2026-07-12
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

Sau quá trình thực tập tại **Công ty TNHH Amazon Web Services Viet Nam** trong chương trình First Cloud AI Journey, tôi muốn tổng kết một số cảm nhận và góp ý dựa trên trải nghiệm thực tế khi học AWS và triển khai dự án **Vertex IntervAI / Talent Graph AI**.

### Đánh giá chung

**1. Môi trường học tập và làm việc**  
Môi trường thực tập tạo điều kiện để sinh viên tiếp cận các dịch vụ cloud theo hướng thực hành. Việc đi từ kiến thức nền tảng như IAM, S3, EC2, VPC đến các dịch vụ serverless và AI giúp lộ trình học có tính hệ thống, không bị rời rạc.

**2. Sự hỗ trợ của mentor**  
Cán bộ hướng dẫn tại đơn vị thực tập, anh **Nguyễn Gia Hưng**, cung cấp định hướng rõ ràng và giúp tôi hiểu cách liên kết kiến thức AWS với một sản phẩm cụ thể. Quá trình phản hồi theo từng giai đoạn giúp tôi chủ động hơn trong cách đặt mục tiêu, kiểm tra tiến độ và hoàn thiện tài liệu.

**3. Tính phù hợp với chuyên ngành**  
Các nhiệm vụ trong kỳ thực tập phù hợp với chuyên ngành Công nghệ phần mềm: thiết kế kiến trúc, xây dựng backend, tích hợp API, quản lý dữ liệu, kiểm thử và viết tài liệu kỹ thuật. Đây là những kỹ năng có thể áp dụng trực tiếp vào công việc phát triển phần mềm sau này.

**4. Giá trị của dự án Vertex IntervAI**  
Dự án giúp tôi hiểu rõ hơn cách kết hợp frontend React, API Gateway, Lambda, S3, DynamoDB, Cognito và Bedrock để tạo một sản phẩm có luồng nghiệp vụ hoàn chỉnh. Việc xây dựng MVP từ upload CV đến phân tích AI, phỏng vấn AI, kết quả và profile giúp quá trình học trở nên thực tế hơn.

### Góp ý cải thiện

* Nên có checklist onboarding cho tuần đầu tiên, bao gồm tài khoản, công cụ, tài liệu AWS cần đọc và mục tiêu đầu ra.
* Nên tổ chức các buổi review ngắn theo chu kỳ 1-2 tuần để thực tập sinh trình bày kết quả, vướng mắc và kế hoạch tiếp theo.
* Nên có template thống nhất cho kiến trúc, API, biến môi trường, IAM policy và test case để việc bàn giao dễ hơn.
* Nên bổ sung một buổi hướng dẫn riêng về triển khai production, CI/CD, monitoring và bảo mật API.

### Điều tôi hài lòng nhất

Điều tôi đánh giá cao nhất là chương trình cho phép thực tập sinh học qua sản phẩm thực tế thay vì chỉ làm bài lab rời rạc. Khi áp dụng AWS vào Vertex IntervAI, tôi hiểu rõ hơn vì sao cần thiết kế quyền IAM cẩn thận, cần kiểm tra logs, cần chuẩn hóa dữ liệu và cần có fallback khi tích hợp AI.

### Lời cảm ơn

Tôi xin cảm ơn mentor, giảng viên theo dõi và các thành viên hỗ trợ chương trình đã tạo điều kiện cho tôi hoàn thành giai đoạn thực tập. Những kiến thức và kinh nghiệm tích lũy được trong kỳ thực tập là nền tảng quan trọng để tôi tiếp tục phát triển theo hướng cloud, serverless và ứng dụng AI.
""",
    "content/7-Feedback/_index.md": """---
title: "Sharing and Feedback"
date: 2026-07-12
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

After completing my internship at **Amazon Web Services Viet Nam Company Limited** through the First Cloud AI Journey program, I would like to summarize my feedback based on the practical experience of learning AWS and developing the **Vertex IntervAI / Talent Graph AI** project.

### Overall Feedback

**1. Learning and working environment**  
The internship environment supports hands-on cloud learning. The progression from foundational services such as IAM, S3, EC2, and VPC to serverless and AI services makes the learning path structured and practical.

**2. Mentor support**  
My company mentor, **Nguyễn Gia Hưng**, provided clear direction and helped me connect AWS knowledge with a concrete product. Stage-by-stage feedback helped me become more proactive in setting goals, checking progress, and improving documentation.

**3. Alignment with my major**  
The assigned tasks aligned well with Software Engineering: architecture design, backend development, API integration, data management, testing, and technical documentation. These skills are directly useful for future software development work.

**4. Value of the Vertex IntervAI project**  
The project helped me understand how React, API Gateway, Lambda, S3, DynamoDB, Cognito, and Bedrock can be combined into a complete product workflow. Building an MVP from CV upload to AI analysis, AI interview, results, and profile made the learning experience much more realistic.

### Improvement Suggestions

* Add a first-week onboarding checklist covering accounts, tools, required AWS reading, and expected outputs.
* Hold short review sessions every 1-2 weeks so interns can present results, blockers, and next steps.
* Provide unified templates for architecture, APIs, environment variables, IAM policies, and test cases to simplify handover.
* Add a dedicated session about production deployment, CI/CD, monitoring, and API security.

### Most Valuable Point

The strongest part of the program is that interns learn through a practical product instead of isolated labs only. By applying AWS to Vertex IntervAI, I understood why IAM permissions, logs, data modeling, and fallback mechanisms are important when building AI-enabled applications.

### Appreciation

I would like to thank my mentor, university supervisor, and the program support team for helping me complete this internship period. The knowledge and experience gained from the internship are an important foundation for my continued growth in cloud, serverless, and AI application development.
""",
    "content/4-EventParticipated/_index.vi.md": """---
title: "Các events đã tham gia"
date: 2026-04-17
weight: 4
chapter: false
pre: " <b> 4. </b> "
---

Trong quá trình thực tập, tôi tham gia các hoạt động học tập và trao đổi nhóm gắn trực tiếp với tiến độ 12 tuần. Các hoạt động này giúp tôi hiểu rõ định hướng thực tập, tiếp cận hệ sinh thái AWS và phối hợp với nhóm trong quá trình xây dựng dự án **Vertex IntervAI / Talent Graph AI**.

### [Event 1](4.1-Event1/)

&emsp;**Tên sự kiện:** AWS internship onboarding và cloud foundation orientation

&emsp;**Thời gian:** 17/04/2026 - 26/04/2026

&emsp;**Địa điểm:** Chương trình thực tập AWS Vietnam / FCAJ

&emsp;**Vai trò trong sự kiện:** Thực tập sinh tham gia học tập, thiết lập môi trường và ghi nhận tiến độ

&emsp;**Giá trị đạt được:** Nắm được mục tiêu thực tập, tạo tài khoản AWS, làm quen AWS Console/CLI, tìm hiểu EC2, S3, IAM và quản lý chi phí.

### [Event 2](4.2-Event2/)

&emsp;**Tên sự kiện:** Vertex IntervAI architecture, backend và demo planning sessions

&emsp;**Thời gian:** 22/06/2026 - 12/07/2026

&emsp;**Địa điểm:** Nhóm dự án Vertex IntervAI

&emsp;**Vai trò trong sự kiện:** Thành viên tham gia thiết kế kiến trúc, phát triển backend, kiểm thử và chuẩn bị demo

&emsp;**Giá trị đạt được:** Đóng góp vào thiết kế kiến trúc serverless, triển khai các Lambda function, tích hợp S3/DynamoDB/Bedrock/API Gateway và hoàn thiện MVP.
""",
    "content/4-EventParticipated/_index.md": """---
title: "Events Participated"
date: 2026-04-17
weight: 4
chapter: false
pre: " <b> 4. </b> "
---

During the internship, I participated in learning and team-collaboration activities that directly supported the 12-week progress plan. These activities helped me understand the internship direction, explore the AWS ecosystem, and work with the team on the **Vertex IntervAI / Talent Graph AI** project.

### [Event 1](4.1-Event1/)

&emsp;**Event name:** AWS internship onboarding and cloud foundation orientation

&emsp;**Date:** 17/04/2026 - 26/04/2026

&emsp;**Location:** AWS Vietnam / FCAJ internship program

&emsp;**Role:** Intern participant responsible for learning, environment setup, and progress tracking

&emsp;**Value gained:** Understood the internship goals, created an AWS account, practiced AWS Console/CLI, and learned EC2, S3, IAM, and cost management.

### [Event 2](4.2-Event2/)

&emsp;**Event name:** Vertex IntervAI architecture, backend, and demo planning sessions

&emsp;**Date:** 22/06/2026 - 12/07/2026

&emsp;**Location:** Vertex IntervAI project team

&emsp;**Role:** Team member supporting architecture design, backend development, testing, and demo preparation

&emsp;**Value gained:** Contributed to serverless architecture design, Lambda implementation, S3/DynamoDB/Bedrock/API Gateway integration, and MVP completion.
""",
    "content/4-EventParticipated/4.1-Event1/_index.vi.md": """---
title: "Event 1 - AWS onboarding và cloud foundation"
date: 2026-04-17
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# AWS internship onboarding và cloud foundation orientation

### Mục đích

Hoạt động onboarding giúp tôi hiểu mục tiêu thực tập, phạm vi công việc và các yêu cầu cần hoàn thành trong giai đoạn đầu. Đây cũng là bước khởi động để làm quen với AWS account, AWS Management Console, AWS CLI và cách quản lý chi phí trên cloud.

### Nội dung chính

* Làm quen với nội dung thực tập và xác định mục tiêu cần đạt.
* Tạo tài khoản Amazon Web Services và kích hoạt gói Free Tier.
* Khám phá AWS Management Console, cách tổ chức dịch vụ theo Region.
* Tìm hiểu các dịch vụ cơ bản như EC2, S3 và IAM.
* Cài đặt AWS CLI và thực hiện một số lệnh cơ bản.
* Tìm hiểu quản lý chi phí, ngân sách và tài liệu hỗ trợ chính thức của AWS.

### Kết quả đạt được

* Tạo và sử dụng thành công tài khoản AWS phục vụ quá trình thực tập.
* Hiểu được cấu trúc cơ bản của nền tảng AWS và vai trò của một số dịch vụ cốt lõi.
* Biết cách thao tác với AWS qua cả giao diện web và dòng lệnh.
* Có nhận thức ban đầu về kiểm soát chi phí khi sử dụng tài nguyên cloud.

### Bài học rút ra

Giai đoạn onboarding cho thấy việc học cloud cần đi cùng thực hành. Khi trực tiếp tạo tài khoản, thao tác Console/CLI và kiểm tra chi phí, tôi hiểu rõ hơn trách nhiệm của người dùng cloud trong việc cấu hình, bảo mật và theo dõi tài nguyên.
""",
    "content/4-EventParticipated/4.1-Event1/_index.md": """---
title: "Event 1 - AWS onboarding and cloud foundation"
date: 2026-04-17
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# AWS internship onboarding and cloud foundation orientation

### Purpose

The onboarding activity helped me understand the internship objectives, work scope, and early-stage expectations. It also introduced AWS account setup, AWS Management Console, AWS CLI, and cloud cost-management basics.

### Main Activities

* Got familiar with the internship content and defined early-stage goals.
* Created an Amazon Web Services account and activated the Free Tier.
* Explored the AWS Management Console and Region-based service organization.
* Learned basic services such as EC2, S3, and IAM.
* Installed AWS CLI and ran several basic commands.
* Studied cost management, budget setup, and official AWS support documentation.

### Outcomes

* Successfully created and used an AWS account for the internship.
* Understood the basic structure of the AWS platform and the role of several core services.
* Learned how to operate AWS through both the web console and command line.
* Built initial awareness of cloud cost control and responsible resource usage.

### Lessons Learned

The onboarding phase showed that cloud learning needs hands-on practice. By setting up an account, using Console/CLI, and checking cost controls, I better understood the user's responsibility in configuring, securing, and monitoring cloud resources.
""",
    "content/4-EventParticipated/4.2-Event2/_index.vi.md": """---
title: "Event 2 - Vertex IntervAI planning và demo"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Vertex IntervAI architecture, backend và demo planning sessions

### Mục đích

Chuỗi hoạt động này tập trung vào việc chuyển kiến thức AWS đã học thành một dự án hoàn chỉnh: **Vertex IntervAI / Talent Graph AI**. Nhóm cùng thiết kế kiến trúc tổng thể, phân chia công việc backend/frontend, kiểm thử các luồng chính và chuẩn bị tài liệu demo.

### Nội dung chính

* Tham gia họp nhóm và cùng thiết kế High-level Architecture cho dự án.
* Đề xuất kiến trúc AWS serverless gồm React frontend, Cognito, API Gateway, Lambda, S3, DynamoDB, Bedrock và CloudWatch.
* Phát triển các Lambda function chính như `upload_cv`, `analyze_cv`, `create_interview` và `submit_answer`.
* Tích hợp S3 để lưu CV, DynamoDB để quản lý metadata và Bedrock để phân tích CV/chấm điểm phỏng vấn.
* Thực hiện test tích hợp các luồng Upload CV -> Analyze -> Interview.
* Chuẩn bị tài liệu demo, diagram kiến trúc và báo cáo tiến độ dự án.

### Kết quả đạt được

* Hoàn thành backend core cho các chức năng chính của dự án.
* Hệ thống có thể xử lý luồng Upload và Analyze CV end-to-end.
* Frontend và backend kết nối qua API Gateway.
* Hoàn thiện phiên bản MVP với các luồng Upload CV, Phân tích AI, Phỏng vấn AI, Profile và kết quả.
* Có tài liệu kiến trúc và demo sẵn sàng trình bày.

### Bài học rút ra

Khi triển khai một ứng dụng AI trên AWS, phần khó không chỉ nằm ở gọi model mà còn ở dữ liệu, quyền truy cập, logging, fallback và trải nghiệm người dùng. Việc phối hợp nhóm và kiểm thử tích hợp giúp tôi hiểu rõ hơn cách biến một ý tưởng thành sản phẩm có thể demo.
""",
    "content/4-EventParticipated/4.2-Event2/_index.md": """---
title: "Event 2 - Vertex IntervAI planning and demo"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Vertex IntervAI architecture, backend, and demo planning sessions

### Purpose

This activity series focused on turning the AWS knowledge learned during the internship into a complete project: **Vertex IntervAI / Talent Graph AI**. The team designed the high-level architecture, divided backend/frontend tasks, tested key flows, and prepared demo documentation.

### Main Activities

* Joined team meetings and contributed to the project's High-level Architecture.
* Proposed a serverless AWS architecture with React frontend, Cognito, API Gateway, Lambda, S3, DynamoDB, Bedrock, and CloudWatch.
* Developed key Lambda functions such as `upload_cv`, `analyze_cv`, `create_interview`, and `submit_answer`.
* Integrated S3 for CV storage, DynamoDB for metadata management, and Bedrock for CV analysis/interview scoring.
* Ran integration tests for the Upload CV -> Analyze -> Interview flow.
* Prepared demo documents, architecture diagrams, and the project progress report.

### Outcomes

* Completed the backend core for the main project features.
* The system can process the Upload and Analyze CV flow end-to-end.
* Frontend and backend communicate through API Gateway.
* Completed an MVP covering CV upload, AI analysis, AI interview, profile, and results.
* Prepared architecture documents and demo materials for presentation.

### Lessons Learned

When building an AI application on AWS, the challenge is not only calling the model. Data design, permissions, logging, fallback handling, and user experience are equally important. Team coordination and integration testing helped me understand how to turn an idea into a demo-ready product.
""",
    "content/3-BlogsPosted/_index.vi.md": """---
title: "Các bài blogs đã đăng"
date: 2026-05-04
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

Trong quá trình thực tập, tôi tổng hợp lại kiến thức và kinh nghiệm thực hành thành các bài viết ngắn. Nội dung tập trung vào những chủ đề xuất hiện xuyên suốt trong phiếu tiến độ: nền tảng AWS, serverless backend và ứng dụng AI với Amazon Bedrock trong dự án Vertex IntervAI.

### [Blog 1 - AWS foundation: IAM, S3, EC2 và quản lý chi phí](3.1-Blog1/)

Tóm tắt quá trình làm quen AWS, tạo tài khoản, sử dụng Console/CLI, tìm hiểu IAM/S3/EC2 và thiết lập tư duy kiểm soát chi phí.

### [Blog 2 - Xây dựng backend serverless với Lambda, API Gateway và DynamoDB](3.2-Blog2/)

Ghi chú về cách kết nối API Gateway, Lambda, DynamoDB, S3 và CloudWatch để tạo backend có thể mở rộng và dễ quan sát.

### [Blog 3 - Ứng dụng Amazon Bedrock trong Vertex IntervAI](3.3-Blog3/)

Chia sẻ cách dùng Amazon Bedrock để phân tích CV, tạo câu hỏi phỏng vấn và hỗ trợ chấm điểm câu trả lời trong dự án Vertex IntervAI.
""",
    "content/3-BlogsPosted/_index.md": """---
title: "Blogs Posted"
date: 2026-05-04
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

During the internship, I summarized practical learning notes into short technical posts. The topics follow the progress report: AWS foundations, serverless backend development, and AI integration with Amazon Bedrock in the Vertex IntervAI project.

### [Blog 1 - AWS foundation: IAM, S3, EC2, and cost management](3.1-Blog1/)

Summary of AWS onboarding, account setup, Console/CLI usage, IAM/S3/EC2 basics, and cost-control awareness.

### [Blog 2 - Building a serverless backend with Lambda, API Gateway, and DynamoDB](3.2-Blog2/)

Notes on combining API Gateway, Lambda, DynamoDB, S3, and CloudWatch into a scalable and observable backend.

### [Blog 3 - Applying Amazon Bedrock in Vertex IntervAI](3.3-Blog3/)

Reflection on using Amazon Bedrock for CV analysis, interview question generation, and answer scoring in Vertex IntervAI.
""",
    "content/3-BlogsPosted/3.1-Blog1/_index.vi.md": """---
title: "AWS foundation: IAM, S3, EC2 và quản lý chi phí"
date: 2026-05-04
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# AWS foundation: IAM, S3, EC2 và quản lý chi phí

### Bối cảnh

Ở giai đoạn đầu thực tập, tôi tập trung làm quen với nền tảng AWS: tạo tài khoản, khám phá AWS Management Console, cài AWS CLI và tìm hiểu các dịch vụ cơ bản. Đây là phần quan trọng vì mọi nội dung thực hành sau đó đều cần nền tảng tài khoản, quyền truy cập và tư duy kiểm soát chi phí.

### Nội dung chính

* **IAM:** hiểu vai trò của user, group, role, policy và nguyên tắc least privilege.
* **S3:** làm quen bucket, object storage, static website hosting, versioning và bucket policy.
* **EC2:** tạo instance, cấu hình Security Group, key pair, Elastic IP và kết nối SSH.
* **VPC:** hiểu subnet public/private, Internet Gateway và Route Table.
* **Cost control:** theo dõi chi phí, thiết lập ngân sách và kiểm tra tài nguyên đang chạy.

### Bài học

AWS không chỉ là tập hợp dịch vụ riêng lẻ. Khi triển khai thực tế, cần hiểu cách các dịch vụ kết nối với nhau, cách phân quyền đúng và cách tránh phát sinh chi phí ngoài dự kiến. Việc thao tác song song Console và CLI cũng giúp tôi hiểu rõ hơn quy trình quản trị tài nguyên cloud.
""",
    "content/3-BlogsPosted/3.1-Blog1/_index.md": """---
title: "AWS foundation: IAM, S3, EC2, and cost management"
date: 2026-05-04
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# AWS foundation: IAM, S3, EC2, and cost management

### Context

In the early internship phase, I focused on AWS fundamentals: account setup, AWS Management Console, AWS CLI, and core services. This foundation was important because later hands-on tasks depended on accounts, permissions, and cost-control awareness.

### Main Topics

* **IAM:** user, group, role, policy, and the principle of least privilege.
* **S3:** bucket, object storage, static website hosting, versioning, and bucket policy.
* **EC2:** instance launch, Security Group, key pair, Elastic IP, and SSH connection.
* **VPC:** public/private subnets, Internet Gateway, and Route Table.
* **Cost control:** budget setup, cost tracking, and checking active resources.

### Lessons Learned

AWS is not just a list of independent services. In real implementation, it is important to understand how services connect, how permissions should be designed, and how to avoid unexpected costs. Using both Console and CLI also helped me understand cloud resource management more clearly.
""",
    "content/3-BlogsPosted/3.2-Blog2/_index.vi.md": """---
title: "Xây dựng backend serverless với Lambda, API Gateway và DynamoDB"
date: 2026-05-25
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# Xây dựng backend serverless với Lambda, API Gateway và DynamoDB

### Bối cảnh

Sau khi nắm các dịch vụ nền tảng, tôi chuyển sang nhóm dịch vụ serverless: AWS Lambda, Amazon API Gateway, Amazon SQS/SNS, CloudFront và Route 53. Đây là giai đoạn giúp tôi hiểu cách xây dựng backend ít vận hành nhưng vẫn có khả năng mở rộng.

### Kiến trúc tham khảo

* **API Gateway** nhận request từ frontend và định tuyến đến Lambda.
* **Lambda** xử lý logic nghiệp vụ như upload CV, phân tích CV, tạo phiên phỏng vấn hoặc lưu profile.
* **DynamoDB** lưu metadata có cấu trúc như Users, CVs và Interviews.
* **S3** lưu file CV/audio và các dữ liệu dạng object.
* **CloudWatch** ghi log, hỗ trợ debug và theo dõi lỗi tích hợp.

### Bài học

Khi dùng serverless, việc viết function chỉ là một phần. Cần chú ý IAM permission, environment variables, CORS, format response và logging. Nếu các phần này không thống nhất, frontend có thể không gọi được API dù function chạy đúng khi test riêng.
""",
    "content/3-BlogsPosted/3.2-Blog2/_index.md": """---
title: "Building a serverless backend with Lambda, API Gateway, and DynamoDB"
date: 2026-05-25
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# Building a serverless backend with Lambda, API Gateway, and DynamoDB

### Context

After learning core AWS services, I moved into serverless services: AWS Lambda, Amazon API Gateway, Amazon SQS/SNS, CloudFront, and Route 53. This phase helped me understand how to build a backend with low operational overhead while keeping scalability.

### Reference Architecture

* **API Gateway** receives frontend requests and routes them to Lambda.
* **Lambda** handles business logic such as CV upload, CV analysis, interview creation, and profile storage.
* **DynamoDB** stores structured metadata such as Users, CVs, and Interviews.
* **S3** stores CV/audio files and object data.
* **CloudWatch** captures logs and supports debugging integration issues.

### Lessons Learned

In serverless development, writing the function is only one part. IAM permissions, environment variables, CORS, response format, and logging are equally important. If these parts are inconsistent, the frontend may fail to call the API even when the Lambda works in isolated tests.
""",
    "content/3-BlogsPosted/3.3-Blog3/_index.vi.md": """---
title: "Ứng dụng Amazon Bedrock trong Vertex IntervAI"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Ứng dụng Amazon Bedrock trong Vertex IntervAI

### Bối cảnh

Trong dự án **Vertex IntervAI / Talent Graph AI**, Amazon Bedrock được dùng để đưa AI vào các luồng chính: phân tích CV, tạo câu hỏi phỏng vấn và hỗ trợ đánh giá câu trả lời. Đây là phần giúp dự án vượt khỏi một ứng dụng lưu trữ dữ liệu thông thường và trở thành công cụ luyện phỏng vấn cá nhân hóa.

### Luồng xử lý

1. Người dùng upload CV lên frontend.
2. Backend lưu file vào S3 và metadata vào DynamoDB.
3. Lambda `analyze_cv` gọi Bedrock để rút trích kỹ năng, kinh nghiệm và gợi ý role.
4. Lambda `create_interview` tạo câu hỏi dựa trên CV và role được chọn.
5. Lambda `submit_answer` đánh giá câu trả lời, trả điểm số và nhận xét cải thiện.

### Điều cần lưu ý

* Prompt cần rõ ràng về format output để backend dễ parse.
* Cần có fallback analyzer khi AI service lỗi hoặc trả về dữ liệu không đúng format.
* Kết quả AI nên được lưu lại để người dùng có thể xem history và cải thiện dần.
* Logging qua CloudWatch rất quan trọng để debug prompt, timeout và permission.

### Bài học

Tích hợp AI vào sản phẩm không chỉ là gọi model. Cần thiết kế dữ liệu, prompt, fallback, quyền truy cập và trải nghiệm người dùng. Khi các phần này phối hợp tốt, AI mới trở thành một phần ổn định của ứng dụng.
""",
    "content/3-BlogsPosted/3.3-Blog3/_index.md": """---
title: "Applying Amazon Bedrock in Vertex IntervAI"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Applying Amazon Bedrock in Vertex IntervAI

### Context

In **Vertex IntervAI / Talent Graph AI**, Amazon Bedrock is used to add AI to the core workflows: CV analysis, interview question generation, and answer evaluation. This turns the project from a normal data-storage application into a personalized interview practice tool.

### Processing Flow

1. The user uploads a CV from the frontend.
2. The backend stores the file in S3 and metadata in DynamoDB.
3. The `analyze_cv` Lambda calls Bedrock to extract skills, experience, and role suggestions.
4. The `create_interview` Lambda generates questions based on the CV and selected role.
5. The `submit_answer` Lambda evaluates the answer and returns scores plus improvement feedback.

### Key Notes

* Prompts should clearly define the output format so the backend can parse results safely.
* A fallback analyzer is needed when the AI service fails or returns malformed data.
* AI results should be saved so users can review history and improve over time.
* CloudWatch logging is important for debugging prompts, timeouts, and permissions.

### Lessons Learned

Integrating AI into a product is not only about calling a model. Data design, prompts, fallback handling, permissions, and user experience all matter. When these parts work together, AI becomes a stable part of the application.
""",
}


DATE_PATCHES: dict[str, tuple[str, str]] = {
    "content/2-Proposal/_index.vi.md": ("date: 2024-01-01", "date: 2026-05-11"),
    "content/2-Proposal/_index.md": ("date: 2024-01-01", "date: 2026-05-11"),
    "content/5-Workshop/_index.vi.md": ("date: 2024-01-01", "date: 2026-06-22"),
    "content/5-Workshop/_index.md": ("date: 2024-01-01", "date: 2026-06-22"),
}

WORKSHOP_DATE = "2026-06-22"


def write_if_changed(path: Path, text: str) -> bool:
    old = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    if old == text:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def replace_if_changed(path: Path, old: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    patched = text.replace(old, new, 1)
    if text == patched:
        return False
    path.write_text(patched, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    changed: list[Path] = []
    for relative, text in FILES.items():
        path = ROOT / relative
        if write_if_changed(path, text):
            changed.append(path)

    for relative, (old, new) in DATE_PATCHES.items():
        path = ROOT / relative
        if replace_if_changed(path, old, new):
            changed.append(path)

    for path in (ROOT / "content" / "5-Workshop").rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        patched = text.replace("date : 2024-01-01", f"date: {WORKSHOP_DATE}")
        patched = patched.replace("date: 2024-01-01", f"date: {WORKSHOP_DATE}")
        if text != patched:
            path.write_text(patched, encoding="utf-8", newline="\n")
            changed.append(path)

    print(f"Updated {len(changed)} files")
    for path in changed:
        print(path)


if __name__ == "__main__":
    main()
