---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/internxt/cli/internxt-cli.yml
  title: ''
  type: CLI
  url: cli/internxt-cli.yml
- group: agent
  href: https://artifacts.apis.io/internxt/llms/internxt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/internxt-llms.txt
- group: auth
  href: https://artifacts.apis.io/internxt/well-known/internxt-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/internxt-help-security.txt
- group: agent
  href: https://artifacts.apis.io/internxt/well-known/internxt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/internxt-well-known.yml
- group: other
  href: https://artifacts.apis.io/internxt/hosts/internxt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/internxt-hosts.yml
- group: other
  href: https://artifacts.apis.io/internxt/vendors/internxt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/internxt-vendors.yml
- group: auth
  href: https://artifacts.apis.io/internxt/security/internxt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/internxt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://internxt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://internxt.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.internxt.com/
- group: operate
  title: ''
  type: Support
  url: https://help.internxt.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://internxt.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://internxt.com/legal
coverage:
  checked: '2026-10-28'
  detail: Internxt's help center provides markdown documentation but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts are publicly available.
  evidence:
  - status: 404
    url: https://help.internxt.com/openapi.json
  - status: 500
    url: https://api.internxt.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Internxt provides encrypted cloud storage and a suite of privacy‑focused services including Drive, Antivirus, VPN, Cleaner, Mail and Send. Based in Europe, it offers zero‑knowledge encryption, open‑source audits and a commitment to sustainability, targeting individuals and enterprises seeking secure, private data storage.
image: https://internxt.com/images/previewLink/PreviewGenericEN.png
layout: provider
modified: '2026-10-28'
name: Internxt
nav: Providers
network: true
overview: 'Internxt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Storage, Encryption, Privacy, and Europe.


  Internxt''s developer surface includes CLI, documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 4
scopes:
- name: Internxt Scopes
  scope_count: 0
  slug: internxt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 18
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
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Internxt Authentication
  slug: internxt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Internxt Domain Security
  slug: internxt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: internxt
tags:
- Company
- Cloud Storage
- Encryption
- Privacy
- Europe
website: https://internxt.com/
---
