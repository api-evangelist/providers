---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolttech/refs/heads/main/security/bolttech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bolttech-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolttech/refs/heads/main/hosts/bolttech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bolttech-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolttech/refs/heads/main/vendors/bolttech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bolttech-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolttech/refs/heads/main/security/bolttech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bolttech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bolttech.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bolttech.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bolttech.io/get-started
- group: operate
  title: ''
  type: FAQ
  url: https://developers.bolttech.io/faqs
- group: operate
  title: ''
  type: Support
  url: mailto:dev-bolttechex-api@bolttech.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bolttech.io/privacy-notice-au/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolttech/refs/heads/main/authentication/bolttech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bolttech-authentication.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/bolttech/refs/heads/main/sandbox/bolttech-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bolttech-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolttech/refs/heads/main/security/bolttech-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bolttech-vulnerability-disclosure.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://bolttech.io
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: bolttech is a global insurtech running an embedded insurance exchange that connects insurers, distribution partners and customers. It operates a developer portal (Apigee integrated portal) with a free mock-data sandbox; the API catalogue and specifications are behind partner login.
image: https://bolttech.io/wp-content/uploads/2024/08/bolttech-OG-e1734627475705.png
layout: provider
modified: '2026-10-13'
name: bolttech
nav: Providers
network: true
overview: 'bolttech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Embedded Insurance, and Insurtech.


  bolttech''s developer surface includes getting-started guide, FAQ, support, authentication, sandbox, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 39.3
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 19.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bolttech Authentication
  slug: bolttech-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bolttech Domain Security
  slug: bolttech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bolttech Vulnerability Disclosure
  slug: bolttech-vulnerability-disclosure
  summary_line: contact published
slug: bolttech
tags:
- Company
- Insurance
- Embedded Insurance
- Insurtech
website: https://bolttech.io
---
