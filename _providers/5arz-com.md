---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Proof‑of‑human service API providing human verification and credential issuance.
  name: 5arz Proof-of-Human API
  slug: 5arz-proof-of-human-api
- baseURL: https://api.5arz.com
  baseurl_source: declared
  description: '5arz is the proof-of-human layer for the internet. It issues **Proof-of-Human-Fulfillment (PoHF)** credentials: ES256-signed JWTs asserting that a real, ID-verified, live human — not a bot or AI agent'
  name: 5arz Proof-of-Human API API
  slug: 5arz-proof-of-human-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/5arz-com/rules/5arz-com-rules.yml
  title: ''
  type: Spectral
  url: rules/5arz-com-rules.yml
- group: design
  href: https://artifacts.apis.io/5arz-com/json-ld/5arz-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/5arz-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/5arz-com/vocabulary/5arz-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/5arz-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/5arz-com/conformance/5arz-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/5arz-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/5arz-com/plans/5arz-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/5arz-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/5arz-com/data-model/5arz-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/5arz-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://5arz.com/terms
- group: design
  href: https://artifacts.apis.io/5arz-com/errors/5arz-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/5arz-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/5arz-com/llms/5arz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/5arz-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/5arz-com/well-known/5arz-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/5arz-com-security.txt
- group: agent
  href: https://artifacts.apis.io/5arz-com/well-known/5arz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/5arz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/5arz-com/hosts/5arz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/5arz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/5arz-com/vendors/5arz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/5arz-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://5arz.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://5arz.com/terms
- group: operate
  title: ''
  type: Support
  url: https://5arz.com/help
- group: build
  title: ''
  type: SDKs
  url: https://5arz.com/sdk/sarz.js
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://5arz.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://5arz.com/pricing
- group: start
  title: ''
  type: Login
  url: https://5arz.com/signin
- group: docs
  title: ''
  type: APIReference
  url: https://5arz.com/docs
- group: auth
  href: https://artifacts.apis.io/5arz-com/security/5arz-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/5arz-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/5arz-com/security/5arz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/5arz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://5arz.com/
created: '2026-10-31'
description: 5arz provides a proof‑of‑human service that verifies a real person behind online interactions. Their platform offers APIs to confirm human presence, Know‑Your‑Agent verification, and human‑labeled data for AI agents. Built as a free, privacy‑first solution, 5arz signs cryptographic seals proving personhood without storing personal data. The company targets developers, businesses, and AI platforms needing trustworthy human verification, offering documentation, pricing, and support openly.
image: https://5arz.com/assets/og/home.jpg
json_schemas:
- name: Credential
  property_count: 7
  slug: 5arz-com-credential
- name: HolderJwk
  property_count: 4
  slug: 5arz-com-holder-jwk
jsonld:
- class_count: 3
  name: 5Arz Com Context
  property_count: 14
  slug: 5arz-com-context
layout: provider
modified: '2026-10-31'
name: 5arz
nav: Providers
network: true
overview: '5arz publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Proof-of-Human API API, and 1 more. Tagged areas include Human Verification, Artificial Intelligence, Privacy, Developer Tools, and Authentication.


  The 5arz catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  5arz''s developer surface includes support, pricing, API reference, and 21 more developer resources.'
plans:
- name: 5Arz Com Plans Pricing
  plan_count: 4
  slug: 5arz-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 5arz API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: 5arz-com-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 46.7
    developer_ergonomics: 13.1
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 44.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 5Arz Com Domain Security
  slug: 5arz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 5Arz Com Vulnerability Disclosure
  slug: 5arz-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 5arz-com
tags:
- Human Verification
- Artificial Intelligence
- Privacy
- Developer Tools
- Authentication
website: https://5arz.com/
---
