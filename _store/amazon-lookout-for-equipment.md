---
aid: amazon-lookout-for-equipment
name: Amazon Lookout for Equipment
description: Amazon Lookout for Equipment uses machine learning to analyze sensor data from your industrial equipment and detect abnormal patterns that signal potential failures. It helps you avoid unplanned equipment downtime by identifying potential equipment failures before they occur.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Equipment Monitoring
  - Industrial IoT
  - Machine Learning
  - Predictive Maintenance
url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-equipment/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-lookout-for-equipment:amazon-lookout-for-equipment-api
    name: Amazon Lookout for Equipment API
    description: The Amazon Lookout for Equipment API provides programmatic access to create and manage datasets, models, inference schedulers, and labels for predictive maintenance of industrial equipment.
    humanURL: https://aws.amazon.com/lookout-for-equipment/
    baseURL: https://lookoutequipment.amazonaws.com
    tags:
      - Industrial IoT
      - Machine Learning
      - Predictive Maintenance
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_Reference.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/lookoutequipment/2020-12-15/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/lookout-for-equipment/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/lookout-for-equipment/pricing/
      - type: FAQ
        url: https://aws.amazon.com/lookout-for-equipment/faqs/
      - type: JSONSchema
        url: json-schema/amazon-lookout-for-equipment-dataset-schema.json
      - type: JSONSchema
        url: json-schema/amazon-lookout-for-equipment-model-schema.json
      - type: JSONLD
        url: json-ld/amazon-lookout-for-equipment-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/lookout-for-equipment/
  - type: Portal
    url: https://aws.amazon.com/lookout-for-equipment/
  - type: Documentation
    url: https://docs.aws.amazon.com/lookout-for-equipment/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/tag/amazon-lookout-for-equipment/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/lookoutequipment/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Features
    data:
      - name: Anomaly Detection
        description: Detect abnormal equipment behavior using ML models trained on equipment sensor data.
      - name: Predictive Maintenance
        description: Predict equipment failures before they occur to reduce unplanned downtime.
      - name: No ML Expertise Required
        description: Automatically build ML models from historical sensor data without data science expertise.
      - name: Multi-Sensor Support
        description: Analyze data from hundreds of sensors simultaneously to detect complex failure patterns.
      - name: Real-Time Inference
        description: Run continuous inference on streaming sensor data for real-time failure detection.
  - type: UseCases
    data:
      - name: Manufacturing Predictive Maintenance
        description: Detect early warning signs of equipment failures in manufacturing machinery.
      - name: Energy Sector Monitoring
        description: Monitor industrial equipment in power plants, wind turbines, and oil refineries.
      - name: Mining Equipment Health
        description: Track the health of heavy mining equipment to prevent costly breakdowns.
      - name: HVAC System Monitoring
        description: Detect anomalies in HVAC systems to prevent equipment failures in buildings.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store and access equipment sensor data in S3 for model training and inference.
      - name: AWS IoT SiteWise
        description: Collect and organize equipment sensor data with IoT SiteWise and analyze with Lookout.
      - name: Amazon Kinesis Data Streams
        description: Stream real-time sensor data from equipment to Lookout for Equipment.
      - name: AWS IoT Core
        description: Connect industrial equipment to AWS via IoT Core for data ingestion.
  - type: SpectralRules
    url: rules/amazon-lookout-for-equipment-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-lookout-for-equipment-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-lookout-for-equipment-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
