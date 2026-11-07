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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only analysis tool that scans Google Ads search terms to identify wasteful spend.
  name: Ads MCP API
  slug: ads-mcp-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/adsmcp-dev/llms/adsmcp-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adsmcp-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/adsmcp-dev/well-known/adsmcp-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adsmcp-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/adsmcp-dev/hosts/adsmcp-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adsmcp-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/adsmcp-dev/vendors/adsmcp-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adsmcp-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adsmcp-dev/security/adsmcp-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adsmcp-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adsmcp.dev/
- group: company
  title: ''
  type: Blog
  url: https://adsmcp.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adsmcp.dev/#pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://adsmcp.dev/#connect
- group: operate
  title: ''
  type: Support
  url: mailto:support@adsmcp.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adsmcp.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adsmcp.dev/privacy
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint requires authentication (401) and no public contract is available.
  evidence:
  - status: 401
    url: https://adsmcp.dev/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Ads MCP provides a read‑only analysis tool that scans your Google Ads search terms and identifies wasteful spend. Users can paste a report into AI assistants like ChatGPT or Claude to ask plain‑language questions such as “Where am I wasting money?”. The service never modifies campaigns and requires only read‑only access to Google Ads, ensuring safety. It offers a free check with no sign‑up, and paid pricing plans for higher volume. Detailed explanations of each cost‑driving query are provided.
image: https://adsmcp.dev/favicon.svg
layout: provider
modified: '2026-10-31'
name: Ads MCP
nav: Providers
network: true
overview: 'Ads MCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Artificial Intelligence, Google Ads, Cost Optimization, and MCP.


  Ads MCP''s developer surface includes engineering blog, pricing, getting-started guide, support, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 16.3
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
  name: Adsmcp Dev Domain Security
  slug: adsmcp-dev-domain-security
  summary_line: TLSv1.3
slug: adsmcp-dev
tags:
- Advertising
- Artificial Intelligence
- Google Ads
- Cost Optimization
- MCP
website: https://adsmcp.dev/
---
