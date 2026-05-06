---
name: Amazon Rekognition
description: Amazon Rekognition is a cloud-based computer vision service that makes it easy to add image and video analysis to your applications, providing capabilities such as object and scene detection, facial analysis, face comparison, celebrity recognition, text detection, content moderation, custom labels, face liveness detection, and streaming video analysis using deep learning technology.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-rekognition/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.18'
x-type: company
apis:
  - name: Amazon Rekognition
    description: Amazon Rekognition provides image and video analysis APIs for label detection, facial analysis, face comparison, celebrity recognition, text detection, content moderation, custom labels, face liveness detection, and streaming video analysis.
    humanURL: https://aws.amazon.com/rekognition/
    baseURL: https://rekognition.amazonaws.com
    tags:
      - Computer Vision
      - Image Analysis
      - Video Analysis
      - Facial Recognition
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html
      - type: OpenAPI
        url: openapi/amazon-rekognition-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/rekognition/latest/APIReference/Welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html
      - type: Authentication
        url: https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_service-with-iam.html
      - type: Pricing
        url: https://aws.amazon.com/rekognition/pricing/
      - type: FAQ
        url: https://aws.amazon.com/rekognition/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/rekognition/
  - type: Documentation
    url: https://docs.aws.amazon.com/rekognition/
  - type: Console
    url: https://console.aws.amazon.com/rekognition/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Pricing
    url: https://aws.amazon.com/rekognition/pricing/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/rekognition/faqs/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-rekognition
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: SpectralRules
    url: rules/amazon-rekognition-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-rekognition-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/rekognition.yaml
  - type: NaftikoCapability
    url: capabilities/computer-vision-workflows.yaml
  - type: Features
    data:
      - name: Object and Scene Detection
        description: Detect thousands of objects, scenes, and concepts in images and videos with high confidence scores using deep learning.
      - name: Facial Analysis
        description: Detect and analyze faces with attributes including age range, emotions, gender, and facial landmarks.
      - name: Face Comparison
        description: Compare faces across images to determine if they are the same person with a similarity score.
      - name: Face Collections
        description: Create searchable face collections to index and search millions of faces in near real-time.
      - name: Celebrity Recognition
        description: Identify thousands of celebrities in images and videos across categories like sports, entertainment, and politics.
      - name: Text Detection
        description: Detect and extract printed and handwritten text from images and videos in multiple languages.
      - name: Content Moderation
        description: Detect explicit, inappropriate, or violent content in images and videos for automated content moderation.
      - name: Custom Labels
        description: Build and train custom image classifiers using your own labeled images for domain-specific object detection.
      - name: Protective Equipment Detection
        description: Detect personal protective equipment such as face covers, hand covers, and head covers on persons in images.
      - name: Face Liveness Detection
        description: Verify that a user is physically present during identity verification to prevent spoofing attacks.
      - name: People Pathing
        description: Track and follow identified people across frames in stored video footage.
      - name: Video Segmentation
        description: Identify technical cues and segments such as black frames, end credits, and color bars in video content.
      - name: Streaming Video Analysis
        description: Analyze live streaming video in real-time using Amazon Kinesis Video Streams integration.
      - name: Image Properties Analysis
        description: Evaluate image quality attributes including sharpness, brightness, contrast, and dominant colors.
  - type: UseCases
    data:
      - name: Identity Verification
        description: Verify user identities by comparing selfies to ID documents or previously stored face images for onboarding and authentication.
      - name: Content Moderation
        description: Automatically moderate user-generated content on platforms to detect and filter explicit or inappropriate imagery.
      - name: Searchable Media Libraries
        description: Build searchable image and video archives by automatically tagging media with detected labels, faces, and text.
      - name: Workplace Safety Compliance
        description: Monitor camera feeds to detect whether workers are wearing required personal protective equipment in industrial settings.
      - name: Fraud Prevention
        description: Prevent identity fraud during digital onboarding by using face liveness detection to confirm real users.
      - name: Smart Retail Analytics
        description: Analyze in-store camera feeds to track customer behavior, measure foot traffic, and optimize product placement.
      - name: Public Safety and Security
        description: Search video archives for persons of interest by comparing faces against a known collection.
      - name: Media and Entertainment
        description: Automatically tag celebrities in photos and videos for media companies to improve content discoverability.
      - name: Custom Object Detection
        description: Train custom classifiers to detect proprietary products, logos, brand assets, or industry-specific objects.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Process images and videos stored in Amazon S3 buckets directly without downloading content.
      - name: Amazon Kinesis Video Streams
        description: Analyze live video streams in real-time by integrating with Kinesis Video Streams for streaming analysis.
      - name: AWS Lambda
        description: Trigger serverless analysis pipelines by invoking Rekognition from Lambda functions in event-driven architectures.
      - name: Amazon SNS
        description: Receive asynchronous notifications when stored video analysis jobs complete via Amazon SNS.
      - name: AWS IAM
        description: Control access to Rekognition APIs using AWS Identity and Access Management policies and roles.
      - name: Amazon CloudWatch
        description: Monitor Rekognition API usage, latency, and error metrics through CloudWatch dashboards and alarms.
      - name: AWS Step Functions
        description: Orchestrate multi-step computer vision workflows using Step Functions to chain Rekognition operations.
      - name: Amazon Augmented AI (A2I)
        description: Route low-confidence Rekognition predictions to human reviewers using Amazon Augmented AI for quality control.
  - type: JSON-LD
    url: json-ld/amazon-rekognition-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-rekognition-bounding-box-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-compare-faces-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-compare-faces-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-create-collection-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-create-collection-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-create-face-liveness-session-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-create-face-liveness-session-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-custom-labels-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-custom-labels-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-faces-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-faces-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-labels-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-labels-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-moderation-labels-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-moderation-labels-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detect-text-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-detectlabelsresponse-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-face-detail-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-get-face-liveness-session-results-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-get-face-liveness-session-results-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-get-label-detection-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-get-video-job-result-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-image-only-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-image-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-index-faces-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-index-faces-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-label-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-list-collections-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-notification-channel-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-recognize-celebrities-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-s3-object-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-search-faces-by-image-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-search-faces-by-image-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-start-label-detection-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-start-video-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-rekognition-video-schema.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-bounding-box-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-compare-faces-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-compare-faces-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-create-collection-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-create-collection-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-create-face-liveness-session-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-create-face-liveness-session-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-custom-labels-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-custom-labels-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-faces-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-faces-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-labels-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-labels-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-moderation-labels-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-moderation-labels-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detect-text-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-detectlabelsresponse-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-face-detail-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-get-face-liveness-session-results-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-get-face-liveness-session-results-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-get-label-detection-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-get-video-job-result-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-image-only-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-image-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-index-faces-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-index-faces-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-label-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-list-collections-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-notification-channel-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-recognize-celebrities-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-s3-object-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-search-faces-by-image-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-search-faces-by-image-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-start-label-detection-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-start-video-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-rekognition-video-structure.json
  - type: Example
    url: examples/amazon-rekognition-bounding-box-example.json
  - type: Example
    url: examples/amazon-rekognition-compare-faces-request-example.json
  - type: Example
    url: examples/amazon-rekognition-compare-faces-response-example.json
  - type: Example
    url: examples/amazon-rekognition-create-collection-request-example.json
  - type: Example
    url: examples/amazon-rekognition-create-collection-response-example.json
  - type: Example
    url: examples/amazon-rekognition-create-face-liveness-session-request-example.json
  - type: Example
    url: examples/amazon-rekognition-create-face-liveness-session-response-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-custom-labels-request-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-custom-labels-response-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-faces-request-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-faces-response-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-labels-request-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-labels-response-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-moderation-labels-request-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-moderation-labels-response-example.json
  - type: Example
    url: examples/amazon-rekognition-detect-text-response-example.json
  - type: Example
    url: examples/amazon-rekognition-detectlabelsresponse-example.json
  - type: Example
    url: examples/amazon-rekognition-face-detail-example.json
  - type: Example
    url: examples/amazon-rekognition-get-face-liveness-session-results-request-example.json
  - type: Example
    url: examples/amazon-rekognition-get-face-liveness-session-results-response-example.json
  - type: Example
    url: examples/amazon-rekognition-get-label-detection-response-example.json
  - type: Example
    url: examples/amazon-rekognition-get-video-job-result-request-example.json
  - type: Example
    url: examples/amazon-rekognition-image-example.json
  - type: Example
    url: examples/amazon-rekognition-image-only-request-example.json
  - type: Example
    url: examples/amazon-rekognition-index-faces-request-example.json
  - type: Example
    url: examples/amazon-rekognition-index-faces-response-example.json
  - type: Example
    url: examples/amazon-rekognition-label-example.json
  - type: Example
    url: examples/amazon-rekognition-list-collections-response-example.json
  - type: Example
    url: examples/amazon-rekognition-notification-channel-example.json
  - type: Example
    url: examples/amazon-rekognition-recognize-celebrities-response-example.json
  - type: Example
    url: examples/amazon-rekognition-s3-object-example.json
  - type: Example
    url: examples/amazon-rekognition-search-faces-by-image-request-example.json
  - type: Example
    url: examples/amazon-rekognition-search-faces-by-image-response-example.json
  - type: Example
    url: examples/amazon-rekognition-start-label-detection-request-example.json
  - type: Example
    url: examples/amazon-rekognition-start-video-job-response-example.json
  - type: Example
    url: examples/amazon-rekognition-video-example.json
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
tags:
  - AWS
  - Celebrity Recognition
  - Computer Vision
  - Content Moderation
  - Custom Labels
  - Deep Learning
  - Face Liveness
  - Facial Recognition
  - Image Analysis
  - Machine Learning
  - Object Detection
  - Text Detection
  - Video Analysis
---
