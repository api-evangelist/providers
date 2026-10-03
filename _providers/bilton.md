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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bilton/refs/heads/main/llms/bilton-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bilton-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bilton/refs/heads/main/hosts/bilton-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bilton-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bilton/refs/heads/main/vendors/bilton-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bilton-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bilton/refs/heads/main/security/bilton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bilton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bilton.tech
- group: docs
  title: ''
  type: Documentation
  url: https://bilton.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://bilton.tech/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bilton.tech/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://bilton.tech/getting-started
- group: operate
  title: ''
  type: Support
  url: https://bilton.tech/contact-us
- group: company
  title: ''
  type: Blog
  url: https://bilton.tech/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bilton.tech/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bilton.tech/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bilton.tech/privacy-policy
coverage:
  checked: '2026-09-28'
  detail: Documentation pages return HTML shells and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://bilton.tech/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BiltOn empowers construction owners and general contractors to streamline site operations, improve safety, reduce risk, and stay compliant. The AI‑powered platform offers crew safety visibility, risk compliance management, and integrated solutions for building loops, labor management, and site safety, delivering real‑time data and analytics across field, trailer, and office.
image: https://www.bilton.tech/wp-content/uploads/2026/01/logo.svg
layout: provider
modified: '2026-09-28'
name: BiltOn
nav: Providers
network: true
overview: 'BiltOn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Safety, Artificial Intelligence, Software-as-a-Service, and Platform.


  BiltOn''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bilton Domain Security
  slug: bilton-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bilton
tags:
- Construction
- Safety
- Artificial Intelligence
- Software-as-a-Service
- Platform
website: https://bilton.tech
---
