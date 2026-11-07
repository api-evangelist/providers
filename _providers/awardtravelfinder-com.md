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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Awardtravelfinder Com Agentic Access
  operation_count: 13
  slug: awardtravelfinder-com-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 1
apis:
- baseURL: https://awardtravelfinder.com
  baseurl_source: declared
  description: The Agent API from Award Travel Finder — 1 operation(s) for agent.
  name: Award Travel Finder Agent API
  slug: awardtravelfinder-com-agent-api
- baseURL: https://awardtravelfinder.com
  baseurl_source: declared
  description: The Airlines API from Award Travel Finder — 1 operation(s) for airlines.
  name: Award Travel Finder Airlines API
  slug: awardtravelfinder-com-airlines-api
- baseURL: https://awardtravelfinder.com
  baseurl_source: declared
  description: The British Airways (Admin Only) API from Award Travel Finder — 3 operation(s) for british airways (admin only).
  name: Award Travel Finder British Airways (Admin Only) API
  slug: awardtravelfinder-com-british-airways-admin-only-api
- baseURL: https://awardtravelfinder.com
  baseurl_source: declared
  description: The Cathay Pacific API from Award Travel Finder — 3 operation(s) for cathay pacific.
  name: Award Travel Finder Cathay Pacific API
  slug: awardtravelfinder-com-cathay-pacific-api
- baseURL: https://awardtravelfinder.com
  baseurl_source: declared
  description: The Hotels API from Award Travel Finder — 5 operation(s) for hotels.
  name: Award Travel Finder Hotels API
  slug: awardtravelfinder-com-hotels-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/awardtravelfinder-com/agentic-access/awardtravelfinder-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/awardtravelfinder-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/awardtravelfinder-com/plans/awardtravelfinder-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/awardtravelfinder-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/awardtravelfinder-com/rules/awardtravelfinder-com-rules.yml
  title: ''
  type: Spectral
  url: rules/awardtravelfinder-com-rules.yml
- group: design
  href: https://artifacts.apis.io/awardtravelfinder-com/vocabulary/awardtravelfinder-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/awardtravelfinder-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/awardtravelfinder-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/awardtravelfinder-com/components/awardtravelfinder-com-components.yml
  title: ''
  type: Components
  url: components/awardtravelfinder-com-components.yml
- group: auth
  href: https://artifacts.apis.io/awardtravelfinder-com/authentication/awardtravelfinder-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/awardtravelfinder-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/awardtravelfinder-com/errors/awardtravelfinder-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/awardtravelfinder-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/awardtravelfinder-com/conformance/awardtravelfinder-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/awardtravelfinder-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/awardtravelfinder-com/llms/awardtravelfinder-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awardtravelfinder-com-llms.txt
- group: other
  href: https://artifacts.apis.io/awardtravelfinder-com/a2a/awardtravelfinder-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/awardtravelfinder-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/awardtravelfinder-com/well-known/awardtravelfinder-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/awardtravelfinder-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/awardtravelfinder-com/hosts/awardtravelfinder-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awardtravelfinder-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/awardtravelfinder-com/vendors/awardtravelfinder-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/awardtravelfinder-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://awardtravelfinder.com/status
- group: docs
  title: ''
  type: Documentation
  url: https://awardtravelfinder.com/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://awardtravelfinder.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://awardtravelfinder.com/mcp/chatgpt
- group: docs
  title: ''
  type: APIReference
  url: https://awardtravelfinder.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AwardTravelFinder
- group: auth
  href: https://artifacts.apis.io/awardtravelfinder-com/security/awardtravelfinder-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awardtravelfinder-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awardtravelfinder.com/
- group: company
  title: ''
  type: Blog
  url: https://awardtravelfinder.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://awardtravelfinder.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awardtravelfinder.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://awardtravelfinder.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://awardtravelfinder.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://awardtravelfinder.com/openapi.json
  - status: 401
    url: https://awardtravelfinder.com/mcp
  - status: 200
    url: https://awardtravelfinder.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Award Travel Finder is an AI‑native award flight search platform that helps travelers find award seats and business‑class upgrades across 24 airline loyalty programs. Users can query award availability directly from Claude, ChatGPT, or Cursor agents, receiving real‑time results without needing to log into each airline. The service offers a free tier with limited searches and a paid plan for higher usage, and it respects user privacy by not storing conversation data for training.
image: https://og-image-api.merchantai.workers.dev/?subtitle=Award+Flight+Finder+%E2%80%94+Find+Award+Seats+with+AI+Agents&template=minimal&title=Award+Travel+Finder
layout: provider
modified: '2026-11-02'
name: Award Travel Finder
nav: Providers
network: true
overview: 'Award Travel Finder publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Airlines API, British Airways (Admin Only) API, and 2 more. Tagged areas include Travel, Awards, Artificial Intelligence, Flights, and Loyalty.


  The Award Travel Finder catalog on APIs.io includes 1 Spectral governance ruleset.


  Award Travel Finder''s developer surface includes authentication, documentation, getting-started guide, API reference, engineering blog, pricing, support, and 20 more developer resources.'
plans:
- name: Awardtravelfinder Com Plans Pricing
  plan_count: 3
  slug: awardtravelfinder-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Awardtravelfinder Com Rate Limits
  slug: awardtravelfinder-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Award Travel Finder API Rules
  rule_count: 51
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 4
  slug: awardtravelfinder-com-rules
scopes:
- name: Awardtravelfinder Com Scopes
  scope_count: 0
  slug: awardtravelfinder-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 50.8
    developer_ergonomics: 36.3
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Awardtravelfinder Com Authentication
  slug: awardtravelfinder-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Awardtravelfinder Com Domain Security
  slug: awardtravelfinder-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: awardtravelfinder-com
tags:
- Travel
- Awards
- Artificial Intelligence
- Flights
- Loyalty
website: https://awardtravelfinder.com/
---
