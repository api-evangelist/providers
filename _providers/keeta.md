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
  href: https://artifacts.apis.io/keeta/llms/keeta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keeta-llms.txt
- group: agent
  href: https://artifacts.apis.io/keeta/well-known/keeta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keeta-well-known.yml
- group: other
  href: https://artifacts.apis.io/keeta/hosts/keeta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keeta-hosts.yml
- group: other
  href: https://artifacts.apis.io/keeta/vendors/keeta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keeta-vendors.yml
- group: auth
  href: https://artifacts.apis.io/keeta/security/keeta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keeta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keeta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keeta.com/
- group: company
  title: ''
  type: Blog
  url: https://keeta.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keetanetwork
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.keeta.com/other-documentation/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://keeta.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keeta.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.keeta.com/introduction/start-developing
created: '2026-10-21'
description: Keeta provides a unifying layer for modern global finance, offering flexible APIs that connect institutions to digital payment, crypto, and investment services. Their platform supports high‑volume transactions, cross‑chain stablecoin transfers, and compliance‑focused onboarding, aiming to modernize legacy financial stacks with scalable, secure solutions.
image: https://framerusercontent.com/images/uPVrPTyyj7GeaNFrnLnIm7fqxM.png
layout: provider
modified: '2026-10-21'
name: Keeta
nav: Providers
network: true
overview: 'Keeta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Payments, API, and Fintech.


  Keeta''s developer surface includes documentation, engineering blog, getting-started guide, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Keeta Domain Security
  slug: keeta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: keeta
tags:
- Company
- Finance
- Payments
- API
- Fintech
website: https://keeta.com/
---
