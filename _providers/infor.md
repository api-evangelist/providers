---
access_model:
  confidence: high
  label: Contact sales · API access bundled with a CloudSuite subscription
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - probe
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Infor Agentic Access
  operation_count: 4
  slug: infor-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: The Infor M3 (CloudSuite Industrial) APIs provide access to production orders, inventory management, supply chain planning, and financial data for discrete and process manufacturing enterprises. The M
  name: Infor M3 / LN CloudSuite Industrial API
  slug: infor-m3-api
- description: 'Infor XtendM3 provides a Java SDK for extending and customizing Infor M3 (CloudSuite Industrial) business logic without modifying core code. Extensions are deployed and executed within the M3 runtime '
  name: Infor XtendM3 API
  slug: infor-xtendm3-api
- description: Infor CloudSuite Financials APIs provide integration with general ledger, accounts payable, accounts receivable, cash management, and financial reporting for enterprise finance operations.
  name: Infor CloudSuite Financials API
  slug: infor-cloudsuite-financials-api
- description: The Infor Document Management REST API, published on the Infor Developer Portal at developer.infor.com/api and served through the ION API Gateway under the IDM suite path. It covers the content reposi
  name: Infor Document Management (IDM) API
  slug: infor-idm-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The Contents API from Infor — 7 operation(s) for contents.
  name: Infor Contents API
  slug: infor-contents-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The ICUA API from Infor — 5 operation(s) for icua.
  name: Infor ICUA API
  slug: infor-icua-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The Languages API from Infor — 1 operation(s) for languages.
  name: Infor Languages API
  slug: infor-languages-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The Products API from Infor — 18 operation(s) for products.
  name: Infor Products API
  slug: infor-products-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The RecentTopics API from Infor — 2 operation(s) for recenttopics.
  name: Infor Recent Topics API
  slug: infor-recenttopics-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The S3 Docs API from Infor — 1 operation(s) for s3 docs.
  name: Infor S3 Docs API
  slug: infor-s3-docs-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The Search API from Infor — 6 operation(s) for search.
  name: Infor Search API
  slug: infor-search-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The Security API from Infor — 4 operation(s) for security.
  name: Infor Security API
  slug: infor-security-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The Solutions API from Infor — 3 operation(s) for solutions.
  name: Infor Solutions API
  slug: infor-solutions-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The UserFavorites API from Infor — 7 operation(s) for userfavorites.
  name: Infor User Favorites API
  slug: infor-userfavorites-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: The Web API from Infor — 12 operation(s) for web.
  name: Infor Web API
  slug: infor-web-api
artifact_total: 33
asyncapis:
- description: Infor ION event framework AsyncAPI specification for event-driven integrations with Infor CloudSuite applications. The ION Event Hub publishes business events when transactions occur in Infor applicat
  name: Infor ION Events
  slug: infor-ion-events-asyncapi
collections:
- collection_type: open
  name: Infor ION API Gateway
  slug: open-infor-ion-api-gateway
- collection_type: open
  name: Infor ION API Gateway ION Documents API
  slug: open-infor-ion-documents-api
- collection_type: open
  name: Infor ION API Gateway ION Documents M3 API API
  slug: open-infor-m3-api-api
common:
- group: other
  href: https://artifacts.apis.io/infor/overlays/infor-ion-documents-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infor-ion-documents-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/infor/overlays/infor-m3-api-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infor-m3-api-api-overlay.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.infor.com/products
- group: agent
  href: https://artifacts.apis.io/infor/agentic-access/infor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/infor-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/infor/security/infor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/infor-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/infor/security/infor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infor-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/infor/authentication/infor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infor-authentication.yml
- group: auth
  href: https://artifacts.apis.io/infor/scopes/infor-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/infor-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infor
- group: start
  title: ''
  type: Portal
  url: https://www.infor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infor.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/infor-cloud/ion-api-sdk
- group: auth
  title: ''
  type: Authentication
  url: https://github.com/infor-cloud/ion-api-sdk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infor.com/en/about/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infor.com/en/about/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.infor.com/blog
- group: company
  title: ''
  type: Website
  url: https://www.infor.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infor-cloud
- group: build
  title: ''
  type: SDKs
  url: https://github.com/infor-cloud/ion-api-sdk
- group: docs
  href: https://artifacts.apis.io/infor/openapi/_original/infor-ion-api-gateway-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/infor-ion-api-gateway-openapi.yml
- group: docs
  href: https://artifacts.apis.io/infor/json-schema/infor-m3-customer-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/infor-m3-customer-schema.json
- group: design
  href: https://artifacts.apis.io/infor/json-ld/infor-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/infor-context.jsonld
- group: docs
  href: https://artifacts.apis.io/infor/asyncapi/infor-ion-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/infor-ion-events-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/infor/llms/infor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infor-llms.txt
- group: build
  href: https://artifacts.apis.io/infor/packages/infor-packages.yml
  title: ''
  type: Packages
  url: packages/infor-packages.yml
- group: build
  href: https://artifacts.apis.io/infor/packages/infor-packages.yml
  title: ''
  type: SDKs
  url: packages/infor-packages.yml
- group: build
  href: https://artifacts.apis.io/infor/cli/infor-cli.yml
  title: ''
  type: CLI
  url: cli/infor-cli.yml
- group: design
  href: https://artifacts.apis.io/infor/components/infor-components.yml
  title: ''
  type: Components
  url: components/infor-components.yml
- group: agent
  href: https://artifacts.apis.io/infor/mcp/infor-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/infor-mcp.yml
- group: build
  href: https://artifacts.apis.io/infor/mcp/infor-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/infor-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/infor/conventions/infor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infor-conventions.yml
- group: design
  href: https://artifacts.apis.io/infor/errors/infor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infor-problem-types.yml
- group: design
  href: https://artifacts.apis.io/infor/lifecycle/infor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/infor-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/infor/lifecycle/infor-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/infor-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/infor/conformance/infor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infor-conformance.yml
- group: auth
  href: https://artifacts.apis.io/infor/conformance/infor-conformance.yml
  title: ''
  type: Compliance
  url: conformance/infor-conformance.yml
- group: design
  href: https://artifacts.apis.io/infor/data-model/infor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infor-data-model.yml
- group: operate
  href: https://artifacts.apis.io/infor/changelog/infor-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/infor-changelog.yml
- group: agent
  href: https://artifacts.apis.io/infor/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/infor/asyncapi/infor-ion-events-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/infor-ion-events-asyncapi.yml
- group: commercial
  href: https://artifacts.apis.io/infor/plans/infor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/infor/rate-limits/infor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/infor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/infor/finops/infor-finops.yml
  title: ''
  type: FinOps
  url: finops/infor-finops.yml
- group: design
  href: https://artifacts.apis.io/infor/rules/infor-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/infor-jsonschema-spectral-rules.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.infor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.infor.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.infor.com/tutorials
- group: operate
  title: ''
  type: Support
  url: https://www.infor.com/customer-success/support
- group: operate
  title: ''
  type: Community
  url: https://community.infor.com/categories/developer
- group: start
  title: ''
  type: Login
  url: https://concierge.infor.com
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.infor.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.infor.com/
created: '2026-04-28'
description: Infor provides industry-specific cloud ERP platforms including CloudSuite Industrial (M3), CloudSuite Financials, and Infor LN. The Infor ION API Gateway enables OAuth 2.0-based integration across Infor applications and third-party systems. SDKs are available via the infor-cloud GitHub organization for Java, .NET, Go, and HTML5 development.
finops:
- has_sources: true
  method: derived
  name: Infor Finops
  primary_unit: ''
  service_category: ''
  slug: infor-finops
  template: true
image: https://www.infor.com/logo-infor.png
json_schemas:
- name: Infor M3 Customer
  property_count: 22
  slug: infor-m3-customer
jsonld:
- class_count: 22
  name: Infor Context
  property_count: 6
  slug: infor-context
layout: provider
modified: '2026-09-16'
name: Infor
nav: Providers
network: true
overview: 'Infor publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contents API, ICUA API, Languages API, and 12 more. Tagged areas include ERP, Manufacturing, Supply Chain, Cloud, and Integration.


  The Infor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Infor''s developer surface includes pricing, authentication, developer portal, documentation, engineering blog, CLI, changelog, and 45 more developer resources.'
plans:
- name: Infor Plans Pricing
  plan_count: 1
  slug: infor-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Infor Rate Limits
  slug: infor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Infor — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: infor-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Infor — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: infor-jsonschema-spectral-rules
scopes:
- name: Infor Scopes
  scope_count: 0
  slug: infor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 65.5
    catalog_earned_first_party: 16.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 69.7
    contract_governance: 31.8
    contract_quality: 61.9
    developer_ergonomics: 82.7
    discoverability: 73.2
    operational_transparency: 63.2
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 78.6
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/infor/infor-2026-06-20T183339.png
security:
- kind: authentication
  name: Infor Authentication
  slug: infor-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Infor Domain Security
  slug: infor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Infor Trust Center
  slug: infor-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
skill_count: 2
skills:
- name: infor-call-m3-business-api
  slug: infor-call-m3-business-api
- name: infor-read-ion-documents
  slug: infor-read-ion-documents
slug: infor
tags:
- ERP
- Manufacturing
- Supply Chain
- Cloud
- Integration
website: https://www.infor.com/
---
