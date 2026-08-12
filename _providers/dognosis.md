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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dognosis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dognosis-llms.txt
- group: company
  title: ''
  type: Website
  url: https://dognosis.tech
created: '2026-07-17'
description: Dognosis is a Bengaluru, India deeptech company building olfaction AI that pairs trained detection dogs with machine learning to find disease from a single breath sample. Its product, BreathEasy, is a non-invasive breath test that produces a VOC-based cancer risk score for clinicians; a Phase 2 study published in the Journal of Clinical Oncology reported over 90% accuracy across seven cancer types, including at early and treatable stages. Dognosis is a portfolio company of Prosus Ventures. No public developer API is published today; this API Evangelist profile tracks the company's digital, discovery, and security surface (an llms.txt is served; no /.well-known discovery documents are published).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dognosis.png
layout: provider
modified: '2026-07-18'
name: Dognosis
nav: Providers
network: true
overview: Dognosis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and Cancer Detection.
random_paper: 58
score:
  band: minimal
  composite: 6.0
  delta: -0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dognosis/refs/heads/main/screenshots/dognosis-2026-07-25T212234.png
security:
- kind: domain-security
  name: Dognosis Domain Security
  slug: dognosis-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dognosis
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Cancer Detection
- Breath Analysis
- Olfaction AI
- Deeptech
website: https://dognosis.tech
---
