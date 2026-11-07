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
    agent_skills: unknown
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public integration surface for AI agent compliance checks.
  name: Cyphrex API
  slug: cyphrex-api
- baseURL: https://cyphrexapi-production.up.railway.app
  baseurl_source: declared
  description: 'Public integration surface: POST /v1/check and the MCP agent routes (API key), and verification routes (no auth). Dashboard JWT routes are not in this document. Official SDK package name is cyphrex on'
  name: Cyphrex API API
  slug: cyphrex-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/cyphrex-io/rules/cyphrex-io-rules.yml
  title: ''
  type: Spectral
  url: rules/cyphrex-io-rules.yml
- group: design
  href: https://artifacts.apis.io/cyphrex-io/vocabulary/cyphrex-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cyphrex-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cyphrex-io/conformance/cyphrex-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cyphrex-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cyphrex-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cyphrex-io/errors/cyphrex-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cyphrex-io-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/cyphrex-io/llms/cyphrex-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cyphrex-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/cyphrex-io/well-known/cyphrex-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cyphrex-io-security.txt
- group: agent
  href: https://artifacts.apis.io/cyphrex-io/well-known/cyphrex-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cyphrex-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/cyphrex-io/hosts/cyphrex-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyphrex-io-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://cyphrex.io/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cyphrex.io/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://cyphrex.io/security/disclosure
- group: operate
  title: ''
  type: Roadmap
  url: https://cyphrex.io/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cyphrex.io/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://cyphrex.io/news
- group: start
  title: ''
  type: Login
  url: https://cyphrex.io/login
- group: auth
  href: https://artifacts.apis.io/cyphrex-io/security/cyphrex-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cyphrex-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cyphrex-io/security/cyphrex-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyphrex-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyphrex.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cyphrex.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cyphrex.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cyphrex.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://cyphrex.io/docs/quickstart.md
- group: commercial
  title: ''
  type: Pricing
  url: https://cyphrex.io/plans
- group: operate
  title: ''
  type: Contact
  url: https://cyphrex.io/contact
created: '2026-11-04'
description: Cyphrex provides compliance infrastructure for AI agents, offering a tamper‑evident audit log and cryptographically signed evidence to satisfy audits and insurance requirements. It enforces deterministic, rule‑based policies before actions run, supporting regulated sectors like legal, healthcare, accounting, and insurance, as well as solo builders and small teams needing identity, enforcement, and audit trails.
image: https://cyphrex.io/og-image.png
layout: provider
modified: '2026-11-04'
name: Cyphrex
nav: Providers
network: true
overview: 'Cyphrex publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company.


  The Cyphrex catalog on APIs.io includes 1 Spectral governance ruleset.


  Cyphrex''s developer surface includes documentation, API reference, getting-started guide, pricing, and 21 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Cyphrex API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 2
  slug: cyphrex-io-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 44.5
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cyphrex Io Domain Security
  slug: cyphrex-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cyphrex Io Vulnerability Disclosure
  slug: cyphrex-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cyphrex-io
tags:
- Company
website: https://cyphrex.io/
---
