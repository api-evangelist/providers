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
  href: https://raw.githubusercontent.com/api-evangelist/boutiqaat/refs/heads/main/hosts/boutiqaat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boutiqaat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boutiqaat/refs/heads/main/vendors/boutiqaat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boutiqaat-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boutiqaat/refs/heads/main/security/boutiqaat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boutiqaat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boutiqaat.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.boutiqaat.com/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Boutiqaat is a fashion e‑commerce platform operating primarily in the Middle East, offering a curated selection of clothing, accessories, and beauty products through its online store and mobile applications. The company provides APIs for product catalog, order management, and customer data, enabling integration with third‑party services and partners. It aims to deliver a seamless shopping experience with localized content and payment options.
layout: provider
modified: '2026-10-03'
name: Boutiqaat
nav: Providers
network: true
overview: Boutiqaat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Fashion, and Middle East.
random_paper: 2
score:
  band: minimal
  composite: 2.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boutiqaat Domain Security
  slug: boutiqaat-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: boutiqaat
tags:
- Company
- E-Commerce
- Fashion
- Middle East
website: https://www.boutiqaat.com
---
