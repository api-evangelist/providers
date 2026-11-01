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
- group: other
  href: https://artifacts.apis.io/gccpay/hosts/gccpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gccpay-hosts.yml
- group: build
  href: https://artifacts.apis.io/gccpay/packages/gccpay-packages.yml
  title: ''
  type: SDKs
  url: packages/gccpay-packages.yml
- group: build
  href: https://artifacts.apis.io/gccpay/packages/gccpay-packages.yml
  title: ''
  type: Packages
  url: packages/gccpay-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.payriff.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PayRiff
- group: auth
  href: https://artifacts.apis.io/gccpay/security/gccpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gccpay-domain-security.yml
- group: other
  title: ''
  type: Image
  url: https://payriff.com/assets/images/1200x630.png
- group: company
  title: ''
  type: Website
  url: https://payriff.com/
coverage:
  checked: '2026-10-27'
  detail: The provider's homepage and /docs return HTML shells with no machine‑readable OpenAPI or other contracts.
  evidence:
  - status: 200
    url: https://gccpay.sa/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: GCCPAY offers a digital payment platform enabling online merchants to accept and manage payments securely and at scale. Their APIs provide tools for transaction processing, settlement, recurring billing, fraud detection, and reporting, aimed at simplifying e‑commerce payment workflows for businesses of all sizes.
image: https://payriff.com/assets/images/1200x630.png
layout: provider
modified: '2026-10-26'
name: GCCPAY
nav: Providers
network: true
overview: 'GCCPAY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, E-commerce, API, and Fintech.


  GCCPAY''s developer surface includes documentation and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 5.3
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
  name: Gccpay Domain Security
  slug: gccpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gccpay
tags:
- Company
- Payments
- E-commerce
- API
- Fintech
website: https://payriff.com/
---
