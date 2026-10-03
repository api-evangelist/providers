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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.atolio.com/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atolio/refs/heads/main/hosts/atolio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atolio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atolio/refs/heads/main/vendors/atolio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atolio-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.atolio.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.atolio.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atolio.com/configuration/sources/google/gmail/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atolio
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atolio/refs/heads/main/security/atolio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/atolio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atolio/refs/heads/main/security/atolio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atolio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atolio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atolio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.atolio.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atolio.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atolio.com/msa
- group: operate
  title: ''
  type: Support
  url: https://www.atolio.com/contact
coverage:
  checked: 2026-09-26
  detail: Documentation is available at https://docs.atolio.com/ but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://docs.atolio.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atolio delivers an AI‑powered enterprise search platform that enables organizations to securely index and retrieve data across cloud and on‑premise sources. It offers self‑hosted deployment, sovereign data control, and integrations with tools like Atlassian, GitHub, Google Workspace, and Microsoft services, empowering teams in sales, support, engineering, and more to find critical information instantly.
image: https://cdn.prod.website-files.com/66ad62d99d312335962805ce/66adc585116dfcb0fd9e5cd3_atolio-opengraph.png
layout: provider
modified: '2026-09-26'
name: Atolio
nav: Providers
network: true
overview: 'Atolio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Enterprise Search, Data Security, Integration, and Software-as-a-Service.


  Atolio''s developer surface includes getting-started guide, documentation, engineering blog, support, and 11 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atolio Domain Security
  slug: atolio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Atolio Trust Center
  slug: atolio-trust-center
  summary_line: HIPAA, GDPR
slug: atolio
tags:
- Artificial Intelligence
- Enterprise Search
- Data Security
- Integration
- Software-as-a-Service
website: https://www.atolio.com/
---
