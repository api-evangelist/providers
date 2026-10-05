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
  href: https://raw.githubusercontent.com/api-evangelist/andrena/refs/heads/main/hosts/andrena-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andrena-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/andrena/refs/heads/main/vendors/andrena-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andrena-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://andrena.com/account/login/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.andrena.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/andrena/refs/heads/main/security/andrena-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andrena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://andrena.com
- group: docs
  title: ''
  type: Documentation
  url: https://andrena.com/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://andrena.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://andrena.com/privacypolicy/
- group: operate
  title: ''
  type: Support
  url: https://andrena.com/contact/
coverage:
  checked: 2026-09-24
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on api.andrena.com or dev.andrena.com.
  evidence:
  - status: 404
    url: https://dev.andrena.com/openapi.json
  - status: 404
    url: https://dev.andrena.com/swagger.json
  - status: 0
    url: https://api.andrena.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Andrena provides high-speed wireless internet service to multi-tenant buildings, businesses, and households at affordable rates. Founded to make internet accessible for everyone, Andrena offers plans up to 1 Gbps with simple sign‑up, no installation delays, and a focus on customer experience. The company emphasizes data privacy, network management policies, and community support, aiming to deliver reliable connectivity across residential and commercial properties.
layout: provider
modified: '2026-09-24'
name: Andrena
nav: Providers
network: true
overview: 'Andrena is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Internet, Wireless, Broadband, and Residential.


  Andrena''s developer surface includes documentation, support, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Andrena Domain Security
  slug: andrena-domain-security
  summary_line: TLSv1.3 · DMARC
slug: andrena
tags:
- Company
- Internet
- Wireless
- Broadband
- Residential
- Business
website: https://andrena.com
---
