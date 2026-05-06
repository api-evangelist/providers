---
name: Amazon Elastic Transcoder
description: Amazon Elastic Transcoder is media transcoding in the cloud. It is designed to be a highly scalable, easy-to-use, and cost-effective way for developers and businesses to convert or transcode media files from their source format into versions that will play back on devices like smartphones, tablets, and PCs.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/elastictranscoder/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - Media
  - Transcoding
  - Video
apis:
  - name: Amazon Elastic Transcoder API
    description: API for creating and managing media transcoding pipelines, presets, and jobs to convert media files for playback on various devices.
    humanURL: https://aws.amazon.com/elastictranscoder/
    baseURL: https://elastictranscoder.amazonaws.com
    tags:
      - Media
      - Transcoding
      - Video
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/
      - type: OpenAPI
        url: openapi/amazon-elastic-transcoder-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/api-reference.html
      - type: GettingStarted
        url: https://aws.amazon.com/elastictranscoder/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/elastictranscoder/pricing/
      - type: FAQ
        url: https://aws.amazon.com/elastictranscoder/faqs/
      - type: JSONSchema
        url: json-schema/amazon-elastic-transcoder-access-control-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elastic-transcoder-access-controls-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elastic-transcoder-access-denied-exception-schema.json
      - type: JSONLD
        url: json-ld/amazon-elastic-transcoder-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/elastictranscoder/
  - type: Documentation
    url: https://docs.aws.amazon.com/elastictranscoder/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/elastictranscoder/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/elastictranscoder/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/elastictranscoder
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-elastic-transcoder-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-elastic-transcoder-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-elastic-transcoder-vocabulary.yaml
  - type: Features
    data:
      - name: Managed Transcoding Pipelines
        description: Create pipelines that manage media transcoding jobs with configurable input/output settings
      - name: Preset Library
        description: Use built-in presets optimized for popular devices and formats
      - name: Custom Presets
        description: Create custom presets for specific output requirements
      - name: Thumbnail Generation
        description: Automatically generate thumbnails from video files during transcoding
      - name: Content Protection
        description: Apply HLS content protection and digital rights management
  - type: UseCases
    data:
      - name: Video-on-Demand Transcoding
        description: Convert video files for streaming across different devices and bandwidths
      - name: Mobile Video Delivery
        description: Transcode content optimized for smartphone and tablet playback
      - name: HLS Streaming
        description: Create adaptive bitrate HLS streams for seamless playback
      - name: Audio File Conversion
        description: Convert audio files between different formats and bitrates
  - type: Integrations
    data:
      - name: Amazon S3
        description: Use S3 for input and output media file storage
      - name: Amazon SNS
        description: Receive notifications when transcoding jobs complete
      - name: Amazon CloudFront
        description: Distribute transcoded content via CDN
      - name: AWS Lambda
        description: Trigger transcoding workflows from Lambda functions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
