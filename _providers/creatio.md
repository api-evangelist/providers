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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-04'
api_count: 8
apis:
- baseURL: https://mycreatio.com/0/odata
  baseurl_source: declared
  description: OData 4 (recommended) and legacy OData 3 access to Creatio platform entities. The OData 4 service is at /0/odata with EDMX metadata at /0/odata/$metadata; supports $filter/$select/$expand/$orderby/$to
  name: Creatio OData API
  slug: creatio-odata-api
- description: 'RESTful DataService web service for reading and writing platform records via InsertQuery, SelectQuery, UpdateQuery, DeleteQuery, and BatchQuery over HTTP POST. Supports JSON/XML/CSV/JSV serialization '
  name: Creatio DataService API
  slug: creatio-dataservice-api
- description: ProcessEngineService.svc runs Creatio business processes from an external application over HTTP. Execute() runs a process by schema name, passing incoming parameters and returning the execution result
  name: Creatio Business Process Service
  slug: creatio-business-process-service
- description: Inbound webhook receiver. Lets an external app push data into Creatio in real time over an authenticated POST, writing a record into a target object named by the EntityName parameter. Contact, Lead, O
  name: Creatio Webhook Service
  slug: creatio-webhook-service
- baseURL: https://mycreatio.com/0/odata
  baseurl_source: declared
  description: The Clear Bundles API from Creatio — 1 operation(s) for clear bundles.
  name: Creatio Clear Bundles API
  slug: creatio-clear-bundles-api
- baseURL: https://mycreatio.com/0/odata
  baseurl_source: declared
  description: The Minify Content API from Creatio — 1 operation(s) for minify content.
  name: Creatio Minify Content API
  slug: creatio-minify-content-api
- baseURL: https://mycreatio.com/0/odata
  baseurl_source: declared
  description: The Odata API from Creatio — 1 operation(s) for odata.
  name: Creatio Odata API
  slug: creatio-odata-api
- baseURL: https://mycreatio.com/0/odata
  baseurl_source: declared
  description: The Process Content API from Creatio — 1 operation(s) for process content.
  name: Creatio Process Content API
  slug: creatio-process-content-api
artifact_total: 20
asyncapis:
- description: ''
  name: Creatio Webhooks
  slug: creatio-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/rules/creatio-rules.yml
  title: ''
  type: Spectral
  url: rules/creatio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/json-ld/creatio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/creatio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/vocabulary/creatio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/creatio-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/data-model/creatio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/creatio-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/cli/creatio-cli.yml
  title: ''
  type: CLI
  url: cli/creatio-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/llms/creatio-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/creatio-api-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/hosts/creatio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/creatio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/vendors/creatio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/creatio-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.creatio.com/our-technologies/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.creatio.com/company/news
- group: company
  title: ''
  type: Website
  url: https://www.creatio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://academy.creatio.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://academy.creatio.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://academy.creatio.com/docs/developer/integrations_and_api/data_services/odata/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.creatio.com/docs/developer/integrations_and_api/integration_options
- group: operate
  title: ''
  type: Support
  url: https://community.creatio.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.creatio.com/services/support/options
- group: company
  title: ''
  type: Blog
  url: https://www.creatio.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.creatio.com/products/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.creatio.com/trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creatio.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creatio.com/privacy-policy
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.creatio.com/
- group: operate
  title: ''
  type: Community
  url: https://community.creatio.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/authentication/creatio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/creatio-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/conventions/creatio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/creatio-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/conformance/creatio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/creatio-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/security/creatio-trust-center.yml
  title: ''
  type: Compliance
  url: security/creatio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/security/creatio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/creatio-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/lifecycle/creatio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/creatio-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/changelog/creatio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/creatio-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/security/creatio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creatio-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/llms/creatio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/creatio-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/packages/creatio-packages.yml
  title: ''
  type: Packages
  url: packages/creatio-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/packages/creatio-packages.yml
  title: ''
  type: SDKs
  url: packages/creatio-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/plans/creatio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/creatio-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/rate-limits/creatio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/creatio-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/asyncapi/creatio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/creatio-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/errors/creatio-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/creatio-error-codes.yml
coverage:
  checked: '2026-10-04'
  detail: The Creatio developer portal provides documentation but no OpenAPI or other machine‑readable contract was found (e.g., https://api.creatio.com/openapi.json returned 404).
  evidence:
  - status: 404
    url: https://api.creatio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Creatio is a global software vendor of an AI-native no-code platform for customer relationship management (CRM) and workflow / business process automation. Its product line spans Sales Creatio, Marketing Creatio, and Service Creatio, built on Studio Creatio — a no-code toolkit with visual designers, AI agents, and a business process engine. Creatio serves banking, insurance, manufacturing, high tech, retail, CPG, pharmaceuticals, telecom, the public sector, and other industries. For integrations, Creatio exposes platform data and processes over an OData 4 service (recommended), a legacy OData 3 service, and the RESTful DataService web service, secured with forms (cookie) authentication via AuthService.svc or OAuth 2.0 through the Creatio Identity Service. Extensions and connectors are distributed through the Creatio Marketplace. This profile was enriched by the API Evangelist enrichment pipeline from Creatio's public developer documentation.
image: https://www.creatio.com/sites/default/files/creatio-logo.svg
json_schemas:
- name: PostClearBundlesRequest
  property_count: 3
  slug: creatio-post-clear-bundles-request
- name: PostMinifyContentRequest
  property_count: 2
  slug: creatio-post-minify-content-request
- name: Post0OdataOdataidRequest
  property_count: 1
  slug: creatio-post0-odata-odataid-request
- name: Post0OdataOdataidResponse
  property_count: 2
  slug: creatio-post0-odata-odataid-response
jsonld:
- class_count: 4
  name: Creatio Context
  property_count: 3
  slug: creatio-context
layout: provider
modified: '2026-08-13'
name: Creatio
nav: Providers
network: true
overview: 'Creatio publishes 8 APIs on the [APIs.io](https://apis.io/) network, including OData API, Clear Bundles API, Minify Content API, and 5 more. Tagged areas include Company, Software-as-a-Service, CRM, No-Code, and Low-Code.


  The Creatio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Creatio''s developer surface includes CLI, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 32 more developer resources.'
plans:
- name: Creatio Plans Pricing
  plan_count: 3
  slug: creatio-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Creatio Rate Limits
  slug: creatio-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Creatio API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: creatio-rules
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 83.8
    catalog_earned_first_party: 24.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 28.3
    developer_ergonomics: 71.4
    discoverability: 80.4
    operational_transparency: 65.8
  previous_composite: 59.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/screenshots/creatio-2026-07-25T210701.png
security:
- kind: authentication
  name: Creatio Authentication
  slug: creatio-authentication
  summary_line: http/oauth2/cookie · 4 schemes
- kind: domain-security
  name: Creatio Domain Security
  slug: creatio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Creatio Trust Center
  slug: creatio-trust-center
  summary_line: ISO/IEC 27001:2013, SOC 1, SOC 2, GDPR, HIPAA, FedRAMP
slug: creatio
tags:
- Company
- Software-as-a-Service
- CRM
- No-Code
- Low-Code
- Business Process Management
- Workflow Automation
- Sales
- Marketing
- Customer Service
- OData
- AI Agents
website: https://www.creatio.com/
---
