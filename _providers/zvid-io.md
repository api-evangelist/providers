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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Zvid Io Agentic Access
  operation_count: 52
  slug: zvid-io-agentic-access
  summary_line: 52 operations · 24 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: API key management operations
  name: zvid-io API Keys API
  slug: zvid-io-api-keys-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Free creative planning and project-authoring helpers
  name: zvid-io Authoring API
  slug: zvid-io-authoring-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: One template + many variable sets in a single request
  name: zvid-io Bulk Render API
  slug: zvid-io-bulk-render-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Credit balance and transaction management
  name: zvid-io Credits API
  slug: zvid-io-credits-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Designed examples and reusable creative assets
  name: zvid-io Library API
  slug: zvid-io-library-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Editor draft projects (open them in the visual editor)
  name: zvid-io Projects API
  slug: zvid-io-projects-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Video and image rendering operations
  name: zvid-io Render API
  slug: zvid-io-render-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Zvid's stock library
  name: zvid-io Stock API
  slug: zvid-io-stock-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Stored, variable-driven project templates
  name: zvid-io Templates API
  slug: zvid-io-templates-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: Your hosted media library
  name: zvid-io Uploads API
  slug: zvid-io-uploads-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: User profile operations
  name: zvid-io User API
  slug: zvid-io-user-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: HMAC-signed render event deliveries
  name: zvid-io Webhooks API
  slug: zvid-io-webhooks-api
- baseURL: https://api.zvid.io
  baseurl_source: declared
  description: The Zvid API API from zvid-io — 0 operation(s) for zvid api.
  name: zvid-io Zvid API
  slug: zvid-io-zvid-api-api
artifact_total: 30
asyncapis:
- description: ''
  name: Zvid Io Webhooks
  slug: zvid-io-webhooks
common:
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zvid.io/docs/endpoints/zvid-api/
- group: agent
  href: https://artifacts.apis.io/zvid-io/agentic-access/zvid-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zvid-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/zvid-io/plans/zvid-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zvid-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zvid-io/rules/zvid-io-rules.yml
  title: ''
  type: Spectral
  url: rules/zvid-io-rules.yml
- group: design
  href: https://artifacts.apis.io/zvid-io/json-ld/zvid-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zvid-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/zvid-io/vocabulary/zvid-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zvid-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/zvid-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/zvid-io/asyncapi/zvid-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/zvid-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/zvid-io/data-model/zvid-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zvid-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/zvid-io/authentication/zvid-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zvid-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/zvid-io/errors/zvid-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zvid-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zvid-io/conformance/zvid-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zvid-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zvid-io/llms/zvid-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zvid-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/zvid-io/well-known/zvid-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zvid-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/zvid-io/hosts/zvid-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zvid-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/zvid-io/vendors/zvid-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zvid-io-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://zvid.io/features/webhooks
- group: build
  title: ''
  type: SDKs
  url: https://zvid.io/features/sdks
- group: company
  title: ''
  type: Newsroom
  url: https://zvid.io/templates/category/news
- group: start
  title: ''
  type: Login
  url: https://app.zvid.io/login
- group: auth
  href: https://artifacts.apis.io/zvid-io/security/zvid-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zvid-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zvid.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://editor.zvid.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zvid.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zvid.io/docs/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://zvid.io/contact
- group: company
  title: ''
  type: Blog
  url: https://zvid.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zvid-io
- group: commercial
  title: ''
  type: Pricing
  url: https://zvid.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zvid.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zvid.io/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zvid-io/workspace
created: '2026-10-31'
description: Zvid provides a video generation platform that lets developers create videos and images programmatically via a JSON‑based API. Users can design templates visually in a web editor, then render personalized videos at scale, with support for bulk rendering, webhooks, and credit‑based pricing. The service offers a free tier with monthly credits and paid plans for higher volume, and includes extensive documentation, SDKs, and integration guides.
image: https://zvid.io/logo.png
json_schemas:
- name: BulkRenderAccepted
  property_count: 10
  slug: zvid-io-bulk-render-accepted
- name: CreativePlanRequest
  property_count: 11
  slug: zvid-io-creative-plan-request
- name: RenderJobRequest
  property_count: 6
  slug: zvid-io-render-job-request
- name: RenderJobStatus
  property_count: 9
  slug: zvid-io-render-job-status
- name: Zvid authoring project and template input
  property_count: 19
  slug: zvid-io-render-payload
- name: UserProfile
  property_count: 3
  slug: zvid-io-user-profile
jsonld:
- class_count: 94
  name: Zvid Io Context
  property_count: 266
  slug: zvid-io-context
layout: provider
modified: '2026-10-31'
name: zvid-io
nav: Providers
network: true
overview: 'zvid-io publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Authoring API, Bulk Render API, and 10 more. Tagged areas include Company, Video, Automation, and Media.


  The zvid-io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  zvid-io''s developer surface includes API reference, authentication, documentation, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Zvid Io Plans Pricing
  plan_count: 5
  slug: zvid-io-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: zvid-io API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 4
  slug: zvid-io-rules
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 74.5
    developer_ergonomics: 45.8
    discoverability: 58.0
    operational_transparency: 6.6
  previous_composite: 60.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zvid Io Authentication
  slug: zvid-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zvid Io Domain Security
  slug: zvid-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: zvid-io-create-and-preview-template
  slug: zvid-io-create-and-preview-template
- name: zvid-io-create-and-test-webhook
  slug: zvid-io-create-and-test-webhook
- name: zvid-io-project-lifecycle
  slug: zvid-io-project-lifecycle
- name: zvid-io-upload-file
  slug: zvid-io-upload-file
slug: zvid-io
tags:
- Company
- Video
- Automation
- Media
website: https://zvid.io/
---
