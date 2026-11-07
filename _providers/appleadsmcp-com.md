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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/appleadsmcp-com/llms/appleadsmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appleadsmcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/appleadsmcp-com/well-known/appleadsmcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appleadsmcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/appleadsmcp-com/hosts/appleadsmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appleadsmcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appleadsmcp-com/vendors/appleadsmcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appleadsmcp-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://appleadsmcp.com/register
- group: auth
  href: https://artifacts.apis.io/appleadsmcp-com/security/appleadsmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appleadsmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appleadsmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://appleadsmcp.com/docs/queries
- group: commercial
  title: ''
  type: Pricing
  url: https://appleadsmcp.com/tools
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appleadsmcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appleadsmcp.com/privacy
coverage:
  checked: '2026-11-01'
  detail: The provider's documentation is public but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published; attempts to fetch common spec URLs on the API host returned HTTP 525 errors.
  evidence:
  - status: 525
    url: https://api.appleadsmcp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Apple Search Ads MCP provides a programmatic interface for accessing Apple Search Ads data. It enables AI agents and applications to query campaign performance, keyword analysis, and spend metrics through natural language queries. The platform offers tools, workflows, and pricing plans for marketers, agencies, and growth teams to integrate Apple Ads data into their automation pipelines.
layout: provider
modified: '2026-11-01'
name: Apple Search Ads MCP
nav: Providers
network: true
overview: 'Apple Search Ads MCP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Apple, Search Ads, MCP, Artificial Intelligence, and Advertising.


  Apple Search Ads MCP''s developer surface includes signup flow, documentation, pricing, and 8 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 15.8
  provenance:
    mcp: derived
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
  name: Appleadsmcp Com Domain Security
  slug: appleadsmcp-com-domain-security
  summary_line: TLSv1.3
slug: appleadsmcp-com
tags:
- Apple
- Search Ads
- MCP
- Artificial Intelligence
- Advertising
website: https://appleadsmcp.com/
---
