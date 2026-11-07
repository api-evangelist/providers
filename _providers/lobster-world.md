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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lobster World Agentic Access
  operation_count: 1
  slug: lobster-world-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.lobster-world.com
  baseurl_source: declared
  description: Manage communication channels of an integration partner.
  name: Lobster Data GmbH Channels API
  slug: lobster-world-channels-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/lobster-world/agentic-access/lobster-world-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lobster-world-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/lobster-world/rules/lobster-world-rules.yml
  title: ''
  type: Spectral
  url: rules/lobster-world-rules.yml
- group: design
  href: https://artifacts.apis.io/lobster-world/vocabulary/lobster-world-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lobster-world-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/lobster-world/changelog/lobster-world-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lobster-world-changelog.yml
- group: design
  href: https://artifacts.apis.io/lobster-world/conventions/lobster-world-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lobster-world-conventions.yml
- group: auth
  href: https://artifacts.apis.io/lobster-world/security/lobster-world-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lobster-world-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lobster-world/authentication/lobster-world-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lobster-world-authentication.yml
- group: design
  href: https://artifacts.apis.io/lobster-world/errors/lobster-world-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lobster-world-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lobster-world/conformance/lobster-world-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lobster-world-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lobster-world/llms/lobster-world-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lobster-world-llms.txt
- group: auth
  href: https://artifacts.apis.io/lobster-world/well-known/lobster-world-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lobster-world-security.txt
- group: agent
  href: https://artifacts.apis.io/lobster-world/well-known/lobster-world-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lobster-world-well-known.yml
- group: other
  href: https://artifacts.apis.io/lobster-world/hosts/lobster-world-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lobster-world-hosts.yml
- group: other
  href: https://artifacts.apis.io/lobster-world/vendors/lobster-world-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lobster-world-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lobstersoftware.com/docs/ai-azure-chat-gpt-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lobster-world.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lobstersoftware.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/lobster-world/security/lobster-world-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lobster-world-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lobster-world/security/lobster-world-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lobster-world-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lobstersoftware.com/
created: '2026-10-20'
description: Lobster Data GmbH provides a data platform for real‑time analytics, integration, and monitoring of industrial and IoT environments. The company offers APIs for data ingestion, querying, and management, supporting secure, high‑throughput pipelines. Their documentation and developer portal are hosted on www.lobstersoftware.com, with detailed guides, SDKs, and support resources. Lobster Data focuses on scalability, compliance, and flexible deployment options for enterprises seeking actionable insights from massive data streams.
image: https://cdn.lobstersoftware.com/sites/web30/26/02/20120346/rankmath_default_social_share_image_v1-1200x630-1.png
layout: provider
modified: '2026-10-20'
name: Lobster Data GmbH
nav: Providers
network: true
overview: 'Lobster Data GmbH publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Channels API. Tagged areas include Company, Data, Analytics, IoT, and Real-Time.


  The Lobster Data GmbH catalog on APIs.io includes 1 Spectral governance ruleset.


  Lobster Data GmbH''s developer surface includes changelog, authentication, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Lobster Data GmbH API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: lobster-world-rules
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 43.5
    developer_ergonomics: 27.4
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/lobster-world/lobster-world-2026-11-03T135017.png
security:
- kind: authentication
  name: Lobster World Authentication
  slug: lobster-world-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lobster World Domain Security
  slug: lobster-world-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lobster World Vulnerability Disclosure
  slug: lobster-world-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lobster-world
tags:
- Company
- Data
- Analytics
- IoT
- Real-Time
website: https://www.lobstersoftware.com/
---
