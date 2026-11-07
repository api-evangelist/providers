---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Centeringlab Com Agentic Access
  operation_count: 6
  slug: centeringlab-com-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://centeringlab.com
  baseurl_source: declared
  description: The Grade API from Centering Lab — 1 operation(s) for grade.
  name: Centering Lab Grade API
  slug: centeringlab-com-grade-api
- baseURL: https://centeringlab.com
  baseurl_source: declared
  description: The Health API from Centering Lab — 1 operation(s) for health.
  name: Centering Lab Health API
  slug: centeringlab-com-health-api
- baseURL: https://centeringlab.com
  baseurl_source: declared
  description: The Measure API from Centering Lab — 2 operation(s) for measure.
  name: Centering Lab Measure API
  slug: centeringlab-com-measure-api
- baseURL: https://centeringlab.com
  baseurl_source: declared
  description: The Openapi.json API from Centering Lab — 1 operation(s) for openapi.json.
  name: Centering Lab Openapi.json API
  slug: centeringlab-com-openapi-json-api
- baseURL: https://centeringlab.com
  baseurl_source: declared
  description: The Standards API from Centering Lab — 1 operation(s) for standards.
  name: Centering Lab Standards API
  slug: centeringlab-com-standards-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/centeringlab-com/agentic-access/centeringlab-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/centeringlab-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/centeringlab-com/rules/centeringlab-com-rules.yml
  title: ''
  type: Spectral
  url: rules/centeringlab-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/centeringlab-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/centeringlab-com/errors/centeringlab-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/centeringlab-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/centeringlab-com/conformance/centeringlab-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centeringlab-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/centeringlab-com/llms/centeringlab-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centeringlab-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/centeringlab-com/mcp/centeringlab-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/centeringlab-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/centeringlab-com/well-known/centeringlab-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centeringlab-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/centeringlab-com/hosts/centeringlab-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centeringlab-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centeringlab.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centeringlab.com/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://centeringlab.com/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://centeringlab.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/centeringlab-com/authentication/centeringlab-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/centeringlab-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/centeringlab-com/security/centeringlab-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centeringlab-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centeringlab.com/
created: '2026-11-03'
description: Centering Lab provides a free online card centering tool and app for collectors of Pokémon, One Piece, and sports cards. Users can check PSA, BGS, CGC, and SGC grades by uploading a photo directly from Android or iPhone browsers. The service requires no installation, no upload to a server, and operates entirely in the browser, offering a quick calculator and visual checker for card alignment and centering.
image: https://centeringlab.com/assets/social/c15ae5bd931d405a.png
layout: provider
mcp_servers:
- description: Remote MCP server at centeringlab.com.
  name: Centering Lab MCP Server
  slug: centeringlab-com-mcp-yml
modified: '2026-11-03'
name: Centering Lab
nav: Providers
network: true
overview: 'Centering Lab publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Grade API, Health API, Measure API, and 2 more. Tagged areas include Cards, Centering, Collectors, and Web App.


  The Centering Lab catalog on APIs.io includes 1 Spectral governance ruleset.


  Centering Lab''s developer surface includes documentation, API reference, authentication, and 13 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Centering Lab API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: centeringlab-com-rules
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 49.5
    developer_ergonomics: 22.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Centeringlab Com Authentication
  slug: centeringlab-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Centeringlab Com Domain Security
  slug: centeringlab-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 1
skills:
- name: card-centering
  slug: centeringlab-com-card-centering
slug: centeringlab-com
tags:
- Cards
- Centering
- Collectors
- Web App
website: https://centeringlab.com/
---
