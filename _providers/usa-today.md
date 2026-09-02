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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/usa-today-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usa-today-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usatoday
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usa-today
- group: company
  title: ''
  type: Website
  url: https://www.usatoday.com/
created: '2026-05-05'
description: A major American daily national newspaper and digital news platform owned by Gannett. One of the most widely circulated newspapers in the United States covering news, sports, entertainment, and lifestyle topics.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usa-today.png
layout: provider
modified: '2026-05-05'
name: USA TODAY
nav: Providers
network: true
overview: USA TODAY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, News, and Publishing.
random_paper: 16
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 96.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.2
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usa-today/refs/heads/main/screenshots/usa-today-2026-06-20T200638.png
security:
- kind: domain-security
  name: Usa Today Domain Security
  slug: usa-today-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usa Today Vulnerability Disclosure
  slug: usa-today-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: usa-today
tags:
- Media
- News
- Publishing
website: https://www.usatoday.com/
---
