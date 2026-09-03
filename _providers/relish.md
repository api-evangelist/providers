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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hellorelish.com
created: '2026-07-17'
description: Relish is a consumer product operated at hellorelish.com and backed by Bullpen Capital, added to the API Evangelist network as a venture-portfolio lead. Live enrichment probing found the marketing site sitting behind a bot/captcha challenge and marked noindex, with no developer, API, or documentation subdomains resolving, no first-party GitHub organization, no published SDK packages, and no machine-readable well-known files. No public API surface was discovered during enrichment; the only verified technical artifact is a domain-security posture probe (TLS 1.3, SPF and DMARC present, no HSTS/DNSSEC/CAA records).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relish.png
layout: provider
modified: '2026-07-21'
name: Relish
nav: Providers
network: true
overview: Relish is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Venture Backed, Bullpen Capital, and No Public API.
random_paper: 17
score:
  band: minimal
  composite: 5.0
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
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relish/refs/heads/main/screenshots/relish-2026-09-02T153328.png
security:
- kind: domain-security
  name: Relish Domain Security
  slug: relish-domain-security
  summary_line: TLSv1.3 · DMARC
slug: relish
tags:
- Company
- Consumer
- Venture Backed
- Bullpen Capital
- No Public API
website: https://hellorelish.com
---
