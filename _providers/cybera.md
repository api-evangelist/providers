---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Cybera provides AI‑powered mule intelligence and scam response solutions for financial institutions.
  name: Cybera API
  slug: cybera-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cybera/vendors/cybera-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cybera-vendors.yml
- group: agent
  href: https://artifacts.apis.io/cybera/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/cybera/hosts/cybera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cybera-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  href: https://artifacts.apis.io/cybera/security/cybera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cybera-domain-security.yml
coverage:
  checked: '2026-10-22'
  detail: Main website renders content via JavaScript, and no machine‑readable OpenAPI or other contract was found despite probing common spec URLs.
  evidence:
  - status: 200
    url: https://www.cybera.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Cybera is a company identified in the API Evangelist secondary‑market harvest. Public information about its operations, products, or services is limited, and no dedicated corporate website or official online presence could be located through standard web searches. The entry remains a stub pending further discovery of verifiable sources.
layout: provider
modified: '2026-10-21'
name: Cybera
nav: Providers
network: true
overview: Cybera is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Platform, and Data.
random_paper: 6
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cybera Domain Security
  slug: cybera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cybera
tags:
- Company
- Technology
- Platform
- Data
website: https://www.nasdaqprivatemarket.com/
---
