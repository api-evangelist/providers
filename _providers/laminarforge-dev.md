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
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
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
  score: 34.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Laminarforge Dev Agentic Access
  operation_count: 4
  slug: laminarforge-dev-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: lf-format-utils — JSON/CSV/XML/YAML converters, case, slug, base64, date, color, roman, cron
  name: LaminarForge API Format Utils API
  slug: laminarforge-dev-format-utils-api
- description: Shared platform endpoints — health, keys, usage, billing (available on both workers)
  name: LaminarForge API Platform API
  slug: laminarforge-dev-platform-api
artifact_total: 7
asyncapis:
- description: ''
  name: Laminarforge Dev Webhooks
  slug: laminarforge-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/laminarforge-dev/agentic-access/laminarforge-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/laminarforge-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/laminarforge-dev/rules/laminarforge-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/laminarforge-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/laminarforge-dev/vocabulary/laminarforge-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/laminarforge-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/laminarforge-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/laminarforge-dev/asyncapi/laminarforge-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/laminarforge-dev-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/laminarforge-dev/authentication/laminarforge-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/laminarforge-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/laminarforge-dev/errors/laminarforge-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/laminarforge-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/laminarforge-dev/conformance/laminarforge-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/laminarforge-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/laminarforge-dev/llms/laminarforge-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/laminarforge-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/laminarforge-dev/well-known/laminarforge-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/laminarforge-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/laminarforge-dev/hosts/laminarforge-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/laminarforge-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/laminarforge-dev/vendors/laminarforge-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/laminarforge-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/laminarforge
- group: start
  title: ''
  type: GettingStarted
  url: https://lf-format-utils.laminarforge.dev/v1/register
- group: docs
  title: ''
  type: APIReference
  url: https://laminarforge.dev/docs
- group: auth
  href: https://artifacts.apis.io/laminarforge-dev/security/laminarforge-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/laminarforge-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://laminarforge.dev
- group: docs
  title: ''
  type: Documentation
  url: https://laminarforge.dev/v1/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://laminarforge.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://laminarforge.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://laminarforge.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://laminarforge.dev/blog
- group: operate
  title: ''
  type: Support
  url: https://laminarforge.dev/support
- group: start
  title: ''
  type: SignUp
  url: https://laminarforge.dev/signup
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://laminarforge.dev
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: LaminarForge provides a unified API marketplace offering over 175 production‑ready utility APIs across categories such as format conversion, validation, security, and web intelligence. Developers can access all services with a single API key under a pay‑per‑request pricing model. The platform aims to simplify integration by consolidating diverse functionalities into one endpoint, supporting rapid development and scaling.
image: https://laminarforge.dev/images/og-image.jpg
layout: provider
modified: '2026-11-05'
name: LaminarForge API
nav: Providers
network: true
overview: 'LaminarForge API publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Format Utils API and Platform API. Tagged areas include API Marketplace, Utilities, Developer Tools, Integration, and Cloud Services.


  The LaminarForge API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LaminarForge API''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, engineering blog, support, and 17 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: LaminarForge API API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: laminarforge-dev-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 49.4
    developer_ergonomics: 54.0
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Laminarforge Dev Authentication
  slug: laminarforge-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Laminarforge Dev Domain Security
  slug: laminarforge-dev-domain-security
  summary_line: TLSv1.3
slug: laminarforge-dev
tags:
- API Marketplace
- Utilities
- Developer Tools
- Integration
- Cloud Services
website: https://laminarforge.dev
---
