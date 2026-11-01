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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dgpays/llms/dgpays-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dgpays-llms.txt
- group: other
  href: https://artifacts.apis.io/dgpays/hosts/dgpays-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dgpays-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dgpays
- group: auth
  href: https://artifacts.apis.io/dgpays/security/dgpays-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dgpays-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dgpays.com
coverage:
  checked: '2026-10-23'
  detail: Documentation pages are rendered via JavaScript and cannot be parsed for machine-readable contracts.
  evidence:
  - status: 200
    url: https://www.dgpays.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Dgpays is a fintech company offering payment processing solutions for merchants and platforms. It provides APIs for transaction initiation, status tracking, refunds, and reporting, aiming to simplify integration and improve payment experiences. The company focuses on security, compliance, and scalable infrastructure to serve businesses of various sizes.
layout: provider
modified: '2026-10-23'
name: Dgpays
nav: Providers
network: true
overview: Dgpays is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Merchant Services, and Platform.
random_paper: 0
score:
  band: minimal
  composite: 2.1
  coverage:
    artifact_dirs: 7
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
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dgpays Domain Security
  slug: dgpays-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dgpays
tags:
- Fintech
- Payments
- Merchant Services
- Platform
website: https://www.dgpays.com
---
