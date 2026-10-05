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
  href: https://raw.githubusercontent.com/api-evangelist/boost-payment-solutions/refs/heads/main/hosts/boost-payment-solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boost-payment-solutions-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boost-payment-solutions/refs/heads/main/vendors/boost-payment-solutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boost-payment-solutions-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.boostb2b.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boost-payment-solutions/refs/heads/main/security/boost-payment-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boost-payment-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boostb2b.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.boostb2b.com/insights
- group: company
  title: ''
  type: Blog
  url: https://www.boostb2b.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boostb2b.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boostb2b.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.boostb2b.com/customer-support-form
coverage:
  checked: '2026-10-02'
  detail: Boost Payment Solutions provides HTML documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.boostb2b.com/insights
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Boost Payment Solutions provides a comprehensive suite of B2B payment solutions, including commercial card processing, virtual card payments, and AP/AR automation. Founded in 2009, the company serves global enterprises across 180+ countries, offering patented technologies such as Boost 100, Boost Intercept, and Dynamic Boost to optimize payment efficiency, security, and data insights.
layout: provider
modified: '2026-10-02'
name: Boost Payment Solutions
nav: Providers
network: true
overview: 'Boost Payment Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, B2B, and Commercial Cards.


  Boost Payment Solutions'' developer surface includes documentation, engineering blog, support, and 7 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boost Payment Solutions Domain Security
  slug: boost-payment-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boost-payment-solutions
tags:
- Company
- Payments
- Fintech
- B2B
- Commercial Cards
website: https://www.boostb2b.com/
---
