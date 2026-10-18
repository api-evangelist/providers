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
api_count: 1
apis:
- description: Alio Financial provides banking APIs (no public spec discovered).
  name: Alio API
  slug: alio-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alio/refs/heads/main/hosts/alio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alio/refs/heads/main/vendors/alio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alio-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://aliofinance.com/signup.php
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alio/refs/heads/main/security/alio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aliofinance.com/
coverage:
  checked: '2026-10-05'
  detail: The provider's website and API host return HTML pages but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://aliofinance.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Alio is a technology company delivering innovative financial services solutions, including data‑driven platforms for asset management, investment analytics, and digital banking. It streamlines workflows, enhances decision‑making, and offers modern APIs for seamless connectivity across financial ecosystems, supporting both retail and institutional clients with robust, secure, and scalable services.
layout: provider
modified: '2026-09-24'
name: Alio
nav: Providers
network: true
overview: 'Alio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, and Banking.


  Alio''s developer surface includes signup flow and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 1.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alio Domain Security
  slug: alio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alio
tags:
- Company
- Financial Services
- Fintech
- Banking
website: https://aliofinance.com/
---
