---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Scalable virtual servers in the cloud.
  name: Amazon EC2
  slug: amazon-ec2
- description: Scalable object storage service for data backup, archival, and analytics.
  name: Amazon S3
  slug: amazon-s3
- description: Run code without thinking about servers or clusters.
  name: Amazon Lambda
  slug: amazon-lambda
- description: Fast and flexible NoSQL database service for any scale.
  name: Amazon DynamoDB
  slug: amazon-dynamodb
- description: Managed relational database service for MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB.
  name: Amazon RDS
  slug: amazon-rds
artifact_total: 54
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amazon-web-services
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/pricing/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://aws.amazon.com/new/
- group: agent
  title: ''
  type: MCPServer
  url: https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/
created: '2024-01-01'
description: Amazon Web Services is a comprehensive collection of cloud computing services and APIs provided by Amazon, offering infrastructure as a service, platform as a service, and software as a service solutions globally.
features:
- 'Amazon Web Services (AWS): hundreds of services across Cloud Infrastructure'
- 'Detailed pricing: see https://aws.amazon.com/pricing/'
- 'Service: EC2 (compute)'
- 'Service: S3 (object storage)'
- 'Service: EBS (block storage)'
- 'Service: RDS (managed SQL)'
- 'Service: DynamoDB (NoSQL)'
- 'Service: Lambda (serverless)'
- 'Service: API Gateway'
- 'Service: CloudFront (CDN)'
- 'Service: Route 53 (DNS)'
- 'Service: VPC (networking)'
- 'Service: IAM (identity)'
- 'Service: KMS (encryption)'
- 'Service: Secrets Manager'
- 'Service: CloudWatch (monitoring)'
- 'Service: EKS (Kubernetes)'
- 'Service: ECS (containers)'
- 'Service: ECR (container registry)'
- 'Service: SQS (queue)'
- 'Service: SNS (pub-sub)'
- 'Service: SES (email)'
- 'Service: Bedrock (AI/ML)'
- 'Service: SageMaker (ML)'
- 'Service: Comprehend (NLP)'
- 'Service: Rekognition (vision)'
- 'Service: Polly (TTS)'
- 'Service: Transcribe (STT)'
- 'Service: Translate'
- 'Service: Athena (SQL on S3)'
- 'Service: Redshift (data warehouse)'
- 'Service: Glue (ETL)'
- 'Service: EMR (Hadoop)'
- 'Service: Kinesis (streaming)'
- 'Service: MSK (managed Kafka)'
- 'Service: OpenSearch'
- 'Service: QuickSight (BI)'
finops:
- name: Aws Finops
  service_category: Cloud Infrastructure
  slug: aws-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Amazon Web Services (AWS)
nav: Providers
network: true
overview: 'Amazon Web Services (AWS) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Amazon EC2, Amazon S3, Amazon Lambda, and 2 more. Tagged areas include Cloud Computing, IaaS, Infrastructure, PaaS, and Platform as a Service.


  Amazon Web Services (AWS)''s developer surface includes developer portal, documentation, authentication, engineering blog, support, pricing, developer console, and 11 more developer resources.'
plans:
- name: Aws Plans Pricing
  plan_count: 3
  slug: aws-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 2
  name: Aws Rate Limits
  slug: aws-rate-limits
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 32.3
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 50.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws/refs/heads/main/screenshots/aws-2026-06-20T172738.png
security:
- kind: domain-security
  name: Aws Domain Security
  slug: aws-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Vulnerability Disclosure
  slug: aws-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Trust Center
  slug: aws-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws
tags:
- Cloud Computing
- IaaS
- Infrastructure
- PaaS
- Platform as a Service
- Serverless
use_cases:
- description: Host scalable web applications with EC2, S3, CloudFront, and RDS.
  name: Web Application Hosting
- description: Process and analyze large datasets using EMR, Redshift, Athena, and Glue.
  name: Data Analytics
- description: Build and deploy ML models at scale using SageMaker, Rekognition, and Comprehend.
  name: Machine Learning
- description: Implement multi-region disaster recovery strategies with minimal RPO and RTO.
  name: Disaster Recovery
- description: Collect, process, and analyze IoT device data with AWS IoT Core and related services.
  name: IoT Applications
website: https://aws.amazon.com/
---
