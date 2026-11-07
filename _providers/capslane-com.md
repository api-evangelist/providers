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
    agent_skills: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Capslane Com Agentic Access
  operation_count: 3
  slug: capslane-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://capslane.com
  baseurl_source: declared
  description: YouTube transcript extraction and generation
  name: capslane-com Transcript API
  slug: capslane-com-transcript-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/capslane-com/agentic-access/capslane-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/capslane-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/capslane-com/plans/capslane-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capslane-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/capslane-com/rules/capslane-com-rules.yml
  title: ''
  type: Spectral
  url: rules/capslane-com-rules.yml
- group: design
  href: https://artifacts.apis.io/capslane-com/vocabulary/capslane-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capslane-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/capslane-com/errors/capslane-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/capslane-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/capslane-com/conformance/capslane-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capslane-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capslane-com/llms/capslane-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capslane-com-llms.txt
- group: other
  href: https://artifacts.apis.io/capslane-com/hosts/capslane-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capslane-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capslane.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://capslane.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capslane.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://capslane.com/changelog
- group: auth
  href: https://artifacts.apis.io/capslane-com/authentication/capslane-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capslane-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/capslane-com/security/capslane-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capslane-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capslane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://capslane.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://capslane.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://capslane.com/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://capslane.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://capslane.com/auth/login
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://capslane.com/openapi.json
  - status: 401
    url: https://capslane.com/mcp
  - status: 200
    url: https://capslane.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Capslane provides a YouTube Transcript API that offers reliable fallback using AI to generate transcripts when captions are missing. It supports retrieving captions from public YouTube videos, automatic caption generation, and delivers results with timestamps, language selection, and structured segments. The service includes asynchronous job handling for longer videos, quota management, and a free tier of 50 requests. Documentation, integrations, pricing, and a playground are available on the site.
image: https://capslane.com/og-capslane.png
layout: provider
modified: '2026-10-30'
name: capslane-com
nav: Providers
network: true
overview: 'capslane-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Transcript API. Tagged areas include Company, YouTube, Transcript, and Artificial Intelligence.


  The capslane-com catalog on APIs.io includes 1 Spectral governance ruleset.


  capslane-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Capslane Com Plans Pricing
  plan_count: 4
  slug: capslane-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: capslane-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: capslane-com-rules
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 50.2
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 50.4
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/capslane-com/capslane-com-2026-11-03T123216.png
security:
- kind: authentication
  name: Capslane Com Authentication
  slug: capslane-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Capslane Com Domain Security
  slug: capslane-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: capslane-com
tags:
- Company
- YouTube
- Transcript
- Artificial Intelligence
website: https://capslane.com/
---
