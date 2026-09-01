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
  url: security/nbc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nbc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nbcnews
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nationalbroadcastingcompany
- group: company
  title: ''
  type: Website
  url: https://www.nbc.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.nbcuniversal.com/
- group: other
  title: ''
  type: Advertising
  url: https://together.nbcuni.com/
created: '2026-05-05'
description: NBC (National Broadcasting Company) is a major American commercial broadcast television network and a subsidiary of Comcast through NBCUniversal. NBC produces news (NBC News, Today), entertainment, late-night, and sports programming (Sunday Night Football, Olympic Games). NBC and parent company NBCUniversal do not publish a public developer portal. Programmatic advertising APIs (NBCUniversal One Platform) and streaming partner integrations (Peacock) are offered only through direct sales relationships rather than self-serve developer signup.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nbc.png
layout: provider
modified: '2026-05-16'
name: NBC
nav: Providers
network: true
overview: NBC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Broadcasting, Television, Entertainment, and Fortune 500.
random_paper: 13
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 2
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
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nbc/refs/heads/main/screenshots/nbc-2026-06-20T190110.png
security:
- kind: domain-security
  name: Nbc Domain Security
  slug: nbc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nbc Vulnerability Disclosure
  slug: nbc-vulnerability-disclosure
  summary_line: disclosure policy published
slug: nbc
tags:
- Media
- Broadcasting
- Television
- Entertainment
- Fortune 500
website: https://www.nbc.com/
---
