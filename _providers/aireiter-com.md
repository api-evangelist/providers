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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Aireiter Com Agentic Access
  operation_count: 8
  slug: aireiter-com-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: One API key for leading text, image and video models. Task API for async generation plus OpenAI / Anthropic compatible gateways.
  name: AIReiter API
  slug: aireiter-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/aireiter-com/agentic-access/aireiter-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aireiter-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aireiter-com/rules/aireiter-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aireiter-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aireiter-com/conformance/aireiter-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aireiter-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aireiter-com/llms/aireiter-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aireiter-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aireiter-com/a2a/aireiter-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aireiter-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aireiter-com/well-known/aireiter-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aireiter-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aireiter-com/hosts/aireiter-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aireiter-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aireiter-com/vendors/aireiter-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aireiter-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aireiter.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aireiter.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://aireiter.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mintlify
- group: company
  title: ''
  type: Blog
  url: https://aireiter.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aireiter.com/zh/api-reference/tasks/status
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aireiter.com/
- group: auth
  href: https://artifacts.apis.io/aireiter-com/authentication/aireiter-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aireiter-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aireiter-com/security/aireiter-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aireiter-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aireiter.com
created: '2026-10-28'
description: AIReiter provides a unified AI API platform offering text, image, and video generation across multiple leading models such as Claude, GPT, Gemini, VEO3, and Seedance. It supports asynchronous job handling, transparent credit‑based pricing, and OpenAI‑compatible endpoints, enabling developers to integrate multimodal AI capabilities with a single API key and billing system. The service includes model‑specific channels, webhook callbacks, and a developer console for API key management.
image: https://static.aireiter.com/images/og-default.png
layout: provider
modified: '2026-10-28'
name: AIReiter
nav: Providers
network: true
overview: 'AIReiter is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Multi-Modal, Generation, OpenAI-Compatible, and Credit-Pricing.


  The AIReiter catalog on APIs.io includes 1 Spectral governance ruleset.


  AIReiter''s developer surface includes pricing, engineering blog, API reference, documentation, authentication, and 13 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AIReiter API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: aireiter-com-rules
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 15.8
    contract_governance: 15.9
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 23.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aireiter-com/aireiter-com-2026-11-03T120527.png
security:
- kind: authentication
  name: Aireiter Com Authentication
  slug: aireiter-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aireiter Com Domain Security
  slug: aireiter-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aireiter-com
tags:
- Artificial Intelligence
- Multi-Modal
- Generation
- OpenAI-Compatible
- Credit-Pricing
website: https://aireiter.com
---
