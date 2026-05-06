---
aid: amazon-interactive-video-service
name: Amazon Interactive Video Service
description: Amazon Interactive Video Service (Amazon IVS) is a managed live streaming solution designed to provide interactive video experiences. It handles the operational complexity of live streaming so you can focus on building engaging applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Live Streaming
  - Media
  - Video
  - Real-Time
url: https://raw.githubusercontent.com/api-evangelist/amazon-interactive-video-service/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-interactive-video-service:aws-ivs-api
    name: AWS Amazon IVS API
    description: The Amazon IVS API provides programmatic control over channels, stream keys, recordings, and playback keys for building interactive live streaming applications.
    humanURL: https://aws.amazon.com/ivs/
    baseURL: https://ivs.us-east-1.amazonaws.com
    tags:
      - Live Streaming
      - Media
      - Video
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-ivs-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/ivs/pricing/
      - type: FAQ
        url: https://aws.amazon.com/ivs/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/ivs/
  - type: Website
    url: https://aws.amazon.com/ivs/
  - type: Documentation
    url: https://docs.aws.amazon.com/ivs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/media/tag/amazon-interactive-video-service/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/ivs/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-interactive-video-service-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/ivs.yaml
  - type: NaftikoCapability
    url: capabilities/live-streaming-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-interactive-video-service-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-interactive-video-service-context.jsonld
  - type: Features
    data:
      - name: Low Latency Streaming
        description: Deliver live video with sub-second latency for real-time interactivity.
      - name: Managed Infrastructure
        description: AWS handles all the infrastructure complexity of live streaming at scale.
      - name: Recording and Playback
        description: Automatically record live streams to S3 and generate playback URLs.
      - name: Chat Integration
        description: Built-in chat messaging for interactive viewer experiences.
  - type: UseCases
    data:
      - name: Interactive Gaming Streams
        description: Build gaming livestreams with viewer interaction and real-time overlays.
      - name: Virtual Events
        description: Host virtual conferences, concerts, and events with large audiences.
      - name: Social Commerce
        description: Enable live shopping experiences with interactive product displays.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Stores live stream recordings automatically for on-demand playback.
      - name: Amazon CloudFront
        description: Distributes live streams globally with low latency.
      - name: AWS Lambda
        description: Triggers automation based on stream state changes and events.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
