---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Speech To Text Agentic Access
  operation_count: 5
  slug: google-cloud-speech-to-text-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://speech.googleapis.com/v1
  baseurl_source: declared
  description: Manage long-running operations
  name: Google Cloud Speech-To-Text Operations API
  slug: google-cloud-speech-to-text-operations-api
- baseURL: https://speech.googleapis.com/v1
  baseurl_source: declared
  description: Perform speech recognition on audio
  name: Google Cloud Speech-To-Text Speech API
  slug: google-cloud-speech-to-text-speech-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Cloud Speech-to-Text Operations API
  slug: postman-google-cloud-speech-to-text-operations-api
- collection_type: postman
  name: Google Cloud -to-Text Operations Speech API
  slug: postman-google-cloud-speech-to-text-speech-api
- collection_type: open
  name: Google Cloud Speech-to-Text Operations API
  slug: open-google-cloud-speech-to-text-operations-api
- collection_type: open
  name: Google Cloud -to-Text Operations Speech API
  slug: open-google-cloud-speech-to-text-speech-api
- collection_type: open
  name: Google Cloud Speech-to-Text API
  slug: open-openapi
common:
- group: other
  href: https://artifacts.apis.io/google-cloud-speech-to-text/capabilities/google-cloud-speech-to-text-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-speech-to-text-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-speech-to-text/plans/google-cloud-speech-to-text-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-speech-to-text-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-speech-to-text/rate-limits/google-cloud-speech-to-text-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-speech-to-text-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-speech-to-text/finops/google-cloud-speech-to-text-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-speech-to-text-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-speech-to-text/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-speech-to-text/agentic-access/google-cloud-speech-to-text-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-speech-to-text-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-speech-to-text/security/google-cloud-speech-to-text-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-speech-to-text-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-speech-to-text/security/google-cloud-speech-to-text-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-speech-to-text-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-speech-to-text/authentication/google-cloud-speech-to-text-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-speech-to-text-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-speech-to-text/scopes/google-cloud-speech-to-text-scopes.yml
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
  href: https://artifacts.apis.io/google-cloud-speech-to-text/json-ld/json-ld.yml
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
- has_sources: true
  method: derived
  name: Google Cloud Speech To Text Finops
  primary_unit: minute
  service_category: ''
  slug: google-cloud-speech-to-text-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-speech-to-text.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Speech-To-Text
nav: Providers
network: true
overview: 'Google Cloud Speech-To-Text publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Operations API and Speech API. Tagged areas include Audio Processing, Google Cloud, Machine Learning, Speech Recognition, and Transcription.


  The Google Cloud Speech-To-Text catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Speech-To-Text''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Google Cloud Speech To Text Plans Pricing
  plan_count: 12
  slug: google-cloud-speech-to-text-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Google Cloud Speech To Text Rate Limits
  slug: google-cloud-speech-to-text-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Speech-To-Text — jsonschema rules
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
  composite: 51.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.7
    catalog_earned_first_party: 12.0
    catalog_gap: 56.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 53.6
    developer_ergonomics: 51.2
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-speech-to-text/google-cloud-speech-to-text-2026-06-20T182137.png
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
website: https://www.google.com/
---
