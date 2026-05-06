---
aid: amazon-mediatailor
name: Amazon MediaTailor
description: AWS Elemental MediaTailor is a channel assembly and personalized ad-insertion service that enables you to monetize your video content with server-side targeted advertising while maintaining broadcast-quality.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediatailor/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mediatailor:mediatailor-api
    name: Amazon MediaTailor API
    description: AWS Elemental MediaTailor is a channel assembly and personalized ad-insertion service that enables you to monetize your video content with server-side targeted advertising while maintaining broadcast-quality.
    humanURL: https://aws.amazon.com/mediatailor/
    baseURL: http://api.mediatailor.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/mediatailor/
      - type: OpenAPI
        url: openapi/amazon-mediatailor-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/mediatailor/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/mediatailor/pricing/
      - type: FAQ
        url: https://aws.amazon.com/mediatailor/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/mediatailor/
  - type: Documentation
    url: https://docs.aws.amazon.com/mediatailor/
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
    url: https://console.aws.amazon.com/mediatailor/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-mediatailor-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mediatailor-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-mediatailor-media-workflow.yaml
  - type: Features
    data:
      - name: Server-Side Ad Insertion
        description: Seamless ad replacement at the server side for consistent viewer experience across devices.
      - name: Personalized Ad Targeting
        description: Insert targeted ads based on viewer demographics, geography, and behavioral data.
      - name: Channel Assembly
        description: Create linear channels from VOD assets and live streams with automated ad scheduling.
      - name: Ad Decision Server Integration
        description: Connect to any VAST/VPAID-compliant ad decision server for programmatic advertising.
      - name: Playback Configuration
        description: Configure ad insertion parameters, slate, and CDN settings per playback session.
  - type: UseCases
    data:
      - name: VOD Monetization
        description: Insert targeted ads into video-on-demand content for revenue generation.
      - name: Live Stream Advertising
        description: Replace live ad markers with personalized ads during live events.
      - name: FAST Channel Creation
        description: Build free ad-supported streaming TV channels from VOD libraries.
      - name: Addressable Advertising
        description: Deliver personalized ad experiences to individual viewers at scale.
  - type: Integrations
    data:
      - name: AWS Elemental MediaPackage
        description: Ingest packaged live streams for ad insertion.
      - name: Amazon CloudFront
        description: Deliver ad-inserted content via CloudFront with low latency.
      - name: Amazon S3
        description: Store VOD source content and slate media assets in S3.
      - name: Amazon CloudWatch
        description: Monitor ad insertion metrics and playback session data.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
