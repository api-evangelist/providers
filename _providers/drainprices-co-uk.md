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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://drainprices.co.uk/terms
- group: agent
  href: https://artifacts.apis.io/drainprices-co-uk/llms/drainprices-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drainprices-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/drainprices-co-uk/mcp/drainprices-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/drainprices-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/drainprices-co-uk/mcp/drainprices-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/drainprices-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/drainprices-co-uk/well-known/drainprices-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drainprices-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/drainprices-co-uk/well-known/drainprices-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drainprices-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/drainprices-co-uk/hosts/drainprices-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drainprices-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/drainprices-co-uk/vendors/drainprices-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drainprices-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drainprices.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drainprices.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/drainprices-co-uk/security/drainprices-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drainprices-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/drainprices-co-uk/security/drainprices-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drainprices-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drainprices.co.uk/
created: '2026-11-05'
description: Drain Prices provides up‑to‑date UK emergency drain unblocking cost data, offering price ranges for call‑outs, jetting, CCTV surveys and excavations. The site aggregates local contractor quotes, explains responsibility for blocked drains, and supplies a free data set for homeowners and professionals.
image: https://drainprices.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at drainprices.co.uk.
  name: Drain Prices MCP Server
  slug: drainprices-co-uk-mcp-yml
modified: '2026-11-05'
name: Drain Prices
nav: Providers
network: true
overview: Drain Prices is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Plumbing, Home Services, United Kingdom, Pricing, and Drainage.
random_paper: 16
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Drainprices Co Uk Domain Security
  slug: drainprices-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Drainprices Co Uk Vulnerability Disclosure
  slug: drainprices-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: drainprices-co-uk
tags:
- Plumbing
- Home Services
- United Kingdom
- Pricing
- Drainage
website: https://drainprices.co.uk/
---
