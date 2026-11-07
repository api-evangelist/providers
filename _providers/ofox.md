---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
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
  score: 24.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ofox Agentic Access
  operation_count: 3
  slug: ofox-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Unified API platform aggregating 100+ LLMs
  name: OfoxAI API
  slug: ofoxai-api
artifact_total: 10
asyncapis:
- description: ''
  name: Ofox Webhooks
  slug: ofox-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/ofox/agentic-access/ofox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ofox-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ofox/plans/ofox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ofox-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ofox/rules/ofox-rules.yml
  title: ''
  type: Spectral
  url: rules/ofox-rules.yml
- group: design
  href: https://artifacts.apis.io/ofox/json-ld/ofox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ofox-context.jsonld
- group: design
  href: https://artifacts.apis.io/ofox/vocabulary/ofox-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ofox-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ofox/asyncapi/ofox-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ofox-webhooks.yml
- group: design
  href: https://artifacts.apis.io/ofox/data-model/ofox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ofox-data-model.yml
- group: build
  href: https://artifacts.apis.io/ofox/cli/ofox-cli.yml
  title: ''
  type: CLI
  url: cli/ofox-cli.yml
- group: operate
  href: https://artifacts.apis.io/ofox/changelog/ofox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ofox-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ofox.ai/trust
- group: auth
  title: ''
  type: Security
  url: https://ofox.ai/docs/security
- group: auth
  href: https://artifacts.apis.io/ofox/authentication/ofox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ofox-authentication.yml
- group: design
  href: https://artifacts.apis.io/ofox/conformance/ofox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ofox-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ofox/llms/ofox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ofox-llms.txt
- group: auth
  href: https://artifacts.apis.io/ofox/well-known/ofox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ofox-security.txt
- group: agent
  href: https://artifacts.apis.io/ofox/well-known/ofox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ofox-well-known.yml
- group: other
  href: https://artifacts.apis.io/ofox/hosts/ofox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ofox-hosts.yml
- group: other
  href: https://artifacts.apis.io/ofox/vendors/ofox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ofox-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ofox.ai/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ofox.ai/llm
- group: start
  title: ''
  type: SignUp
  url: https://app.ofox.ai/auth/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ofox.ai/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://ofox.ai/docs/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.ofox.ai</code
- group: auth
  href: https://artifacts.apis.io/ofox/security/ofox-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ofox-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ofox/security/ofox-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ofox-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ofox/security/ofox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ofox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ofox.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://ofox.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ofox.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://ofox.ai/docs/develop
- group: company
  title: ''
  type: Blog
  url: https://ofox.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ofox.ai/enterprise
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ofoxai
created: '2026-10-18'
description: NICE TALK, operating as OfoxAI, provides a unified API platform that aggregates access to over 100 large language models including GPT, Claude, Gemini, and specialized models like GLM-5.3 and Qwen3.8. The service offers developers streamlined integration through OpenAI‑compatible endpoints, comprehensive documentation, and tools for model selection, pricing, and enterprise deployment, enabling rapid AI application development across text, image, video, and multimodal tasks.
image: https://ofox.ai/en/opengraph-image?2cf3f2a2897fe6c8
jsonld:
- class_count: 5
  name: Ofox Context
  property_count: 14
  slug: ofox-context
layout: provider
modified: '2026-10-18'
name: NICE TALK
nav: Providers
network: true
overview: 'NICE TALK is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, LLM, and Platform.


  The NICE TALK catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  NICE TALK''s developer surface includes CLI, changelog, authentication, signup flow, documentation, API reference, getting-started guide, and 27 more developer resources.'
plans:
- name: Ofox Plans Pricing
  plan_count: 1
  slug: ofox-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: NICE TALK API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: ofox-rules
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 56.0
    catalog_earned_first_party: 8.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.3
  facets:
    access_clarity: 55.3
    contract_governance: 33.3
    contract_quality: 53.2
    developer_ergonomics: 39.3
    discoverability: 64.3
    operational_transparency: 31.6
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ofox Authentication
  slug: ofox-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ofox Domain Security
  slug: ofox-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ofox Vulnerability Disclosure
  slug: ofox-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ofox Trust Center
  slug: ofox-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: ofox
tags:
- Company
- Artificial Intelligence
- LLM
- Platform
website: https://ofox.ai/
---
