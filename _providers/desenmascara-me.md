---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Desenmascara Me Agentic Access
  operation_count: 2
  slug: desenmascara-me-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://desenmascara.me
  baseurl_source: spec
  description: desenmascara.me API from Desenmascara.me — 2 path(s) described in OpenAPI.
  name: desenmascara.me API
  slug: desenmascara-me-openapi
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/desenmascara-me/agentic-access/desenmascara-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/desenmascara-me-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/desenmascara-me/rules/desenmascara-me-rules.yml
  title: ''
  type: Spectral
  url: rules/desenmascara-me-rules.yml
- group: design
  href: https://artifacts.apis.io/desenmascara-me/vocabulary/desenmascara-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/desenmascara-me-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/desenmascara-me/errors/desenmascara-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/desenmascara-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/desenmascara-me/conformance/desenmascara-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/desenmascara-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/desenmascara-me/llms/desenmascara-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/desenmascara-me-llms.txt
- group: other
  href: https://artifacts.apis.io/desenmascara-me/hosts/desenmascara-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/desenmascara-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/desenmascara-me/vendors/desenmascara-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/desenmascara-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://desenmascara.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://desenmascara.me/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://desenmascara.me/media/deception-observatory/
- group: start
  title: ''
  type: Login
  url: https://desenmascara.me/login
- group: auth
  href: https://artifacts.apis.io/desenmascara-me/security/desenmascara-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/desenmascara-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://desenmascara.me/
created: '2026-11-05'
description: Desenmascara.me provides real‑time fraud detection and scam‑prevention intelligence for websites. Users can submit a URL or domain and receive risk scores, evidence, and detailed signals about fraudulent intent, phishing kits, impersonation, and other threats. The service offers a free tier without account, as well as paid plans for businesses, API access, and AI‑agent integration. It also publishes a public API feed and documentation for developers to integrate fraud‑risk checks into their own systems.
layout: provider
modified: '2026-11-05'
name: Desenmascara.me
nav: Providers
network: true
overview: 'Desenmascara.me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Desenmascara.me catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Desenmascara.me API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: desenmascara-me-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 25.8
    catalog_earned_first_party: 0.0
    catalog_gap: 89.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 50.2
    developer_ergonomics: 0.0
    discoverability: 37.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Desenmascara Me Domain Security
  slug: desenmascara-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: desenmascara-me
tags:
- Company
website: https://desenmascara.me/
---
