---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Account information, stats, balance and preferred translators.
  name: Gengo Account API
  slug: gengo-account-api
- description: Manage translation glossaries.
  name: Gengo Glossary API
  slug: gengo-glossary-api
- description: Operations on a single translation job.
  name: Gengo Job API
  slug: gengo-job-api
- description: Submit and manage groups of translation jobs.
  name: Gengo Jobs API
  slug: gengo-jobs-api
- description: Operations on an order (a group of jobs submitted together).
  name: Gengo Order API
  slug: gengo-order-api
- description: Language pairs, supported languages, quotes and unit counts.
  name: Gengo Service API
  slug: gengo-service-api
artifact_total: 17
asyncapis:
- description: ''
  name: Gengo Callbacks Webhooks
  slug: gengo-callbacks-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: OpenAPI
  url: openapi/_original/gengo-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gengo-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/gengo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gengo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gengo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gengo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/gengo-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/gengo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gengo-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gengo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gengo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gengo-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gengo-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gengo-callbacks-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gengo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gengo.com
created: '2026-07-17'
description: 'Gengo is a people-powered translation platform that delivers fast, affordable, high-quality human translation in every major language through a global network of thousands of certified translators. The Gengo API (v2) lets developers order translation programmatically: submit text or file jobs, group them into orders, run cost quotes, look up supported language pairs and tiers, manage glossaries, retrieve completed translations and revisions, exchange comments with translators, and receive job-status updates through per-job callback URLs. Authentication uses a public API key plus an HMAC-SHA1 request signature, with a full sandbox for testing. Gengo was surfaced as a portfolio company of 500 Global and Point Nine and enriched into the API Evangelist network.'
image: https://gengo.com/wp-content/themes/gengo_theme/images/common/apple-touch-icon-precomposed.png
layout: provider
mcp_servers:
- description: ''
  name: Gengo MCP Server
  slug: gengo-mcp-server
modified: '2026-07-19'
name: Gengo
nav: Providers
network: true
overview: 'Gengo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Glossary API, Job API, and 3 more. Tagged areas include Company, Translation, Localization, Human Translation, and Language Services.


  The Gengo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gengo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 45.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gengo/refs/heads/main/screenshots/gengo-2026-07-25T215611.png
security:
- kind: authentication
  name: Gengo Authentication
  slug: gengo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gengo Domain Security
  slug: gengo-domain-security
  summary_line: TLSv1.3 · DMARC
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
