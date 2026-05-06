---
aid: amazon-swf
name: Amazon Simple Workflow Service
description: Amazon Simple Workflow Service (Amazon SWF) helps developers build, run, and scale background jobs that have parallel or sequential steps. It is a fully managed state tracker and task coordinator in the cloud that manages intertask dependencies, scheduling, and concurrency for application workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - AWS
  - Task Coordination
  - Workflow
url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-swf:amazon-swf-api
    name: Amazon Simple Workflow Service API
    description: The Amazon SWF API provides programmatic access to manage workflows, activity tasks, decision tasks, and workflow execution history. It enables developers to coordinate distributed application components using asynchronous task processing and state tracking.
    humanURL: https://aws.amazon.com/swf/
    baseURL: https://swf.amazonaws.com
    tags:
      - AWS
      - Task Coordination
      - Workflow
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/amazonswf/latest/apireference/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-intro-to-swf.html
      - type: Pricing
        url: https://aws.amazon.com/swf/pricing/
      - type: FAQ
        url: https://aws.amazon.com/swf/faqs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/openapi/amazon-swf-openapi-original.yml
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/swf/
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/
  - type: Console
    url: https://console.aws.amazon.com/swf/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Features
    data:
      - name: Task Coordination
        description: Manages inter-task dependencies, scheduling, and concurrency for distributed workflows.
      - name: State Tracking
        description: Durably maintains application execution state throughout workflow lifecycle.
      - name: Long-Running Workflows
        description: Supports workflows that run for up to 1 year with activity timeouts and retries.
      - name: Decider and Activity Workers
        description: Separates orchestration logic (deciders) from execution logic (activity workers).
      - name: Workflow Versioning
        description: Supports multiple versions of workflow and activity types for safe deployments.
  - type: UseCases
    data:
      - name: Media Processing Pipelines
        description: Coordinate multi-step media encoding, transcoding, and publishing workflows.
      - name: Order Processing
        description: Orchestrate e-commerce order fulfillment with parallel and sequential steps.
      - name: Data Analytics Workflows
        description: Manage ETL pipelines and data processing jobs across distributed systems.
      - name: Human Task Orchestration
        description: Coordinate workflows that require human review or approval steps.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/rules/amazon-swf-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/vocabulary/amazon-swf-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/amazon-swf/refs/heads/main/capabilities/amazon-swf-workflow-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
