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
  score: 17.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Fresh, sourced civic/tax/financial facts for AI agents.
  name: botcorpus API
  slug: botcorpus-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/botcorpus-com/conformance/botcorpus-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botcorpus-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botcorpus-com/llms/botcorpus-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botcorpus-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/botcorpus-com/mcp/botcorpus-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/botcorpus-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/botcorpus-com/well-known/botcorpus-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/botcorpus-com-security.txt
- group: agent
  href: https://artifacts.apis.io/botcorpus-com/well-known/botcorpus-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botcorpus-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/botcorpus-com/hosts/botcorpus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botcorpus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/botcorpus-com/vendors/botcorpus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botcorpus-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://botcorpus.com/fakt/au/security/nato-status
- group: company
  title: ''
  type: Blog
  url: https://botcorpus.com/blog
- group: auth
  href: https://artifacts.apis.io/botcorpus-com/security/botcorpus-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/botcorpus-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/botcorpus-com/security/botcorpus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botcorpus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botcorpus.com/
created: '2026-11-02'
description: 'botcorpus-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://botcorpus.com/wp-content/uploads/2026/06/Snimka-obrazovky_20260627_120242.png
layout: provider
mcp_servers:
- description: Remote MCP server at botcorpus.com.
  name: botcorpus MCP Server
  slug: botcorpus-com-mcp-yml
modified: '2026-11-02'
name: botcorpus
nav: Providers
network: true
overview: 'botcorpus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Agents, LLM, and Tax.


  botcorpus'' developer surface includes engineering blog and 11 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.3
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botcorpus Com Domain Security
  slug: botcorpus-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Botcorpus Com Vulnerability Disclosure
  slug: botcorpus-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: botcorpus-com
tags:
- Data
- Agents
- LLM
- Tax
website: https://botcorpus.com/
---
