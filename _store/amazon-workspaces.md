---
aid: amazon-workspaces
name: Amazon WorkSpaces
description: Amazon WorkSpaces is a managed, secure Desktop-as-a-Service (DaaS) solution that enables you to provision cloud-based virtual desktops for your users. It eliminates the need to procure and deploy hardware or install complex software, providing persistent desktops accessible from various devices with built-in security and management capabilities. The API provides 65 operations for workspace lifecycle management, bundle and directory management, image management, and IP access control groups.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/amazon-workspaces/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
type: Index
tags:
  - AWS
  - Desktop
  - End User Computing
  - Virtual Desktop
  - Desktop as a Service
apis:
  - aid: amazon-workspaces:amazon-workspaces-api
    name: Amazon WorkSpaces API
    description: The Amazon WorkSpaces API provides programmatic access to manage cloud-based virtual desktops. It enables developers to create, modify, and terminate WorkSpaces, manage workspace bundles and directories, configure IP access control groups, and automate desktop provisioning and lifecycle management at scale. 65 operations for workspace lifecycle, bundles, directories, images, and access control.
    humanURL: https://aws.amazon.com/workspaces/
    baseURL: https://workspaces.amazonaws.com
    tags:
      - AWS
      - Desktop
      - End User Computing
      - Virtual Desktop
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/workspaces/
      - type: OpenAPI
        url: openapi/amazon-workspaces-openapi-original.yaml
      - type: Pricing
        url: https://aws.amazon.com/workspaces/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/workspaces/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/workspaces/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/workspaces/latest/api/welcome.html
      - type: JSONSchema
        url: json-schema/workspaces-workspace-schema.json
      - type: JSONLD
        url: json-ld/amazon-workspaces-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/workspaces/
  - type: Documentation
    url: https://docs.aws.amazon.com/workspaces/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/workspaces/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-workspaces-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-workspaces-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/virtual-desktop-management.yaml
  - type: Features
    data:
      - name: Persistent Virtual Desktops
        description: Cloud-based Windows or Linux desktops with persistent storage that users can access from any device or location.
      - name: Desktop Bundle Catalog
        description: Configurable compute bundles ranging from Value to Graphics.g4dn to match workload requirements and cost targets.
      - name: Active Directory Integration
        description: Integration with AWS Managed Microsoft AD and AD Connector for user authentication and policy management.
      - name: Application Management
        description: Deploy and manage applications across WorkSpaces using application assignment and streaming capabilities.
      - name: IP Access Control Groups
        description: Restrict workspace access by IP address ranges to enforce network-based access controls.
      - name: Running Mode Flexibility
        description: AlwaysOn mode for power users and AutoStop mode for cost optimization of occasional-use desktops.
      - name: BYOD Support
        description: Thin client, web browser, iOS, Android, Linux, macOS, and Windows client access for bring-your-own-device scenarios.
      - name: Workspace Snapshots and Restore
        description: Automated snapshots enable restoring workspaces to previous states for disaster recovery and user error correction.
  - type: UseCases
    data:
      - name: Remote Work Enablement
        description: Provide secure cloud desktops to remote and distributed employees without managing physical hardware.
      - name: Contractor and Temporary Worker Access
        description: Quickly provision and terminate secure desktops for contractors with time-limited access needs.
      - name: Desktop Refresh and Modernization
        description: Replace aging desktop hardware with cloud-based virtual desktops to reduce capital expenditure.
      - name: BYOD Security
        description: Enable personal device usage while keeping corporate data and applications in the secure cloud environment.
      - name: Regulated Industry Compliance
        description: Maintain data residency and security compliance in regulated industries like healthcare and finance.
  - type: Integrations
    data:
      - name: AWS Directory Service
        description: Managed Microsoft AD and AD Connector for user authentication and group policy management.
      - name: AWS IAM
        description: IAM-based access control for WorkSpaces API operations and resource-level permissions.
      - name: Amazon S3
        description: User storage and workspace image storage backed by Amazon S3.
      - name: AWS CloudTrail
        description: Audit logging of all WorkSpaces API calls for compliance and security monitoring.
      - name: Amazon CloudWatch
        description: Metrics and monitoring for workspace performance, connectivity, and health status.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
