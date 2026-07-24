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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kronos-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kronosbio.com
created: '2026-07-17'
description: 'Kronos Bio was a clinical-stage biopharmaceutical company in the life-sciences sector, backed by GV, working on cancer therapeutics. It surfaced in the API Evangelist network as a GV portfolio lead. The company operates no public API, developer portal, SDK, or technical documentation surface. A live probe on 2026-07-19 found that kronosbio.com no longer hosts a corporate website: the apex and www hosts both return a GoDaddy domain-parking lander that answers HTTP 200 for every path, and the ir, docs, api, and developer subdomains do not resolve at all. No GitHub organization or public repositories were found. This profile is retained as a network record of a company with no API surface rather than as an active API provider.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kronos-bio.png
layout: provider
modified: '2026-07-19'
name: Kronos Bio *
nav: Providers
network: true
overview: Kronos Bio * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biotechnology, Oncology, and Pharmaceuticals.
random_paper: 7
score:
  band: minimal
  composite: 7.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Kronos Bio Domain Security
  slug: kronos-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kronos-bio
tags:
- Company
- Life Sciences
- Biotechnology
- Oncology
- Pharmaceuticals
- Drug Discovery
website: https://kronosbio.com
---
