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
    agent_skills: derived
    agentic_access: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Caldogbiteevidence Com Agentic Access
  operation_count: 3
  slug: caldogbiteevidence-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://caldogbiteevidence.com
  baseurl_source: declared
  description: The Check Dog Bite Evidence API from JSM Injury Firm — 1 operation(s) for check dog bite evidence.
  name: JSM Injury Firm Check Dog Bite Evidence API
  slug: caldogbiteevidence-com-check-dog-bite-evidence-api
- baseURL: https://caldogbiteevidence.com
  baseurl_source: declared
  description: The Mcp API from JSM Injury Firm — 1 operation(s) for mcp.
  name: JSM Injury Firm MCP API
  slug: caldogbiteevidence-com-mcp-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/caldogbiteevidence-com/agentic-access/caldogbiteevidence-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/caldogbiteevidence-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/caldogbiteevidence-com/rules/caldogbiteevidence-com-rules.yml
  title: ''
  type: Spectral
  url: rules/caldogbiteevidence-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/caldogbiteevidence-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/caldogbiteevidence-com/conformance/caldogbiteevidence-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caldogbiteevidence-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caldogbiteevidence-com/llms/caldogbiteevidence-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caldogbiteevidence-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/caldogbiteevidence-com/mcp/caldogbiteevidence-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caldogbiteevidence-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/caldogbiteevidence-com/well-known/caldogbiteevidence-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caldogbiteevidence-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/caldogbiteevidence-com/hosts/caldogbiteevidence-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caldogbiteevidence-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/caldogbiteevidence-com/vendors/caldogbiteevidence-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caldogbiteevidence-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/caldogbiteevidence-com/security/caldogbiteevidence-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caldogbiteevidence-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caldogbiteevidence.com/
- group: company
  title: ''
  type: About
  url: https://caldogbiteevidence.com/about
- group: company
  title: ''
  type: Blog
  url: https://caldogbiteevidence.com/blog
created: '2026-11-03'
description: Bitten or injured by a dog in California? Use this private checklist to understand what evidence to preserve, what insurance issues may matter, and whether attorney review may be appropriate. The site provides resources, a checklist, and contact information for legal consultation.
image: https://caldogbiteevidence.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at caldogbiteevidence.com.
  name: JSM Injury Firm MCP Server
  slug: caldogbiteevidence-com-mcp-yml
modified: '2026-11-03'
name: JSM Injury Firm
nav: Providers
network: true
overview: 'JSM Injury Firm publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Check Dog Bite Evidence API and MCP API. Tagged areas include DogBite, Legal, California, Checklist, and Evidence.


  The JSM Injury Firm catalog on APIs.io includes 1 Spectral governance ruleset.


  JSM Injury Firm''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: JSM Injury Firm API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: caldogbiteevidence-com-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 3.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caldogbiteevidence Com Domain Security
  slug: caldogbiteevidence-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: caldogbiteevidence-com-evaluate-dog-bite
  slug: caldogbiteevidence-com-evaluate-dog-bite
slug: caldogbiteevidence-com
tags:
- DogBite
- Legal
- California
- Checklist
- Evidence
website: https://caldogbiteevidence.com/
---
