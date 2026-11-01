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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/eplane/llms/eplane-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eplane-llms.txt
- group: other
  href: https://artifacts.apis.io/eplane/hosts/eplane-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eplane-hosts.yml
- group: other
  href: https://artifacts.apis.io/eplane/vendors/eplane-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eplane-vendors.yml
- group: auth
  href: https://artifacts.apis.io/eplane/security/eplane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eplane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eplane.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.eplane.ai/news
- group: operate
  title: ''
  type: Support
  url: https://www.eplane.ai/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://www.eplane.ai/about
coverage:
  checked: '2026-10-29'
  detail: The provider's website returns HTML but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract files were found at common spec endpoints.
  evidence:
  - status: 200
    url: https://www.eplane.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: ePlane is an Indian aerospace startup developing compact electric vertical take‑off and landing (eVTOL) aircraft for air‑ambulance, air‑taxi, and air‑cargo services. Their flagship e200X platform offers a 3‑passenger cabin, 110 km range, 250 km/h cruise speed, and zero‑emission operation from existing helipads. Founded in 2019 within the IIT Madras incubation cell, ePlane holds a global patent portfolio and has secured DGCA Type Certification approval, positioning it as a leading player in the emerging urban air mobility market.
image: https://www.eplane.ai/opengraph-image.jpg?opengraph-image.0znny89ak1hwz.jpg
layout: provider
modified: '2026-10-29'
name: ePlane
nav: Providers
network: true
overview: 'ePlane is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, eVTOL, Air Taxi, and Air Ambulance.


  ePlane''s developer surface includes engineering blog, support, getting-started guide, and 5 more developer resources.'
plans:
- name: Eplane Plans Pricing
  plan_count: 0
  slug: eplane-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Eplane Rate Limits
  slug: eplane-rate-limits
scopes:
- name: Eplane Scopes
  scope_count: 0
  slug: eplane-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eplane Authentication
  slug: eplane-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Eplane Domain Security
  slug: eplane-domain-security
  summary_line: TLSv1.3 · HSTS
slug: eplane
tags:
- Company
- Aviation
- eVTOL
- Air Taxi
- Air Ambulance
- Air Cargo
website: https://www.eplane.ai/
---
