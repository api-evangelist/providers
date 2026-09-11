---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activeon8016-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.activon-global.com/
- group: company
  title: ''
  type: Website
  url: https://www.activon.kr/
- group: company
  title: ''
  type: Blog
  url: https://www.activon-global.com/blog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/activeon8016-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/activeon8016-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/activeon8016-conformance.yml
created: '2026-09-06'
description: 'ACTIVON Co., Ltd. (엑티브온) is a South Korean green-biotechnology materials company founded in 2009 and headquartered in Suwon, Gyeonggi-do, that develops and manufactures cosmetic ingredients and micro-encapsulation technology — skin-safe preservative alternatives, multifunctional actives, emollients, humectants and bio-converted ingredients — alongside functional pigment lines (EnergiON heat-storage, Thermon thermochromic, Photon, Fragron, Memorion, MultiON) sold into textiles, coatings, plastics and cosmetics. It is a specialty-materials manufacturer, not a software vendor: it publishes no developer portal, no API reference and no machine-readable API contract. Its only machine-readable agent surface is the Wix-platform site MCP endpoint and llms.txt served on its corporate site, both probed live by API Evangelist.'
image: https://www.activon.kr/assets/images/common/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Wix site MCP endpoint (platform-provided, live)
  slug: wix-site-mcp-endpoint-platform-provided-live
modified: '2026-09-06'
name: ACTIVON Co., Ltd.
nav: Providers
network: true
overview: 'ACTIVON Co., Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cosmetics, Chemicals, Ingredients, and Materials.


  ACTIVON Co., Ltd.''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Activeon8016 Plans Pricing
  plan_count: 0
  slug: activeon8016-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Activeon8016 Rate Limits
  slug: activeon8016-rate-limits
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 8.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Activeon8016 Domain Security
  slug: activeon8016-domain-security
  summary_line: TLSv1.3 · HSTS
slug: activeon8016
tags:
- Company
- Cosmetics
- Chemicals
- Ingredients
- Materials
- Manufacturing
- Biotechnology
- Micro-Encapsulation
- Pigments
- South Korea
website: https://www.activon-global.com/
---
