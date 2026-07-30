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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Camtasia Agentic Access
  operation_count: 38
  slug: camtasia-agentic-access
  summary_line: 38 operations · 15 acting
api_count: 11
apis:
- description: 'Public oEmbed API for TechSmith Screencast (app.screencast.com), the cloud destination where Camtasia videos and images are shared. The oEmbed endpoint returns embed HTML, thumbnail, and metadata for '
  name: TechSmith Screencast oEmbed API
  slug: screencast-oembed-api
- description: Browse and manage media assets
  name: Camtasia Assets API
  slug: camtasia-assets-api
- description: Browse asset categories
  name: Camtasia Categories API
  slug: camtasia-categories-api
- description: Download asset files
  name: Camtasia Downloads API
  slug: camtasia-downloads-api
- description: Manage asset libraries and collections
  name: Camtasia Libraries API
  slug: camtasia-libraries-api
- description: Manage media items on project tracks
  name: Camtasia Media API
  slug: camtasia-media-api
- description: Produce and export finished videos
  name: Camtasia Productions API
  slug: camtasia-productions-api
- description: Create and manage Camtasia projects
  name: Camtasia Projects API
  slug: camtasia-projects-api
- description: Manage screen recordings
  name: Camtasia Recordings API
  slug: camtasia-recordings-api
- description: Manage video project templates
  name: Camtasia Templates API
  slug: camtasia-templates-api
- description: Manage timeline tracks within a project
  name: Camtasia Tracks API
  slug: camtasia-tracks-api
artifact_total: 24
collections:
- collection_type: open
  name: Camtasia Asset Library API
  slug: open-camtasia-asset-library
- collection_type: open
  name: Camtasia Project Management API
  slug: open-camtasia-project-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/camtasia-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/camtasia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/camtasia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/camtasia-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/techsmith-corporation
- group: company
  title: ''
  type: Website
  url: https://www.techsmith.com/camtasia.html
- group: other
  title: ''
  type: Screencast
  url: https://www.techsmith.com/screencast/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.techsmith.com/learn/camtasia/
- group: company
  title: ''
  type: Blog
  url: https://www.techsmith.com/blog/category/camtasia/
- group: operate
  title: ''
  type: Support
  url: https://support.techsmith.com
- group: other
  title: ''
  type: PublicAPIRepository
  url: https://github.com/TechSmith/screencast-public-api-docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.techsmith.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.techsmith.com/privacy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/camtasia-context.jsonld
created: '2024-01-15'
description: Camtasia is a screen recording and video editing software by TechSmith that allows users to create professional videos, tutorials, and presentations with built-in editing tools, effects, and media assets. Camtasia itself does not publish a public REST API, but it integrates tightly with TechSmith Screencast for sharing, and TechSmith publishes a public Screencast oEmbed API plus the Camtasia Screen Recorder SDK for embedding recording capabilities into third-party applications.
finops:
- name: Camtasia Finops
  service_category: API
  slug: camtasia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/camtasia.png
json_schemas:
- name: Camtasia Asset
  property_count: 16
  slug: camtasia-asset
- name: Camtasia Project
  property_count: 11
  slug: camtasia-project
jsonld:
- class_count: 0
  name: Camtasia Context
  property_count: 7
  slug: camtasia-context
layout: provider
modified: '2026-07-25'
name: Camtasia
nav: Providers
network: true
overview: 'Camtasia publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Categories API, Downloads API, and 7 more. Tagged areas include Screen Recording, Video Editing, Tutorial Creation, E-Learning, and Screencast.


  The Camtasia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Camtasia''s developer surface includes authentication, getting-started guide, engineering blog, support, and 10 more developer resources.'
plans:
- name: Camtasia Plans Pricing
  plan_count: 3
  slug: camtasia-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Camtasia Rate Limits
  slug: camtasia-rate-limits
rules:
- name: Camtasia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: camtasia-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.8
  delta: -4.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.1
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/camtasia/refs/heads/main/screenshots/camtasia-2026-06-20T173915.png
security:
- kind: authentication
  name: Camtasia Authentication
  slug: camtasia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Camtasia Domain Security
  slug: camtasia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Camtasia Vulnerability Disclosure
  slug: camtasia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: camtasia
tags:
- Screen Recording
- Video Editing
- Tutorial Creation
- E-Learning
- Screencast
- oEmbed
- SDK
website: https://www.techsmith.com/camtasia.html
---
