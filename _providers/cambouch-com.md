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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cambouch-com/plans/cambouch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cambouch-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cambouch-com/well-known/cambouch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cambouch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cambouch-com/hosts/cambouch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cambouch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cambouch-com/vendors/cambouch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cambouch-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cambouch.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cambouch.com/pricing
- group: auth
  href: https://artifacts.apis.io/cambouch-com/security/cambouch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cambouch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cambouch.com/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on api.cambouch.com
  evidence:
  - status: 0
    url: https://api.cambouch.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: StudioMotion provides animated graphic films, interactive 3D objects, optical visuals and interface effects through an MCP library for AI tools like Claude, Cursor, Lovable and ChatGPT. It offers a catalog of themes and motion‑graphics assets, pricing plans, and a sign‑in portal for creators. The platform showcases premium motion‑graphics, 3D showcases, and customizable visual effects for web and app experiences, targeting developers and designers seeking high‑quality motion assets.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_3qgz8g1tsz821bprgnb28yw9vw/1cd2489fead3101c85702344dac90295_1793035689947.png
layout: provider
modified: '2026-11-04'
name: StudioMotion
nav: Providers
network: true
overview: 'StudioMotion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  StudioMotion''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Cambouch Com Plans Pricing
  plan_count: 2
  slug: cambouch-com-plans-pricing
random_paper: 22
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cambouch Com Domain Security
  slug: cambouch-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cambouch-com
tags:
- Company
website: https://cambouch.com/
---
