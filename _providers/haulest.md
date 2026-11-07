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
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote streamable-HTTP MCP server (no auth) exposing moving cost estimates, route facts, mover search, mover profiles, licence checks, guide search, checklists and quote requests.
  name: Haulest MCP Server
  slug: haulest-mcp
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/haulest/security/haulest-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/haulest-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/haulest/llms/haulest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/haulest-llms.txt
- group: build
  href: https://artifacts.apis.io/haulest/mcp/haulest-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/haulest-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/haulest/mcp/haulest-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/haulest-mcp.yml
- group: auth
  href: https://artifacts.apis.io/haulest/well-known/haulest-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/haulest-security.txt
- group: agent
  href: https://artifacts.apis.io/haulest/well-known/haulest-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/haulest-well-known.yml
- group: other
  href: https://artifacts.apis.io/haulest/hosts/haulest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/haulest-hosts.yml
- group: other
  href: https://artifacts.apis.io/haulest/vendors/haulest-vendors.yml
  title: ''
  type: Vendors
  url: vendors/haulest-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://haulest.com/news
- group: auth
  href: https://artifacts.apis.io/haulest/security/haulest-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/haulest-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/haulest/security/haulest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/haulest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://haulest.com
- group: docs
  title: ''
  type: Documentation
  url: https://haulest.com/developers/mcp
- group: operate
  title: ''
  type: ChangeLog
  url: https://haulest.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://haulest.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://haulest.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://haulest.com/llms.txt
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://haulest.com/mcp
  - status: 200
    url: https://haulest.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Haulest, operated by Panaweb LLC (Dover, Delaware), publishes moving-cost ranges, route facts, reviewed movers, mover licence checks, moving guides and checklists for the US, Canada and the UK, and exposes them to AI assistants through a no-auth remote MCP server at https://haulest.com/mcp with eight tools including estimate_moving_cost, find_movers and request_moving_quotes. Haulest is not a carrier and does not operate trucks.
image: https://haulest.com/og?title=Your+next+chapter.+Less+moving+stress.&src=%2Fphotos%2Fgen%2Fhome.jpg&eyebrow=Haulest&text=Know+what+to+budget.+Find+the+right+help.+Plan+the+move%2C+then+call+%2B1+%28866%29+961-9682+or+send+From+and+To.+Haulest+is+not+a+carrier.
layout: provider
mcp_servers:
- description: Remote MCP server at haulest.com over streamable HTTP; 8 tools listed.
  name: Haulest MCP Server
  slug: haulest-mcp-server
modified: '2026-10-09'
name: Haulest
nav: Providers
network: true
overview: 'Haulest is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Moving, Relocation, Cost Estimation, and MCP.


  Haulest''s developer surface includes documentation, changelog, and 15 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.8
    operational_transparency: 18.4
  previous_composite: 17.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/haulest/haulest-2026-10-11T105136.png
security:
- kind: domain-security
  name: Haulest Domain Security
  slug: haulest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Haulest Vulnerability Disclosure
  slug: haulest-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: haulest
tags:
- Company
- Moving
- Relocation
- Cost Estimation
- MCP
- Movers
- Consumer
website: https://haulest.com
---
