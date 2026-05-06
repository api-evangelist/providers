---
aid: amazon-mechanical-turk
name: Amazon Mechanical Turk
description: Amazon Mechanical Turk (MTurk) is a crowdsourcing marketplace that makes it easier for individuals and businesses to coordinate the use of human intelligence to perform tasks that computers are currently unable to do well. It enables access to a global, on-demand, 24x7 workforce for data labeling, content moderation, surveys, transcription, and machine learning training data collection.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Crowdsourcing
  - Human Intelligence
  - Labor
  - Machine Learning
  - Tasks
url: https://raw.githubusercontent.com/api-evangelist/amazon-mechanical-turk/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mechanical-turk:amazon-mturk-api
    name: Amazon Mechanical Turk API
    description: The Amazon Mechanical Turk API provides programmatic access to create and manage HITs, qualifications, workers, assignments, and bonuses for coordinating crowdsourced human intelligence tasks. Covers 39 operations for the complete HIT lifecycle from creation through assignment review, worker management, and payment processing.
    humanURL: https://www.mturk.com/
    baseURL: https://mturk-requester.amazonaws.com
    tags:
      - Crowdsourcing
      - Human Intelligence
      - Machine Learning
      - Tasks
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-mechanical-turk-openapi-original.yaml
      - type: GettingStarted
        url: https://www.mturk.com/get-started
      - type: Pricing
        url: https://www.mturk.com/pricing
      - type: FAQ
        url: https://www.mturk.com/faqs
      - type: JSONSchema
        url: json-schema/amazon-mechanical-turk-hit-schema.json
      - type: JSONStructure
        url: json-structure/amazon-mechanical-turk-hit-structure.json
      - type: JSON-LD
        url: json-ld/amazon-mechanical-turk-context.jsonld
common:
  - type: Portal
    url: https://www.mturk.com/
  - type: Documentation
    url: https://docs.aws.amazon.com/mturk/
  - type: TermsOfService
    url: https://www.mturk.com/participation-agreement
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://www.mturk.com/contact
  - type: Blog
    url: https://blog.mturk.com/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SignUp
    url: https://www.mturk.com/get-started
  - type: Login
    url: https://requester.mturk.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://www.mturk.com/contact
  - type: SpectralRules
    url: rules/amazon-mechanical-turk-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mechanical-turk-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/crowdsourcing-workflow.yaml
  - type: Features
    data:
      - name: Human Intelligence Tasks (HITs)
        description: Create and manage discrete units of work distributed to the global MTurk worker population.
      - name: Qualification Types
        description: Define custom qualification tests and requirements to target the right worker pool for each task type.
      - name: Assignment Review and Approval
        description: Review submitted assignments and approve or reject work with feedback to workers.
      - name: Worker Bonuses
        description: Award bonus payments to workers for exceptional task completion beyond the base HIT reward.
      - name: Worker Notifications
        description: Send targeted messages to specific workers to communicate task updates or instructions.
      - name: Worker Blocks
        description: Prevent specific workers from accessing your HITs when quality does not meet requirements.
      - name: Sandbox Environment
        description: Test HIT templates and requester workflows using the MTurk sandbox before going to production.
  - type: UseCases
    data:
      - name: Machine Learning Data Labeling
        description: Label images, text, audio, and video to create training datasets for machine learning models.
      - name: Content Moderation
        description: Review and moderate user-generated content for inappropriate material at scale.
      - name: Transcription Services
        description: Transcribe audio and video recordings using human workers for high accuracy.
      - name: Survey and Research Data Collection
        description: Conduct surveys and collect research data from a diverse global workforce.
      - name: Data Validation and Quality Assurance
        description: Validate and verify structured data for accuracy using human review.
      - name: Sentiment Analysis Training Data
        description: Generate labeled sentiment data for training NLP and sentiment analysis models.
  - type: Integrations
    data:
      - name: Amazon SageMaker Ground Truth
        description: Use MTurk workers directly within SageMaker Ground Truth for ML data labeling jobs.
      - name: AWS Lambda
        description: Trigger Lambda functions on HIT completion events for automated downstream processing.
      - name: Amazon S3
        description: Store HIT input data and collect worker output files in S3 buckets.
      - name: Amazon CloudWatch
        description: Monitor MTurk task completion rates and worker performance metrics.
      - name: AWS IAM
        description: Control requester access to the MTurk API through IAM policies and roles.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
