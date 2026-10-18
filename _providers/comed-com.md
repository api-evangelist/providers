---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comed-com/refs/heads/main/hosts/comed-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comed-com-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comed-com/refs/heads/main/security/comed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comed-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.comed.com
coverage:
  checked: '2026-10-13'
  detail: www.comed.com returns a 2963-byte bot-challenge shell for every path (including robots.txt and sitemap.xml); preflight found no OpenAPI, AsyncAPI, GraphQL or MCP on api.comed.com or www.comed.com. Green Button Connect My Data exists as a registered-third-party program (2018 ICC filing cites three registered non-RES third parties) but no public ESPI endpoint, registration URL or developer documentation could be verified, so no apis[] entry is recorded.
  evidence:
  - status: 200
    url: https://www.comed.com/
  - status: unresolved
    url: https://api.comed.com/
  reason: customer-only-docs
  state: gated
created: '2026-10-13'
description: ComEd (Commonwealth Edison) is the Exelon-owned electric utility serving northern Illinois, including Chicago. It publishes no public developer portal or API contract; customer energy-usage data sharing runs through the Green Button program, with third-party Green Button Connect My Data access arranged through a utility registration process referenced in Illinois Commerce Commission filings.
layout: provider
modified: '2026-10-13'
name: ComEd
nav: Providers
network: true
overview: ComEd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Utility, Energy, Green Button, and Illinois.
random_paper: 4
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Comed Com Domain Security
  slug: comed-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: comed-com
tags:
- Company
- Electric Utility
- Energy
- Green Button
- Illinois
- Utilities
website: https://www.comed.com
---
