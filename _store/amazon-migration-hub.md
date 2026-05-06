---
aid: amazon-migration-hub
name: Amazon Migration Hub
description: AWS Migration Hub provides a single location to track the progress of application migrations across multiple AWS and partner solutions, giving visibility into migration progress and enabling the use of other AWS migration tools.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-migration-hub/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-migration-hub:migration-hub-api
    name: Amazon Migration Hub API
    description: AWS Migration Hub provides a single location to track the progress of application migrations across multiple AWS and partner solutions, giving visibility into migration progress and enabling the use of other AWS migration tools.
    humanURL: https://aws.amazon.com/migration-hub/
    baseURL: http://mgh.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/migration-hub/
      - type: OpenAPI
        url: openapi/amazon-migration-hub-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/migration-hub/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/migration-hub/pricing/
      - type: FAQ
        url: https://aws.amazon.com/migration-hub/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/migration-hub/
  - type: Documentation
    url: https://docs.aws.amazon.com/migration-hub/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/media/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/migration-hub/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-migration-hub-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-migration-hub-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-migration-hub-media-workflow.yaml
  - type: Features
    data:
      - name: Centralized Migration Tracking
        description: Track migration progress across multiple applications and migration tools from a single console.
      - name: Multi-Tool Integration
        description: Integrate with AWS Database Migration Service, Server Migration Service, and partner tools.
      - name: Application Discovery
        description: Discover on-premises servers and dependencies to plan migrations effectively.
      - name: Migration Status Notifications
        description: Receive real-time updates on task progress and resource migration status.
      - name: Resource Association
        description: Associate discovered resources with migration tasks for tracking.
  - type: UseCases
    data:
      - name: Large-Scale Cloud Migration
        description: Manage complex migrations of hundreds or thousands of servers to AWS.
      - name: Migration Portfolio Management
        description: Track the status of all applications in a migration portfolio.
      - name: Multi-Tool Orchestration
        description: Coordinate migrations using multiple AWS and partner migration tools simultaneously.
      - name: Migration Reporting
        description: Generate progress reports and status updates for stakeholders.
  - type: Integrations
    data:
      - name: AWS Server Migration Service
        description: Track SMS migration job progress in Migration Hub.
      - name: AWS Database Migration Service
        description: Monitor DMS database migration tasks from Migration Hub.
      - name: AWS Application Discovery Service
        description: Import discovery data to identify and plan server migrations.
      - name: AWS CloudFormation
        description: Track CloudFormation stack deployments as migration tasks.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
