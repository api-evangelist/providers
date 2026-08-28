---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Cloud Video Intelligence Agentic Access
  operation_count: 3
  slug: google-cloud-video-intelligence-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 2
apis:
- description: The Operations API from Google Cloud Video Intelligence — 1 operation(s) for operations.
  name: Google Cloud Video Intelligence Operations API
  slug: google-cloud-video-intelligence-operations-api
- description: The Videos:annotate API from Google Cloud Video Intelligence — 1 operation(s) for videos:annotate.
  name: Google Cloud Video Intelligence Videos:annotate API
  slug: google-cloud-video-intelligence-videos-annotate-api
artifact_total: 17
collections:
- collection_type: postman
  name: Google Cloud Video Intelligence Operations API
  slug: postman-google-cloud-video-intelligence-operations-api
- collection_type: postman
  name: Google Cloud Video Intelligence Operations Videos:annotate API
  slug: postman-google-cloud-video-intelligence-videos-annotate-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Video Intelligence Operations API
  slug: open-google-cloud-video-intelligence-operations-api
- collection_type: open
  name: Google Cloud Video Intelligence Operations Videos:annotate API
  slug: open-google-cloud-video-intelligence-videos-annotate-api
- collection_type: open
  name: Google Cloud Video Intelligence API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-video-intelligence/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-video-intelligence-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-video-intelligence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-video-intelligence-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/video-intelligence
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/video-intelligence/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/video-intelligence/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/video-intelligence/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/video-intelligence/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/video-intelligence-api-release-notes.xml
created: '2026-03-13'
description: Google Cloud Video Intelligence API makes videos searchable and discoverable by extracting metadata with an easy-to-use REST API. It enables annotation of videos stored in Google Cloud Storage with video-level, shot-level, and frame-level labels, object tracking, text detection, and explicit content detection.
finops:
- name: Google Cloud Video Intelligence Finops
  service_category: API
  slug: google-cloud-video-intelligence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-video-intelligence.png
json_schemas:
- name: Video Annotation Request
  property_count: 6
  slug: video-annotation
jsonld:
- class_count: 13
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Video Intelligence
nav: Providers
network: true
overview: 'Google Cloud Video Intelligence publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Videos:annotate API. Tagged areas include Content Moderation, Google Cloud, Machine-Learning, Object Detection, and Video Analysis.


  The Google Cloud Video Intelligence catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Video Intelligence''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Video Intelligence Plans Pricing
  plan_count: 3
  slug: google-cloud-video-intelligence-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Google Cloud Video Intelligence Rate Limits
  slug: google-cloud-video-intelligence-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Video Intelligence API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-video-intelligence-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.7
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-video-intelligence/refs/heads/main/screenshots/google-cloud-video-intelligence-2026-06-20T182146.png
security:
- kind: domain-security
  name: Google Cloud Video Intelligence Domain Security
  slug: google-cloud-video-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Video Intelligence Vulnerability Disclosure
  slug: google-cloud-video-intelligence-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-video-intelligence
tags:
- Content Moderation
- Google Cloud
- Machine-Learning
- Object Detection
- Video Analysis
- Video Intelligence
website: https://cloud.google.com/video-intelligence
---
