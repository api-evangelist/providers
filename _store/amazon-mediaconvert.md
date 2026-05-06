---
aid: amazon-mediaconvert
name: Amazon MediaConvert
description: AWS Elemental MediaConvert is a file-based video transcoding service that allows you to easily create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale. It supports broadcast-grade features including graphic overlays, content protection, multi-language audio, closed captioning, and a comprehensive range of video formats.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediaconvert/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mediaconvert:mediaconvert-api
    name: Amazon MediaConvert API
    description: AWS Elemental MediaConvert is a file-based video transcoding service that allows you to easily create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale. It supports broadcast-grade features including graphic overlays, content protection, multi-language audio, closed captioning, and a comprehensive range of video formats.
    humanURL: https://aws.amazon.com/mediaconvert/
    baseURL: http://mediaconvert.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/mediaconvert/
      - type: OpenAPI
        url: openapi/amazon-mediaconvert-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/mediaconvert/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/mediaconvert/pricing/
      - type: FAQ
        url: https://aws.amazon.com/mediaconvert/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/mediaconvert/
  - type: Documentation
    url: https://docs.aws.amazon.com/mediaconvert/
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
    url: https://console.aws.amazon.com/mediaconvert/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-mediaconvert-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mediaconvert-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-mediaconvert-media-workflow.yaml
  - type: Features
    data:
      - name: Broadcast-Grade Video Processing
        description: Graphic overlays, content protection, multi-language audio, closed captioning, and professional broadcast formats.
      - name: Comprehensive Format Support
        description: Supports AVC, HEVC, AV1, Apple ProRes, MPEG-2, CMAF, HLS, DASH ISO, Smooth Streaming, 4K, 8K, and HDR including Dolby Vision.
      - name: Automated Infrastructure Management
        description: Automates workload provisioning, scaling, monitoring, and resource optimization without manual server management.
      - name: Built-in Reliability
        description: Jobs run on redundant infrastructure across multiple Availability Zones with automatic health monitoring and failover.
      - name: Job Templates and Presets
        description: Create reusable job templates and output presets to standardize and accelerate video transcoding workflows.
      - name: Queue Management
        description: Organize and prioritize transcoding jobs using on-demand and reserved queues.
  - type: UseCases
    data:
      - name: VOD Content Production
        description: Transcode video files for video-on-demand delivery at broadcast quality.
      - name: Large Library Transcoding
        description: Process large content libraries for multiscreen delivery at any scale.
      - name: Broadcast Distribution
        description: Create broadcast-format outputs for television and streaming platform distribution.
      - name: Peak Workload Processing
        description: Handle variable transcoding workloads with elastic auto-scaling.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Use S3 for input and output storage of video files.
      - name: AWS Elemental MediaPackage
        description: Package transcoded outputs for adaptive bitrate streaming delivery.
      - name: Amazon CloudWatch
        description: Monitor job metrics and set alerts for transcoding workflows.
      - name: Amazon EventBridge
        description: Trigger downstream workflows based on MediaConvert job state changes.
      - name: AWS IAM
        description: Control access to MediaConvert resources and S3 buckets using IAM roles.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
