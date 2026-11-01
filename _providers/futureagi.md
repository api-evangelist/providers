---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for evaluating, monitoring, and optimizing AI applications.
  name: Future AGI API
  slug: future-agi-api
- baseURL: https://api.futureagi.com
  baseurl_source: declared
  description: API for evaluating, monitoring, and optimizing AI applications.
  name: Future AGI API API
  slug: future-agi-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/futureagi/rules/futureagi-rules.yml
  title: ''
  type: Spectral
  url: rules/futureagi-rules.yml
- group: design
  href: https://artifacts.apis.io/futureagi/conformance/futureagi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/futureagi-conformance.yml
- group: operate
  href: https://artifacts.apis.io/futureagi/rate-limits/futureagi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/futureagi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/futureagi/plans/futureagi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/futureagi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/futureagi/changelog/futureagi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/futureagi-changelog.yml
- group: design
  href: https://artifacts.apis.io/futureagi/conventions/futureagi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/futureagi-conventions.yml
- group: design
  href: https://artifacts.apis.io/futureagi/conventions/futureagi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/futureagi-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://futureagi.com/security/
- group: auth
  href: https://artifacts.apis.io/futureagi/authentication/futureagi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/futureagi-authentication.yml
- group: agent
  href: https://artifacts.apis.io/futureagi/llms/futureagi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/futureagi-llms.txt
- group: agent
  href: https://artifacts.apis.io/futureagi/well-known/futureagi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/futureagi-well-known.yml
- group: other
  href: https://artifacts.apis.io/futureagi/hosts/futureagi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/futureagi-hosts.yml
- group: other
  href: https://artifacts.apis.io/futureagi/vendors/futureagi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/futureagi-vendors.yml
- group: build
  href: https://artifacts.apis.io/futureagi/packages/futureagi-packages.yml
  title: ''
  type: SDKs
  url: packages/futureagi-packages.yml
- group: build
  href: https://artifacts.apis.io/futureagi/packages/futureagi-packages.yml
  title: ''
  type: Packages
  url: packages/futureagi-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://futureagi.com/glossary/webhook/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.futureagi.com
- group: auth
  title: ''
  type: Security
  url: https://futureagi.com/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://futureagi.com/roadmap/
- group: operate
  title: ''
  type: ChangeLog
  url: https://futureagi.com/changelog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.futureagi.com</code
- group: auth
  href: https://artifacts.apis.io/futureagi/security/futureagi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/futureagi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/futureagi/security/futureagi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/futureagi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/futureagi/security/futureagi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/futureagi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://futureagi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.futureagi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.futureagi.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.futureagi.com/docs/sdk
- group: company
  title: ''
  type: Blog
  url: https://futureagi.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://futureagi.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://futureagi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://futureagi.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/future-agi
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.futureagi.com/swagger.json
  - status: null
    url: https://docs.futureagi.com/openapi.json
  - status: 401
    url: https://api.futureagi.com/mcp
  - status: 200
    url: https://futureagi.com/
  reason: partner-login
  state: gated
created: '2026-10-20'
description: Future AGI provides a platform for building, testing, and optimizing AI agents at scale. Their services include simulation environments, synthetic data generation, agent IDEs, evaluation tools, optimization via AI, and real‑time monitoring. The company targets enterprises and startups, offering documentation, SDKs, and integrations to accelerate AI agent development and deployment.
image: https://futureagi.com/og-image.png
layout: provider
modified: '2026-10-20'
name: Future AGI
nav: Providers
network: true
overview: 'Future AGI publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, AI, Platform, Agents, and Simulation.


  The Future AGI catalog on APIs.io includes 1 Spectral governance ruleset.


  Future AGI''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Futureagi Plans Pricing
  plan_count: 5
  slug: futureagi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Futureagi Rate Limits
  slug: futureagi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Future AGI API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: futureagi-rules
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 64.8
    catalog_earned_first_party: 24.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 15.9
    contract_quality: 42.7
    developer_ergonomics: 59.5
    discoverability: 66.1
    operational_transparency: 92.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Futureagi Authentication
  slug: futureagi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Futureagi Domain Security
  slug: futureagi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Futureagi Vulnerability Disclosure
  slug: futureagi-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Futureagi Trust Center
  slug: futureagi-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: futureagi
tags:
- Company
- AI
- Platform
- Agents
- Simulation
- Monitoring
website: https://futureagi.com/
---
