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
- description: Developer portal for Capango offering API documentation and integration guides.
  name: Capango Developer Portal
  slug: capango-developer-portal
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/capango/refs/heads/main/plans/capango-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capango-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capango/refs/heads/main/llms/capango-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capango-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capango/refs/heads/main/well-known/capango-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capango-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capango/refs/heads/main/well-known/capango-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capango-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capango/refs/heads/main/hosts/capango-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capango-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capango/refs/heads/main/vendors/capango-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capango-vendors.yml
- group: operate
  title: ''
  type: Support
  url: http://help.capango.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.capango.com/privacy.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.capango.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capango/refs/heads/main/security/capango-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capango-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capango.com/
coverage:
  checked: '2026-10-06'
  detail: Documentation is public but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://dev.capango.com/
  - status: 200
    url: http://help.capango.com/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Capango provides a hiring suite for the service economy, offering employer portals, seeker mobile apps, a job board, and a Job Launchpad for first‑time workers. It connects employers and hourly workers in retail, restaurants, and hospitality, enabling posting, screening, interviewing, and hiring through a unified platform available in English, Spanish, and French.
image: https://www.capango.com/og-image.png
layout: provider
modified: '2026-10-06'
name: Capango
nav: Providers
network: true
overview: 'Capango is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hiring, Workforce, Software-as-a-Service, and ServiceEconomy.


  Capango''s developer surface includes support, documentation, and 9 more developer resources.'
plans:
- name: Capango Plans Pricing
  plan_count: 3
  slug: capango-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capango Domain Security
  slug: capango-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capango
tags:
- Company
- Hiring
- Workforce
- Software-as-a-Service
- ServiceEconomy
website: https://capango.com/
---
