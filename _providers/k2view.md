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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.k2view.com/security/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/k2view/refs/heads/main/hosts/k2view-hosts.yml
  title: ''
  type: Hosts
  url: hosts/k2view-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/k2view/refs/heads/main/vendors/k2view-vendors.yml
  title: ''
  type: Vendors
  url: vendors/k2view-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.k2view.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.k2view.com/
- group: auth
  title: ''
  type: Security
  url: https://www.k2view.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.k2view.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.k2view.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.k2view.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/k2view/refs/heads/main/security/k2view-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/k2view-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/k2view/refs/heads/main/security/k2view-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/k2view-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.k2view.com
coverage:
  checked: '2026-10-03'
  detail: No public developer program or API documentation found on api.k2view.com.
  evidence:
  - status: 0
    url: https://api.k2view.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Turn fragmented enterprise data into reusable data products that power AI, operational systems, and downstream analytics without rebuilding pipelines. K2view provides a Data Product Platform, AI Context Platform, and Micro‑Database technology to enable data integration, virtualization, and data‑as‑a‑service automation for enterprises.
layout: provider
modified: '2026-10-03'
name: K2view
nav: Providers
network: true
overview: 'K2view is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Data Platform, Artificial Intelligence, and Enterprise.


  K2view''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: K2View Domain Security
  slug: k2view-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: K2View Trust Center
  slug: k2view-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, FIPS 140
slug: k2view
tags:
- Company
- Data Integration
- Data Platform
- Artificial Intelligence
- Enterprise
website: https://www.k2view.com
---
