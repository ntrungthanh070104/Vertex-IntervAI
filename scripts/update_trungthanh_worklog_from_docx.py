from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

from docx import Document


@dataclass(frozen=True)
class WeekVi:
    week: int
    start: datetime
    end: datetime
    tasks: list[str]
    achievements: list[str]


EN_DATA: dict[int, dict[str, list[str] | str]] = {
    1: {
        "objectives": [
            "Get familiar with the internship scope and early-stage goals.",
            "Create an AWS account and learn the AWS Console, CLI, and cost-control basics.",
        ],
        "tasks": [
            "Get acquainted with the internship content and define early-stage goals",
            "Create an Amazon Web Services account and activate the Free Tier",
            "Explore the AWS Management Console and Region-based service organization",
            "Learn core services such as EC2, S3, and IAM",
            "Install AWS CLI and run basic commands",
            "Learn cost management and budget setup on AWS",
            "Review official AWS documentation and support channels",
        ],
        "achievements": [
            "Successfully created and used an AWS account.",
            "Understood the basic structure of the AWS cloud platform.",
            "Understood the purpose of several core AWS services.",
            "Learned how to control cloud-service costs.",
            "Became familiar with both AWS Console and CLI operations.",
        ],
        "summary": "AWS onboarding, account setup, Console/CLI, and cost management",
    },
    2: {
        "objectives": [
            "Understand VPC and basic AWS network architecture.",
            "Practice EC2 connectivity and basic security controls.",
        ],
        "tasks": [
            "Learn Virtual Private Cloud (VPC) and AWS network design",
            "Distinguish Security Groups and Network ACLs",
            "Practice creating a VPC and configuring public/private subnets",
            "Set up an Internet Gateway and Route Table",
            "Create an EC2 instance and verify SSH connectivity",
            "Explore basic system management and monitoring tools",
            "Create and complete a personal LinkedIn profile",
        ],
        "achievements": [
            "Understood how to design a basic AWS network.",
            "Deployed a simple cloud environment.",
            "Connected to and used an EC2 instance successfully.",
            "Understood basic AWS security mechanisms.",
            "Completed a LinkedIn profile for learning and career development.",
        ],
        "summary": "VPC, EC2, basic AWS networking, and LinkedIn profile setup",
    },
    3: {
        "objectives": [
            "Deepen practical knowledge of Amazon S3 and IAM policy design.",
            "Deploy a first Lambda function and connect it to S3 events.",
        ],
        "tasks": [
            "Deep dive into Amazon S3: Static Website Hosting, Bucket Policy, Versioning, and CORS",
            "Practice advanced IAM Policy, Principle of Least Privilege, and IAM Role",
            "Deploy the first Lambda Function, write Python code, and test invocation",
            "Integrate Lambda with an S3 Event trigger",
        ],
        "achievements": [
            "Became more proficient with Amazon S3 and practical features.",
            "Successfully deployed a Lambda Function and understood service integration.",
            "Understood the Event-Driven Architecture model more clearly.",
        ],
        "summary": "Advanced S3, IAM policy, Lambda, and S3 event trigger",
    },
    4: {
        "objectives": [
            "Practice DynamoDB, API Gateway, and Amazon Bedrock.",
            "Start shaping the Vertex IntervAI workshop idea.",
        ],
        "tasks": [
            "Continue learning and practicing key AWS services: Amazon DynamoDB, Amazon API Gateway, and Amazon Bedrock",
            "Practice designing and deploying DynamoDB tables with suitable primary and secondary keys",
            "Configure API Gateway to create a REST API and integrate it with a Lambda Function",
            "Learn Amazon Bedrock (Claude 3.5 Sonnet) and how to use it through an API",
            "Discuss with the team and agree on the workshop project name: Vertex IntervAI",
            "Draft the initial logo and overall project idea",
            "Update the Worklog and Proposal for the workshop",
        ],
        "achievements": [
            "Understood how to use and integrate DynamoDB in a Serverless application.",
            "Successfully deployed API Gateway connected with Lambda.",
            "Gained an initial view of how Amazon Bedrock can support natural-language processing.",
            "Completed the project name and core idea for the personal workshop: Vertex IntervAI.",
            "Learning and AWS practice progress stayed on track.",
        ],
        "summary": "DynamoDB, API Gateway, Bedrock, and Vertex IntervAI kickoff",
    },
    5: {
        "objectives": [
            "Practice core AWS services across identity, storage, compute, and networking.",
            "Build a stronger foundation for cloud environment design.",
        ],
        "tasks": [
            "Learn and practice IAM: User, Group, Role, custom Policy, and MFA setup",
            "Practice Amazon S3 in depth: bucket creation, Versioning, static website hosting, Bucket Policy, and Lifecycle rules",
            "Deploy and manage Amazon EC2: launch Linux and Windows instances, Security Group, Key Pair, Elastic IP, and User Data",
            "Learn basic VPC Networking: Public/Private Subnet, Internet Gateway, Route Table, and NAT Gateway",
            "Explore RDS, DynamoDB, and CloudWatch at a basic level",
        ],
        "achievements": [
            "Became familiar with and practiced six important AWS services.",
            "Gained the ability to build a basic cloud environment (VPC + EC2 + S3).",
            "Understood the Shared Responsibility Model and core AWS concepts more clearly.",
        ],
        "summary": "IAM, S3, EC2, VPC, RDS, DynamoDB, and CloudWatch basics",
    },
    6: {
        "objectives": [
            "Practice Serverless, messaging, CDN, and DNS services.",
            "Integrate Lambda, API Gateway, SQS/SNS, CloudFront, and Route 53.",
        ],
        "tasks": [
            "Learn and practice AWS Lambda: create function, trigger, version, Layer, and environment",
            "Learn and deploy API Gateway: REST API, Lambda integration, method, stage, and usage plan",
            "Practice Amazon SQS and SNS: queue, topic, subscription, message send/receive, and Dead Letter Queue",
            "Learn Amazon CloudFront: Distribution for S3, caching, HTTPS, and Geo Restriction",
            "Learn Route 53: Hosted Zone, record sets (A, CNAME, Alias), and basic Health Check",
            "Practice service integration: Lambda + API Gateway + SQS + CloudFront",
        ],
        "achievements": [
            "Mastered how to use and connect five additional AWS services.",
            "Gained the ability to build a basic Serverless application (API + Compute + Messaging + CDN).",
            "Understood Serverless design and Low Operational Overhead more clearly.",
        ],
        "summary": "Lambda, API Gateway, SQS/SNS, CloudFront, and Route 53",
    },
    7: {
        "objectives": [
            "Practice container, database, monitoring, and security services.",
            "Apply AWS Well-Architected concepts through hands-on labs.",
        ],
        "tasks": [
            "Learn and practice Amazon ECS: create Cluster, Task Definition, Service, and run containers on Fargate",
            "Learn Application Load Balancer (ALB) and Auto Scaling Group: configure load balancing and automatic scaling",
            "Study Amazon RDS in depth: deploy MySQL/PostgreSQL, Multi-AZ, Read Replica, Backup, and Restore",
            "Practice Amazon CloudWatch: Metrics, Alarms, Logs Insights, and Dashboard",
            "Explore security services: AWS WAF, AWS Shield, and advanced IAM (Condition, Permission Boundary)",
            "Complete integrated labs across ECS + ALB + RDS + CloudWatch",
            "Read AWS Well-Architected Framework documentation and practice on AWS Skill Builder / AWS Console",
        ],
        "achievements": [
            "Mastered five more important AWS services, especially Container and Monitoring.",
            "Gained the ability to deploy a basic containerized application with load balancing and monitoring.",
            "Accumulated more than 21 hours of hands-on practice during the week.",
            "Understood scalable, reliable, and observable system design more clearly.",
        ],
        "summary": "ECS, ALB, RDS, CloudWatch, Security, and Well-Architected practice",
    },
    8: {
        "objectives": [
            "Continue container, monitoring, database, and security practice.",
            "Strengthen scalable and observable architecture design skills.",
        ],
        "tasks": [
            "Learn and practice Amazon ECS: create Cluster, Task Definition, Service, and run containers on Fargate",
            "Learn Application Load Balancer (ALB) and Auto Scaling Group: configure load balancing and automatic scaling",
            "Study Amazon RDS in depth: deploy MySQL/PostgreSQL, Multi-AZ, Read Replica, Backup, and Restore",
            "Practice Amazon CloudWatch: Metrics, Alarms, Logs Insights, and Dashboard",
            "Explore security services: AWS WAF, AWS Shield, and advanced IAM (Condition, Permission Boundary)",
            "Complete integrated labs across ECS + ALB + RDS + CloudWatch",
            "Read AWS Well-Architected Framework documentation and practice on AWS Skill Builder / AWS Console",
        ],
        "achievements": [
            "Mastered five more important AWS services, especially Container and Monitoring.",
            "Gained the ability to deploy a basic containerized application with load balancing and monitoring.",
            "Accumulated more than 21 hours of hands-on practice during the week.",
            "Understood scalable, reliable, and observable system design more clearly.",
        ],
        "summary": "Continued ECS, ALB, RDS, CloudWatch, Security, and Well-Architected practice",
    },
    9: {
        "objectives": [
            "Study advanced AWS networking, security, and cost optimization.",
            "Consolidate AWS knowledge before project implementation.",
        ],
        "tasks": [
            "Study advanced Networking, Security, and cost optimization services",
            "Consolidate comprehensive AWS knowledge",
            "Prepare the technical foundation for the project",
        ],
        "achievements": [
            "Learned advanced Amazon VPC topics: VPC Peering, Transit Gateway, and PrivateLink.",
            "Practiced AWS Direct Connect, VPN, and advanced Route 53.",
            "Studied AWS Cost Explorer, Budgets, and Trusted Advisor.",
            "Studied AWS Config, CloudTrail, and GuardDuty for monitoring and compliance.",
            "Completed hands-on labs about Hybrid Networking and Cost Optimization.",
        ],
        "summary": "Advanced Networking, Security, and Cost Optimization",
    },
    10: {
        "objectives": [
            "Learn basic AWS AI/ML services and workflow orchestration.",
            "Contribute to the high-level architecture for the workshop project.",
        ],
        "tasks": [
            "Learn Amazon SageMaker basics, Rekognition, and Comprehend for AI/ML use cases",
            "Learn AWS Step Functions and EventBridge for workflow orchestration",
            "Join group meetings and design the overall project High-level Architecture",
            "Draw the proposed architecture diagram using draw.io or AWS Perspective",
            "Practice labs integrating AI/ML and workflow orchestration",
        ],
        "achievements": [
            "Completed foundational knowledge for most core AWS services.",
            "Contributed the initial architecture design for the group project.",
            "Accumulated more than 18 hours of hands-on practice and group discussion.",
            "Gained the ability to propose suitable architecture solutions.",
        ],
        "summary": "AWS AI/ML, Step Functions, EventBridge, and project architecture",
    },
    11: {
        "objectives": [
            "Implement backend features for Vertex IntervAI.",
            "Integrate S3, DynamoDB, Bedrock, API Gateway, and frontend flows.",
        ],
        "tasks": [
            "Implement backend Lambda functions for Vertex IntervAI: upload_cv, analyze_cv, create_interview, and submit_answer",
            "Integrate Amazon S3 for CV storage and DynamoDB for metadata management (CVs, Users, Interviews)",
            "Implement CV analysis logic using Amazon Bedrock (Claude 3.5 Sonnet) with fallback analyzer",
            "Support React frontend integration with API Gateway: upload CV, create AI interview, and submit answers",
            "Run integration tests for the main flow: Upload CV -> Analyze -> Interview",
            "Join team meetings to review architecture and divide tasks",
            "Update the Worklog and project documentation",
        ],
        "achievements": [
            "Completed the backend core for the main project features.",
            "The system can process the end-to-end Upload and Analyze CV flow successfully.",
            "Successfully integrated Amazon Bedrock into CV analysis and interview scoring.",
            "Frontend and backend communicate smoothly through API Gateway.",
            "The team has the first demo version of Vertex IntervAI.",
        ],
        "summary": "Vertex IntervAI backend, Bedrock integration, API Gateway, and frontend connection",
    },
    12: {
        "objectives": [
            "Complete and optimize the Vertex IntervAI MVP.",
            "Prepare demo materials, architecture documentation, and final testing.",
        ],
        "tasks": [
            "Complete and optimize Lambda functions (error handling, CORS, fallback mechanism)",
            "Implement Profile storage and synchronization with DynamoDB; add AI interview features (voice recording mock + text-to-speech) and improve AI feedback",
            "Run full-system tests (Lambda unit tests + end-to-end test); set up basic CI/CD with AWS CodePipeline if applicable",
            "Prepare demo documentation, architecture diagram, and progress report",
            "Join the final team meeting to summarize work and prepare the presentation",
        ],
        "achievements": [
            "Completed the MVP (Minimum Viable Product) version of Vertex IntervAI.",
            "The system supports the main flows: CV upload, AI analysis, interactive AI interview, and Profile.",
            "Improved stability and fallback behavior when AWS services have issues.",
            "Prepared architecture documents and demo materials for presentation.",
            "Completed the internship phase with practical Serverless development experience on AWS.",
        ],
        "summary": "Vertex IntervAI MVP optimization, testing, demo docs, and final presentation",
    },
}


VI_OBJECTIVES: dict[int, list[str]] = {
    1: [
        "Làm quen với nội dung thực tập và mục tiêu giai đoạn đầu.",
        "Tạo tài khoản AWS, làm quen Console/CLI và quản lý chi phí cơ bản.",
    ],
    2: [
        "Tìm hiểu VPC và kiến trúc mạng cơ bản trên AWS.",
        "Thực hành EC2, kết nối SSH và các cơ chế bảo mật nền tảng.",
    ],
    3: [
        "Tìm hiểu sâu hơn về Amazon S3 và IAM Policy.",
        "Triển khai Lambda Function đầu tiên và tích hợp với S3 Event.",
    ],
    4: [
        "Thực hành DynamoDB, API Gateway và Amazon Bedrock.",
        "Khởi tạo ý tưởng dự án Workshop Vertex IntervAI.",
    ],
    5: [
        "Thực hành các dịch vụ AWS cốt lõi về định danh, lưu trữ, compute và networking.",
        "Củng cố nền tảng để tự xây dựng môi trường cloud cơ bản.",
    ],
    6: [
        "Thực hành nhóm dịch vụ Serverless, messaging, CDN và DNS.",
        "Tích hợp Lambda, API Gateway, SQS/SNS, CloudFront và Route 53.",
    ],
    7: [
        "Thực hành container, database, monitoring và security trên AWS.",
        "Áp dụng AWS Well-Architected Framework qua các bài lab tích hợp.",
    ],
    8: [
        "Tiếp tục củng cố container, monitoring, database và security.",
        "Nâng cao khả năng thiết kế hệ thống scalable, reliable và observable.",
    ],
    9: [
        "Tìm hiểu networking, security nâng cao và tối ưu chi phí trên AWS.",
        "Củng cố kiến thức AWS trước giai đoạn triển khai dự án.",
    ],
    10: [
        "Tìm hiểu các dịch vụ AI/ML cơ bản và workflow orchestration trên AWS.",
        "Đóng góp thiết kế kiến trúc tổng thể cho dự án Workshop.",
    ],
    11: [
        "Triển khai backend cho dự án Vertex IntervAI.",
        "Tích hợp S3, DynamoDB, Bedrock, API Gateway và frontend.",
    ],
    12: [
        "Hoàn thiện và tối ưu phiên bản MVP của Vertex IntervAI.",
        "Chuẩn bị tài liệu demo, diagram kiến trúc và kiểm thử cuối kỳ.",
    ],
}


def parse_date(raw: str) -> datetime:
    return datetime.strptime(raw.strip(), "%d-%m-%Y")


def parse_docx(docx_path: Path) -> dict[int, WeekVi]:
    doc = Document(docx_path)
    weeks: dict[int, WeekVi] = {}

    for table in doc.tables:
        for row in table.rows[1:]:
            week_text = " ".join(row.cells[0].text.split())
            match = re.search(r"\d+", week_text)
            if not match:
                continue
            week = int(match.group(0))

            dates = re.findall(r"\d{2}-\d{2}-\d{4}", row.cells[1].text)
            if len(dates) != 2:
                raise ValueError(f"Could not parse date range for week {week}: {row.cells[1].text!r}")

            lines = [
                line.strip().replace("•", "<br> -")
                for line in row.cells[2].text.splitlines()
                if line.strip()
            ]
            try:
                start_tasks = lines.index("Nội dung thực hiện:") + 1
                start_achievements = lines.index("Kết quả đạt được:")
            except ValueError as exc:
                raise ValueError(f"Could not parse content sections for week {week}") from exc

            tasks = lines[start_tasks:start_achievements]
            achievements = lines[start_achievements + 1 :]
            weeks[week] = WeekVi(week, parse_date(dates[0]), parse_date(dates[1]), tasks, achievements)

    missing = sorted(set(range(1, 13)) - set(weeks))
    if missing:
        raise ValueError(f"Missing weeks in DOCX: {missing}")
    return weeks


def date_slash(value: datetime) -> str:
    return value.strftime("%d/%m/%Y")


def date_iso(value: datetime) -> str:
    return value.strftime("%Y-%m-%d")


def split_task_dates(start: datetime, end: datetime, count: int) -> list[tuple[str, str]]:
    total_days = (end - start).days + 1
    ranges: list[tuple[str, str]] = []
    for index in range(count):
        start_offset = round(index * total_days / count)
        end_offset = round((index + 1) * total_days / count) - 1
        if end_offset < start_offset:
            end_offset = start_offset
        ranges.append((date_slash(start + timedelta(days=start_offset)), date_slash(start + timedelta(days=end_offset))))
    return ranges


def reference_for(task: str) -> str:
    task_lower = task.lower()
    checks = [
        (("bedrock", "claude"), "AWS Bedrock Documentation"),
        (("dynamodb",), "AWS DynamoDB Documentation"),
        (("api gateway",), "AWS API Gateway Documentation"),
        (("lambda",), "AWS Lambda Documentation"),
        (("s3", "bucket", "cv"), "AWS S3 Documentation"),
        (("iam", "mfa", "policy", "permission"), "AWS IAM Documentation"),
        (("ec2", "elastic ip"), "AWS EC2 Documentation"),
        (("vpc", "subnet", "internet gateway", "route table", "network", "networking", "direct connect", "vpn", "privatelink", "transit gateway"), "AWS Networking Documentation"),
        (("cloudwatch", "logs", "metrics", "alarms"), "AWS CloudWatch Documentation"),
        (("sqs", "sns"), "AWS SQS/SNS Documentation"),
        (("cloudfront",), "AWS CloudFront Documentation"),
        (("route 53",), "AWS Route 53 Documentation"),
        (("ecs", "fargate", "container"), "AWS ECS Documentation"),
        (("alb", "auto scaling"), "AWS Elastic Load Balancing Documentation"),
        (("rds", "mysql", "postgresql"), "AWS RDS Documentation"),
        (("waf", "shield", "guardduty", "cloudtrail", "config", "security"), "AWS Security Documentation"),
        (("cost", "budget", "trusted advisor"), "AWS Cost Management Documentation"),
        (("sagemaker", "rekognition", "comprehend", "ai/ml"), "AWS AI/ML Documentation"),
        (("step functions", "eventbridge", "workflow"), "AWS Serverless Documentation"),
        (("vertex", "workshop", "project", "architecture", "diagram", "demo", "frontend", "backend", "profile", "mvp", "proposal", "họp", "nhóm", "trình bày", "dự án"), "FCAJ Workshop / Vertex IntervAI"),
    ]
    for keywords, reference in checks:
        if any(keyword in task_lower for keyword in keywords):
            return reference
    return "AWS Documentation"


def md_table_vi(week: WeekVi) -> str:
    rows = [
        "| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |",
        "| --- | --- | ------------ | --------------- | -------------- |",
    ]
    for index, (task, (start, end)) in enumerate(zip(week.tasks, split_task_dates(week.start, week.end, len(week.tasks))), 1):
        rows.append(f"| {index} | - {task} | {start} | {end} | {reference_for(task)} |")
    return "\n".join(rows)


def md_table_en(week: WeekVi, tasks: list[str]) -> str:
    rows = [
        "| Day | Task | Start Date | Completion Date | Reference Material |",
        "| --- | --- | ------------ | --------------- | -------------- |",
    ]
    for index, (task, (start, end)) in enumerate(zip(tasks, split_task_dates(week.start, week.end, len(tasks))), 1):
        rows.append(f"| {index} | - {task} | {start} | {end} | {reference_for(task)} |")
    return "\n".join(rows)


def bullets(items: list[str]) -> str:
    return "\n".join(f"* {item}" for item in items)


def render_vi(week: WeekVi) -> str:
    return f"""---
title: "Worklog Tuần {week.week}"
date: {date_iso(week.start)}
weight: {week.week}
chapter: false
pre: " <b> 1.{week.week}. </b> "
---

### Mục tiêu tuần {week.week}:

{bullets(VI_OBJECTIVES[week.week])}

### Các công việc cần triển khai trong tuần này:
{md_table_vi(week)}

### Kết quả đạt được tuần {week.week}:

{bullets(week.achievements)}
"""


def render_en(week: WeekVi) -> str:
    data = EN_DATA[week.week]
    return f"""---
title: "Week {week.week} Worklog"
date: {date_iso(week.start)}
weight: {week.week}
chapter: false
pre: " <b> 1.{week.week}. </b> "
---

### Week {week.week} Objectives:

{bullets(data["objectives"])}

### Tasks to be carried out this week:
{md_table_en(week, data["tasks"])}

### Week {week.week} Achievements:

{bullets(data["achievements"])}
"""


def render_overview_en(weeks: dict[int, WeekVi]) -> str:
    lines = [
        "---",
        'title: "Work Log"',
        f"date: {date_iso(weeks[1].start)}",
        "weight: 1",
        "chapter: false",
        'pre: " <b> 1. </b> "',
        "---",
        "",
        f"This page summarizes the **12-week** internship work log at AWS Vietnam ({date_slash(weeks[1].start)} - {date_slash(weeks[12].end)}), focusing on AWS learning and the **Vertex IntervAI** Workshop project.",
        "",
    ]
    for week in range(1, 13):
        lines.append(f"**Week {week}:** [{EN_DATA[week]['summary']}](1.{week}-Week{week}/)")
        lines.append("")
    return "\n".join(lines)


VI_SUMMARIES = {
    1: "Làm quen AWS, tạo tài khoản, Console/CLI và quản lý chi phí",
    2: "VPC, EC2, networking cơ bản và hồ sơ LinkedIn",
    3: "Amazon S3 nâng cao, IAM Policy, Lambda và S3 Event",
    4: "DynamoDB, API Gateway, Bedrock và khởi tạo Vertex IntervAI",
    5: "IAM, S3, EC2, VPC, RDS, DynamoDB và CloudWatch cơ bản",
    6: "Lambda, API Gateway, SQS/SNS, CloudFront và Route 53",
    7: "ECS, ALB, RDS, CloudWatch, Security và Well-Architected",
    8: "Tiếp tục ECS, ALB, RDS, CloudWatch, Security và Well-Architected",
    9: "Networking, Security nâng cao và tối ưu chi phí",
    10: "AWS AI/ML, Step Functions, EventBridge và kiến trúc dự án",
    11: "Backend Vertex IntervAI, Bedrock, API Gateway và frontend",
    12: "Tối ưu MVP Vertex IntervAI, kiểm thử, tài liệu demo và tổng kết",
}


def render_overview_vi(weeks: dict[int, WeekVi]) -> str:
    lines = [
        "---",
        'title: "Nhật ký công việc"',
        f"date: {date_iso(weeks[1].start)}",
        "weight: 1",
        "chapter: false",
        'pre: " <b> 1. </b> "',
        "---",
        "",
        f"**Trong trang này** ghi lại nhật ký công việc thực tập tại AWS Vietnam trong **12 tuần** ({date_slash(weeks[1].start)} - {date_slash(weeks[12].end)}), tập trung vào học AWS và phát triển dự án Workshop **Vertex IntervAI**.",
        "",
    ]
    for week in range(1, 13):
        lines.append(f"**Tuần {week}:** [{VI_SUMMARIES[week]}](1.{week}-Week{week}/)")
        lines.append("")
    return "\n".join(lines)


def write_text(path: Path, text: str) -> bool:
    old = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else None
    if old == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def update_worklog(root: Path, source_docx: Path, dry_run: bool = False) -> list[Path]:
    weeks = parse_docx(source_docx)
    worklog = root / "content" / "1-Worklog"
    changes: list[tuple[Path, str]] = []

    changes.append((worklog / "_index.vi.md", render_overview_vi(weeks)))
    changes.append((worklog / "_index.md", render_overview_en(weeks)))
    for week in range(1, 13):
        week_dir = worklog / f"1.{week}-Week{week}"
        changes.append((week_dir / "_index.vi.md", render_vi(weeks[week])))
        changes.append((week_dir / "_index.md", render_en(weeks[week])))

    changed_paths: list[Path] = []
    for path, text in changes:
        if dry_run:
            old = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else None
            if old != text:
                changed_paths.append(path)
        elif write_text(path, text):
            changed_paths.append(path)

    return changed_paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(r"C:\Users\admin\Downloads\FCAJ-workshop-trungthanh"))
    parser.add_argument("--docx", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--backup-to", type=Path, default=None)
    args = parser.parse_args()

    root = args.root
    docx_path = args.docx or next(root.glob("*.docx"))

    if args.backup_to and not args.dry_run:
        backup_target = args.backup_to / "1-Worklog"
        if backup_target.exists():
            shutil.rmtree(backup_target)
        shutil.copytree(root / "content" / "1-Worklog", backup_target)

    changed = update_worklog(root, docx_path, dry_run=args.dry_run)
    mode = "Would update" if args.dry_run else "Updated"
    print(f"{mode} {len(changed)} files")
    for path in changed:
        print(path)


if __name__ == "__main__":
    main()
