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
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aicitely Com Agentic Access
  operation_count: 2
  slug: aicitely-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- baseURL: https://aicitely.com
  baseurl_source: declared
  description: The Health API from Citely — 1 operation(s) for health.
  name: Citely Health API
  slug: aicitely-com-health-api
- baseURL: https://aicitely.com
  baseurl_source: declared
  description: The Public API from Citely — 1 operation(s) for public.
  name: Citely Public API
  slug: aicitely-com-public-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/aicitely-com/agentic-access/aicitely-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aicitely-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aicitely-com/rules/aicitely-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aicitely-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/aicitely-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/aicitely-com/authentication/aicitely-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicitely-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/aicitely-com/errors/aicitely-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicitely-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aicitely-com/conformance/aicitely-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicitely-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicitely-com/llms/aicitely-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicitely-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aicitely-com/a2a/aicitely-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aicitely-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aicitely-com/well-known/aicitely-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicitely-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aicitely-com/hosts/aicitely-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicitely-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aicitely-com/vendors/aicitely-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aicitely-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://aicitely.com/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/aicitely-com/security/aicitely-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicitely-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicitely.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://aicitely.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aicitely.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicitely.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://aicitely.com/signup
created: '2026-11-01'
description: Citely provides AI-driven brand citation services, helping companies ensure their products and services are referenced accurately in AI chat responses. The platform offers GEO audits, methodology guides, case studies, and a free audit tool, alongside detailed pricing and signup options. It aims to improve AI search visibility and brand presence across major AI assistants.
image: https://aicitely.com/og-image.png
layout: provider
modified: '2026-11-01'
name: Citely
nav: Providers
network: true
overview: 'Citely publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Public API. Tagged areas include Company, Artificial Intelligence, BrandCitation, SEO, and Analytics.


  The Citely catalog on APIs.io includes 1 Spectral governance ruleset.


  Citely''s developer surface includes authentication, API reference, pricing, signup flow, and 14 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Citely API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aicitely-com-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 44.1
    developer_ergonomics: 21.9
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aicitely Com Authentication
  slug: aicitely-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aicitely Com Domain Security
  slug: aicitely-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aicitely-com
tags:
- Company
- Artificial Intelligence
- BrandCitation
- SEO
- Analytics
website: https://aicitely.com/
---
