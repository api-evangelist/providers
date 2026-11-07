---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Amzscout Net Agentic Access
  operation_count: 16
  slug: amzscout-net-agentic-access
  summary_line: 16 operations · 15 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: http://chatbot.amzscout.net
  baseurl_source: declared
  description: The discovery API from AMZScout — 1 operation(s) for discovery.
  name: AMZScout Discovery API
  slug: amzscout-net-discovery-api
- baseURL: http://chatbot.amzscout.net
  baseurl_source: declared
  description: The dispatch API from AMZScout — 1 operation(s) for dispatch.
  name: AMZScout Dispatch API
  slug: amzscout-net-dispatch-api
- baseURL: http://chatbot.amzscout.net
  baseurl_source: declared
  description: The tools API from AMZScout — 14 operation(s) for tools.
  name: AMZScout Tools API
  slug: amzscout-net-tools-api
artifact_total: 10
common:
- group: operate
  title: ''
  type: Support
  url: https://amzscout.net/help/?r=footer
- group: agent
  href: https://artifacts.apis.io/amzscout-net/agentic-access/amzscout-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amzscout-net-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/amzscout-net/rules/amzscout-net-rules.yml
  title: ''
  type: Spectral
  url: rules/amzscout-net-rules.yml
- group: design
  href: https://artifacts.apis.io/amzscout-net/vocabulary/amzscout-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amzscout-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/amzscout-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/amzscout-net/errors/amzscout-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amzscout-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amzscout-net/conformance/amzscout-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amzscout-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amzscout-net/llms/amzscout-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amzscout-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/amzscout-net/mcp/amzscout-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amzscout-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/amzscout-net/well-known/amzscout-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amzscout-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/amzscout-net/hosts/amzscout-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amzscout-net-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amzscout.net/terms-of-use?r=footer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amzscout.net/privacy-policy?r=footer
- group: auth
  href: https://artifacts.apis.io/amzscout-net/security/amzscout-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amzscout-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amzscout.net/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.amzscout.net/
- group: docs
  title: ''
  type: APIReference
  url: https://chatbot.amzscout.net/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://amzscout.net/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://amzscout.net/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://amzscout.net/signup/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://chatbot.amzscout.net/openapi.json
  - status: 401
    url: https://chatbot.amzscout.net/mcp
  - status: 200
    url: https://amzscout.net/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: 'Use AMZScout and make Amazon product research easy with accurate research tools and seller software: AMZScout PRO Chrome Extension, Product Database, Keyword Search and more. Analyze niches and find the right product to make money. Start your free trial.'
image: https://amzscout.net/static/mainscreen-390d476b8043cf70d709c569987d0c64.png
layout: provider
mcp_servers:
- description: Remote MCP server at chatbot.amzscout.net.
  name: AMZScout MCP Server
  slug: amzscout-net-mcp-yml
modified: '2026-11-01'
name: AMZScout
nav: Providers
network: true
overview: 'AMZScout publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, Dispatch API, and Tools API. Tagged areas include Amazon, FBA, Product Research, Software-as-a-Service, and E-Commerce.


  The AMZScout catalog on APIs.io includes 1 Spectral governance ruleset.


  AMZScout''s developer surface includes support, documentation, API reference, engineering blog, pricing, signup flow, and 14 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AMZScout API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 3
  slug: amzscout-net-rules
scopes:
- name: Amzscout Net Scopes
  scope_count: 0
  slug: amzscout-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 44.5
    developer_ergonomics: 18.3
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Amzscout Net Authentication
  slug: amzscout-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Amzscout Net Domain Security
  slug: amzscout-net-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: analyze-product
  slug: amzscout-net-analyze-product
slug: amzscout-net
tags:
- Amazon
- FBA
- Product Research
- Software-as-a-Service
- E-Commerce
- Company
website: https://amzscout.net/
---
