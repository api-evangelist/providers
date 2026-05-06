---
aid: amazon-mediastore
name: Amazon MediaStore
description: AWS Elemental MediaStore is an AWS storage service optimized for media, providing the performance, consistency, and low latency required to deliver live streaming video content at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediastore/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mediastore:mediastore-api
    name: Amazon MediaStore API
    description: AWS Elemental MediaStore is an AWS storage service optimized for media, providing the performance, consistency, and low latency required to deliver live streaming video content at scale.
    humanURL: https://aws.amazon.com/mediastore/
    baseURL: http://mediastore.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/mediastore/
      - type: OpenAPI
        url: openapi/amazon-mediastore-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/mediastore/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/mediastore/pricing/
      - type: FAQ
        url: https://aws.amazon.com/mediastore/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/mediastore/
  - type: Documentation
    url: https://docs.aws.amazon.com/mediastore/
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
    url: https://console.aws.amazon.com/mediastore/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-mediastore-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mediastore-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-mediastore-media-workflow.yaml
  - type: Features
    data:
      - name: High-Performance Media Storage
        description: Optimized object storage for live video with consistent low-latency performance.
      - name: Container and Object Management
        description: Organize media assets in containers with fine-grained access control policies.
      - name: CORS Support
        description: Cross-origin resource sharing configuration for browser-based media players.
      - name: Lifecycle Policies
        description: Automatically expire and delete media objects based on age or other criteria.
      - name: Access Logging
        description: Detailed access logs for auditing and monitoring media storage activity.
  - type: UseCases
    data:
      - name: Live Video Origin Storage
        description: Use as a high-performance origin for live video workflows.
      - name: Media Asset Management
        description: Store and manage media files with low-latency access.
      - name: Streaming Video Delivery
        description: Serve HLS and DASH segments with consistent performance for video streaming.
  - type: Integrations
    data:
      - name: AWS Elemental MediaLive
        description: Use MediaStore as an output destination for live encoded streams.
      - name: Amazon CloudFront
        description: Serve MediaStore content via CloudFront for global distribution.
      - name: AWS IAM
        description: Control access to MediaStore containers using IAM policies.
      - name: Amazon CloudWatch
        description: Monitor MediaStore request metrics and latency.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
