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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sora-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soraschools.com
created: '2026-07-17'
description: Sora Schools is a fully online, project-based independent middle and high school (soraschools.com), backed by Union Square Ventures. Students learn through interdisciplinary, interest-driven projects and live small-group expeditions rather than traditional grade-level classes, with an accredited diploma path. It is surfaced in the API Evangelist network as a Union Square Ventures portfolio company. As of this enrichment pass the public site is served behind a Cloudflare bot challenge and Sora publishes no public developer, API, or integrations program, so this profile carries only probed infrastructure signals (DNS/TLS/security) rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sora.png
layout: provider
modified: '2026-07-21'
name: Sora
nav: Providers
network: true
overview: Sora is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Online Learning, K-12, and EdTech.
random_paper: 17
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Sora Domain Security
  slug: sora-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: sora
tags:
- Company
- Education
- Online Learning
- K-12
- EdTech
- Project-Based Learning
- Schools
website: https://soraschools.com
---
