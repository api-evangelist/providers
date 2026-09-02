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
api_count: 1
apis:
- description: Get all the services on which a song is available
  name: Songlink / Odesli
  slug: songlink-odesli
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/songlink-odesli-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/songlink-odesli-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/songlink-odesli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.notion.so/API-d0ebe08a5e304a55928405eb682f6741
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Get all the services on which a song is available
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/songlink-odesli.png
layout: provider
modified: '2026-05-28'
name: Songlink / Odesli
nav: Providers
network: true
overview: Songlink / Odesli publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music and Public APIs.
random_paper: 0
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/songlink-odesli/refs/heads/main/screenshots/songlink-odesli-2026-06-20T194212.png
security:
- kind: domain-security
  name: Songlink Odesli Domain Security
  slug: songlink-odesli-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Songlink Odesli Vulnerability Disclosure
  slug: songlink-odesli-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Songlink Odesli Trust Center
  slug: songlink-odesli-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: songlink-odesli
tags:
- Music
- Public APIs
website: https://www.notion.so/API-d0ebe08a5e304a55928405eb682f6741
---
