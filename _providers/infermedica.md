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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: NLP based symptom checker and patient triage API for health diagnosis from text
  name: Infermedica
  slug: infermedica
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/infermedica-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infermedica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.infermedica.com/docs/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://infermedica.com/blog
created: '2026-05-28'
description: NLP based symptom checker and patient triage API for health diagnosis from text
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infermedica.png
layout: provider
modified: '2026-05-28'
name: Infermedica
nav: Providers
network: true
overview: 'Infermedica publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.


  Infermedica''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 99
score:
  band: minimal
  composite: 8.7
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infermedica/refs/heads/main/screenshots/infermedica-2026-06-20T183329.png
security:
- kind: domain-security
  name: Infermedica Domain Security
  slug: infermedica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Infermedica Trust Center
  slug: infermedica-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: infermedica
tags:
- Health
- Public APIs
website: https://developer.infermedica.com/docs/
---
