---
aid: amazon-medialive
name: Amazon MediaLive
description: AWS Elemental MediaLive is a broadcast-grade live video processing service that creates high-quality video streams for delivery to broadcast televisions and internet-connected multiscreen devices.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-medialive/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-medialive:medialive-api
    name: Amazon MediaLive API
    description: AWS Elemental MediaLive is a broadcast-grade live video processing service that creates high-quality video streams for delivery to broadcast televisions and internet-connected multiscreen devices.
    humanURL: https://aws.amazon.com/medialive/
    baseURL: http://medialive.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/medialive/
      - type: OpenAPI
        url: openapi/amazon-medialive-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/medialive/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/medialive/pricing/
      - type: FAQ
        url: https://aws.amazon.com/medialive/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/medialive/
  - type: Documentation
    url: https://docs.aws.amazon.com/medialive/
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
    url: https://console.aws.amazon.com/medialive/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-medialive-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-medialive-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-medialive-media-workflow.yaml
  - type: Features
    data:
      - name: Live Video Encoding
        description: Broadcast-grade live video encoding supporting H.264, H.265, and other professional codecs.
      - name: Multiple Input Types
        description: Accept live video from RTP, RTMP, HLS pull, MediaConnect, MP4, and other source types.
      - name: Redundant Encoding
        description: Pipeline redundancy for high-availability live events with automatic failover.
      - name: Dynamic Ad Insertion Markers
        description: Insert SCTE-35 markers for downstream ad replacement in live streams.
      - name: Multiple Output Groups
        description: Deliver to HLS, DASH, RTMP, archive, UDP, MediaPackage, and other output destinations simultaneously.
      - name: Input Switching
        description: Dynamically switch between input sources during a live event without interruption.
  - type: UseCases
    data:
      - name: Live Television Broadcast
        description: Encode and deliver live TV channels with broadcast-grade quality.
      - name: Live Sports Streaming
        description: Handle large-scale live sports events with redundant pipelines.
      - name: Live News Production
        description: Create live news channel workflows with multi-source input switching.
      - name: Virtual Events
        description: Stream virtual conferences, concerts, and entertainment events.
  - type: Integrations
    data:
      - name: AWS Elemental MediaConnect
        description: Receive high-quality video transport feeds from MediaConnect.
      - name: AWS Elemental MediaPackage
        description: Send encoded outputs to MediaPackage for adaptive bitrate packaging.
      - name: Amazon S3
        description: Archive live stream recordings to S3 for storage and later processing.
      - name: Amazon CloudWatch
        description: Monitor channel health metrics and set alerts for live events.
      - name: Amazon EventBridge
        description: Trigger workflows based on channel state change events.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
