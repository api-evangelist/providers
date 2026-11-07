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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/canalnav-com/plans/canalnav-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canalnav-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/canalnav-com/llms/canalnav-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canalnav-com-llms.txt
- group: other
  href: https://artifacts.apis.io/canalnav-com/hosts/canalnav-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canalnav-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canalnav-com/vendors/canalnav-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canalnav-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canalnav.com/terms/
- group: docs
  title: ''
  type: Documentation
  url: https://canalnav.com/guides/
- group: auth
  href: https://artifacts.apis.io/canalnav-com/security/canalnav-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canalnav-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canalnav.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://canalnav.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canalnav.com/privacy/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite public documentation pages.
  evidence:
  - status: 404
    url: https://api.canalnav.com/openapi.json
  - status: 404
    url: https://api.canalnav.com/openapi.yaml
  - status: 404
    url: https://api.canalnav.com/v1/openapi.json
  - status: 404
    url: https://api.canalnav.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Canal Nav is a free route planner and live map for the UK’s canals and rivers, providing boaters with tools to plan cruises, work through locks, and explore waterways. The service offers real‑time navigation, route optimization, and open data integrations to help users enjoy the canal network safely and efficiently.
image: https://canalnav.com/app/uploads/2026/07/canalnav-og.png
layout: provider
modified: '2026-11-04'
name: Canal Nav
nav: Providers
network: true
overview: 'Canal Nav is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Navigation, Boating, UK Canals, Route Planner, and Open Data.


  Canal Nav''s developer surface includes documentation, pricing, and 8 more developer resources.'
plans:
- name: Canalnav Com Plans Pricing
  plan_count: 5
  slug: canalnav-com-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Canalnav Com Domain Security
  slug: canalnav-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: canalnav-com
tags:
- Navigation
- Boating
- UK Canals
- Route Planner
- Open Data
website: https://canalnav.com/
---
