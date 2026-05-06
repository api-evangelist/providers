---
aid: amazon-fraud-detector
name: Amazon Fraud Detector
description: Amazon Fraud Detector is a fully managed service that uses machine learning to identify potentially fraudulent activities and accurately distinguish between legitimate and high-risk transactions. It uses your data and the same technology that Amazon uses to protect its own business from fraud.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Financial Services
  - Fraud Detection
  - Machine Learning
  - Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-fraud-detector:amazon-fraud-detector-api
    name: Amazon Fraud Detector API
    description: The Amazon Fraud Detector API provides programmatic access to create and manage detectors, models, event types, entities, labels, outcomes, rules, and variables for automated fraud detection workflows.
    humanURL: https://aws.amazon.com/fraud-detector/
    baseURL: https://frauddetector.amazonaws.com
    tags:
      - Fraud Detection
      - Machine Learning
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/frauddetector/latest/ug/what-is-frauddetector.html
      - type: OpenAPI
        url: openapi/amazon-fraud-detector-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-fraud-detector-detector-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fraud-detector-model-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fraud-detector-rule-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fraud-detector-event-type-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fraud-detector-tag-schema.json
      - type: JSONStructure
        url: json-structure/amazon-fraud-detector-detector-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fraud-detector-model-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fraud-detector-rule-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fraud-detector-event-type-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fraud-detector-tag-structure.json
      - type: Example
        url: examples/amazon-fraud-detector-detector-example.json
      - type: Example
        url: examples/amazon-fraud-detector-model-example.json
      - type: Example
        url: examples/amazon-fraud-detector-rule-example.json
      - type: Example
        url: examples/amazon-fraud-detector-event-type-example.json
      - type: Example
        url: examples/amazon-fraud-detector-tag-example.json
      - type: GettingStarted
        url: https://aws.amazon.com/fraud-detector/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/fraud-detector/pricing/
      - type: FAQ
        url: https://aws.amazon.com/fraud-detector/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/frauddetector/latest/api/Welcome.html
common:
  - type: Portal
    url: https://aws.amazon.com/fraud-detector/
  - type: Website
    url: https://aws.amazon.com/fraud-detector/
  - type: Documentation
    url: https://docs.aws.amazon.com/frauddetector/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/frauddetector/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-fraud-detector
  - type: SpectralRules
    url: rules/amazon-fraud-detector-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/fraud-detector.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-fraud-detector-real-time-detection.yaml
  - type: Vocabulary
    url: vocabulary/amazon-fraud-detector-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-fraud-detector-context.jsonld
  - type: Features
    data:
      - name: No ML Expertise Required
        description: Automatically trains and deploys ML models using your historical transaction data without requiring ML expertise.
      - name: Real-Time Fraud Scoring
        description: Returns fraud scores within milliseconds for integration into transaction approval flows.
      - name: Pre-Built Models
        description: Online Fraud Insights (OFI), Transaction Fraud Insights (TFI), and Account Takeover Insights (ATI) pre-trained model types.
      - name: Rule Engine
        description: DETECTORPL rule language allows writing conditional logic using model scores and event variables.
      - name: Model Explainability
        description: Variable importance scores explain which factors most influenced a fraud prediction.
      - name: Cold Start Protection
        description: Uses Amazon fraud experience to provide immediate predictions even with limited historical data.
      - name: Event Ingestion
        description: Ingest historical labeled events to continuously improve model accuracy over time.
  - type: UseCases
    data:
      - name: Payment Fraud Detection
        description: Score credit card and payment transactions in real-time to block fraudulent purchases.
      - name: Account Takeover Prevention
        description: Detect unauthorized login attempts and account compromise using behavioral signals.
      - name: New Account Fraud
        description: Identify fraudulent new account registrations at signup to prevent synthetic identity fraud.
      - name: Promotion Abuse Detection
        description: Flag users abusing discount codes, referral bonuses, and promotional offers.
      - name: Chargeback Prevention
        description: Reduce chargeback rates by blocking high-risk transactions before they complete.
      - name: Insurance Claims Fraud
        description: Score insurance claims for fraudulent patterns in real-time during claim submission.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store training datasets and export labeled event data to S3 for model training.
      - name: AWS IAM
        description: Control access to detectors, models, and predictions using IAM roles and policies.
      - name: Amazon SageMaker
        description: Combine Fraud Detector with SageMaker for custom ML pipelines and model integration.
      - name: Amazon CloudWatch
        description: Monitor prediction volumes, model performance, and API error rates.
      - name: AWS KMS
        description: Encrypt training data and model artifacts with customer-managed KMS keys.
      - name: Amazon EventBridge
        description: Route fraud detection outcomes to downstream systems for automated response workflows.
      - name: Amazon SNS
        description: Send real-time fraud alert notifications to operations teams via SNS topics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
