---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Vulk Dev Agentic Access
  operation_count: 11
  slug: vulk-dev-agentic-access
  summary_line: 11 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.vulk.dev/api/v1
  baseurl_source: declared
  description: The models your account may generate with, as the editor's picker shows them.
  name: vulk-dev Models API
  slug: vulk-dev-models-api
- baseURL: https://app.vulk.dev/api/v1
  baseurl_source: declared
  description: Follow or stop one build or one instruction by its requestId. Reading is free and safe to repeat.
  name: vulk-dev Operations API
  slug: vulk-dev-operations-api
- baseURL: https://app.vulk.dev/api/v1
  baseurl_source: declared
  description: 'Endpoints of the previous VULK, kept for keys created there (hex body, pay-as-you-go credits). Not part of the plans'' API: a key created in Settings › API keys is refused here.'
  name: vulk-dev Pay-as-you-go (previous VULK) API
  slug: vulk-dev-pay-as-you-go-previous-vulk-api
- baseURL: https://app.vulk.dev/api/v1
  baseurl_source: declared
  description: Start, continue, list, read and delete projects; read their delivered files.
  name: vulk-dev Projects API
  slug: vulk-dev-projects-api
- baseURL: https://app.vulk.dev/api/v1
  baseurl_source: declared
  description: Plan, credit balance and the last 30 days.
  name: vulk-dev Usage API
  slug: vulk-dev-usage-api
artifact_total: 22
asyncapis:
- description: ''
  name: Vulk Dev Webhooks
  slug: vulk-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/vulk-dev/agentic-access/vulk-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vulk-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/vulk-dev/plans/vulk-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vulk-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vulk-dev/rules/vulk-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/vulk-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/vulk-dev/json-ld/vulk-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vulk-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/vulk-dev/vocabulary/vulk-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vulk-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/vulk-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vulk-dev/asyncapi/vulk-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vulk-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/vulk-dev/data-model/vulk-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vulk-dev-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://vulk.dev/security
- group: auth
  href: https://artifacts.apis.io/vulk-dev/authentication/vulk-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vulk-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/vulk-dev/errors/vulk-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vulk-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vulk-dev/conformance/vulk-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vulk-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vulk-dev/llms/vulk-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vulk-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/vulk-dev/well-known/vulk-dev-v2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vulk-dev-v2-security.txt
- group: auth
  href: https://artifacts.apis.io/vulk-dev/well-known/vulk-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vulk-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/vulk-dev/well-known/vulk-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vulk-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/vulk-dev/hosts/vulk-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vulk-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/vulk-dev/vendors/vulk-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vulk-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://vulk.dev/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VULK-dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://vulk.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://vulk.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://support.vulk.dev/docs/getting-started/what-is-vulk
- group: docs
  title: ''
  type: APIReference
  url: https://support.vulk.dev/docs/api
- group: company
  title: ''
  type: Website
  url: https://vulk.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://support.vulk.dev/docs/api/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.vulk.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://vulk.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vulk.dev/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vulk.dev/privacy-policy
- group: auth
  href: https://artifacts.apis.io/vulk-dev/security/vulk-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vulk-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vulk-dev/security/vulk-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vulk-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vulk-dev/security/vulk-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vulk-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vulk.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://vulk.dev/openapi.json
  - status: 401
    url: https://vulk.dev/api/mcp
  - status: 401
    url: https://app.vulk.dev/mcp
  - status: 200
    url: https://vulk.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: VULK is an AI-powered app builder platform that enables creators to design full‑stack applications, 3D websites, and Flutter apps without extensive coding. The service offers a visual interface, AI‑assisted design tools, and a marketplace of templates, supporting over 19,000 creators worldwide. VULK provides features such as AI‑generated code, 3D rendering, multi‑platform deployment, and integration with popular app stores, aiming to accelerate product development and reduce time‑to‑market.
image: https://vulk.dev/api/og?title=VULK+%E2%80%94+AI+App+Builder%3A+Full-Stack+Apps%2C+3D+Websites+%26+Flutter+Apps&subtitle=Build+web%2C+iOS+and+Android+apps%2C+3D+websites+and+GLB+models+with+VULK.+Generate+images+and+video%2C+connect+a+backend%2C+export+code+and%E2%80%A6
json_schemas:
- name: AdmissionReceipt
  property_count: 6
  slug: vulk-dev-admission-receipt
- name: FileList
  property_count: 6
  slug: vulk-dev-file-list
- name: Instruction
  property_count: 3
  slug: vulk-dev-instruction
- name: Operation
  property_count: 13
  slug: vulk-dev-operation
- name: Project
  property_count: 13
  slug: vulk-dev-project
- name: Usage
  property_count: 10
  slug: vulk-dev-usage
jsonld:
- class_count: 14
  name: Vulk Dev Context
  property_count: 67
  slug: vulk-dev-context
layout: provider
modified: '2026-10-30'
name: vulk-dev
nav: Providers
network: true
overview: 'vulk-dev publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Models API, Operations API, Pay-as-you-go (previous VULK) API, and 2 more. Tagged areas include Company, AI, AppBuilder, NoCode, and 3D.


  The vulk-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  vulk-dev''s developer surface includes authentication, changelog, engineering blog, getting-started guide, API reference, documentation, pricing, and 27 more developer resources.'
plans:
- name: Vulk Dev Plans Pricing
  plan_count: 3
  slug: vulk-dev-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: vulk-dev API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: vulk-dev-rules
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 33.3
    contract_quality: 72.7
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
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
  name: Vulk Dev Authentication
  slug: vulk-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vulk Dev Domain Security
  slug: vulk-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vulk Dev Vulnerability Disclosure
  slug: vulk-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Vulk Dev Trust Center
  slug: vulk-dev-trust-center
  summary_line: PCI DSS, GDPR
skill_count: 2
skills:
- name: vulk-dev-create-project-and-retrieve-files
  slug: vulk-dev-create-project-and-retrieve-files
- name: vulk-dev-stop-operation
  slug: vulk-dev-stop-operation
slug: vulk-dev
tags:
- Company
- AI
- AppBuilder
- NoCode
- 3D
website: https://vulk.dev/
---
