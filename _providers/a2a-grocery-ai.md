---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    mcp_server: false
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
  score: 16.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: A2A Grocery Ai Agentic Access
  operation_count: 7
  slug: a2a-grocery-ai-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- description: API for A2A Grocery door, providing product facts and paid receipt services.
  name: A2A Grocery API
  slug: a2a-grocery-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/a2a-grocery-ai/agentic-access/a2a-grocery-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/a2a-grocery-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/a2a-grocery-ai/rules/a2a-grocery-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/a2a-grocery-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/a2a-grocery-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/a2a-grocery-ai/authentication/a2a-grocery-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/a2a-grocery-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/a2a-grocery-ai/errors/a2a-grocery-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/a2a-grocery-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/a2a-grocery-ai/conformance/a2a-grocery-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/a2a-grocery-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/a2a-grocery-ai/llms/a2a-grocery-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2a-grocery-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/a2a-grocery-ai/a2a/a2a-grocery-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/a2a-grocery-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/a2a-grocery-ai/well-known/a2a-grocery-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/a2a-grocery-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/a2a-grocery-ai/well-known/a2a-grocery-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/a2a-grocery-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/a2a-grocery-ai/hosts/a2a-grocery-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a2a-grocery-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/a2a-grocery-ai/vendors/a2a-grocery-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a2a-grocery-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://a2a-grocery.ai/security
- group: auth
  href: https://artifacts.apis.io/a2a-grocery-ai/security/a2a-grocery-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/a2a-grocery-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/a2a-grocery-ai/security/a2a-grocery-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2a-grocery-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a2a-grocery.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://a2a-grocery.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://a2a-grocery.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://a2a-grocery.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://a2a-grocery.ai/setup
- group: operate
  title: ''
  type: Support
  url: https://a2a-grocery.ai/support
- group: commercial
  title: ''
  type: Pricing
  url: https://a2a-grocery.ai/rate-card
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a2a-grocery.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a2a-grocery.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://a2a-grocery.ai/status
created: '2026-10-31'
description: A2A Grocery is the agentic hub for retail grocery procurement, connecting food makers directly with AI agents that handle buying for retailers. The platform maintains cleared supplier records across 20 markets, enabling trade‑only transactions. It offers tools such as Answer Engine Optimization, Listing, and others to streamline commerce between makers, distributors, and retailers. The service is built by GreenCore Solutions Corp and operates via a secure, stateless API infrastructure.
image: https://a2a-grocery.ai/og-image-1200x630.png
layout: provider
modified: '2026-10-31'
name: A2A Grocery
nav: Providers
network: true
overview: 'A2A Grocery is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Grocery, Procurement, Agents, and Marketplace.


  The A2A Grocery catalog on APIs.io includes 1 Spectral governance ruleset.


  A2A Grocery''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 19 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: A2A Grocery API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: a2a-grocery-ai-rules
scopes:
- name: A2A Grocery Ai Scopes
  scope_count: 0
  slug: a2a-grocery-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 39.8
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A2A Grocery Ai Authentication
  slug: a2a-grocery-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: A2A Grocery Ai Domain Security
  slug: a2a-grocery-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: A2A Grocery Ai Vulnerability Disclosure
  slug: a2a-grocery-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: a2a-grocery-ai
tags:
- Artificial Intelligence
- Grocery
- Procurement
- Agents
- Marketplace
website: https://a2a-grocery.ai/
---
