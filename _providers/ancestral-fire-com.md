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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The AncestralFire MCP server: its address, how sign-in works, every tool it offers and what each one does, its cards, its limits and its privacy rules.'
  name: AncestralFire MCP
  slug: ancestralfire-mcp
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/ancestral-fire-com/plans/ancestral-fire-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ancestral-fire-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/ancestral-fire-com/security/ancestral-fire-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ancestral-fire-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/ancestral-fire-com/llms/ancestral-fire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ancestral-fire-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ancestral-fire-com/mcp/ancestral-fire-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ancestral-fire-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ancestral-fire-com/well-known/ancestral-fire-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ancestral-fire-com-security.txt
- group: agent
  href: https://artifacts.apis.io/ancestral-fire-com/well-known/ancestral-fire-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ancestral-fire-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ancestral-fire-com/hosts/ancestral-fire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ancestral-fire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ancestral-fire-com/vendors/ancestral-fire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ancestral-fire-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ancestral-fire.com/guides
- group: auth
  href: https://artifacts.apis.io/ancestral-fire-com/security/ancestral-fire-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ancestral-fire-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ancestral-fire-com/security/ancestral-fire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ancestral-fire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ancestral-fire.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://ancestral-fire.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://ancestral-fire.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://ancestral-fire.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ancestral-fire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ancestral-fire.com/privacy
coverage:
  checked: '2026-11-01'
  detail: Documentation is public but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found.
  evidence:
  - status: 404
    url: https://ancestral-fire.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AncestralFire is an AI‑powered genealogy platform that lets users import their family tree from FamilySearch or upload a genealogy file, then explore each ancestor’s life story, view historical context, and discover missing connections. The service presents facts with source citations, offers interactive maps and timelines, and prompts users for clarification when records are ambiguous. It aims to make family history research accessible, transparent, and engaging for anyone interested in their heritage.
image: https://ancestral-fire.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at ancestral-fire.com.
  name: AncestralFire MCP Server
  slug: ancestral-fire-com-mcp-yml
modified: '2026-11-01'
name: AncestralFire
nav: Providers
network: true
overview: 'AncestralFire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Genealogy, Family Tree, Ancestry, Artificial Intelligence, and History.


  AncestralFire''s developer surface includes documentation, getting-started guide, support, pricing, and 13 more developer resources.'
plans:
- name: Ancestral Fire Com Plans Pricing
  plan_count: 3
  slug: ancestral-fire-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    mcp: first-party
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
  name: Ancestral Fire Com Domain Security
  slug: ancestral-fire-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ancestral Fire Com Vulnerability Disclosure
  slug: ancestral-fire-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ancestral-fire-com
tags:
- Genealogy
- Family Tree
- Ancestry
- Artificial Intelligence
- History
website: https://ancestral-fire.com/
---
