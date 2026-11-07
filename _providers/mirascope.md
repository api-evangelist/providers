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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Mirascope LLM services
  name: Mirascope API
  slug: mirascope-api-2
- description: 'Mirascope API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Mirascope API
  slug: mirascope-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/mirascope/rules/mirascope-rules.yml
  title: ''
  type: Spectral
  url: rules/mirascope-rules.yml
- group: design
  href: https://artifacts.apis.io/mirascope/vocabulary/mirascope-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mirascope-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/mirascope/changelog/mirascope-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mirascope-changelog.yml
- group: auth
  href: https://artifacts.apis.io/mirascope/authentication/mirascope-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mirascope-authentication.yml
- group: design
  href: https://artifacts.apis.io/mirascope/conformance/mirascope-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mirascope-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mirascope/llms/mirascope-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mirascope-llms.txt
- group: other
  href: https://artifacts.apis.io/mirascope/hosts/mirascope-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mirascope-hosts.yml
- group: other
  href: https://artifacts.apis.io/mirascope/vendors/mirascope-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mirascope-vendors.yml
- group: build
  href: https://artifacts.apis.io/mirascope/packages/mirascope-packages.yml
  title: ''
  type: SDKs
  url: packages/mirascope-packages.yml
- group: build
  href: https://artifacts.apis.io/mirascope/packages/mirascope-packages.yml
  title: ''
  type: Packages
  url: packages/mirascope-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mirascope.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://mirascope.com/docs
- group: company
  title: ''
  type: Blog
  url: https://mirascope.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://mirascope.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/mirascope/security/mirascope-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mirascope-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mirascope.com/
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are rendered via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://mirascope.com/docs/api/llm
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: 'Mirascope is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://mirascope.com/social-cards/index.webp
layout: provider
modified: '2026-10-18'
name: Mirascope
nav: Providers
network: true
overview: 'Mirascope is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include LLM, Framework, Artificial Intelligence, Versioning, and Tracing.


  The Mirascope catalog on APIs.io includes 1 Spectral governance ruleset.


  Mirascope''s developer surface includes changelog, authentication, documentation, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Mirascope API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: mirascope-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 31.0
    discoverability: 55.4
    operational_transparency: 15.8
  previous_composite: 24.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mirascope/mirascope-2026-11-03T135645.png
security:
- kind: authentication
  name: Mirascope Authentication
  slug: mirascope-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Mirascope Domain Security
  slug: mirascope-domain-security
  summary_line: TLSv1.3
slug: mirascope
tags:
- LLM
- Framework
- Artificial Intelligence
- Versioning
- Tracing
- Cost Tracking
website: https://mirascope.com/
---
