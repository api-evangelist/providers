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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
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
  score: 34.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Treasury infrastructure for autonomous agents.
  name: Cofferline API
  slug: cofferline-api
artifact_total: 7
asyncapis:
- description: ''
  name: Cofferline Com Webhooks
  slug: cofferline-com-webhooks
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cofferline.com/docs/privacy-v1
- group: design
  href: https://artifacts.apis.io/cofferline-com/rules/cofferline-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cofferline-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cofferline-com/json-ld/cofferline-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cofferline-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cofferline-com/vocabulary/cofferline-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cofferline-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cofferline-com/asyncapi/cofferline-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cofferline-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cofferline-com/data-model/cofferline-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cofferline-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cofferline-com/conventions/cofferline-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cofferline-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/cofferline-com/conventions/cofferline-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cofferline-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cofferline-com/security/cofferline-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cofferline-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cofferline-com/authentication/cofferline-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cofferline-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cofferline-com/errors/cofferline-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cofferline-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cofferline-com/conformance/cofferline-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cofferline-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cofferline-com/llms/cofferline-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cofferline-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cofferline-com/a2a/cofferline-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cofferline-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/cofferline-com/well-known/cofferline-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cofferline-com-security.txt
- group: auth
  href: https://artifacts.apis.io/cofferline-com/well-known/cofferline-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cofferline-com-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/cofferline-com/well-known/cofferline-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cofferline-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cofferline-com/hosts/cofferline-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cofferline-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cofferline-com/vendors/cofferline-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cofferline-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.cofferline.com/
- group: auth
  href: https://artifacts.apis.io/cofferline-com/security/cofferline-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cofferline-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cofferline-com/security/cofferline-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cofferline-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cofferline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cofferline.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.cofferline.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://cofferline.com/docs/agent-quickstart
- group: operate
  title: ''
  type: Support
  url: https://cofferline.com/legal/custody.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cofferline.com/legal/tos
created: '2026-11-04'
description: Cofferline provides treasury and risk infrastructure for prediction‑market agents. It offers a non‑custodial, API‑first service where agents can set risk policies, manage funds, and execute trades via SIWE authentication. The platform aims to enable autonomous agents to handle money safely, with features like per‑market caps, daily loss stops, and double‑entry bookkeeping, all accessible through a single OpenAPI.
image: https://cofferline.com/brand/logo.png
jsonld:
- class_count: 12
  name: Cofferline Com Context
  property_count: 78
  slug: cofferline-com-context
layout: provider
modified: '2026-11-04'
name: Cofferline
nav: Providers
network: true
overview: 'Cofferline publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Treasury, Prediction Markets, Non-Custodial, SIWE Authentication, and Agent Infrastructure.


  The Cofferline catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cofferline''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 23 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Cofferline API Rules
  rule_count: 45
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 4
  slug: cofferline-com-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 53.2
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cofferline Com Authentication
  slug: cofferline-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cofferline Com Domain Security
  slug: cofferline-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cofferline Com Vulnerability Disclosure
  slug: cofferline-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cofferline-com
tags:
- Treasury
- Prediction Markets
- Non-Custodial
- SIWE Authentication
- Agent Infrastructure
website: https://cofferline.com/
---
