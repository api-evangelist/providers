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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/askatria-ai/plans/askatria-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askatria-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/askatria-ai/llms/askatria-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askatria-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/askatria-ai/well-known/askatria-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askatria-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/askatria-ai/hosts/askatria-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askatria-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/askatria-ai/vendors/askatria-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askatria-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askatria.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askatria.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://askatria.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://askatria.ai/sign-in
- group: docs
  title: ''
  type: APIReference
  url: https://askatria.ai/dashboard/scout/agents/reference
- group: auth
  href: https://artifacts.apis.io/askatria-ai/security/askatria-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askatria-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askatria.ai/
coverage:
  checked: '2026-11-01'
  detail: API reference page at https://askatria.ai/api returns HTML rendered by JavaScript with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://askatria.ai/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Atria provides site intelligence for teams and AI, offering AI‑driven analysis of land acquisition, zoning, permitting, and feasibility studies across the United States. Their platform scores sites, aggregates parcel data, and enables agents to query the Atria MCP server for detailed insights, supporting developers, consultants, and government agencies in making data‑informed decisions.
image: https://askatria.ai/og-card.png
layout: provider
modified: '2026-11-01'
name: Atria
nav: Providers
network: true
overview: 'Atria is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Land-Intelligence, Site Selection, and Zoning.


  Atria''s developer surface includes pricing, API reference, and 10 more developer resources.'
plans:
- name: Askatria Ai Plans Pricing
  plan_count: 4
  slug: askatria-ai-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 22.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askatria Ai Domain Security
  slug: askatria-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askatria-ai
tags:
- Company
- Artificial Intelligence
- Land-Intelligence
- Site Selection
- Zoning
website: https://askatria.ai/
---
