---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Blendduck Com Agentic Access
  operation_count: 25
  slug: blendduck-com-agentic-access
  summary_line: 25 operations · 11 acting
api_count: 1
apis:
- baseURL: https://blendduck.com
  baseurl_source: declared
  description: Attributed post, campaign, channel, model, topic, and approval performance.
  name: BlendDuck Analytics API
  slug: blendduck-com-analytics-api
- baseURL: https://blendduck.com
  baseurl_source: declared
  description: Connected social accounts and safe health state.
  name: BlendDuck Channels API
  slug: blendduck-com-channels-api
- baseURL: https://blendduck.com
  baseurl_source: declared
  description: Inspected media assets and upload ingestion.
  name: BlendDuck Media API
  slug: blendduck-com-media-api
- baseURL: https://blendduck.com
  baseurl_source: declared
  description: Logical posts with independently addressed targets.
  name: BlendDuck Posts API
  slug: blendduck-com-posts-api
- baseURL: https://blendduck.com
  baseurl_source: declared
  description: Provider capability and configuration declarations.
  name: BlendDuck Providers API
  slug: blendduck-com-providers-api
- baseURL: https://blendduck.com
  baseurl_source: declared
  description: Organization metadata selected by the bearer API key.
  name: BlendDuck Tenant API
  slug: blendduck-com-tenant-api
- baseURL: https://blendduck.com
  baseurl_source: declared
  description: Organization event subscriptions and signing-secret lifecycle.
  name: BlendDuck Webhooks API
  slug: blendduck-com-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Blendduck Com Webhooks
  slug: blendduck-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/blendduck-com/agentic-access/blendduck-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blendduck-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/blendduck-com/plans/blendduck-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blendduck-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/rules/blendduck-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blendduck-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/json-ld/blendduck-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blendduck-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blendduck-com/vocabulary/blendduck-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blendduck-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blendduck-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/asyncapi/blendduck-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/blendduck-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/data-model/blendduck-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blendduck-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/conventions/blendduck-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blendduck-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/conventions/blendduck-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blendduck-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/blendduck-com/authentication/blendduck-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blendduck-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/errors/blendduck-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blendduck-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blendduck-com/conformance/blendduck-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blendduck-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blendduck-com/llms/blendduck-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blendduck-com-llms.txt
- group: other
  href: https://artifacts.apis.io/blendduck-com/a2a/blendduck-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blendduck-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/blendduck-com/well-known/blendduck-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blendduck-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blendduck-com/hosts/blendduck-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blendduck-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blendduck-com/vendors/blendduck-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blendduck-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/blendduck-com/packages/blendduck-com-packages.yml
  title: ''
  type: SDKs
  url: packages/blendduck-com-packages.yml
- group: build
  href: https://artifacts.apis.io/blendduck-com/packages/blendduck-com-packages.yml
  title: ''
  type: Packages
  url: packages/blendduck-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blendduck.com/terms
- group: operate
  title: ''
  type: Support
  url: https://blendduck.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://blendduck.com/status
- group: auth
  title: ''
  type: Security
  url: https://blendduck.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blendduck.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://blendduck.com/pricing
- group: start
  title: ''
  type: Login
  url: https://blendduck.com/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blendduck
- group: operate
  title: ''
  type: ChangeLog
  url: https://blendduck.com/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://blendduck.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blendduck.com/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blendduck.com/
- group: docs
  title: ''
  type: APIReference
  url: https://blendduck.com/docs
- group: auth
  href: https://artifacts.apis.io/blendduck-com/security/blendduck-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blendduck-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blendduck.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://blendduck.com/openapi.json
  - status: null
    url: https://docs.blendduck.com/mcp
  - status: 401
    url: https://blendduck.com/api/mcp
  - status: 401
    url: https://work.blendduck.com/v1/graphql
  - status: 200
    url: https://blendduck.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BlendDuck is an agent‑native social workspace that unifies brand voice, knowledge, and guardrails for teams and AI agents. It lets brands turn ideas into channel‑ready content, offering shared workflows, collaborative editing, and controlled publishing, all while keeping AI agents aligned with brand guidelines. The platform emphasizes seamless integration, real‑time collaboration, and secure content management for modern marketing teams.
image: https://blendduck.com/og.png
json_schemas:
- name: AnalyticsResponse
  property_count: 2
  slug: blendduck-com-analytics-response
- name: PostResponse
  property_count: 2
  slug: blendduck-com-post-response
- name: PostsResponse
  property_count: 2
  slug: blendduck-com-posts-response
- name: ProviderResponse
  property_count: 2
  slug: blendduck-com-provider-response
- name: ProvidersResponse
  property_count: 2
  slug: blendduck-com-providers-response
- name: UpdatePostInput
  property_count: 10
  slug: blendduck-com-update-post-input
jsonld:
- class_count: 25
  name: Blendduck Com Context
  property_count: 20
  slug: blendduck-com-context
layout: provider
modified: '2026-11-02'
name: BlendDuck
nav: Providers
network: true
overview: 'BlendDuck publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Channels API, Media API, and 4 more. Tagged areas include Social, Collaboration, Artificial Intelligence, Branding, and Marketing.


  The BlendDuck catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BlendDuck''s developer surface includes authentication, support, pricing, changelog, engineering blog, getting-started guide, documentation, and 28 more developer resources.'
plans:
- name: Blendduck Com Plans Pricing
  plan_count: 4
  slug: blendduck-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: BlendDuck API Rules
  rule_count: 68
  severity_counts:
    error: 65
    hint: 0
    info: 1
    warn: 2
  slug: blendduck-com-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 70.6
    developer_ergonomics: 38.7
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blendduck Com Authentication
  slug: blendduck-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blendduck Com Domain Security
  slug: blendduck-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: blendduck-com-create-and-test-webhook
  slug: blendduck-com-create-and-test-webhook
- name: blendduck-com-media-upload-and-retrieve
  slug: blendduck-com-media-upload-and-retrieve
slug: blendduck-com
tags:
- Social
- Collaboration
- Artificial Intelligence
- Branding
- Marketing
- Company
website: https://blendduck.com/
---
