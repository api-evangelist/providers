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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adm-cc/refs/heads/main/hosts/adm-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adm-cc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adm-cc/refs/heads/main/vendors/adm-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adm-cc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adm.cc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adm.cc/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://adm.cc/pricing
- group: start
  title: ''
  type: Login
  url: https://adm.cc/identity/account/login
- group: company
  title: ''
  type: Blog
  url: https://adm.cc/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adm-cc/refs/heads/main/security/adm-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adm-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adm.cc
- group: docs
  title: ''
  type: Documentation
  url: https://adm.cc/docs/google-ads-skill
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.adm.cc/mcp
  - status: 200
    url: https://adm.cc
  reason: partner-login
  state: gated
created: '2026-10-11'
description: ADM provides a remote MCP (Managed Customer Platform) for Google Ads accounts, enabling reading of campaigns and drafting of Search campaigns via a bearer token authentication. The service is accessed through the app.adm.cc domain and documentation is referenced at adm.cc/docs/google-ads-skill. Currently the API endpoints are limited to POST-only access and no public OpenAPI specification is available.
layout: provider
modified: '2026-10-11'
name: ADM
nav: Providers
network: true
overview: 'ADM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Google-Ads, and MCP.


  ADM''s developer surface includes pricing, engineering blog, documentation, and 7 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adm Cc Domain Security
  slug: adm-cc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adm-cc
tags:
- Company
- Advertising
- Marketing
- Google-Ads
- MCP
website: https://adm.cc
---
