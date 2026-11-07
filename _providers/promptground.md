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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Promptground Agentic Access
  operation_count: 36
  slug: promptground-agentic-access
  summary_line: 36 operations · 21 acting
api_count: 1
apis:
- description: The API v1 API from PromptGround — 1 operation(s) for api v1.
  name: PromptGround API v1 API
  slug: promptground-api-v1-api
- description: The API v2 API from PromptGround — 2 operation(s) for api v2.
  name: PromptGround API v2 API
  slug: promptground-api-v2-api
- description: The Invites API from PromptGround — 2 operation(s) for invites.
  name: PromptGround Invites API
  slug: promptground-invites-api
- description: The Models API from PromptGround — 2 operation(s) for models.
  name: PromptGround Models API
  slug: promptground-models-api
- description: The Payments API from PromptGround — 4 operation(s) for payments.
  name: PromptGround Payments API
  slug: promptground-payments-api
- description: The Projects API from PromptGround — 4 operation(s) for projects.
  name: PromptGround Projects API
  slug: promptground-projects-api
- description: The Prompts API from PromptGround — 8 operation(s) for prompts.
  name: PromptGround Prompts API
  slug: promptground-prompts-api
- description: The Sessions API from PromptGround — 2 operation(s) for sessions.
  name: PromptGround Sessions API
  slug: promptground-sessions-api
- description: The Settings API from PromptGround — 4 operation(s) for settings.
  name: PromptGround Settings API
  slug: promptground-settings-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/promptground/agentic-access/promptground-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/promptground-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/promptground/rules/promptground-rules.yml
  title: ''
  type: Spectral
  url: rules/promptground-rules.yml
- group: design
  href: https://artifacts.apis.io/promptground/json-ld/promptground-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/promptground-context.jsonld
- group: design
  href: https://artifacts.apis.io/promptground/vocabulary/promptground-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/promptground-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/promptground/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/promptground/data-model/promptground-data-model.yml
  title: ''
  type: DataModel
  url: data-model/promptground-data-model.yml
- group: design
  href: https://artifacts.apis.io/promptground/errors/promptground-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/promptground-problem-types.yml
- group: design
  href: https://artifacts.apis.io/promptground/conformance/promptground-conformance.yml
  title: ''
  type: Conformance
  url: conformance/promptground-conformance.yml
- group: other
  href: https://artifacts.apis.io/promptground/hosts/promptground-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptground-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptground/vendors/promptground-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptground-vendors.yml
- group: build
  href: https://artifacts.apis.io/promptground/packages/promptground-packages.yml
  title: ''
  type: SDKs
  url: packages/promptground-packages.yml
- group: build
  href: https://artifacts.apis.io/promptground/packages/promptground-packages.yml
  title: ''
  type: Packages
  url: packages/promptground-packages.yml
- group: auth
  href: https://artifacts.apis.io/promptground/authentication/promptground-authentication.yml
  title: ''
  type: Authentication
  url: authentication/promptground-authentication.yml
- group: auth
  href: https://artifacts.apis.io/promptground/security/promptground-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptground-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptground.io/
- group: docs
  title: ''
  type: Documentation
  url: https://app.promptground.io/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.promptground.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NoCodeInc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nocodeinc
coverage:
  checked: '2026-10-18'
  detail: Unable to verify ownership of the OpenAPI spec at https://api.promptground.io/openapi.json; the spec lacks company identifiers.
  evidence:
  - status: 200
    url: https://api.promptground.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: PromptGround provides AI prompt management, version tracking, and testing platform. It offers a unified API key to access multiple AI models, detailed run logs, team collaboration, and SDKs for Python and JavaScript. Users get 10,000 free tokens to start, with pay‑as‑you‑go pricing and bulk discounts. The service includes a live prompt editor, variable support, and analytics for prompt performance, targeting developers, prompt engineers, and teams seeking scalable prompt workflows.
image: https://www.promptground.io/images/prompt-ground-cover.png
jsonld:
- class_count: 11
  name: Promptground Context
  property_count: 28
  slug: promptground-context
layout: provider
modified: '2026-10-18'
name: PromptGround
nav: Providers
network: true
overview: 'PromptGround publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including API v1 API, API v2 API, Invites API, and 6 more. Tagged areas include Artificial Intelligence, Prompt Engineering, Collaboration, Analytics, and SDK.


  The PromptGround catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PromptGround''s developer surface includes authentication, documentation, and 17 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: PromptGround API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 1
  slug: promptground-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 48.9
    developer_ergonomics: 30.4
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/promptground/promptground-2026-11-03T141603.png
security:
- kind: authentication
  name: Promptground Authentication
  slug: promptground-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Promptground Domain Security
  slug: promptground-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: promptground-create-and-run-prompt
  slug: promptground-create-and-run-prompt
- name: promptground-manage-project
  slug: promptground-manage-project
- name: promptground-payments-process-payment
  slug: promptground-payments-process-payment
slug: promptground
tags:
- Artificial Intelligence
- Prompt Engineering
- Collaboration
- Analytics
- SDK
website: https://promptground.io/
---
