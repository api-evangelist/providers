---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Unified generation API for image, video, audio, 3D, training and LLM models. Most generation endpoints are asynchronous: a request returns either a completed result or a "processing" status with an id'
  name: ModelsLab Generation API
  slug: modelslab-generation-api
- baseURL: https://modelslab.com/api
  baseurl_source: declared
  description: 'Unified generation API for image, video, audio, 3D, training and LLM models. Most generation endpoints are asynchronous: a request returns either a completed result or a "processing" status with an id'
  name: ModelsLab Generation API API
  slug: modelslab-generation-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/modelslab-com/rules/modelslab-com-rules.yml
  title: ''
  type: Spectral
  url: rules/modelslab-com-rules.yml
- group: design
  href: https://artifacts.apis.io/modelslab-com/json-ld/modelslab-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/modelslab-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/modelslab-com/vocabulary/modelslab-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/modelslab-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/modelslab-com/rate-limits/modelslab-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/modelslab-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/modelslab-com/plans/modelslab-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/modelslab-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/modelslab-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/modelslab-com/data-model/modelslab-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/modelslab-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://modelslab.com/terms-of-service
- group: auth
  href: https://artifacts.apis.io/modelslab-com/authentication/modelslab-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/modelslab-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/modelslab-com/lifecycle/modelslab-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/modelslab-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/modelslab-com/errors/modelslab-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/modelslab-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/modelslab-com/conformance/modelslab-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/modelslab-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/modelslab-com/llms/modelslab-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/modelslab-com-llms.txt
- group: other
  href: https://artifacts.apis.io/modelslab-com/a2a/modelslab-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/modelslab-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/modelslab-com/well-known/modelslab-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modelslab-com-security.txt
- group: agent
  href: https://artifacts.apis.io/modelslab-com/well-known/modelslab-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/modelslab-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/modelslab-com/hosts/modelslab-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/modelslab-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/modelslab-com/vendors/modelslab-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/modelslab-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/modelslab-com/packages/modelslab-com-packages.yml
  title: ''
  type: SDKs
  url: packages/modelslab-com-packages.yml
- group: build
  href: https://artifacts.apis.io/modelslab-com/packages/modelslab-com-packages.yml
  title: ''
  type: Packages
  url: packages/modelslab-com-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ModelsLab
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.modelslab.com/release-notes/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.modelslab.com\
- group: auth
  href: https://artifacts.apis.io/modelslab-com/security/modelslab-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/modelslab-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/modelslab-com/security/modelslab-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modelslab-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modelslab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.modelslab.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.modelslab.com
- group: start
  title: ''
  type: GettingStarted
  url: https://modelslab.com/docs
- group: operate
  title: ''
  type: Support
  url: https://modelslab.com/support
- group: company
  title: ''
  type: Blog
  url: https://modelslab.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://modelslab.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modelslab.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modelslab.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modelslab.com
- group: start
  title: ''
  type: Login
  url: https://modelslab.com/login
created: '2026-10-29'
description: ModelsLab provides enterprise‑grade API access to over 10,000 AI models spanning image generation, video creation, voice synthesis, and large language models. Developers can integrate generative AI capabilities such as text‑to‑image, video generation, audio synthesis, and LLM chat via a single unified API. The platform offers scalable, fast, and cost‑effective endpoints, detailed documentation, and support for multiple programming languages. Founded in 2022, ModelsLab serves businesses building AI‑enhanced applications.
image: https://imagedelivery.net/PP4qZJxMlvGLHJQBm3ErNg/58efe4a6-3522-4240-b80c-7c3140109300/768
json_schemas:
- name: Generation response
  property_count: 0
  slug: modelslab-com-generation-response
- name: LLM response
  property_count: 0
  slug: modelslab-com-llm-response
- name: Video batch request
  property_count: 6
  slug: modelslab-com-video-batch-request
- name: Video batch response
  property_count: 0
  slug: modelslab-com-video-batch-response
jsonld:
- class_count: 7
  name: Modelslab Com Context
  property_count: 33
  slug: modelslab-com-context
layout: provider
modified: '2026-10-29'
name: modelslab-com
nav: Providers
network: true
overview: 'modelslab-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including ModelsLab Generation API API, and 1 more. Tagged areas include Company, AI, GenerativeAI, Image, and Video.


  The modelslab-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  modelslab-com''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 29 more developer resources.'
plans:
- name: Modelslab Com Plans Pricing
  plan_count: 3
  slug: modelslab-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Modelslab Com Rate Limits
  slug: modelslab-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: modelslab-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: modelslab-com-rules
scopes:
- name: Modelslab Com Scopes
  scope_count: 0
  slug: modelslab-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 56.7
    developer_ergonomics: 70.7
    discoverability: 66.1
    operational_transparency: 78.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Modelslab Com Authentication
  slug: modelslab-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Modelslab Com Domain Security
  slug: modelslab-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Modelslab Com Vulnerability Disclosure
  slug: modelslab-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: modelslab-com
tags:
- Company
- AI
- GenerativeAI
- Image
- Video
- Audio
- LLM
website: https://modelslab.com/
---
