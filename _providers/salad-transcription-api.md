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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The default API from Salad Transcription API — 2 operation(s) for default.
  name: Salad Transcription API default API
  slug: salad-transcription-api-default-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salad Transcription default API
  slug: open-salad-transcription-api-default-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/salad-transcription-api-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salad-transcription-api-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SaladTechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salad-technologies
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/salad-apis/salad/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://salad.com/pricing
- group: company
  title: ''
  type: About
  url: https://salad.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.salad.com/?_gl=1*wlg1yz*_gcl_au*NTI4MzE4NzY0LjE3MzU5MjAxNzc.
- group: auth
  title: ''
  type: Security
  url: https://salad.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://salad.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://salad.com/terms
- group: operate
  title: ''
  type: PressReleases
  url: https://salad.com/press
- group: auth
  title: ''
  type: Trust
  url: https://trust.salad.com/?_gl=1*b0d9i*_gcl_au*NTI4MzE4NzY0LjE3MzU5MjAxNzc.
created: '2024-11-17'
description: Salad Transcription API provides speech-to-text conversion powered by Salad's distributed GPU cloud network. Designed for high-volume audio and video transcription workloads with support for 97 languages, speaker diarization, and caption generation.
examples:
- key_count: 6
  name: Salad Get Transcript Example
  slug: salad-get-transcript-example
- key_count: 6
  name: Salad Transcribe Example
  slug: salad-transcribe-example
finops:
- name: Salad Transcription Api Finops
  service_category: API
  slug: salad-transcription-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salad-transcription-api.png
json_schemas:
- name: Salad Transcription Job
  property_count: 8
  slug: salad-transcription-job
json_structures:
- name: Salad Transcription Api Structure
  property_count: 0
  slug: salad-transcription-api-structure
jsonld:
- class_count: 6
  name: Salad Transcription Api Context
  property_count: 19
  slug: salad-transcription-api-context
layout: provider
modified: '2026-05-02'
name: Salad Transcription API
nav: Providers
network: true
overview: 'Salad Transcription API publishes 1 API on the [APIs.io](https://apis.io/) network: default API. Tagged areas include Audio Transcription, Captions, Diarization, GPU, and Speech Recognition.


  The Salad Transcription API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salad Transcription API''s developer surface includes pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Salad Transcription Api Plans Pricing
  plan_count: 3
  slug: salad-transcription-api-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Salad Transcription Api Rate Limits
  slug: salad-transcription-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Salad Transcription API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: salad-transcription-api-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Salad Transcription API API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 2
  slug: salad-transcription-api-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 28.8
    contract_quality: 53.7
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 21.1
  previous_composite: 40.0
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salad-transcription-api/refs/heads/main/screenshots/salad-transcription-api-2026-06-20T193339.png
security:
- kind: domain-security
  name: Salad Transcription Api Domain Security
  slug: salad-transcription-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Salad Transcription Api Trust Center
  slug: salad-transcription-api-trust-center
  summary_line: SOC 2
slug: salad-transcription-api
tags:
- Audio Transcription
- Captions
- Diarization
- GPU
- Speech Recognition
- Transcription
- Video Processing
---
