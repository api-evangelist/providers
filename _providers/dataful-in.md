---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Dataful provides public data APIs accessible via their platform.
  name: Dataful API
  slug: dataful-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dataful-in/plans/dataful-in-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataful-in-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/dataful-in/hosts/dataful-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataful-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataful-in/vendors/dataful-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataful-in-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/factly
- group: auth
  href: https://artifacts.apis.io/dataful-in/security/dataful-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataful-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataful.in/
- group: commercial
  title: ''
  type: Pricing
  url: https://dataful.in/plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataful.in/terms-and-conditions/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://api.dataful.in/openapi.json
  - status: 404
    url: https://dataful.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Dataful provides a platform that makes working with public data easy, fast, and simple. It offers datasets, collections, sector data, and AI‑powered products, enabling users to explore, analyze, and integrate public information across districts, HFIs, and other domains. The service includes a showcase, pricing plans, and various insights tools, all built to streamline data access for developers and analysts.
image: https://images.factly.in/mande/assets/open_graph.png
layout: provider
modified: '2026-11-04'
name: Dataful
nav: Providers
network: true
overview: 'Dataful is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Public Data, and Datasets.


  Dataful''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Dataful In Plans Pricing
  plan_count: 8
  slug: dataful-in-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dataful In Domain Security
  slug: dataful-in-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: dataful-in
tags:
- Company
- Data
- Public Data
- Datasets
website: https://dataful.in/
---
