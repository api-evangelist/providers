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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ginger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ginger.com/
created: '2026-07-17'
description: Ginger (formerly Ginger.io) was a behavioral and emotional health company offering on-demand mental health support — coaching, therapy, and psychiatry — delivered through a mobile app and an employer/health-plan benefits model. Surfaced in the API Evangelist network as a Techstars portfolio lead, Ginger merged with Headspace in 2021 to form Headspace Health; the ginger.com domain now redirects to Headspace for Organizations (organizations.headspace.com). Enrichment probing on 2026-07-19 found no independent public API, developer portal, OpenAPI, SDKs, or /.well-known discovery surface — every /.well-known path resolves to a soft-404 Headspace marketing page. This profile is retained as an acquired-company record; the only genuine machine-derivable artifact is the live domain-security posture of ginger.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ginger.png
layout: provider
modified: '2026-07-19'
name: Ginger
nav: Providers
network: true
overview: Ginger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Behavioral Health, Healthcare, and Wellness.
random_paper: 6
score:
  band: minimal
  composite: 3.3
  delta: -2.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ginger/refs/heads/main/screenshots/ginger-2026-07-25T215825.png
security:
- kind: domain-security
  name: Ginger Domain Security
  slug: ginger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ginger
tags:
- Company
- Mental Health
- Behavioral Health
- Healthcare
- Wellness
- Telehealth
- Coaching
- Acquired
website: https://ginger.com/
---
