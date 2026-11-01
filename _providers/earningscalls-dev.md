---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Earningscalls Dev Agentic Access
  operation_count: 29
  slug: earningscalls-dev-agentic-access
  summary_line: 29 operations · 4 acting
api_count: 1
apis:
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: Company search and details
  name: earningscalls-dev Companies API
  slug: earningscalls-dev-companies-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: Earnings call listing and details
  name: earningscalls-dev Earnings API
  slug: earningscalls-dev-earnings-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: The Exports API from earningscalls-dev — 1 operation(s) for exports.
  name: earningscalls-dev Exports API
  slug: earningscalls-dev-exports-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: The Issuers API from earningscalls-dev — 1 operation(s) for issuers.
  name: earningscalls-dev Issuers API
  slug: earningscalls-dev-issuers-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: Sectors, industries, exchanges, and database stats
  name: earningscalls-dev Metadata API
  slug: earningscalls-dev-metadata-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: Full-text search (Pro/Enterprise)
  name: earningscalls-dev Search API
  slug: earningscalls-dev-search-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: Speaker segments and analysis (Pro/Enterprise)
  name: earningscalls-dev Speakers API
  slug: earningscalls-dev-speakers-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: Full transcript text (Pro/Enterprise)
  name: earningscalls-dev Transcripts API
  slug: earningscalls-dev-transcripts-api
- baseURL: https://earningscalls.dev
  baseurl_source: declared
  description: The Webhooks API from earningscalls-dev — 3 operation(s) for webhooks.
  name: earningscalls-dev Webhooks API
  slug: earningscalls-dev-webhooks-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/earningscalls-dev/agentic-access/earningscalls-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/earningscalls-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/earningscalls-dev/rules/earningscalls-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/earningscalls-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/earningscalls-dev/vocabulary/earningscalls-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/earningscalls-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/earningscalls-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/earningscalls-dev/security/earningscalls-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/earningscalls-dev-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/earningscalls-dev/conformance/earningscalls-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/earningscalls-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/earningscalls-dev/llms/earningscalls-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/earningscalls-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/earningscalls-dev/well-known/earningscalls-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/earningscalls-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/earningscalls-dev/well-known/earningscalls-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/earningscalls-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/earningscalls-dev/hosts/earningscalls-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/earningscalls-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/earningscalls-dev/vendors/earningscalls-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/earningscalls-dev-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://earningscalls.dev/company/team
- group: auth
  href: https://artifacts.apis.io/earningscalls-dev/security/earningscalls-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/earningscalls-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/earningscalls-dev/security/earningscalls-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/earningscalls-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://earningscalls.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://earningscalls.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://earningscalls.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://earningscalls.dev/docs
- group: operate
  title: ''
  type: Support
  url: https://earningscalls.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://earningscalls.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://earningscalls.dev/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://earningscalls.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://earningscalls.dev/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://earningscalls.dev/openapi.json
  - status: 401
    url: https://earningscalls.dev/mcp
  - status: 200
    url: https://earningscalls.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: EarningsCalls.dev provides a REST API delivering earnings call transcripts, speaker segments, and full‑text search for financial analysts and developers. With over 20 endpoints and an OpenAPI 3.0 specification, the service offers pricing plans starting at $24.99/month and aims to simplify integration of corporate earnings data into analytics, research tools, and AI applications.
image: https://earningscalls.dev/public/favicon.png
layout: provider
modified: '2026-10-30'
name: earningscalls-dev
nav: Providers
network: true
overview: 'earningscalls-dev publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Earnings API, Exports API, and 6 more. Tagged areas include Company, Finance, Data, API, and Transcripts.


  The earningscalls-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  earningscalls-dev''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Earningscalls Dev Plans Pricing
  plan_count: 0
  slug: earningscalls-dev-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Earningscalls Dev Rate Limits
  slug: earningscalls-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: earningscalls-dev API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: earningscalls-dev-rules
scopes:
- name: Earningscalls Dev Scopes
  scope_count: 0
  slug: earningscalls-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.7
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 44.3
    developer_ergonomics: 42.1
    discoverability: 67.9
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Earningscalls Dev Authentication
  slug: earningscalls-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Earningscalls Dev Domain Security
  slug: earningscalls-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Earningscalls Dev Vulnerability Disclosure
  slug: earningscalls-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-latest-earnings-calls
  slug: get-latest-earnings-calls
slug: earningscalls-dev
tags:
- Company
- Finance
- Data
- API
- Transcripts
- EarningsCalls
website: https://earningscalls.dev/
---
