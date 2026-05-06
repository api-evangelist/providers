---
name: Amazon EC2
description: Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud, allowing you to launch virtual server instances, manage networking, and configure storage with complete control over your computing resources.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/ec2/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon EC2 API
    description: Core API for managing Amazon EC2 instances, AMIs, key pairs, security groups, Elastic IPs, launch templates, spot instances, capacity reservations, and other compute resources.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/ec2/
    baseURL: https://ec2.amazonaws.com
    tags:
      - AWS
      - Cloud Computing
      - Compute
      - Instances
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-ec2-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-ec2-instance-schema.json
      - type: JSONLD
        url: json-ld/amazon-ec2-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/ec2/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/ec2/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: StatusPage
        url: https://status.aws.amazon.com/
      - type: BestPractices
        url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html
      - type: FAQ
        url: https://aws.amazon.com/ec2/faqs/
      - type: TermsOfService
        url: https://aws.amazon.com/ec2/sla/
      - type: Documentation
        url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/
      - type: APIReference
        url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
      - type: Documentation
        url: https://docs.aws.amazon.com/cli/latest/reference/ec2/
      - type: Security
        url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html
      - type: JSONStructure
        url: json-structure/amazon-ec2-instance-structure.json
      - type: Example
        url: examples/amazon-ec2-instance-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/ec2/
  - type: Documentation
    url: https://docs.aws.amazon.com/ec2/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/ec2/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-ec2
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Diverse Instance Types
        description: Over 750 instance types optimized for compute, memory, storage, GPU, and inferencing workloads.
      - name: Amazon Machine Images
        description: Pre-configured OS images for Windows, Linux, and macOS with custom and marketplace options.
      - name: Elastic IPs
        description: Static IPv4 addresses that can be quickly remapped to different instances for fault tolerance.
      - name: Security Groups
        description: Virtual firewalls to control inbound and outbound traffic to EC2 instances.
      - name: Spot Instances
        description: Access spare EC2 capacity at up to 90% discount over On-Demand prices for flexible workloads.
      - name: Placement Groups
        description: Control instance placement for low-latency cluster networking or high-availability distribution.
      - name: Launch Templates
        description: Version-controlled configurations for launching EC2 instances with consistent settings.
      - name: Nitro System
        description: Next-generation virtualization infrastructure delivering near bare-metal performance and security.
  - type: UseCases
    data:
      - name: Web Application Hosting
        description: Deploy scalable web applications and APIs with full control over the compute environment.
      - name: Machine Learning Training
        description: GPU-accelerated instances for deep learning model training and inference workloads.
      - name: High-Performance Computing
        description: Cluster networking instances for computational fluid dynamics, genomics, and financial modeling.
      - name: SAP and Enterprise Workloads
        description: Certified instances for SAP HANA, SAP S/4HANA, and other enterprise database applications.
      - name: Development and Testing
        description: Flexible on-demand compute for CI/CD pipelines, dev environments, and test automation.
  - type: Integrations
    data:
      - name: Amazon VPC
        description: Launch EC2 instances in logically isolated virtual networks with full networking control.
      - name: Elastic Load Balancing
        description: Distribute incoming traffic across multiple EC2 instances for high availability.
      - name: Amazon RDS
        description: Connect EC2 instances to managed relational database services within the same VPC.
      - name: AWS Auto Scaling
        description: Automatically scale EC2 fleets based on demand metrics and scheduling policies.
      - name: AWS Systems Manager
        description: Manage, patch, and operate EC2 instances at scale without SSH access.
  - type: SpectralRules
    url: rules/amazon-ec2-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-ec2-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ec2-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Cloud Computing
  - Compute
  - IaaS
  - Infrastructure
  - Virtual Machines
---
