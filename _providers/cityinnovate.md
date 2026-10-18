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
- description: Authorium provides a no-code AI‑enabled platform for government operations, including procurement, contract lifecycle, grants, legislative analysis, and budgeting.
  name: Authorium API
  slug: authorium-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://authorium.com/security-and-compliance/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cityinnovate/refs/heads/main/hosts/cityinnovate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cityinnovate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cityinnovate/refs/heads/main/vendors/cityinnovate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cityinnovate-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://authorium.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.authorium.com/portal/en/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authorium.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://authorium.com/team/
- group: company
  title: ''
  type: Blog
  url: https://authorium.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.authorium.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cityinnovate/refs/heads/main/security/cityinnovate-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cityinnovate-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cityinnovate/refs/heads/main/security/cityinnovate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cityinnovate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authorium.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://authorium.com
  - status: 403
    url: https://equityzen.com/company/cityinnovate
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Cityinnovate, now operating under the brand Authorium, provides a no-code AI‑enabled platform for government operations. The solution streamlines procurement, contract lifecycle management, grants, legislative analysis, and budget requests, offering modular, configurable tools to improve transparency and efficiency in public sector projects. Built as a public benefit company, Authorium claims to manage over $50 billion in government projects and aims to reduce process times by up to 15 business days.
image: https://authorium.com/wp-content/uploads/2026/04/DOH-Dashboard.png
layout: provider
modified: '2026-10-08'
name: Cityinnovate
nav: Providers
network: true
overview: 'Cityinnovate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government, No-Code, Artificial Intelligence, Platform, and Public-benefit.


  Cityinnovate''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cityinnovate Domain Security
  slug: cityinnovate-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Cityinnovate Trust Center
  slug: cityinnovate-trust-center
  summary_line: HIPAA, FedRAMP, FIPS 140
slug: cityinnovate
tags:
- Government
- No-Code
- Artificial Intelligence
- Platform
- Public-benefit
website: https://authorium.com
---
