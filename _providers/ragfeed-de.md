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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Ragfeed De Agentic Access
  operation_count: 44
  slug: ragfeed-de-agentic-access
  summary_line: 44 operations · 21 acting
api_count: 1
apis:
- description: Turn websites into LLM-ready markdown and structured data via scraping, crawling, mapping, searching, and extraction.
  name: Ragfeed API
  slug: ragfeed-api
artifact_total: 20
common:
- group: auth
  href: https://artifacts.apis.io/ragfeed-de/security/ragfeed-de-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ragfeed-de-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ragfeed-de/authentication/ragfeed-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ragfeed-de-authentication.yml
- group: design
  href: https://artifacts.apis.io/ragfeed-de/lifecycle/ragfeed-de-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ragfeed-de-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ragfeed-de/conformance/ragfeed-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ragfeed-de-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ragfeed-de/llms/ragfeed-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ragfeed-de-llms.txt
- group: auth
  href: https://artifacts.apis.io/ragfeed-de/well-known/ragfeed-de-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ragfeed-de-security.txt
- group: auth
  href: https://artifacts.apis.io/ragfeed-de/well-known/ragfeed-de-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ragfeed-de-api-security.txt
- group: agent
  href: https://artifacts.apis.io/ragfeed-de/well-known/ragfeed-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ragfeed-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/ragfeed-de/hosts/ragfeed-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ragfeed-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/ragfeed-de/vendors/ragfeed-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ragfeed-de-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://ragfeed.de/signup
- group: auth
  href: https://artifacts.apis.io/ragfeed-de/security/ragfeed-de-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ragfeed-de-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ragfeed-de/security/ragfeed-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ragfeed-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ragfeed.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ragfeed.de/entwickler
- group: docs
  title: ''
  type: Documentation
  url: https://ragfeed.de/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ragfeed.de/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://ragfeed.de/so-funktionierts
- group: operate
  title: ''
  type: Support
  url: https://ragfeed.de/kontakt
- group: company
  title: ''
  type: Blog
  url: https://ragfeed.de/unternehmen
- group: commercial
  title: ''
  type: Pricing
  url: https://ragfeed.de/preise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ragfeed.de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ragfeed.de/datenschutz
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.ragfeed.de/openapi.json
  - status: null
    url: https://ragfeed.de/openapi.json
  - status: 401
    url: https://api.ragfeed.de/mcp
  - status: 401
    url: https://ragfeed.de/mcp
  - status: 200
    url: https://ragfeed.de/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Ragfeed provides a Web‑Scraping API tailored for AI applications, hosted on servers in Germany. It offers compliance‑focused data extraction for enterprises, enabling monitoring of regulatory and government sites, SaaS product data, and more. The service includes features such as EU‑hosting for data protection, customizable chunking, and integrations with popular AI tools like Claude, n8n, Make, Dify, LangChain, and LlamaIndex. Ragfeed aims to help developers quickly ingest web data for AI models while ensuring privacy and regulatory compliance.
image: https://ragfeed.de/static/og.png?v=60ae9b3e8f
json_schemas:
- name: BatchScrapeRequest
  property_count: 26
  slug: ragfeed-de-batch-scrape-request
- name: CrawlRequest
  property_count: 19
  slug: ragfeed-de-crawl-request
- name: ExtractRequest
  property_count: 10
  slug: ragfeed-de-extract-request
- name: MonitorUpdateRequest
  property_count: 9
  slug: ragfeed-de-monitor-update-request
- name: ScrapeRequest
  property_count: 23
  slug: ragfeed-de-scrape-request
- name: SearchRequest
  property_count: 13
  slug: ragfeed-de-search-request
jsonld:
- class_count: 20
  name: Ragfeed De Context
  property_count: 88
  slug: ragfeed-de-context
layout: provider
modified: '2026-10-31'
name: ragfeed-de
nav: Providers
network: true
overview: 'ragfeed-de publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Web Scraping, Ai Data, EU Hosting, Compliance, and Software-as-a-Service.


  The ragfeed-de catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ragfeed-de''s developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Ragfeed De Plans Pricing
  plan_count: 4
  slug: ragfeed-de-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Ragfeed De Rate Limits
  slug: ragfeed-de-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ragfeed-de API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: ragfeed-de-rules
scopes:
- name: Ragfeed De Scopes
  scope_count: 0
  slug: ragfeed-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 76.5
    catalog_earned_first_party: 24.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 14.7
    developer_ergonomics: 34.5
    discoverability: 66.1
    operational_transparency: 42.1
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ragfeed-de/ragfeed-de-2026-11-03T141909.png
security:
- kind: authentication
  name: Ragfeed De Authentication
  slug: ragfeed-de-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ragfeed De Domain Security
  slug: ragfeed-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ragfeed De Vulnerability Disclosure
  slug: ragfeed-de-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: crawl
  slug: crawl
- name: map
  slug: map
- name: parse
  slug: parse
- name: scrape
  slug: scrape
slug: ragfeed-de
tags:
- Web Scraping
- Ai Data
- EU Hosting
- Compliance
- Software-as-a-Service
website: https://ragfeed.de/
---
