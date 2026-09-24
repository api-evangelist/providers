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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-09-24'
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
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/IONSERVICES
  baseurl_source: declared
  description: ION document routing and processing
  name: Infor ION Documents API
  slug: infor-ion-documents-api
- baseURL: https://mingle-ionapi.inforcloudsuite.com/{tenant}/M3
  baseurl_source: declared
  description: Infor M3 business API programs
  name: Infor M3 API
  slug: infor-m3-api-api
- description: The Infor Document Management REST API, published on the Infor Developer Portal at developer.infor.com/api and served through the ION API Gateway under the IDM suite path. It covers the content reposi
  name: Infor Document Management (IDM) API
  slug: infor-idm-api
artifact_total: 23
asyncapis:
- description: Infor ION event framework AsyncAPI specification for event-driven integrations with Infor CloudSuite applications. The ION Event Hub publishes business events when transactions occur in Infor applicat
  name: Infor ION Events
  slug: infor-ion-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/agentic-access/infor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/infor-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/security/infor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/infor-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/security/infor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infor-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/authentication/infor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infor-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/scopes/infor-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/openapi/_original/infor-ion-api-gateway-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/infor-ion-api-gateway-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/json-schema/infor-m3-customer-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/infor-m3-customer-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/json-ld/infor-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/infor-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/asyncapi/infor-ion-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/infor-ion-events-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/llms/infor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infor-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/packages/infor-packages.yml
  title: ''
  type: Packages
  url: packages/infor-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/packages/infor-packages.yml
  title: ''
  type: SDKs
  url: packages/infor-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/cli/infor-cli.yml
  title: ''
  type: CLI
  url: cli/infor-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/components/infor-components.yml
  title: ''
  type: Components
  url: components/infor-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/mcp/infor-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/infor-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/mcp/infor-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/infor-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/conventions/infor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infor-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/errors/infor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infor-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/lifecycle/infor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/infor-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/lifecycle/infor-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/infor-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/conformance/infor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infor-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/conformance/infor-conformance.yml
  title: ''
  type: Compliance
  url: conformance/infor-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/data-model/infor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infor-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/changelog/infor-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/infor-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/asyncapi/infor-ion-events-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/infor-ion-events-asyncapi.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/plans/infor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infor-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/rate-limits/infor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/infor-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/finops/infor-finops.yml
  title: ''
  type: FinOps
  url: finops/infor-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/rules/infor-jsonschema-spectral-rules.yml
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
- name: Infor Finops
  service_category: Enterprise Software
  slug: infor-finops
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
overview: 'Infor publishes 2 APIs on the [APIs.io](https://apis.io/) network: ION Documents API and M3 API. Tagged areas include ERP, Manufacturing, Supply Chain, Cloud, and Integration.


  The Infor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Infor''s developer surface includes authentication, developer portal, documentation, engineering blog, CLI, changelog, API reference, and 42 more developer resources.'
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
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Infor API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: infor-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Infor API Rules
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
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.5
    catalog_earned_first_party: 16.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 72.4
    contract_governance: 31.8
    contract_quality: 64.8
    developer_ergonomics: 82.7
    discoverability: 75.9
    operational_transparency: 63.2
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/screenshots/infor-2026-06-20T183339.png
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
slug: infor
tags:
- ERP
- Manufacturing
- Supply Chain
- Cloud
- Integration
website: https://www.infor.com/
---
