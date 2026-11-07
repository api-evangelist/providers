---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/abcommunity-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/abcommunity-org/llms/abcommunity-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abcommunity-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/abcommunity-org/well-known/abcommunity-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abcommunity-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/abcommunity-org/hosts/abcommunity-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abcommunity-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/abcommunity-org/vendors/abcommunity-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abcommunity-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/abcommunity-org/security/abcommunity-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abcommunity-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abcommunity.org/
coverage:
  checked: '2026-10-31'
  detail: The provider's website returns a JavaScript shell with no machine-readable API documentation.
  evidence:
  - status: 200
    url: https://abcommunity.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: AI Builders Community is an Azerbaijani platform that brings together developers, researchers, and enthusiasts building artificial intelligence solutions. The community provides a forum for sharing projects, resources, events, and a community dashboard, fostering collaboration among AI builders across Azerbaijan and beyond. It serves as a hub for learning, networking, and showcasing AI-driven initiatives.
image: https://abcommunity.org/uploads/default/optimized/1X/0bb2c0fa95aa539e7cf7103ef3c47ba050ce224e_2_32x32.png
layout: provider
modified: '2026-10-31'
name: AI Builders Community
nav: Providers
network: true
overview: AI Builders Community is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Community, Builders, Azerbaijan, and Platform.
random_paper: 5
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - azerbaijan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 5.5
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abcommunity Org Domain Security
  slug: abcommunity-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: abcommunity-org
tags:
- Artificial Intelligence
- Community
- Builders
- Azerbaijan
- Platform
website: https://abcommunity.org/
---
