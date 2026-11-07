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
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Deer Supply services, documented at the Learn page.
  name: Deer Supply API
  slug: deer-supply-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/deer-supply/llms/deer-supply-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deer-supply-llms.txt
- group: agent
  href: https://artifacts.apis.io/deer-supply/mcp/deer-supply-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deer-supply-mcp.yml
- group: agent
  href: https://artifacts.apis.io/deer-supply/well-known/deer-supply-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deer-supply-well-known.yml
- group: other
  href: https://artifacts.apis.io/deer-supply/hosts/deer-supply-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deer-supply-hosts.yml
- group: other
  href: https://artifacts.apis.io/deer-supply/vendors/deer-supply-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deer-supply-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deer.supply/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://deer.supply/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deer.supply/legal/privacy
- group: auth
  href: https://artifacts.apis.io/deer-supply/security/deer-supply-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deer-supply-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deer.supply/
coverage:
  checked: '2026-11-05'
  detail: Provider documentation is public but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or MCP spec could be retrieved.
  evidence:
  - status: 405
    url: https://deer.supply/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Deer Supply & Research is a Canadian supplier of GLP‑1 weight‑loss medications such as Retatrutide, Tirzepatide, and Semaglutide, offered as pre‑filled, ready‑to‑use pens, along with recovery peptides and ancillary capsules. They ship discreetly across Canada, emphasizing consistent quality, regulatory compliance, and customer support in both English and French. The company also provides lab results, detailed product information, and a research blog for health‑focused consumers.
image: https://deer.supply/assets/og-cover.png
layout: provider
mcp_servers:
- description: Remote MCP server at deer.supply.
  name: Deer Supply & Research MCP Server
  slug: deer-supply-mcp-yml
modified: '2026-11-05'
name: Deer Supply & Research
nav: Providers
network: true
overview: 'Deer Supply & Research is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Pharmaceuticals, Weight Loss, Canada, and Peptides.


  Deer Supply & Research''s developer surface includes support and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deer Supply Domain Security
  slug: deer-supply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deer-supply
tags:
- Health
- Pharmaceuticals
- Weight Loss
- Canada
- Peptides
website: https://deer.supply/
---
