---
aid: amazon-kinesis-video-streams
name: Amazon Kinesis Video Streams
description: Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning, playback, and other processing. It automatically provisions and elastically scales all the infrastructure needed to ingest streaming video data from millions of devices.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - IoT
  - Machine Learning
  - Media
  - Video Streaming
url: https://raw.githubusercontent.com/api-evangelist/amazon-kinesis-video-streams/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-kinesis-video-streams:amazon-kinesis-video-streams-api
    name: Amazon Kinesis Video Streams API
    description: The Amazon Kinesis Video Streams API provides programmatic access to create and manage video streams, signaling channels, and WebRTC connections for streaming video from connected devices to AWS.
    humanURL: https://aws.amazon.com/kinesis/video-streams/
    baseURL: https://kinesisvideo.amazonaws.com
    tags:
      - IoT
      - Media
      - Video Streaming
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Reference.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/kinesisvideo/2017-09-30/openapi.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/kinesis/video-streams/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/kinesis/video-streams/pricing/
      - type: FAQ
        url: https://aws.amazon.com/kinesis/video-streams/faqs/
      - type: JSONSchema
        url: json-schema/amazon-kinesis-video-streams-stream-schema.json
      - type: JSONSchema
        url: json-schema/amazon-kinesis-video-streams-channel-schema.json
      - type: JSONLD
        url: json-ld/amazon-kinesis-video-streams-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/kinesis/video-streams/
  - type: Portal
    url: https://aws.amazon.com/kinesis/video-streams/
  - type: Documentation
    url: https://docs.aws.amazon.com/kinesisvideostreams/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/media/tag/amazon-kinesis-video-streams/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/kinesisvideo/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Features
    data:
      - name: Durable Video Storage
        description: Stores, encrypts, and indexes video data in streams and allows access to data through APIs.
      - name: WebRTC Support
        description: Provides signaling and relay services for two-way real-time media streaming between WebRTC-enabled devices.
      - name: ML Integration
        description: Integrates with Amazon Rekognition Video for real-time computer vision and object detection.
      - name: Scalable Ingestion
        description: Automatically provisions and elastically scales infrastructure to ingest video from millions of devices.
      - name: Playback
        description: Supports live and on-demand playback with HLS streaming.
  - type: UseCases
    data:
      - name: Smart Home Security
        description: Stream video from security cameras for real-time monitoring and alerts.
      - name: Industrial Monitoring
        description: Monitor manufacturing processes and equipment with video analytics.
      - name: Autonomous Vehicles
        description: Ingest sensor and video streams from autonomous vehicles for ML model training.
      - name: Live Video Streaming
        description: Deliver live video streams to viewers with low latency using WebRTC.
  - type: Integrations
    data:
      - name: Amazon Rekognition
        description: Analyze streaming video with computer vision for object and face detection.
      - name: AWS IoT Core
        description: Connect IoT cameras and devices to stream video to Amazon Kinesis Video Streams.
      - name: Amazon SageMaker
        description: Use video data for machine learning model training and inference.
  - type: SpectralRules
    url: rules/amazon-kinesis-video-streams-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-kinesis-video-streams-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-kinesis-video-streams-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
