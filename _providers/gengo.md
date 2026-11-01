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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.gengo.com/v2
  baseurl_source: declared
  description: Account information, stats, balance and preferred translators.
  name: Gengo Account API
  slug: gengo-account-api
- baseURL: https://api.gengo.com/v2
  baseurl_source: declared
  description: Manage translation glossaries.
  name: Gengo Glossary API
  slug: gengo-glossary-api
- baseURL: https://api.gengo.com/v2
  baseurl_source: declared
  description: Operations on a single translation job.
  name: Gengo Job API
  slug: gengo-job-api
- baseURL: https://api.gengo.com/v2
  baseurl_source: declared
  description: Submit and manage groups of translation jobs.
  name: Gengo Jobs API
  slug: gengo-jobs-api
- baseURL: https://api.gengo.com/v2
  baseurl_source: declared
  description: Operations on an order (a group of jobs submitted together).
  name: Gengo Order API
  slug: gengo-order-api
- baseURL: https://api.gengo.com/v2
  baseurl_source: declared
  description: Language pairs, supported languages, quotes and unit counts.
  name: Gengo Service API
  slug: gengo-service-api
artifact_total: 19
asyncapis:
- description: ''
  name: Gengo Callbacks Webhooks
  slug: gengo-callbacks-webhooks
collections:
- collection_type: open
  name: Gengo Account API
  slug: open-gengo-account-api
- collection_type: open
  name: Gengo Account Glossary API
  slug: open-gengo-glossary-api
- collection_type: open
  name: Gengo Account Job API
  slug: open-gengo-job-api
- collection_type: open
  name: Gengo Account Jobs API
  slug: open-gengo-jobs-api
- collection_type: open
  name: Gengo Account Order API
  slug: open-gengo-order-api
- collection_type: open
  name: Gengo Account Service API
  slug: open-gengo-service-api
common:
- group: commercial
  href: https://artifacts.apis.io/gengo/plans/gengo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gengo-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gengo.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gengo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gengo.com/v2/api_methods/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gengo.com/v2/first_steps/
- group: operate
  title: ''
  type: Support
  url: https://support.gengo.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://gengo.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gengo
- group: commercial
  title: ''
  type: Pricing
  url: https://gengo.com/pricing-languages/
- group: start
  title: ''
  type: SignUp
  url: https://gengo.com/auth/form/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gengo.com/terms-of-service/
- group: docs
  href: https://artifacts.apis.io/gengo/openapi/_original/gengo-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/gengo-openapi.yml
- group: auth
  href: https://artifacts.apis.io/gengo/authentication/gengo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gengo-authentication.yml
- group: build
  href: https://artifacts.apis.io/gengo/packages/gengo-packages.yml
  title: ''
  type: Packages
  url: packages/gengo-packages.yml
- group: build
  href: https://artifacts.apis.io/gengo/packages/gengo-packages.yml
  title: ''
  type: SDKs
  url: packages/gengo-packages.yml
- group: agent
  href: https://artifacts.apis.io/gengo/mcp/gengo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gengo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gengo/llms/gengo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gengo-llms.txt
- group: other
  href: https://artifacts.apis.io/gengo/overlays/gengo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gengo-overlay.yaml
- group: design
  href: https://artifacts.apis.io/gengo/conformance/gengo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gengo-conformance.yml
- group: design
  href: https://artifacts.apis.io/gengo/errors/gengo-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/gengo-error-codes.yml
- group: design
  href: https://artifacts.apis.io/gengo/lifecycle/gengo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gengo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gengo/conventions/gengo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gengo-conventions.yml
- group: design
  href: https://artifacts.apis.io/gengo/data-model/gengo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gengo-data-model.yml
- group: start
  href: https://artifacts.apis.io/gengo/sandbox/gengo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gengo-sandbox.yml
- group: design
  href: https://artifacts.apis.io/gengo/asyncapi/gengo-callbacks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gengo-callbacks-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/gengo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/gengo/security/gengo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gengo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gengo.com
created: '2026-07-17'
description: 'Gengo is a people-powered translation platform that delivers fast, affordable, high-quality human translation in every major language through a global network of thousands of certified translators. The Gengo API (v2) lets developers order translation programmatically: submit text or file jobs, group them into orders, run cost quotes, look up supported language pairs and tiers, manage glossaries, retrieve completed translations and revisions, exchange comments with translators, and receive job-status updates through per-job callback URLs. Authentication uses a public API key plus an HMAC-SHA1 request signature, with a full sandbox for testing. Gengo was surfaced as a portfolio company of 500 Global and Point Nine and enriched into the API Evangelist network.'
finops:
- has_sources: true
  method: derived
  name: Gengo Finops
  primary_unit: word
  service_category: ''
  slug: gengo-finops
  template: false
image: https://gengo.com/wp-content/themes/gengo_theme/images/common/apple-touch-icon-precomposed.png
layout: provider
modified: '2026-07-19'
name: Gengo
nav: Providers
network: true
overview: 'Gengo publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Glossary API, Job API, and 3 more. Tagged areas include Company, Translation, Localization, Human Translation, and Language Services.


  The Gengo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gengo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Gengo Plans Pricing
  plan_count: 3
  slug: gengo-plans-pricing
random_paper: 0
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 43.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gengo/gengo-2026-07-25T215611.png
security:
- kind: authentication
  name: Gengo Authentication
  slug: gengo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gengo Domain Security
  slug: gengo-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Monitor and manage Gengo translation jobs
  slug: gengo-manage-jobs
- name: Order human translation with Gengo
  slug: gengo-order-translation
slug: gengo
tags:
- Company
- Translation
- Localization
- Human Translation
- Language Services
- Internationalization
- Content
- Text
website: https://gengo.com
---
