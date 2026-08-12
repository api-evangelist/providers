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
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Speech To Text Agentic Access
  operation_count: 5
  slug: google-cloud-speech-to-text-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: Manage long-running operations
  name: Google Cloud Speech-To-Text Operations API
  slug: google-cloud-speech-to-text-operations-api
- description: Perform speech recognition on audio
  name: Google Cloud Speech-To-Text Speech API
  slug: google-cloud-speech-to-text-speech-api
artifact_total: 14
collections:
- collection_type: postman
  name: Google Cloud Speech-to-Text Operations API
  slug: postman-google-cloud-speech-to-text-operations-api
- collection_type: postman
  name: Google Cloud -to-Text Operations Speech API
  slug: postman-google-cloud-speech-to-text-speech-api
- collection_type: open
  name: Google Cloud Speech-to-Text API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-speech-to-text/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-speech-to-text-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-speech-to-text-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-speech-to-text-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-speech-to-text-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-speech-to-text-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/speech-to-text
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/speech-to-text/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/speech-to-text/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/speech-to-text/pricing
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
  url: https://cloud.google.com/speech-to-text/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/speech-release-notes.xml
created: '2026-03-13'
description: Google Cloud Speech-to-Text API converts audio to text using advanced deep learning models, supporting over 125 languages and variants with real-time streaming and batch transcription capabilities.
finops:
- name: Google Cloud Speech To Text Finops
  service_category: API
  slug: google-cloud-speech-to-text-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-speech-to-text.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Speech-To-Text
nav: Providers
network: true
overview: 'Google Cloud Speech-To-Text publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Speech API. Tagged areas include Audio Processing, Google Cloud, Machine Learning, Speech Recognition, and Transcription.


  The Google Cloud Speech-To-Text catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Speech-To-Text''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Speech To Text Plans Pricing
  plan_count: 3
  slug: google-cloud-speech-to-text-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 5
  name: Google Cloud Speech To Text Rate Limits
  slug: google-cloud-speech-to-text-rate-limits
rules:
- name: Google Cloud Speech-To-Text API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-speech-to-text-jsonschema-spectral-rules
scopes:
- name: Google Cloud Speech To Text Scopes
  scope_count: 1
  slug: google-cloud-speech-to-text-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 52.2
  delta: -8.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.2
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 60.7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-speech-to-text/refs/heads/main/screenshots/google-cloud-speech-to-text-2026-06-20T182137.png
security:
- kind: authentication
  name: Google Cloud Speech To Text Authentication
  slug: google-cloud-speech-to-text-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Speech To Text Domain Security
  slug: google-cloud-speech-to-text-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Speech To Text Vulnerability Disclosure
  slug: google-cloud-speech-to-text-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-speech-to-text
tags:
- Audio Processing
- Google Cloud
- Machine Learning
- Speech Recognition
- Transcription
website: https://cloud.google.com/speech-to-text
---
