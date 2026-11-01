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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/cardconnect/well-known/cardconnect-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cardconnect-status-security.txt
- group: agent
  href: https://artifacts.apis.io/cardconnect/well-known/cardconnect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cardconnect-well-known.yml
- group: other
  href: https://artifacts.apis.io/cardconnect/hosts/cardconnect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardconnect-hosts.yml
- group: build
  href: https://artifacts.apis.io/cardconnect/packages/cardconnect-packages.yml
  title: ''
  type: SDKs
  url: packages/cardconnect-packages.yml
- group: build
  href: https://artifacts.apis.io/cardconnect/packages/cardconnect-packages.yml
  title: ''
  type: Packages
  url: packages/cardconnect-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cardconnect.com/
- group: auth
  href: https://artifacts.apis.io/cardconnect/security/cardconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardconnect.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cardconnect.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: CardConnect, a Fiserv company, provides payment processing solutions that enable merchants to accept credit and debit cards both online and in‑store. Their CardPointe platform offers a suite of tools including a payment gateway, virtual terminal, mobile SDKs, and integrated APIs for developers to embed payment functionality directly into applications. CardConnect focuses on secure, PCI‑compliant transactions, fraud detection, and detailed reporting, serving businesses of all sizes across multiple industries.
layout: provider
modified: '2026-10-26'
name: CardConnect (Fiserv)
nav: Providers
network: true
overview: 'CardConnect (Fiserv) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  CardConnect (Fiserv)''s developer surface includes documentation and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 35.7
    operational_transparency: 10.5
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
  name: Cardconnect Domain Security
  slug: cardconnect-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cardconnect
tags:
- Company
website: https://cardconnect.com/
---
