---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Brofindai Com Agentic Access
  operation_count: 14
  slug: brofindai-com-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: AI agent submission and discovery
  name: Bro Find AI Agents API
  slug: brofindai-com-agents-api
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: The Badge API from Bro Find AI — 3 operation(s) for badge.
  name: Bro Find AI Badge API
  slug: brofindai-com-badge-api
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: Tool comments and discussion
  name: Bro Find AI Comments API
  slug: brofindai-com-comments-api
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: General site feedback
  name: Bro Find AI Feedback API
  slug: brofindai-com-feedback-api
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: MCP server submission and discovery
  name: Bro Find AI MCP Servers API
  slug: brofindai-com-mcp-servers-api
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: Tool reviews and ratings
  name: Bro Find AI Reviews API
  slug: brofindai-com-reviews-api
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: Semantic (meaning-based) search over the catalog
  name: Bro Find AI Search API
  slug: brofindai-com-search-api
- baseURL: https://brofindai.com
  baseurl_source: declared
  description: AI tool submission and discovery
  name: Bro Find AI Tools API
  slug: brofindai-com-tools-api
artifact_total: 17
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://brofindai.com/makers/setup
- group: agent
  href: https://artifacts.apis.io/brofindai-com/agentic-access/brofindai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brofindai-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/brofindai-com/plans/brofindai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brofindai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brofindai-com/rules/brofindai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/brofindai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/brofindai-com/vocabulary/brofindai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brofindai-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/brofindai-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/brofindai-com/errors/brofindai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brofindai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brofindai-com/conformance/brofindai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brofindai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brofindai-com/llms/brofindai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brofindai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brofindai-com/well-known/brofindai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brofindai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brofindai-com/hosts/brofindai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brofindai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brofindai-com/vendors/brofindai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brofindai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brofindai.com/terms
- group: operate
  title: ''
  type: Support
  url: https://brofindai.com/support
- group: start
  title: ''
  type: Sandbox
  url: https://brofindai.com/tools/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brofindai.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://brofindai.com/developers
- group: auth
  href: https://artifacts.apis.io/brofindai-com/authentication/brofindai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brofindai-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/brofindai-com/security/brofindai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brofindai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brofindai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://brofindai.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://brofindai.com/pricing
created: '2026-11-03'
description: Bro Find AI is a free AI tools website that curates and indexes over 1000 artificial intelligence tools, applications, and software across categories, pricing models, and use cases. It also lists AI agents and over 340 MCP servers, serving users worldwide from its base in Noida, India. The platform provides detailed descriptions, pricing information, and links to each tool, helping users discover the best AI solutions for their needs.
image: https://brofindai.com/og-image.jpg
layout: provider
modified: '2026-11-03'
name: Bro Find AI
nav: Providers
network: true
overview: 'Bro Find AI publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Badge API, Comments API, and 5 more. Tagged areas include Artificial Intelligence, Directory, Tools, Marketplace, and Company.


  The Bro Find AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Bro Find AI''s developer surface includes getting-started guide, support, sandbox, authentication, API reference, pricing, and 16 more developer resources.'
plans:
- name: Brofindai Com Plans Pricing
  plan_count: 6
  slug: brofindai-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Bro Find AI API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 3
  slug: brofindai-com-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 49.5
    developer_ergonomics: 33.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
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
  name: Brofindai Com Authentication
  slug: brofindai-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brofindai Com Domain Security
  slug: brofindai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: brofindai-com-comments-workflow
  slug: brofindai-com-comments-workflow
- name: brofindai-com-reviews-workflow
  slug: brofindai-com-reviews-workflow
- name: brofindai-com-submit-and-search-agent
  slug: brofindai-com-submit-and-search-agent
- name: brofindai-com-submit-and-search-tools
  slug: brofindai-com-submit-and-search-tools
slug: brofindai-com
tags:
- Artificial Intelligence
- Directory
- Tools
- Marketplace
- Company
website: https://brofindai.com/
---
