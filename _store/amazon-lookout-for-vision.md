---
aid: amazon-lookout-for-vision
name: Amazon Lookout for Vision
description: Amazon Lookout for Vision is a machine learning service that spots defects and anomalies in visual representations using computer vision. With just a small sample of images, it builds a custom computer vision model to enable you to identify damaged products or issues before production issues arise. It supports projects, datasets, model training, and real-time anomaly detection.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Computer Vision
  - Machine Learning
  - Manufacturing
  - Quality Inspection
  - Anomaly Detection
url: https://raw.githubusercontent.com/api-evangelist/amazon-lookout-for-vision/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-lookout-for-vision:amazon-lookout-for-vision-api
    name: Amazon Lookout for Vision API
    description: The Amazon Lookout for Vision API provides programmatic access to create and manage projects, datasets, models, and anomaly detection jobs for visual quality inspection using computer vision. Supports 22 operations covering the full model lifecycle from dataset management through real-time anomaly detection.
    humanURL: https://aws.amazon.com/lookout-for-vision/
    baseURL: https://lookoutvision.amazonaws.com
    tags:
      - Computer Vision
      - Machine Learning
      - Quality Inspection
      - Anomaly Detection
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lookout-for-vision/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-lookout-for-vision-openapi-original.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/lookout-for-vision/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/lookout-for-vision/pricing/
      - type: FAQ
        url: https://aws.amazon.com/lookout-for-vision/faqs/
      - type: JSONSchema
        url: json-schema/amazon-lookout-for-vision-anomaly-class-schema.json
      - type: JSONStructure
        url: json-structure/amazon-lookout-for-vision-anomaly-class-structure.json
      - type: JSON-LD
        url: json-ld/amazon-lookout-for-vision-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/lookout-for-vision/
  - type: Documentation
    url: https://docs.aws.amazon.com/lookout-for-vision/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/tag/amazon-lookout-for-vision/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/lookoutvision/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-lookout-for-vision-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-lookout-for-vision-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/visual-inspection-workflow.yaml
  - type: Features
    data:
      - name: Custom Computer Vision Models
        description: Build custom visual inspection models with just a small sample of images, no ML expertise required.
      - name: Real-Time Defect Detection
        description: Run inference on images in real time to detect defects and anomalies on the production line.
      - name: Edge Deployment
        description: Package and deploy models to edge devices for local inference without cloud connectivity.
      - name: Dataset Management
        description: Manage labeled training and test datasets directly through the API.
      - name: Model Packaging Jobs
        description: Package trained models for deployment to AWS IoT Greengrass edge devices.
  - type: UseCases
    data:
      - name: Manufacturing Quality Control
        description: Automate visual inspection of manufactured products to detect surface defects, assembly errors, and damaged items.
      - name: Electronics Assembly Inspection
        description: Detect solder defects, missing components, and board damage in electronics manufacturing.
      - name: Food and Beverage Quality
        description: Identify contaminated, damaged, or improperly packaged food products on production lines.
      - name: Pharmaceutical Packaging
        description: Verify correct labeling, packaging integrity, and tablet quality in pharmaceutical manufacturing.
      - name: Automotive Parts Inspection
        description: Detect cracks, scratches, and dimensional defects in automotive components.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store training images and dataset manifests in S3 buckets.
      - name: AWS IoT Greengrass
        description: Deploy packaged models to IoT Greengrass edge devices for local inference.
      - name: Amazon CloudWatch
        description: Monitor model performance metrics and detection results in CloudWatch.
      - name: AWS KMS
        description: Encrypt model artifacts using AWS Key Management Service.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
