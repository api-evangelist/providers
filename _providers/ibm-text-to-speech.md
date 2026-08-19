---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Convert text to speech
  name: IBM Text to Speech
  slug: ibm-text-to-speech
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-text-to-speech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-text-to-speech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.ibm.com/docs/text-to-speech/getting-started.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Convert text to speech
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-text-to-speech.png
layout: provider
modified: '2026-05-28'
name: IBM Text to Speech
nav: Providers
network: true
overview: IBM Text to Speech publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Development and Public APIs.
random_paper: 120
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-text-to-speech/refs/heads/main/screenshots/ibm-text-to-speech-2026-06-20T183134.png
security:
- kind: domain-security
  name: Ibm Text To Speech Domain Security
  slug: ibm-text-to-speech-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ibm Text To Speech Vulnerability Disclosure
  slug: ibm-text-to-speech-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-text-to-speech
tags:
- Development
- Public APIs
website: https://cloud.ibm.com/docs/text-to-speech/getting-started.html
---
