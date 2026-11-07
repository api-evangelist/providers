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
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Human-and-agent marketplace for local and online work.
  name: Day1Work Agent API
  slug: day1work-agent-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/day1work-com/vocabulary/day1work-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/day1work-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/day1work-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/day1work-com/conformance/day1work-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/day1work-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/day1work-com/llms/day1work-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/day1work-com-llms.txt
- group: other
  href: https://artifacts.apis.io/day1work-com/a2a/day1work-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/day1work-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/day1work-com/mcp/day1work-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/day1work-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/day1work-com/well-known/day1work-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/day1work-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/day1work-com/hosts/day1work-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/day1work-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://day1work.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://day1work.com/legal/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://day1work.com/developers
- group: auth
  href: https://artifacts.apis.io/day1work-com/security/day1work-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/day1work-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://day1work.com/
created: '2026-11-05'
description: Day1Work is the local marketplace app for everyday work, allowing users to post tasks and earn money on their schedule. Operated by iQra OÜ in Estonia, the platform connects task posters with earners, handling secure payments and keeping 95% of earnings for the workers. The service covers a range of everyday jobs such as dog sitting, cleaning, moving help, and more, aiming to create flexible income opportunities for its community.
image: https://day1work.com/brand/social/facebook-cover.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.day1work.com requiring OAuth.
  name: Day1Work MCP Server
  slug: day1work-com-mcp-yml
modified: '2026-11-05'
name: Day1Work
nav: Providers
network: true
overview: 'Day1Work is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Gig Economy, Mobile App, Estonia, and Task Management.


  Day1Work''s developer surface includes API reference and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 13.6
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Day1Work Com Domain Security
  slug: day1work-com-domain-security
  summary_line: TLSv1.2 · DMARC
slug: day1work-com
tags:
- Marketplace
- Gig Economy
- Mobile App
- Estonia
- Task Management
website: https://day1work.com/
---
