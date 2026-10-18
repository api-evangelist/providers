---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ballranks Agentic Access
  operation_count: 4
  slug: ballranks-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://ballranks.com
  baseurl_source: declared
  description: 'Read-only fantasy basketball and football rankings and projections: four GET operations (weekly, season and player rankings, player projections).'
  name: Ball Ranks API
  slug: ballranks-rankings-and-projections-api
artifact_total: 7
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/well-known/ballranks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ballranks-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/agentic-access/ballranks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ballranks-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/rules/ballranks-rules.yml
  title: ''
  type: Spectral
  url: rules/ballranks-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/errors/ballranks-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ballranks-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/conformance/ballranks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ballranks-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/llms/ballranks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ballranks-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/hosts/ballranks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ballranks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/vendors/ballranks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ballranks-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/authentication/ballranks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ballranks-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/security/ballranks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ballranks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ballranks.com
- group: docs
  title: ''
  type: Documentation
  url: https://ballranks.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://ballranks.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://ballranks.com/support
- group: company
  title: ''
  type: Blog
  url: https://ballranks.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ballranks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ballranks.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://ballranks.com/auth/sign-up?next=%2Faccount
- group: start
  title: ''
  type: GettingStarted
  url: https://ballranks.com/developers#quick-start
- group: operate
  title: ''
  type: ChangeLog
  url: https://ballranks.com/developers#changelog
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/plans/ballranks-access.json
  title: ''
  type: Plans
  url: plans/ballranks-access.json
- group: operate
  title: ''
  type: RateLimits
  url: https://ballranks.com/developers#rate-limits
- group: commercial
  title: ''
  type: Pricing
  url: https://ballranks.com/premium
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://ballranks.com/developers#security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/well-known/ballranks-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ballranks-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/well-known/ballranks-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/ballranks-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/mcp/ballranks-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ballranks-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballranks/refs/heads/main/skills/ball-ranks/SKILL.md
  title: ''
  type: AgentSkill
  url: skills/ball-ranks/SKILL.md
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Ollynov/ball-ranks-skills
created: '2026-10-08'
description: Ball Ranks provides AI‑driven fantasy sports rankings and projections for football and basketball. The 2026 platform offers free basic rankings and a Premium tier with deeper models, player histories, and a BallChat AI assistant. It serves data via a versioned REST API and a read‑only MCP server, supporting API keys for higher limits. The service is aimed at adult fantasy sports participants and explicitly excludes wagering.
image: https://ballranks.com/football/ranks/opengraph-image
layout: provider
mcp_servers:
- description: Ball Ranks serves a read-only remote Model Context Protocol server (Streamable HTTP) on its own host. A GET answers 405 by design; an anonymous POST initialize and tools/list answer 200 with four tool
  name: Ball Ranks MCP Server
  slug: ballranks-mcp-yml
modified: '2026-10-12'
name: Ball Ranks
nav: Providers
network: true
overview: 'Ball Ranks publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fantasy Sports, Artificial Intelligence, Rankings, and Projections.


  The Ball Ranks catalog on APIs.io includes 1 Spectral governance ruleset.


  Ball Ranks'' developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, getting-started guide, and 22 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Ball Ranks API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: ballranks-rules
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 58.3
    discoverability: 75.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Ballranks Authentication
  slug: ballranks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ballranks Domain Security
  slug: ballranks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: ball-ranks
  slug: ball-ranks
slug: ballranks
tags:
- Company
- Fantasy Sports
- Artificial Intelligence
- Rankings
- Projections
website: https://ballranks.com
---
