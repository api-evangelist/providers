---
aid: amazon-mediapackage
name: Amazon MediaPackage
description: AWS Elemental MediaPackage is a video origination and just-in-time packaging service that reliably prepares and protects video for delivery over the internet, creating multiple output formats from a single video input.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mediapackage/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mediapackage:mediapackage-api
    name: Amazon MediaPackage API
    description: AWS Elemental MediaPackage is a video origination and just-in-time packaging service that reliably prepares and protects video for delivery over the internet, creating multiple output formats from a single video input.
    humanURL: https://aws.amazon.com/mediapackage/
    baseURL: http://mediapackage.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/mediapackage/
      - type: OpenAPI
        url: openapi/amazon-mediapackage-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/mediapackage/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/mediapackage/pricing/
      - type: FAQ
        url: https://aws.amazon.com/mediapackage/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/mediapackage/
  - type: Documentation
    url: https://docs.aws.amazon.com/mediapackage/
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
    url: https://console.aws.amazon.com/mediapackage/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-mediapackage-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mediapackage-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-mediapackage-media-workflow.yaml
  - type: Features
    data:
      - name: Just-in-Time Packaging
        description: Package live video into HLS, DASH, CMAF, and Microsoft Smooth Streaming formats on demand.
      - name: Content Protection
        description: Integrated DRM support with PlayReady, Widevine, FairPlay, and SPEKE standard.
      - name: Time-Shifted Viewing
        description: Enable start-over, catch-up TV, and pause live TV with configurable time windows.
      - name: CDN Integration
        description: Direct integration with CloudFront for scalable content delivery.
      - name: Harvest Jobs
        description: Clip and archive live stream segments to S3 for VOD asset creation.
  - type: UseCases
    data:
      - name: Live OTT Streaming
        description: Package live video for over-the-top delivery to mobile and connected devices.
      - name: Time-Shifted Television
        description: Enable catch-up TV and start-over viewing experiences.
      - name: Multi-DRM Content Protection
        description: Protect premium content with multiple DRM systems simultaneously.
      - name: Live Clipping
        description: Create VOD clips from live streams for highlights and replays.
  - type: Integrations
    data:
      - name: AWS Elemental MediaLive
        description: Receive live encoded streams from MediaLive for packaging.
      - name: Amazon CloudFront
        description: Distribute packaged content globally via CloudFront CDN.
      - name: Amazon S3
        description: Store harvested clips and VOD assets in S3.
      - name: AWS Key Management Service
        description: Manage DRM encryption keys with AWS KMS integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
