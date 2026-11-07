---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/absolutebestair-com/llms/absolutebestair-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/absolutebestair-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/absolutebestair-com/mcp/absolutebestair-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/absolutebestair-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/absolutebestair-com/hosts/absolutebestair-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/absolutebestair-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.absolutebestair.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.absolutebestair.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.absolutebestair.com/about/team
- group: company
  title: ''
  type: Blog
  url: https://www.absolutebestair.com/blog
- group: auth
  href: https://artifacts.apis.io/absolutebestair-com/security/absolutebestair-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/absolutebestair-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://absolutebestair.com/
coverage:
  checked: '2026-10-31'
  detail: All attempted OpenAPI spec URLs returned redirects to 404 and the MCP endpoint was rate‑limited, providing no machine‑readable contract.
  evidence:
  - status: 301
    url: https://absolutebestair.com/openapi.json
  - status: 404
    url: https://www.absolutebestair.com/openapi.json
  - status: 429
    url: https://absolutebestair.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Absolute Best Air Inc. is a family‑owned HVAC repair, installation and maintenance company serving Henry County and South Metro Atlanta. Founded in 2009 by third‑generation HVAC professional David Longino, the business offers heating, cooling, indoor air quality, and light commercial services. They provide 24/7 emergency service, AI‑assisted diagnostics, and serve residential and light‑commercial customers across McDonough, Stockbridge, and surrounding cities. Their mission is to deliver reliable climate‑control solutions with a focus on customer service and advanced technology.
image: https://www.absolutebestair.com/aba-official-share-logo.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at absolutebestair.com.
  name: Absolute Best Air MCP Server
  slug: absolutebestair-com-mcp-yml
modified: '2026-10-31'
name: Absolute Best Air
nav: Providers
network: true
overview: 'Absolute Best Air is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Heating, Cooling, Air Quality, and Georgia.


  Absolute Best Air''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Absolutebestair Com Plans Pricing
  plan_count: 0
  slug: absolutebestair-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Absolutebestair Com Rate Limits
  slug: absolutebestair-com-rate-limits
scopes:
- name: Absolutebestair Com Scopes
  scope_count: 0
  slug: absolutebestair-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.2
    operational_transparency: 0.0
  previous_composite: 11.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Absolutebestair Com Authentication
  slug: absolutebestair-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Absolutebestair Com Domain Security
  slug: absolutebestair-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: absolutebestair-com
tags:
- HVAC
- Heating
- Cooling
- Air Quality
- Georgia
- FamilyOwned
website: https://absolutebestair.com/
---
