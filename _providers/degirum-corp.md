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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'DeGirum Corp API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: DeGirum Corp API
  slug: degirum-corp-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/degirum-corp/rules/degirum-corp-rules.yml
  title: ''
  type: Spectral
  url: rules/degirum-corp-rules.yml
- group: design
  href: https://artifacts.apis.io/degirum-corp/vocabulary/degirum-corp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/degirum-corp-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/degirum-corp/changelog/degirum-corp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/degirum-corp-changelog.yml
- group: design
  href: https://artifacts.apis.io/degirum-corp/conformance/degirum-corp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/degirum-corp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/degirum-corp/llms/degirum-corp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/degirum-corp-llms.txt
- group: agent
  href: https://artifacts.apis.io/degirum-corp/well-known/degirum-corp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/degirum-corp-well-known.yml
- group: other
  href: https://artifacts.apis.io/degirum-corp/hosts/degirum-corp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/degirum-corp-hosts.yml
- group: build
  href: https://artifacts.apis.io/degirum-corp/packages/degirum-corp-packages.yml
  title: ''
  type: SDKs
  url: packages/degirum-corp-packages.yml
- group: build
  href: https://artifacts.apis.io/degirum-corp/packages/degirum-corp-packages.yml
  title: ''
  type: Packages
  url: packages/degirum-corp-packages.yml
- group: auth
  href: https://artifacts.apis.io/degirum-corp/security/degirum-corp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/degirum-corp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://degirum.com
- group: docs
  title: ''
  type: Documentation
  url: https://degirum.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://degirum.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://degirum.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://degirum.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://community.degirum.com
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://degirum.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: DeGirum Corp was a technology company providing AI-driven development tools, including an AI Hub, Cloud Compiler, and Python SDK. The company ceased operations on August 1, 2026, with assets acquired by LatticeWork. Its former services are no longer available, but the community forum remains open for legacy users. DeGirum was based in Santa Clara, CA, and focused on accelerating software development through AI.
layout: provider
modified: '2026-10-22'
name: DeGirum Corp
nav: Providers
network: true
overview: 'DeGirum Corp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Development Tools, Cloud, and Python SDK.


  The DeGirum Corp catalog on APIs.io includes 1 Spectral governance ruleset.


  DeGirum Corp''s developer surface includes changelog, documentation, support, and 13 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: DeGirum Corp API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: degirum-corp-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 28.6
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 19.0
    discoverability: 60.7
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 31.1
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Degirum Corp Domain Security
  slug: degirum-corp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: degirum-corp
tags:
- Company
- Artificial Intelligence
- Development Tools
- Cloud
- Python SDK
- CeasedOperations
website: https://degirum.com
---
