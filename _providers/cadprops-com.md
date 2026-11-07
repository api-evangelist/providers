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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cadprops-com/plans/cadprops-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cadprops-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cadprops-com/llms/cadprops-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cadprops-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cadprops-com/hosts/cadprops-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cadprops-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cadprops-com/vendors/cadprops-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cadprops-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cadprops.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cadprops.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cadprops.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cadprops.com/press/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cadprops.com/guides/
- group: auth
  href: https://artifacts.apis.io/cadprops-com/security/cadprops-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cadprops-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cadprops.com/
coverage:
  checked: '2026-11-03'
  detail: The provider's documentation pages are human-readable HTML but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract is published.
  evidence:
  - status: 404
    url: https://api.cadprops.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CADProps provides a multi-format CAD viewer and online measurement tools. Users can quickly view and measure SolidWorks, NX, Inventor, CATIA, Parasolid X_T, SAT, JT, STEP, IGES, and mesh formats directly in the browser. The service also offers file conversion and sharing via link with optional password protection. It aims to simplify 3D model inspection and collaboration without installing specialized software.
image: https://www.cadprops.com/assets/social/cad-guest-workflow.png
layout: provider
modified: '2026-11-03'
name: CADProps
nav: Providers
network: true
overview: 'CADProps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CAD, Viewer, 3D, Measurements, and Conversion.


  CADProps'' developer surface includes pricing, documentation, and 9 more developer resources.'
plans:
- name: Cadprops Com Plans Pricing
  plan_count: 3
  slug: cadprops-com-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 14.6
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
    discoverability: 49.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cadprops Com Domain Security
  slug: cadprops-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cadprops-com
tags:
- CAD
- Viewer
- 3D
- Measurements
- Conversion
website: https://cadprops.com/
---
