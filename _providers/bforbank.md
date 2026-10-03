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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bforbank/refs/heads/main/hosts/bforbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bforbank-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://customers.bforbank.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.bforbank.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bforbank/refs/heads/main/security/bforbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bforbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bforbank.com
coverage:
  checked: '2026-09-28'
  detail: The OpenAPI endpoint returns an HTML page rendered by Next.js instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.bforbank.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bforbank is a French digital bank offering online banking services, credit cards, savings accounts, loans, and investment products. It emphasizes a human‑centric digital experience, providing secure banking, personalized offers, and a range of financial tools through its web and mobile platforms. The bank aims to combine simplicity with comprehensive financial services for individuals and businesses.
layout: provider
modified: '2026-09-28'
name: Bforbank
nav: Providers
network: true
overview: 'Bforbank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Digital Bank, France, and Fintech.


  Bforbank''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bforbank Domain Security
  slug: bforbank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bforbank
tags:
- Company
- Banking
- Digital Bank
- France
- Fintech
website: https://www.bforbank.com
---
