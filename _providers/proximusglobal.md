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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/proximusglobal/refs/heads/main/hosts/proximusglobal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/proximusglobal-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/proximusglobal/refs/heads/main/vendors/proximusglobal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/proximusglobal-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proximusglobal.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.proximusglobal.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.proximusglobal.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proximusglobal/refs/heads/main/security/proximusglobal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proximusglobal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.proximusglobal.com
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at api.proximusglobal.com.
  evidence:
  - status: 0
    url: https://api.proximusglobal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Proximus Global is a global communications and digital identity company combining Telesign, BICS, and Route Mobile. It provides connectivity, fraud protection, messaging, and cloud communications services, reaching over 5 billion subscribers and securing more than 180 billion transactions annually. The company operates in 230+ countries, holds 35+ patents, and invests in next‑gen technologies like 5G, IoT, eSIM, and AI‑driven security.
image: https://www.proximusglobal.com/wp-content/uploads/2025/04/proximusglobal-og-1200x630-1.png
layout: provider
modified: '2026-10-03'
name: Proximus Global
nav: Providers
network: true
overview: Proximus Global is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Digital Identity, Connectivity, and Fraud Prevention.
random_paper: 10
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Proximusglobal Domain Security
  slug: proximusglobal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: proximusglobal
tags:
- Company
- Communications
- Digital Identity
- Connectivity
- Fraud Prevention
website: https://www.proximusglobal.com
---
