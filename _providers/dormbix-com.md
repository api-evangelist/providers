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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dormbix Com Agentic Access
  operation_count: 5
  slug: dormbix-com-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://www.dormbix.com
  baseurl_source: declared
  description: The Ai Feed.json API from DormBix — 1 operation(s) for ai feed.json.
  name: DormBix Ai Feed.json API
  slug: dormbix-com-ai-feed-json-api
- baseURL: https://www.dormbix.com
  baseurl_source: declared
  description: The Public API from DormBix — 3 operation(s) for public.
  name: DormBix Public API
  slug: dormbix-com-public-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/dormbix-com/agentic-access/dormbix-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dormbix-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dormbix-com/rules/dormbix-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dormbix-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/dormbix-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dormbix-com/conventions/dormbix-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dormbix-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/dormbix-com/conventions/dormbix-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dormbix-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dormbix-com/authentication/dormbix-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dormbix-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dormbix-com/errors/dormbix-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dormbix-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dormbix-com/conformance/dormbix-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dormbix-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dormbix-com/llms/dormbix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dormbix-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dormbix-com/a2a/dormbix-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dormbix-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dormbix-com/well-known/dormbix-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dormbix-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dormbix-com/hosts/dormbix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dormbix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dormbix-com/vendors/dormbix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dormbix-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dormbix.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dormbix.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.dormbix.com/manage/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.dormbix.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.dormbix.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.dormbix.com/developers
- group: auth
  href: https://artifacts.apis.io/dormbix-com/security/dormbix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dormbix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dormbix.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://dormbix.com/openapi.json
  - status: null
    url: https://www.dormbix.com/openapi.json
  - status: 401
    url: https://www.dormbix.com/api/mcp
  - status: 200
    url: https://dormbix.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DormBix provides an AI‑powered dormitory management platform that automates billing, utility tracking, lease contracts, meter reading, and rent collection. Users receive real‑time notifications via LINE OA, can sign digital leases, and manage their rooms through a web dashboard. The service aims to streamline operations for dorm owners and enhance tenant experience with intelligent automation and seamless communication.
image: https://www.dormbix.com/og-image.webp
layout: provider
modified: '2026-11-05'
name: DormBix
nav: Providers
network: true
overview: 'DormBix publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Ai Feed.json API and Public API. Tagged areas include Dormitory Management, Artificial Intelligence, Billing Automation, Thai Market, and Software-as-a-Service.


  The DormBix catalog on APIs.io includes 1 Spectral governance ruleset.


  DormBix''s developer surface includes authentication, documentation, engineering blog, API reference, and 17 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: DormBix API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: dormbix-com-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 46.5
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dormbix Com Authentication
  slug: dormbix-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dormbix Com Domain Security
  slug: dormbix-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: dormbix-com-search-and-check-availability
  slug: dormbix-com-search-and-check-availability
slug: dormbix-com
tags:
- Dormitory Management
- Artificial Intelligence
- Billing Automation
- Thai Market
- Software-as-a-Service
website: https://www.dormbix.com/
---
