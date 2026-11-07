---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Andiai Com Agentic Access
  operation_count: 1
  slug: andiai-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.andiai.com
  baseurl_source: declared
  description: The Search API from Andi AI — 1 operation(s) for search.
  name: Andi AI Search API
  slug: andiai-com-search-api
artifact_total: 12
common:
- group: operate
  href: https://artifacts.apis.io/andiai-com/rate-limits/andiai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/andiai-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/andiai-com/vocabulary/andiai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/andiai-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/andiai-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/andiai-com/errors/andiai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/andiai-com-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/andiai-com/well-known/andiai-com-search-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/andiai-com-search-api-security.txt
- group: build
  href: https://artifacts.apis.io/andiai-com/packages/andiai-com-packages.yml
  title: ''
  type: SDKs
  url: packages/andiai-com-packages.yml
- group: build
  href: https://artifacts.apis.io/andiai-com/packages/andiai-com-packages.yml
  title: ''
  type: Packages
  url: packages/andiai-com-packages.yml
- group: agent
  href: https://artifacts.apis.io/andiai-com/agentic-access/andiai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/andiai-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/andiai-com/plans/andiai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/andiai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/andiai-com/rules/andiai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/andiai-com-rules.yml
- group: build
  href: https://artifacts.apis.io/andiai-com/cli/andiai-com-cli.yml
  title: ''
  type: CLI
  url: cli/andiai-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/andiai-com/security/andiai-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/andiai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/andiai-com/authentication/andiai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/andiai-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/andiai-com/conformance/andiai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/andiai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/andiai-com/llms/andiai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/andiai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/andiai-com/a2a/andiai-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/andiai-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/andiai-com/well-known/andiai-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/andiai-com-security.txt
- group: auth
  href: https://artifacts.apis.io/andiai-com/well-known/andiai-com-console-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/andiai-com-console-security.txt
- group: auth
  href: https://artifacts.apis.io/andiai-com/well-known/andiai-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/andiai-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/andiai-com/well-known/andiai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/andiai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/andiai-com/hosts/andiai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andiai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/andiai-com/vendors/andiai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andiai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://andiai.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.andiai.com
- group: start
  title: ''
  type: SignUp
  url: https://console.andiai.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://andiai.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.andiai.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/andisearch
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.andiai.com/getting-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.andiai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.andiai.com/api-reference/introduction
- group: auth
  href: https://artifacts.apis.io/andiai-com/security/andiai-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/andiai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/andiai-com/security/andiai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andiai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://andiai.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://andiai.com/openapi.json
  - status: null
    url: https://api.andiai.com/openapi.json
  - status: null
    url: https://docs.andiai.com/mcp
  - status: 401
    url: https://api.andiai.com/mcp
  - status: 401
    url: https://dashboard.andiai.com/api/graphql
  - status: 401
    url: https://dashboard.andiai.com/api/mcp
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Andi AI provides a next‑generation AI‑powered search engine that returns direct answers instead of links. Founded in 2021, it builds its own index called Trantora, scoring billions of pages for credibility and relevance. The service emphasizes privacy, ad‑free results, and real‑time web search for AI agents via a public API. It powers over a million users and offers documentation, SDKs, and a console for developers to integrate search into applications.
image: https://andiai.com/images/og-default.png
layout: provider
modified: '2026-11-01'
name: Andi AI
nav: Providers
network: true
overview: 'Andi AI publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Search API. Tagged areas include Artificial Intelligence, Search, Privacy, OpenAI, and Community.


  The Andi AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Andi AI''s developer surface includes CLI, authentication, signup flow, pricing, getting-started guide, documentation, API reference, and 27 more developer resources.'
plans:
- name: Andiai Com Plans Pricing
  plan_count: 4
  slug: andiai-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Andiai Com Rate Limits
  slug: andiai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Andi AI API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: andiai-com-rules
scopes:
- name: Andiai Com Scopes
  scope_count: 0
  slug: andiai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 46.5
    developer_ergonomics: 46.9
    discoverability: 66.1
    operational_transparency: 42.1
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  name: Andiai Com Authentication
  slug: andiai-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Andiai Com Domain Security
  slug: andiai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Andiai Com Vulnerability Disclosure
  slug: andiai-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: fetch
  slug: andiai-com-fetch
- name: news
  slug: andiai-com-news
- name: search
  slug: andiai-com-search
slug: andiai-com
tags:
- Artificial Intelligence
- Search
- Privacy
- OpenAI
- Community
website: https://andiai.com/
---
