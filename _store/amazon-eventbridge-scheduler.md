---
name: Amazon EventBridge Scheduler
description: Amazon EventBridge Scheduler is a fully managed, serverless scheduler that enables you to create, run, and manage tasks from one central, managed service. With EventBridge Scheduler, you can create millions of schedules using cron and rate expressions.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/eventbridge/scheduler/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - Cron
  - Event-Driven
  - Scheduling
  - Serverless
apis:
  - name: Amazon EventBridge Scheduler API
    description: API for creating, updating, and managing scheduled tasks using cron expressions, rate expressions, and one-time schedules at scale.
    humanURL: https://aws.amazon.com/eventbridge/scheduler/
    baseURL: https://scheduler.amazonaws.com
    tags:
      - Cron
      - Event-Driven
      - Scheduling
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/scheduler/latest/UserGuide/
      - type: OpenAPI
        url: openapi/amazon-eventbridge-scheduler-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/scheduler/latest/APIReference/
      - type: GettingStarted
        url: https://aws.amazon.com/eventbridge/scheduler/
      - type: Pricing
        url: https://aws.amazon.com/eventbridge/pricing/
      - type: FAQ
        url: https://aws.amazon.com/eventbridge/faqs/
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-scheduler-action-after-completion-schema.json
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-scheduler-assign-public-ip-schema.json
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-scheduler-aws-vpc-configuration-schema.json
      - type: JSONLD
        url: json-ld/amazon-eventbridge-scheduler-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/eventbridge/
  - type: Documentation
    url: https://docs.aws.amazon.com/eventbridge/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/scheduler/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/eventbridge/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/eventbridge
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-eventbridge-scheduler-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-eventbridge-scheduler-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-eventbridge-scheduler-vocabulary.yaml
  - type: Features
    data:
      - name: Cron and Rate Scheduling
        description: Schedule tasks using flexible cron expressions or simple rate expressions
      - name: One-Time Schedules
        description: Create one-time schedules for future tasks with precise timing
      - name: Schedule Groups
        description: Organize schedules into groups for bulk management and operations
      - name: Flexible Time Windows
        description: Allow schedules to run within flexible time windows for load distribution
      - name: Timezone Support
        description: Specify schedules in any timezone for global deployments
  - type: UseCases
    data:
      - name: Batch Job Scheduling
        description: Schedule periodic data processing and ETL batch jobs
      - name: Report Generation
        description: Automatically generate and deliver reports on a schedule
      - name: Resource Cleanup
        description: Schedule automatic cleanup of temporary resources and old data
      - name: Reminder Notifications
        description: Send scheduled notifications and reminders to users
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Invoke Lambda functions on a schedule
      - name: Amazon SQS
        description: Send messages to SQS queues at scheduled intervals
      - name: AWS Step Functions
        description: Start Step Functions state machine executions on a schedule
      - name: Amazon ECS
        description: Run ECS tasks on a scheduled basis
      - name: Amazon EventBridge
        description: Send events to EventBridge event buses on a schedule
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
