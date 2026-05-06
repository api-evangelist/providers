---
aid: amazon-data-lifecycle-manager
name: Amazon Data Lifecycle Manager
description: Amazon Data Lifecycle Manager provides an automated way to manage the lifecycle of your AWS resources. Using lifecycle policies, you can automate the creation, retention, and deletion of Amazon EBS snapshots and EBS-backed AMIs, reducing storage costs and simplifying backup management. Policies target EBS volumes and EC2 instances using tags, execute on configurable schedules, and apply flexible retention rules based on count or age.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Backup
  - EBS Snapshots
  - Lifecycle Management
  - Storage
  - Automation
  - Compliance
url: https://raw.githubusercontent.com/api-evangelist/amazon-data-lifecycle-manager/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-data-lifecycle-manager:amazon-dlm-api
    name: Amazon Data Lifecycle Manager API
    description: The Amazon Data Lifecycle Manager API enables programmatic management of lifecycle policies for automating the creation, retention, and deletion of EBS snapshots and AMIs to meet backup and compliance requirements. Supports EBS snapshot management, AMI lifecycle management, and event-based snapshot policies.
    humanURL: https://aws.amazon.com/ebs/data-lifecycle-manager/
    baseURL: https://dlm.amazonaws.com
    tags:
      - Automation
      - EBS Snapshots
      - Lifecycle Management
      - Backup
      - AMI Management
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/dlm/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-data-lifecycle-manager-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/dlm/2018-01-12/openapi.yaml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html
      - type: APIReference
        url: https://docs.aws.amazon.com/dlm/latest/APIReference/
      - type: JSONSchema
        url: json-schema/lifecycle-policy-schema.json
      - type: JSONSchema
        url: json-schema/policy-details-schema.json
      - type: JSONSchema
        url: json-schema/schedule-schema.json
      - type: JSONLD
        url: json-ld/amazon-data-lifecycle-manager-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/ebs/data-lifecycle-manager/
  - type: DeveloperPortal
    url: https://aws.amazon.com/ebs/data-lifecycle-manager/
  - type: Documentation
    url: https://docs.aws.amazon.com/dlm/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/ec2/v2/home#Lifecycle
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-data-lifecycle-manager-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-data-lifecycle-manager-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/backup-automation-operations.yaml
  - type: NaftikoCapability
    url: capabilities/shared/data-lifecycle-manager.yaml
  - type: Features
    data:
      - name: EBS Snapshot Automation
        description: Automatically create, copy, and delete EBS snapshots on configurable schedules using tag-based targeting of volumes across AWS accounts.
      - name: AMI Lifecycle Management
        description: Automate the creation and deregistration of Amazon Machine Images from EC2 instances on schedules to maintain a library of AMIs.
      - name: Flexible Retention Rules
        description: Retain snapshots by count (keep the last N) or by age (keep for N days/weeks/months/years), automatically deleting older snapshots.
      - name: Tag-Based Targeting
        description: Target EBS volumes or EC2 instances using resource tags for policy scope, enabling granular backup control without managing resource lists.
      - name: Cross-Region Copy
        description: Configure schedules to copy snapshots to other AWS regions for disaster recovery and geographic redundancy automatically.
      - name: Fast Snapshot Restore
        description: Enable fast snapshot restore on snapshots created by DLM policies to dramatically reduce EBS volume initialization time.
      - name: Event-Based Policies
        description: Trigger snapshot sharing and copying workflows in response to CloudWatch Events for cross-account snapshot automation.
  - type: UseCases
    data:
      - name: Automated Daily Backups
        description: Schedule daily EBS volume snapshots with automated retention of the last 7 or 30 days of backups without manual intervention.
      - name: Compliance and Audit Retention
        description: Meet regulatory backup retention requirements by defining long-term retention policies (monthly/yearly) for compliance snapshots.
      - name: Disaster Recovery
        description: Automatically copy EBS snapshots to secondary AWS regions to enable cross-region disaster recovery with minimal RTO and RPO.
      - name: Golden AMI Pipeline
        description: Automate the creation of hardened EC2 AMI images from approved instances and manage their lifecycle for deployment fleets.
      - name: Storage Cost Optimization
        description: Reduce EBS snapshot storage costs by automatically deleting outdated snapshots based on configurable age or count retention rules.
  - type: Integrations
    data:
      - name: Amazon EBS
        description: Native integration with Amazon EBS for snapshot creation, retention, and deletion of volumes across the AWS account.
      - name: Amazon EC2
        description: Target EC2 instances with IMAGE_MANAGEMENT policies to automate AMI creation from running or stopped instances.
      - name: Amazon CloudWatch
        description: Event-based DLM policies are triggered by Amazon CloudWatch Events for cross-account snapshot sharing scenarios.
      - name: AWS Backup
        description: Complementary to DLM, AWS Backup provides centralized backup management across multiple AWS services including EBS, RDS, and DynamoDB.
      - name: AWS IAM
        description: DLM uses IAM execution roles to assume permissions for creating and deleting snapshots on behalf of the lifecycle policy.
      - name: AWS Organizations
        description: Cross-account snapshot sharing policies use AWS Organizations to share EBS snapshots with member accounts automatically.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
