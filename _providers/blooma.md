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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blooma/refs/heads/main/hosts/blooma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blooma-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blooma/refs/heads/main/vendors/blooma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blooma-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blooma.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.blooma.ai/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blooma.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blooma.ai/plans
- group: company
  title: ''
  type: Blog
  url: https://www.blooma.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.blooma.ai/hc/en-us/categories/360003482493-Getting-Started
- group: docs
  title: ''
  type: Documentation
  url: https://help.blooma.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blooma/refs/heads/main/security/blooma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blooma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blooma.ai
coverage:
  checked: '2026-09-29'
  detail: Blooma provides a help center but no machine‑readable API spec was found.
  evidence:
  - status: 404
    url: https://api.blooma.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blooma is an AI‑powered commercial real‑estate (CRE) lending platform that provides data‑driven origination, portfolio intelligence, and workflow automation solutions for lenders. The company helps lenders make faster, data‑driven decisions, monitor portfolios with real‑time alerts, and integrate data sources to streamline CRE lending operations.
layout: provider
modified: '2026-09-29'
name: Blooma
nav: Providers
network: true
overview: 'Blooma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Commercial Real Estate, Lending, and Data Automation.


  Blooma''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blooma Domain Security
  slug: blooma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blooma
tags:
- Company
- Artificial Intelligence
- Commercial Real Estate
- Lending
- Data Automation
- Portfolio Management
website: https://www.blooma.ai
---
