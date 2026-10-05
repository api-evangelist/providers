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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bluetrace/refs/heads/main/well-known/bluetrace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluetrace-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluetrace/refs/heads/main/hosts/bluetrace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluetrace-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluetrace/refs/heads/main/vendors/bluetrace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluetrace-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blue-trace.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blue-trace.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.blue-trace.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://help.blue-trace.com/knowledge/how-do-i-setup-quantities-for-my-items
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluetrace/refs/heads/main/security/bluetrace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluetrace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blue-trace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.blue-trace.com/knowledge
- group: company
  title: ''
  type: Blog
  url: https://blog.blue-trace.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blue-trace.com/get-a-demo
- group: start
  title: ''
  type: SignUp
  url: https://app.blue-trace.com/login
coverage:
  checked: '2026-09-29'
  detail: Documentation is provided as HTML pages without any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://help.blue-trace.com/knowledge
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: BlueTrace provides a cloud‑based platform that streamlines seafood supply‑chain operations, offering tools for inventory management, order processing, pricing, traceability, and compliance. Their solution connects distributors, processors, and retailers, enabling real‑time data sharing, automated invoicing, and analytics to improve efficiency and sustainability across the seafood industry.
image: https://www.blue-trace.com/hubfs/162bb25f-5940-435d-9eb5-af8db4339105%202.jpg
layout: provider
modified: '2026-09-29'
name: BlueTrace
nav: Providers
network: true
overview: 'BlueTrace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Seafood, Supply Chain, Software-as-a-Service, and Traceability.


  BlueTrace''s developer surface includes getting-started guide, documentation, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluetrace Domain Security
  slug: bluetrace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluetrace
tags:
- Company
- Seafood
- Supply Chain
- Software-as-a-Service
- Traceability
website: https://www.blue-trace.com/
---
