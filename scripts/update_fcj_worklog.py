from pathlib import Path


TARGET_ROOT = Path(r"C:\Users\admin\source\fcj-workshop-huydat\content\1-Worklog")

WEEKS = [
    {
        "n": 1,
        "date": "2026-04-17",
        "period": "17/04/2026 - 26/04/2026",
        "vi": {
            "focus": "Định hướng thực tập và làm quen AWS Cloud",
            "objectives": [
                "Tham gia chương trình định hướng thực tập và nắm rõ nội quy của đơn vị thực tập.",
                "Làm quen với môi trường AWS Cloud, AWS Console và các công cụ được sử dụng trong chương trình.",
                "Tạo tài khoản AWS để chuẩn bị cho các bài thực hành và đồ án Vertex-IntervAI.",
            ],
            "tasks": [
                "Tham gia buổi phổ biến nội quy, quy trình làm việc và định hướng chương trình thực tập.",
                "Làm quen với giao diện AWS Management Console và cách tìm kiếm các dịch vụ AWS.",
                "Tạo tài khoản AWS, kiểm tra region sử dụng và chuẩn bị môi trường học tập.",
            ],
            "achievements": [
                "Hoàn thành giai đoạn làm quen ban đầu với chương trình thực tập.",
                "Có thể truy cập AWS Console và nhận biết các nhóm dịch vụ cơ bản.",
                "Chuẩn bị được tài khoản và môi trường để tiếp tục các tuần thực hành tiếp theo.",
            ],
        },
        "en": {
            "focus": "Internship Orientation and AWS Cloud Familiarization",
            "objectives": [
                "Join the internship orientation program and understand the rules of the internship unit.",
                "Become familiar with the AWS Cloud environment, AWS Console, and tools used during the program.",
                "Create an AWS account to prepare for hands-on labs and the Vertex-IntervAI project.",
            ],
            "tasks": [
                "Joined the orientation session about internship rules, working process, and program direction.",
                "Explored the AWS Management Console and learned how to search for AWS services.",
                "Created an AWS account, checked the target region, and prepared the learning environment.",
            ],
            "achievements": [
                "Completed the initial familiarization stage of the internship program.",
                "Able to access AWS Console and recognize basic AWS service groups.",
                "Prepared the account and environment for the following hands-on weeks.",
            ],
        },
        "refs": "AWS Console, AWS Cloud Journey materials",
    },
    {
        "n": 2,
        "date": "2026-04-27",
        "period": "27/04/2026 - 03/05/2026",
        "vi": {
            "focus": "Tìm hiểu các dịch vụ AWS cơ bản",
            "objectives": [
                "Nắm được vai trò của các nhóm dịch vụ AWS nền tảng như Compute, Storage, Database và Networking.",
                "Thực hiện các bài thực hành cơ bản theo hướng dẫn của chương trình.",
                "Xây dựng nền tảng kiến thức để chuẩn bị thiết kế hệ thống serverless.",
            ],
            "tasks": [
                "Tìm hiểu tổng quan các dịch vụ AWS thường dùng trong hệ thống web và backend.",
                "Thực hành thao tác cơ bản trên AWS Console theo tài liệu hướng dẫn.",
                "Ghi chú các dịch vụ có khả năng ứng dụng vào đồ án, đặc biệt là S3, DynamoDB, Lambda và API Gateway.",
            ],
            "achievements": [
                "Hiểu rõ hơn cách AWS tổ chức dịch vụ theo từng nhóm chức năng.",
                "Hoàn thành các bài thực hành nền tảng của chương trình.",
                "Xác định được một số dịch vụ phù hợp với hướng phát triển đồ án AI interview.",
            ],
        },
        "en": {
            "focus": "Learning Basic AWS Services",
            "objectives": [
                "Understand the role of foundational AWS service groups such as Compute, Storage, Database, and Networking.",
                "Complete basic hands-on labs following the program guidance.",
                "Build the knowledge base needed for designing a serverless system.",
            ],
            "tasks": [
                "Studied common AWS services used in web systems and backend applications.",
                "Practiced basic operations in AWS Console following the provided materials.",
                "Documented services that could be applied to the project, especially S3, DynamoDB, Lambda, and API Gateway.",
            ],
            "achievements": [
                "Gained a clearer understanding of how AWS organizes services by functional groups.",
                "Completed the foundational hands-on exercises of the program.",
                "Identified several services suitable for the AI interview project direction.",
            ],
        },
        "refs": "AWS Documentation, AWS Console practice labs",
    },
    {
        "n": 3,
        "date": "2026-05-04",
        "period": "04/05/2026 - 10/05/2026",
        "vi": {
            "focus": "Thảo luận đề tài và tìm hiểu Amazon Bedrock",
            "objectives": [
                "Bắt đầu thảo luận về đề tài sẽ thực hiện trong đồ án.",
                "Làm quen với Amazon Bedrock và các mô hình AI được cung cấp trên AWS.",
                "Tìm hiểu quy trình xây dựng ứng dụng AI trên nền tảng AWS.",
            ],
            "tasks": [
                "Trao đổi các hướng đề tài có thể triển khai trong phạm vi thực tập.",
                "Tìm hiểu khả năng sử dụng Amazon Bedrock cho phân tích nội dung và sinh câu hỏi.",
                "Nghiên cứu cách frontend, backend và AI service có thể phối hợp trong một ứng dụng hoàn chỉnh.",
            ],
            "achievements": [
                "Hiểu được vai trò của Bedrock trong việc tích hợp AI vào ứng dụng.",
                "Có định hướng ban đầu cho một hệ thống phỏng vấn AI dựa trên CV.",
                "Nắm được các thành phần cần có của ứng dụng AI chạy trên AWS.",
            ],
        },
        "en": {
            "focus": "Project Topic Discussion and Amazon Bedrock Research",
            "objectives": [
                "Start discussing the project topic for the internship deliverable.",
                "Become familiar with Amazon Bedrock and AI models provided on AWS.",
                "Study the process of building AI applications on the AWS platform.",
            ],
            "tasks": [
                "Discussed possible project directions within the internship scope.",
                "Studied how Amazon Bedrock could be used for content analysis and question generation.",
                "Researched how frontend, backend, and AI services can work together in a complete application.",
            ],
            "achievements": [
                "Understood the role of Bedrock in integrating AI into an application.",
                "Formed the initial direction for a CV-based AI interview system.",
                "Identified the main components required for an AWS-based AI application.",
            ],
        },
        "refs": "Amazon Bedrock documentation, team discussion notes",
    },
    {
        "n": 4,
        "date": "2026-05-11",
        "period": "11/05/2026 - 17/05/2026",
        "vi": {
            "focus": "Nghiên cứu ý tưởng AI và kiến trúc Serverless",
            "objectives": [
                "Thảo luận các ý tưởng ứng dụng AI có thể triển khai trong đồ án.",
                "Nghiên cứu các dự án mẫu sử dụng AWS Cloud và AI.",
                "Tìm hiểu kiến trúc serverless với AWS Lambda và API Gateway.",
            ],
            "tasks": [
                "So sánh nhiều ý tưởng AI và đánh giá mức độ phù hợp với thời gian thực hiện.",
                "Tìm hiểu luồng request từ frontend đến API Gateway, Lambda và các dịch vụ dữ liệu.",
                "Tham gia trao đổi, chia sẻ kinh nghiệm và nhận góp ý từ các thành viên trong nhóm.",
            ],
            "achievements": [
                "Chọn được hướng phát triển phù hợp hơn cho đồ án Vertex-IntervAI.",
                "Hiểu cách thiết kế backend theo mô hình serverless.",
                "Có cơ sở để chuyển sang giai đoạn khảo sát nhu cầu và xác định phạm vi dự án.",
            ],
        },
        "en": {
            "focus": "AI Idea Research and Serverless Architecture Study",
            "objectives": [
                "Discuss AI application ideas that could be implemented for the project.",
                "Research sample projects using AWS Cloud and AI.",
                "Study serverless architecture with AWS Lambda and API Gateway.",
            ],
            "tasks": [
                "Compared several AI ideas and evaluated their feasibility within the project timeline.",
                "Studied the request flow from frontend to API Gateway, Lambda, and data services.",
                "Joined group discussions, shared experience, and received feedback from team members.",
            ],
            "achievements": [
                "Selected a more suitable development direction for the Vertex-IntervAI project.",
                "Understood how to design backend services using a serverless model.",
                "Prepared the foundation for requirement research and project scope definition.",
            ],
        },
        "refs": "AWS Lambda, API Gateway, AWS serverless references",
    },
    {
        "n": 5,
        "date": "2026-05-18",
        "period": "18/05/2026 - 24/05/2026",
        "vi": {
            "focus": "Khảo sát nhu cầu và thống nhất chủ đề đồ án",
            "objectives": [
                "Tiếp tục thực hiện các bài hướng dẫn của chương trình.",
                "Khảo sát nhu cầu và lựa chọn chủ đề đồ án phù hợp.",
                "Thảo luận, thống nhất hướng phát triển đồ án với các thành viên.",
            ],
            "tasks": [
                "Khảo sát nhu cầu luyện phỏng vấn và chuẩn bị hồ sơ cho sinh viên/người tìm việc.",
                "Xác định ý tưởng Vertex-IntervAI: phân tích CV và tạo phỏng vấn AI theo năng lực ứng viên.",
                "Thống nhất các chức năng trọng tâm như upload CV, phân tích CV, phỏng vấn AI, kết quả và lịch sử.",
            ],
            "achievements": [
                "Hoàn thiện định hướng chủ đề đồ án ở mức chức năng chính.",
                "Xác định được nhóm người dùng mục tiêu và giá trị cốt lõi của hệ thống.",
                "Chuẩn bị yêu cầu đầu vào cho bước thiết kế phạm vi và kiến trúc.",
            ],
        },
        "en": {
            "focus": "Requirement Research and Project Topic Finalization",
            "objectives": [
                "Continue completing the guided program exercises.",
                "Research user needs and select a suitable project topic.",
                "Discuss and agree on the project direction with team members.",
            ],
            "tasks": [
                "Researched the need for interview practice and profile preparation among students/job seekers.",
                "Defined the Vertex-IntervAI idea: analyzing CVs and generating AI interviews based on candidate skills.",
                "Agreed on key features such as CV upload, CV analysis, AI interview, result, and history.",
            ],
            "achievements": [
                "Finalized the project direction at the main-feature level.",
                "Identified target users and the core value of the system.",
                "Prepared input requirements for scope and architecture design.",
            ],
        },
        "refs": "Project requirement notes, AWS workshop exercises",
    },
    {
        "n": 6,
        "date": "2026-05-25",
        "period": "25/05/2026 - 31/05/2026",
        "vi": {
            "focus": "Hoàn thiện phạm vi và thiết kế kiến trúc sơ bộ",
            "objectives": [
                "Hoàn thiện ý tưởng và phạm vi thực hiện đồ án.",
                "Phân chia nhiệm vụ cho từng thành viên trong nhóm.",
                "Thiết kế sơ bộ kiến trúc cho hệ thống Vertex-IntervAI.",
            ],
            "tasks": [
                "Mô tả các module chính của hệ thống: frontend, backend API, database, storage và AI services.",
                "Phân công nhiệm vụ backend và database cho cá nhân phụ trách.",
                "Phác thảo luồng dữ liệu từ người dùng upload CV đến phân tích CV, tạo phỏng vấn và lưu kết quả.",
            ],
            "achievements": [
                "Hoàn thành phạm vi chức năng ban đầu cho đồ án.",
                "Xác định được các service AWS sẽ tích hợp trong hệ thống.",
                "Có bản thiết kế sơ bộ để bắt đầu triển khai backend và database.",
            ],
        },
        "en": {
            "focus": "Scope Finalization and Initial Architecture Design",
            "objectives": [
                "Finalize the project idea and implementation scope.",
                "Assign responsibilities to each team member.",
                "Create the initial architecture design for Vertex-IntervAI.",
            ],
            "tasks": [
                "Described the main system modules: frontend, backend API, database, storage, and AI services.",
                "Assigned backend and database responsibilities to the responsible member.",
                "Drafted the data flow from CV upload to CV analysis, interview generation, and result storage.",
            ],
            "achievements": [
                "Completed the initial functional scope of the project.",
                "Identified the AWS services to be integrated into the system.",
                "Prepared an initial design for backend and database implementation.",
            ],
        },
        "refs": "Architecture notes, AWS Lambda, API Gateway, DynamoDB, S3",
    },
    {
        "n": 7,
        "date": "2026-06-01",
        "period": "01/06/2026 - 07/06/2026",
        "vi": {
            "focus": "Khởi tạo Backend và thiết kế Database",
            "objectives": [
                "Bắt đầu triển khai đồ án theo kế hoạch của nhóm.",
                "Thực hiện phần Backend và Database được phân công.",
                "Phân tích dữ liệu cần lưu trữ và thiết kế cơ sở dữ liệu cho hệ thống.",
            ],
            "tasks": [
                "Thiết kế các bảng dữ liệu phục vụ Users, CVs, Interviews và thông tin hồ sơ người dùng.",
                "Xây dựng cấu trúc thư mục backend cho các AWS Lambda function.",
                "Tạo bucket Amazon S3 để lưu trữ tài liệu CV và kiểm tra kết nối ban đầu.",
            ],
            "achievements": [
                "Hoàn thành thiết kế dữ liệu nền tảng cho hệ thống.",
                "Có cấu trúc backend rõ ràng để phát triển từng Lambda riêng biệt.",
                "Kết nối được S3 storage phục vụ chức năng upload CV.",
            ],
        },
        "en": {
            "focus": "Backend Initialization and Database Design",
            "objectives": [
                "Start implementing the project according to the team plan.",
                "Work on the assigned Backend and Database responsibilities.",
                "Analyze storage requirements and design the system database structure.",
            ],
            "tasks": [
                "Designed data tables for Users, CVs, Interviews, and user profile information.",
                "Created the backend folder structure for AWS Lambda functions.",
                "Created an Amazon S3 bucket for CV document storage and verified the initial connection.",
            ],
            "achievements": [
                "Completed the foundational data design for the system.",
                "Prepared a clear backend structure for developing separate Lambda functions.",
                "Verified S3 storage integration for the CV upload feature.",
            ],
        },
        "refs": "Amazon S3, DynamoDB, AWS Lambda",
    },
    {
        "n": 8,
        "date": "2026-06-08",
        "period": "08/06/2026 - 14/06/2026",
        "vi": {
            "focus": "Xây dựng chức năng Upload CV",
            "objectives": [
                "Xây dựng chức năng Upload CV phía Backend.",
                "Kiểm tra định dạng tệp PDF/DOC/DOCX trước khi lưu trữ.",
                "Lưu thông tin CV vào cơ sở dữ liệu và kiểm thử API upload.",
            ],
            "tasks": [
                "Phát triển Lambda `upload_cv` để nhận CV dạng base64 từ frontend/API client.",
                "Lưu file CV vào Amazon S3 theo cấu trúc thư mục người dùng và CV ID.",
                "Lưu metadata của CV vào DynamoDB và kiểm thử API bằng Postman.",
                "Khắc phục lỗi phát sinh trong quá trình xử lý dữ liệu upload.",
            ],
            "achievements": [
                "Hoàn thành API upload CV đầu tiên của backend.",
                "CV được lưu vào S3 và metadata được ghi nhận trong DynamoDB.",
                "Có nền tảng dữ liệu để tiếp tục phát triển chức năng phân tích CV.",
            ],
        },
        "en": {
            "focus": "Building the CV Upload Feature",
            "objectives": [
                "Build the backend CV upload feature.",
                "Validate PDF/DOC/DOCX file formats before storage.",
                "Save CV information to the database and test the upload API.",
            ],
            "tasks": [
                "Developed the `upload_cv` Lambda to receive base64 CV files from the frontend/API client.",
                "Stored CV files in Amazon S3 using a user and CV ID folder structure.",
                "Saved CV metadata to DynamoDB and tested the API using Postman.",
                "Fixed issues that occurred during upload data processing.",
            ],
            "achievements": [
                "Completed the first backend API for CV upload.",
                "CV files were stored in S3 and metadata was recorded in DynamoDB.",
                "Prepared the data foundation for developing CV analysis.",
            ],
        },
        "refs": "AWS Lambda, Amazon S3, DynamoDB, Postman",
    },
    {
        "n": 9,
        "date": "2026-06-15",
        "period": "15/06/2026 - 21/06/2026",
        "vi": {
            "focus": "Phát triển phiên phỏng vấn AI và lưu câu trả lời",
            "objectives": [
                "Phát triển chức năng tạo phiên phỏng vấn AI.",
                "Xây dựng API lưu câu trả lời và kết quả đánh giá.",
                "Thiết kế cấu trúc dữ liệu lưu lịch sử phỏng vấn.",
            ],
            "tasks": [
                "Xây dựng Lambda `create_interview` để tạo bộ câu hỏi dựa trên CV và vai trò ứng tuyển.",
                "Xây dựng Lambda `submit_answer` để nhận câu trả lời, chấm điểm và lưu kết quả.",
                "Thiết kế cấu trúc bảng Interviews để lưu câu hỏi, câu trả lời, điểm số và trạng thái phiên phỏng vấn.",
                "Sửa các lỗi phát sinh trong quá trình tích hợp giữa frontend và backend.",
            ],
            "achievements": [
                "Hệ thống có thể tạo phiên phỏng vấn AI từ dữ liệu CV.",
                "Câu trả lời của người dùng được lưu cùng điểm và phản hồi đánh giá.",
                "Lịch sử phỏng vấn bắt đầu được lưu trữ theo userId và interviewId.",
            ],
        },
        "en": {
            "focus": "Developing AI Interview Sessions and Answer Storage",
            "objectives": [
                "Develop the AI interview session creation feature.",
                "Build APIs for storing answers and evaluation results.",
                "Design the data structure for interview history.",
            ],
            "tasks": [
                "Built the `create_interview` Lambda to generate questions based on CV data and target roles.",
                "Built the `submit_answer` Lambda to receive answers, score them, and store results.",
                "Designed the Interviews table structure to store questions, answers, scores, and interview status.",
                "Fixed integration issues between frontend and backend.",
            ],
            "achievements": [
                "The system could create AI interview sessions from CV data.",
                "User answers were stored with scores and evaluation feedback.",
                "Interview history started being stored by userId and interviewId.",
            ],
        },
        "refs": "Amazon Bedrock, AWS Lambda, DynamoDB Interviews table",
    },
    {
        "n": 10,
        "date": "2026-06-22",
        "period": "22/06/2026 - 28/06/2026",
        "vi": {
            "focus": "API hồ sơ người dùng và lịch sử hoạt động",
            "objectives": [
                "Xây dựng API quản lý hồ sơ người dùng và lịch sử hoạt động.",
                "Hoàn thiện cấu trúc dữ liệu lưu lịch sử phỏng vấn.",
                "Tiếp tục hoàn thiện API lưu câu trả lời và kết quả đánh giá.",
            ],
            "tasks": [
                "Phát triển Lambda `profile_api` để đọc và cập nhật thông tin người dùng trong DynamoDB.",
                "Chuẩn hóa dữ liệu lịch sử phỏng vấn để frontend có thể hiển thị kết quả và tiến độ.",
                "Kiểm tra lại luồng gửi câu trả lời, chấm điểm và cập nhật điểm tổng kết.",
                "Sửa lỗi phát sinh khi gọi API từ giao diện React.",
            ],
            "achievements": [
                "Hoàn thiện API hồ sơ người dùng ở mức cơ bản.",
                "Dữ liệu câu trả lời và điểm đánh giá được cập nhật ổn định hơn.",
                "Frontend có thể lấy dữ liệu phục vụ trang kết quả và lịch sử.",
            ],
        },
        "en": {
            "focus": "User Profile and Activity History APIs",
            "objectives": [
                "Build APIs for user profile management and activity history.",
                "Complete the data structure for interview history.",
                "Continue improving the answer and evaluation result APIs.",
            ],
            "tasks": [
                "Developed the `profile_api` Lambda to read and update user information in DynamoDB.",
                "Standardized interview history data so the frontend could display results and progress.",
                "Rechecked the flow for submitting answers, scoring, and updating the final score.",
                "Fixed issues when calling APIs from the React interface.",
            ],
            "achievements": [
                "Completed the basic user profile API.",
                "Answer and evaluation score data became more stable.",
                "The frontend could retrieve data for result and history pages.",
            ],
        },
        "refs": "DynamoDB Users, DynamoDB Interviews, React service layer",
    },
    {
        "n": 11,
        "date": "2026-06-29",
        "period": "29/06/2026 - 05/07/2026",
        "vi": {
            "focus": "Hoàn thiện hồ sơ, lịch sử CV và tối ưu web",
            "objectives": [
                "Hoàn thiện API cập nhật thông tin cá nhân.",
                "Xây dựng chức năng lấy lịch sử CV và lịch sử phỏng vấn.",
                "Sửa lỗi và tối ưu tốc độ của web.",
            ],
            "tasks": [
                "Hoàn thiện luồng cập nhật profile và đồng bộ thông tin người dùng từ Cognito/local storage với DynamoDB.",
                "Phát triển Lambda `history_api` để lấy lịch sử CV và lịch sử phỏng vấn theo userId.",
                "Điều chỉnh frontend để hiển thị lịch sử, trạng thái CV, kết quả phỏng vấn và thông tin người dùng ổn định hơn.",
                "Tối ưu trải nghiệm web và sửa các lỗi giao diện phát sinh.",
            ],
            "achievements": [
                "Người dùng có thể cập nhật hồ sơ cá nhân và xem lại dữ liệu đã tạo.",
                "Trang History và Result có dữ liệu rõ ràng hơn từ backend/local fallback.",
                "Giao diện web ổn định hơn trước khi chuyển sang kiểm thử toàn bộ hệ thống.",
            ],
        },
        "en": {
            "focus": "Completing Profile, CV History, and Web Optimization",
            "objectives": [
                "Complete the personal information update API.",
                "Build functions for retrieving CV history and interview history.",
                "Fix issues and optimize web performance.",
            ],
            "tasks": [
                "Completed the profile update flow and synchronized user information from Cognito/local storage with DynamoDB.",
                "Developed the `history_api` Lambda to retrieve CV and interview history by userId.",
                "Adjusted the frontend to display history, CV status, interview results, and user information more reliably.",
                "Optimized the web experience and fixed UI issues.",
            ],
            "achievements": [
                "Users could update their profile and review generated data.",
                "History and Result pages displayed clearer data from backend/local fallback.",
                "The web interface became more stable before full-system testing.",
            ],
        },
        "refs": "profile_api, history_api, DynamoDB, React UI",
    },
    {
        "n": 12,
        "date": "2026-07-06",
        "period": "06/07/2026 - 12/07/2026",
        "vi": {
            "focus": "Kiểm thử API và khắc phục lỗi quyền truy cập",
            "objectives": [
                "Kiểm thử toàn bộ các API của hệ thống.",
                "Khắc phục các lỗi về quyền truy cập và kết nối.",
                "Chuẩn bị hệ thống cho giai đoạn hoàn thiện, demo và triển khai.",
            ],
            "tasks": [
                "Kiểm thử các API chính: upload CV, analyze CV, profile, history, create interview và submit answer.",
                "Kiểm tra quyền IAM cho Lambda khi truy cập S3, DynamoDB, Bedrock, Polly và Transcribe.",
                "Rà soát kết nối API Gateway, CORS và các biến môi trường backend/frontend.",
                "Tổng hợp lỗi còn tồn tại và điều chỉnh để hệ thống sẵn sàng demo.",
            ],
            "achievements": [
                "Các API chính được kiểm thử theo luồng nghiệp vụ của hệ thống.",
                "Nhiều lỗi về quyền truy cập, kết nối service và cấu hình môi trường được phát hiện và xử lý.",
                "Hệ thống đạt trạng thái sẵn sàng để tiếp tục hoàn thiện giao diện, báo cáo và triển khai web thật.",
            ],
        },
        "en": {
            "focus": "API Testing and Permission Issue Resolution",
            "objectives": [
                "Test all APIs of the system.",
                "Resolve permission and connectivity issues.",
                "Prepare the system for finalization, demo, and deployment.",
            ],
            "tasks": [
                "Tested main APIs: upload CV, analyze CV, profile, history, create interview, and submit answer.",
                "Checked Lambda IAM permissions for accessing S3, DynamoDB, Bedrock, Polly, and Transcribe.",
                "Reviewed API Gateway connectivity, CORS, and backend/frontend environment variables.",
                "Summarized remaining issues and adjusted the system for demo readiness.",
            ],
            "achievements": [
                "Main APIs were tested according to the system workflow.",
                "Several permission, service connectivity, and environment configuration issues were identified and resolved.",
                "The system became ready for final UI polishing, reporting, and public web deployment.",
            ],
        },
        "refs": "API Gateway, IAM, CloudWatch Logs, AWS service integration checks",
    },
]


def bullet(items):
    return "\n".join(f"* {item}" for item in items)


def table(items, period, refs, vi):
    if vi:
        rows = [
            "| STT | Công việc | Thời gian | Nguồn tài liệu |",
            "| --- | --- | --- | --- |",
        ]
    else:
        rows = [
            "| No. | Task | Duration | Reference Material |",
            "| --- | --- | --- | --- |",
        ]

    for index, item in enumerate(items, start=1):
        rows.append(f"| {index} | {item} | {period} | {refs} |")
    return "\n".join(rows)


def week_file(week, lang):
    data = week[lang]
    n = week["n"]
    if lang == "vi":
        return f"""---
title: "Worklog Tuần {n}"
date: {week['date']}
weight: {n}
chapter: false
pre: " <b> 1.{n}. </b> "
---

### Mục tiêu tuần {n}: {data['focus']}

{bullet(data['objectives'])}

### Các công việc đã triển khai trong tuần này:

{table(data['tasks'], week['period'], week['refs'], True)}

### Kết quả đạt được tuần {n}:

{bullet(data['achievements'])}
"""

    return f"""---
title: "Week {n} Worklog"
date: {week['date']}
weight: {n}
chapter: false
pre: " <b> 1.{n}. </b> "
---

### Week {n} Objectives: {data['focus']}

{bullet(data['objectives'])}

### Work completed this week:

{table(data['tasks'], week['period'], week['refs'], False)}

### Week {n} Achievements:

{bullet(data['achievements'])}
"""


def index_file(lang):
    if lang == "vi":
        rows = [
            "| Tuần | Thời gian | Nội dung chính | Chi tiết |",
            "| --- | --- | --- | --- |",
        ]
        for week in WEEKS:
            rows.append(
                f"| Tuần {week['n']} | {week['period']} | {week['vi']['focus']} | "
                f"[Xem chi tiết](1.{week['n']}-week{week['n']}/) |"
            )
        return f"""---
title: "Nhật ký công việc"
date: 2026-04-17
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

Phần worklog này ghi lại tiến độ thực tập và quá trình xây dựng đồ án **Vertex-IntervAI / Talent Graph AI** trong 12 tuần, từ ngày **17/04/2026** đến ngày **12/07/2026**.

Trong giai đoạn đầu, tôi làm quen với chương trình thực tập, AWS Cloud, AWS Console và các dịch vụ nền tảng. Ở giai đoạn giữa, tôi cùng nhóm xác định chủ đề đồ án, nghiên cứu Amazon Bedrock và kiến trúc serverless. Ở giai đoạn triển khai, tôi phụ trách phần **Backend** và **Database**, bao gồm AWS Lambda, API Gateway, DynamoDB, S3 và các tích hợp AI/voice phục vụ luồng upload CV, phân tích CV, phỏng vấn AI, lưu kết quả và lịch sử.

### Tổng quan tiến độ

{chr(10).join(rows)}

### Kết quả chung

* Hoàn thành nền tảng backend serverless cho các chức năng chính của hệ thống.
* Thiết kế và sử dụng các bảng dữ liệu phục vụ CV, người dùng và phỏng vấn.
* Tích hợp S3 để lưu CV, audio và transcript; tích hợp Bedrock/Polly/Transcribe cho các chức năng AI và voice.
* Kiểm thử API, xử lý lỗi quyền truy cập, cấu hình môi trường và chuẩn bị hệ thống cho demo/triển khai.
"""

    rows = [
        "| Week | Duration | Main Focus | Details |",
        "| --- | --- | --- | --- |",
    ]
    for week in WEEKS:
        rows.append(
            f"| Week {week['n']} | {week['period']} | {week['en']['focus']} | "
            f"[View details](1.{week['n']}-week{week['n']}/) |"
        )
    return f"""---
title: "Worklog"
date: 2026-04-17
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

This worklog records the internship progress and the development of **Vertex-IntervAI / Talent Graph AI** over 12 weeks, from **17/04/2026** to **12/07/2026**.

In the early stage, I became familiar with the internship program, AWS Cloud, AWS Console, and foundational AWS services. In the middle stage, the team defined the project topic, researched Amazon Bedrock, and studied serverless architecture. During implementation, I focused on **Backend** and **Database** work, including AWS Lambda, API Gateway, DynamoDB, S3, and AI/voice integrations for CV upload, CV analysis, AI interview, result storage, and history tracking.

### Progress overview

{chr(10).join(rows)}

### Overall outcomes

* Completed the serverless backend foundation for the main system features.
* Designed and used data tables for CVs, users, and interviews.
* Integrated S3 for CV, audio, and transcript storage; integrated Bedrock/Polly/Transcribe for AI and voice features.
* Tested APIs, resolved permission issues, configured environments, and prepared the system for demo/deployment.
"""


def main():
    files = {
        TARGET_ROOT / "_index.vi.md": index_file("vi"),
        TARGET_ROOT / "_index.md": index_file("en"),
    }

    for week in WEEKS:
        folder = TARGET_ROOT / f"1.{week['n']}-Week{week['n']}"
        files[folder / "_index.vi.md"] = week_file(week, "vi")
        files[folder / "_index.md"] = week_file(week, "en")

    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")

    print(f"Updated {len(files)} files in {TARGET_ROOT}")


if __name__ == "__main__":
    main()
