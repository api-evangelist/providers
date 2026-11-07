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
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Industrial LTE & 5G RedCap Modems, 1.4M+ Deployed
  name: Hyper Nexus
  slug: hyper-nexus
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/aiotrf-com/llms/aiotrf-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiotrf-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aiotrf-com/mcp/aiotrf-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiotrf-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/aiotrf-com/hosts/aiotrf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiotrf-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aiotrf.com/en/legal/privacy/
- group: auth
  href: https://artifacts.apis.io/aiotrf-com/security/aiotrf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiotrf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiotrf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aiotrf.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aiotrf.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.aiotrf.com/en/support/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aiotrf.com/en/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found despite documentation host.
  evidence:
  - status: 200
    url: https://www.aiotrf.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Hyper Nexus (北京超级联接科技有限公司) provides industrial LTE and 5G RedCap modems, mmWave radar health monitoring, and AI messenger solutions. Their products include MF833V, Dongle 400, F40, HN‑X1 radar and Hala messenger, serving over 1.4M devices in 60+ countries with global certifications and custom firmware.
image: https://www.aiotrf.com/assets/v2/og/home-en.e976588e13.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.aiotrf.com.
  name: Hyper Nexus MCP Server
  slug: aiotrf-com-mcp-yml
modified: '2026-11-01'
name: Hyper Nexus
nav: Providers
network: true
overview: 'Hyper Nexus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Connectivity, Modems, Radar, and Artificial Intelligence.


  Hyper Nexus'' developer surface includes documentation, support, getting-started guide, and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 14.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiotrf Com Domain Security
  slug: aiotrf-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiotrf-com
tags:
- IoT
- Connectivity
- Modems
- Radar
- Artificial Intelligence
website: https://aiotrf.com/
---
