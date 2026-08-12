---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Kinesis Video Streams Agentic Access
  operation_count: 9
  slug: amazon-kinesis-video-streams-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 2
apis:
- description: WebRTC signaling channel management
  name: Amazon Kinesis Video Streams Signaling Channels API
  slug: amazon-kinesis-video-streams-signaling-channels-api
- description: Video stream management
  name: Amazon Kinesis Video Streams Streams API
  slug: amazon-kinesis-video-streams-streams-api
artifact_total: 34
collections:
- collection_type: postman
  name: Amazon Kinesis Video Streams Signaling Channels API
  slug: postman-amazon-kinesis-video-streams-signaling-channels-api
- collection_type: postman
  name: Amazon Kinesis Video Signaling Channels Streams API
  slug: postman-amazon-kinesis-video-streams-streams-api
- collection_type: open
  name: Amazon Kinesis Video Streams API
  slug: open-amazon-kinesis-video-streams
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-kinesis-video-streams/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-kinesis-video-streams-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-kinesis-video-streams-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-kinesis-video-streams-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-kinesis-video-streams-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-kinesis-video-streams-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/video-streams/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/kinesis/video-streams/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/kinesisvideostreams/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/media/tag/amazon-kinesis-video-streams/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/kinesisvideo/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-kinesis-video-streams-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-kinesis-video-streams-vocabulary.yaml
created: '2026-03-16'
description: Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning, playback, and other processing. It automatically provisions and elastically scales all the infrastructure needed to ingest streaming video data from millions of devices.
examples:
- key_count: 5
  name: Amazon Kinesis Video Streams Channel Example
  slug: amazon-kinesis-video-streams-channel-example
- key_count: 5
  name: Amazon Kinesis Video Streams Stream Example
  slug: amazon-kinesis-video-streams-stream-example
features:
- description: Stores, encrypts, and indexes video data in streams and allows access to data through APIs.
  name: Durable Video Storage
- description: Provides signaling and relay services for two-way real-time media streaming between WebRTC-enabled devices.
  name: WebRTC Support
- description: Integrates with Amazon Rekognition Video for real-time computer vision and object detection.
  name: ML Integration
- description: Automatically provisions and elastically scales infrastructure to ingest video from millions of devices.
  name: Scalable Ingestion
- description: Supports live and on-demand playback with HLS streaming.
  name: Playback
finops:
- name: Amazon Kinesis Video Streams Finops
  service_category: API
  slug: amazon-kinesis-video-streams-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-kinesis-video-streams.png
integrations:
- description: Analyze streaming video with computer vision for object and face detection.
  name: Amazon Rekognition
- description: Connect IoT cameras and devices to stream video to Amazon Kinesis Video Streams.
  name: AWS IoT Core
- description: Use video data for machine learning model training and inference.
  name: Amazon SageMaker
json_schemas:
- name: Channel
  property_count: 5
  slug: amazon-kinesis-video-streams-channel
- name: Stream
  property_count: 5
  slug: amazon-kinesis-video-streams-stream
json_structures:
- name: Amazon Kinesis Video Streams Channel Structure
  property_count: 5
  slug: amazon-kinesis-video-streams-channel-structure
- name: Amazon Kinesis Video Streams Stream Structure
  property_count: 5
  slug: amazon-kinesis-video-streams-stream-structure
jsonld:
- class_count: 2
  name: Amazon Kinesis Video Streams Context
  property_count: 7
  slug: amazon-kinesis-video-streams-context
layout: provider
modified: '2026-05-19'
name: Amazon Kinesis Video Streams
nav: Providers
network: true
overview: 'Amazon Kinesis Video Streams publishes 2 APIs on the [APIs.io](https://apis.io/) network: Signaling Channels API and Streams API. Tagged areas include IoT, Machine Learning, Media, and Video Streaming.


  The Amazon Kinesis Video Streams catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Kinesis Video Streams'' developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Kinesis Video Streams Plans Pricing
  plan_count: 3
  slug: amazon-kinesis-video-streams-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Amazon Kinesis Video Streams Rate Limits
  slug: amazon-kinesis-video-streams-rate-limits
rules:
- name: Amazon Kinesis Video Streams API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-kinesis-video-streams-jsonschema-spectral-rules
- name: Amazon Kinesis Video Streams API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 15
  slug: amazon-kinesis-video-streams-spectral-rules
score:
  band: strong
  composite: 57.1
  delta: -8.6
  facets:
    commercial_clarity: 57.9
    contract_quality: 73.9
    developer_ergonomics: 45.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-kinesis-video-streams/refs/heads/main/screenshots/amazon-kinesis-video-streams-2026-06-20T171720.png
security:
- kind: authentication
  name: Amazon Kinesis Video Streams Authentication
  slug: amazon-kinesis-video-streams-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Kinesis Video Streams Domain Security
  slug: amazon-kinesis-video-streams-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Kinesis Video Streams Vulnerability Disclosure
  slug: amazon-kinesis-video-streams-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Kinesis Video Streams Trust Center
  slug: amazon-kinesis-video-streams-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-kinesis-video-streams
tags:
- IoT
- Machine Learning
- Media
- Video Streaming
use_cases:
- description: Stream video from security cameras for real-time monitoring and alerts.
  name: Smart Home Security
- description: Monitor manufacturing processes and equipment with video analytics.
  name: Industrial Monitoring
- description: Ingest sensor and video streams from autonomous vehicles for ML model training.
  name: Autonomous Vehicles
- description: Deliver live video streams to viewers with low latency using WebRTC.
  name: Live Video Streaming
website: https://aws.amazon.com/kinesis/video-streams/
---
