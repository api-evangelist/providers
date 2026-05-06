---
aid: amazon-mediaconnect
name: Amazon MediaConnect
description: AWS Elemental MediaConnect is a high-quality transport service for live video that provides the reliability, security, and visibility customers expect from traditional satellite and fiber services. It enables broadcasters to build live video workflows in the cloud with reliable transport of broadcast-quality content using protocols including Zixi, RIST, SRT, RTP, and RTP with FEC.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Live Video
  - Media
  - Media Transport
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediaconnect/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mediaconnect:aws-elemental-mediaconnect-api
    name: AWS Elemental MediaConnect API
    description: The AWS Elemental MediaConnect API provides programmatic access to create and manage flows, sources, outputs, entitlements, VPC interfaces, bridges, gateways, and media streams for reliable live video transport in the cloud.
    humanURL: https://aws.amazon.com/mediaconnect/
    baseURL: https://mediaconnect.amazonaws.com
    tags:
      - Broadcasting
      - Live Video
      - Media Transport
      - Flows
      - Bridges
      - Gateways
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/mediaconnect/latest/api/welcome.html
      - type: OpenAPI
        url: openapi/amazon-mediaconnect-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/mediaconnect/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/mediaconnect/pricing/
      - type: FAQ
        url: https://aws.amazon.com/mediaconnect/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/mediaconnect/
  - type: Documentation
    url: https://docs.aws.amazon.com/mediaconnect/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/media/tag/aws-elemental-mediaconnect/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/mediaconnect/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-mediaconnect-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mediaconnect-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-mediaconnect-live-video-transport.yaml
  - type: Features
    data:
      - name: Video Transport Protocols
        description: Supports Zixi, RIST, SRT, RTP, and RTP with FEC protocols for reliable live video delivery over IP networks.
      - name: Gateway Capability
        description: Transmit compressed video between on-premises multicast environments and cloud infrastructure via the MediaConnect Gateway.
      - name: Uncompressed Video Support
        description: Handle uncompressed and visually-lossless video through AWS CDI and JPEG XS encoding with low-latency delivery.
      - name: End-to-End Encryption
        description: Built-in AES encryption with AWS Secrets Manager integration for encryption key management.
      - name: Entitlements
        description: Grant partner and customer accounts controlled access to your video streams via entitlements.
      - name: Flow Management
        description: Programmatically create and manage flows, sources, outputs, and VPC interfaces.
      - name: Workflow Monitor
        description: Visualize relationships between resources in live video workflows across connected AWS services.
  - type: UseCases
    data:
      - name: 24/7 TV Channel Operation
        description: Transport continuous broadcast streams reliably for round-the-clock television channels.
      - name: Live Event Streaming
        description: Manage event-based video distribution for sports, concerts, news, and other live events.
      - name: Content Sharing
        description: Share live video feeds with partners and customers through controlled entitlements.
      - name: Disaster Recovery
        description: Provide redundant video pathways for business continuity in broadcast workflows.
  - type: Integrations
    data:
      - name: AWS Elemental MediaLive
        description: Send video flows to MediaLive for transcoding and processing.
      - name: Amazon CloudWatch
        description: Monitor MediaConnect performance metrics and set alarms.
      - name: Amazon EventBridge
        description: Trigger event-driven workflows based on MediaConnect source health changes.
      - name: Amazon CloudFront
        description: Deliver processed video content at scale using CloudFront.
      - name: AWS Secrets Manager
        description: Securely manage encryption keys for content protection.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
