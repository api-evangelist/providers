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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public REST API for PrompTessor prompt workflows, usage, history, presets, library, uploads and webhooks.
  name: PrompTessor API
  slug: promptessor-api
artifact_total: 11
asyncapis:
- description: ''
  name: Promptessor Webhooks
  slug: promptessor-webhooks
common:
- group: design
  href: https://artifacts.apis.io/promptessor/rules/promptessor-rules.yml
  title: ''
  type: Spectral
  url: rules/promptessor-rules.yml
- group: design
  href: https://artifacts.apis.io/promptessor/json-ld/promptessor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/promptessor-context.jsonld
- group: design
  href: https://artifacts.apis.io/promptessor/vocabulary/promptessor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/promptessor-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/promptessor/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/promptessor/asyncapi/promptessor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/promptessor-webhooks.yml
- group: design
  href: https://artifacts.apis.io/promptessor/data-model/promptessor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/promptessor-data-model.yml
- group: operate
  href: https://artifacts.apis.io/promptessor/changelog/promptessor-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/promptessor-changelog.yml
- group: design
  href: https://artifacts.apis.io/promptessor/conventions/promptessor-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/promptessor-conventions.yml
- group: design
  href: https://artifacts.apis.io/promptessor/conventions/promptessor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/promptessor-conventions.yml
- group: auth
  href: https://artifacts.apis.io/promptessor/authentication/promptessor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/promptessor-authentication.yml
- group: operate
  href: https://artifacts.apis.io/promptessor/lifecycle/promptessor-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/promptessor-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/promptessor/lifecycle/promptessor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/promptessor-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/promptessor/errors/promptessor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/promptessor-problem-types.yml
- group: design
  href: https://artifacts.apis.io/promptessor/conformance/promptessor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/promptessor-conformance.yml
- group: agent
  href: https://artifacts.apis.io/promptessor/llms/promptessor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptessor-llms.txt
- group: agent
  href: https://artifacts.apis.io/promptessor/well-known/promptessor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/promptessor-well-known.yml
- group: other
  href: https://artifacts.apis.io/promptessor/hosts/promptessor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptessor-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptessor/vendors/promptessor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptessor-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://promptessor.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promptessor.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://promptessor.com/dev/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://promptessor.com/dev/docs/mcp/integrations
- group: docs
  title: ''
  type: APIReference
  url: https://promptessor.com/dev/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/promptessor/security/promptessor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptessor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptessor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://promptessor.com/docs
- group: company
  title: ''
  type: Blog
  url: https://promptessor.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://promptessor.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://promptessor.com/signup
- group: operate
  title: ''
  type: Support
  url: https://promptessor.com/contact
created: '2026-10-18'
description: PrompTessor provides an AI prompt generation, optimization, and library platform. It offers tools to create, analyze, refine, and reverse‑engineer prompts for various AI models, supporting text, image, video, and code prompts. Users can organize prompts in a workspace, integrate with popular AI services, and access a marketplace of prompt templates. The platform includes documentation, pricing plans, and community resources for developers and prompt engineers.
image: https://promptessor.com/OG-LandingPage.png
jsonld:
- class_count: 32
  name: Promptessor Context
  property_count: 128
  slug: promptessor-context
layout: provider
modified: '2026-10-18'
name: PrompTessor
nav: Providers
network: true
overview: 'PrompTessor publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Prompt Engineering, Platform, Documentation, and Community.


  The PrompTessor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  PrompTessor''s developer surface includes changelog, authentication, getting-started guide, API reference, documentation, engineering blog, pricing, and 23 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: PrompTessor API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: promptessor-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 31.5
    discoverability: 73.2
    operational_transparency: 23.7
  previous_composite: 49.4
  provenance:
    conformance: derived
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/promptessor/promptessor-2026-11-03T141557.png
security:
- kind: authentication
  name: Promptessor Authentication
  slug: promptessor-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Promptessor Domain Security
  slug: promptessor-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: promptessor-create-and-publish-library-item
  slug: promptessor-create-and-publish-library-item
- name: promptessor-create-and-render-prompt-preset
  slug: promptessor-create-and-render-prompt-preset
- name: promptessor-create-upload
  slug: promptessor-create-upload
- name: promptessor-generate-analyze-optimize-prompt
  slug: promptessor-generate-analyze-optimize-prompt
- name: promptessor-webhook-endpoint-setup
  slug: promptessor-webhook-endpoint-setup
slug: promptessor
tags:
- Artificial Intelligence
- Prompt Engineering
- Platform
- Documentation
- Community
website: https://promptessor.com/
---
