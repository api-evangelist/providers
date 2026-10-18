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
- description: Mainframe productivity solutions API (TelTape, Superuser, Co‑Pilot, Speedview, zTrustfer)
  name: Cartagena API
  slug: cartagena-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cartagena/refs/heads/main/hosts/cartagena-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cartagena-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cartagena/refs/heads/main/vendors/cartagena-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cartagena-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cartagena/refs/heads/main/security/cartagena-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cartagena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cartagena.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cartagena.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://cartagena.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://cartagena.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cartagena.com/terms-and-privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cartagena.com/terms-and-privacy/
coverage:
  checked: '2026-10-07'
  detail: The provider's website offers HTML documentation but no discoverable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://cartagena.com/about-us/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cartagena Software Limited provides system productivity solutions for IBM z/OS mainframe environments. With over 25 years of experience, they offer a portfolio of tools such as TelTape, Superuser, Co‑Pilot, Speedview, and zTrustfer, enabling secure data transfer, tape migration, automation, and reporting. Their services include professional consulting, support, and partnerships with leading technology vendors, helping enterprises maximize value and minimize risk across global operations.
layout: provider
modified: '2026-10-07'
name: Cartagena
nav: Providers
network: true
overview: 'Cartagena is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mainframe, z/OS, Data Transfer, Tape Migration, and System Automation.


  Cartagena''s developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cartagena Domain Security
  slug: cartagena-domain-security
  summary_line: TLSv1.3
slug: cartagena
tags:
- Mainframe
- z/OS
- Data Transfer
- Tape Migration
- System Automation
- Security Administration
- Report Management
website: https://cartagena.com/
---
