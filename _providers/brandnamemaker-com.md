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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
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
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Brandnamemaker Com Agentic Access
  operation_count: 4
  slug: brandnamemaker-com-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://brandnamemaker.com
  baseurl_source: declared
  description: The Hero API from True Frontier — 1 operation(s) for hero.
  name: True Frontier Hero API
  slug: brandnamemaker-com-hero-api
- baseURL: https://brandnamemaker.com
  baseurl_source: declared
  description: The Name API from True Frontier — 1 operation(s) for name.
  name: True Frontier Name API
  slug: brandnamemaker-com-name-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/brandnamemaker-com/agentic-access/brandnamemaker-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brandnamemaker-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/brandnamemaker-com/rules/brandnamemaker-com-rules.yml
  title: ''
  type: Spectral
  url: rules/brandnamemaker-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/brandnamemaker-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/brandnamemaker-com/errors/brandnamemaker-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brandnamemaker-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brandnamemaker-com/conformance/brandnamemaker-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brandnamemaker-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brandnamemaker-com/llms/brandnamemaker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brandnamemaker-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brandnamemaker-com/mcp/brandnamemaker-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brandnamemaker-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/brandnamemaker-com/hosts/brandnamemaker-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandnamemaker-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brandnamemaker.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brandnamemaker.com/privacy
- group: auth
  href: https://artifacts.apis.io/brandnamemaker-com/authentication/brandnamemaker-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brandnamemaker-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/brandnamemaker-com/security/brandnamemaker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandnamemaker-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandnamemaker.com/
created: '2026-11-02'
description: Brandname Maker, operated by True Frontier, offers an AI-powered brand and product naming service with real-time .com, .app, and .ai domain availability checks. It provides a pay‑per‑call API for founders and agents, charging $0.25 via stablecoins or $1 via card per naming pass, delivering curated name shortlists with rationales and domain status. The platform emphasizes fast, automated naming assistance integrated into developer workflows.
image: https://brandnamemaker.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at brandnamemaker.com.
  name: True Frontier MCP Server
  slug: brandnamemaker-com-mcp-yml
modified: '2026-11-02'
name: True Frontier
nav: Providers
network: true
overview: 'True Frontier publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Hero API and Name API. Tagged areas include Artificial Intelligence, Naming, Branding, and DomainCheck.


  The True Frontier catalog on APIs.io includes 1 Spectral governance ruleset.


  True Frontier''s developer surface includes authentication and 12 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: True Frontier API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: brandnamemaker-com-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 18.3
    discoverability: 56.7
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
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Brandnamemaker Com Authentication
  slug: brandnamemaker-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Brandnamemaker Com Domain Security
  slug: brandnamemaker-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: naming
  slug: brandnamemaker-com-naming-skill
slug: brandnamemaker-com
tags:
- Artificial Intelligence
- Naming
- Branding
- DomainCheck
website: https://brandnamemaker.com/
---
