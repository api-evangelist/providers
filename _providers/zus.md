---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Zus Agentic Access
  operation_count: 15
  slug: zus-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- description: OAuth2 token issuance and exchange.
  name: Zus Health Auth API
  slug: zus-auth-api
- description: DocumentReference and Binary resources.
  name: Zus Health Documents API
  slug: zus-documents-api
- description: General FHIR R4 resources.
  name: Zus Health FHIR API
  slug: zus-fhir-api
- description: FHIR R4 Patient resources.
  name: Zus Health Patient API
  slug: zus-patient-api
- description: Jobs that retrieve external data into the Zus Aggregated Profile.
  name: Zus Health Patient History API
  slug: zus-patient-history-api
- description: Zus FHIR R4 REST API plus Auth Service and Patient History APIs. Implements FHIR R4 (v4.0.1) across 128 resource types with instance-level CRUD, transaction Bundles, conditional create/update/delete b
  name: Zus FHIR & Platform API
  slug: zus-fhir-platform-api
- description: The Zus FHIR Query Service (FQS) is a read-only GraphQL API over the FHIR data model, exposed at a single endpoint. Supports UPID-scoped (one-human) and builder-scoped queries across resource types in
  name: Zus FHIR GraphQL API (FQS)
  slug: zus-fhir-graphql-api-fqs
artifact_total: 22
asyncapis:
- description: ''
  name: Zus Zushooks
  slug: zus-zushooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zus Health Auth API
  slug: open-zus-auth-api
- collection_type: open
  name: Zus Health Auth Documents API
  slug: open-zus-documents-api
- collection_type: open
  name: Zus Health Auth FHIR API
  slug: open-zus-fhir-api
- collection_type: open
  name: Zus Health Auth Patient API
  slug: open-zus-patient-api
- collection_type: open
  name: Zus Health Auth Patient History API
  slug: open-zus-patient-history-api
- collection_type: open
  name: Zus Health API
  slug: open-zus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zus-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zushealth
- group: company
  title: ''
  type: Website
  url: https://zushealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zushealth.com
- group: commercial
  title: ''
  type: Plans
  url: plans/zus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zus-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://zushealth.com/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zushealth.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zushealth.com/docs/intro-to-zus
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zushealth.com/reference/general
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zushealth.com/docs/getting-started-with-the-zap
- group: operate
  title: ''
  type: Support
  url: https://docs.zushealth.com/contact-support
- group: company
  title: ''
  type: Blog
  url: https://zushealth.com/team/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zushealth
- group: start
  title: ''
  type: SignUp
  url: https://docs.zushealth.com/page/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.zushealth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zushealth.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zushealth.com/website-privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zusapi.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zus-health/workspace/zus-health-workspace
- group: auth
  title: ''
  type: Compliance
  url: https://zushealth.com/platform/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zus-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zus-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zus-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/zus-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zus-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zus-zushooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zus-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zus-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zus-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zus-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zus-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zus-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/zus-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zus-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zus-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zus-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/zus-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zus-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zus-zushooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zus-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zus-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zus-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zus-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zus-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zus-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/zus-components.yml
created: '2026-06-21'
description: Zus Health is a shared health-data platform that aggregates a patient's clinical history from external networks into the Zus Aggregated Profile (ZAP). It exposes a FHIR R4 (v4.0.1) REST API secured with OAuth2 Bearer tokens, Patient History APIs, document ingestion and retrieval, Zushooks webhooks, a GraphQL FHIR Query Service, and embeddable open-source React components.
finops:
- name: Zus Finops
  service_category: Healthcare
  slug: zus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zus.png
layout: provider
mcp_servers:
- description: ''
  name: Zus Health MCP Server
  slug: zus-health-mcp-server
modified: '2026-06-21'
name: Zus Health
nav: Providers
network: true
overview: 'Zus Health publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Documents API, FHIR API, and 2 more. Tagged areas include Health, FHIR, Interoperability, Patient Data, and Healthcare.


  The Zus Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zus Health''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, signup flow, and 48 more developer resources.'
plans:
- name: Zus Plans Pricing
  plan_count: 2
  slug: zus-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Zus Rate Limits
  slug: zus-rate-limits
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 18.2
    contract_quality: 28.3
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zus/refs/heads/main/screenshots/zus-2026-08-17T083124.png
security:
- kind: authentication
  name: Zus Authentication
  slug: zus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zus Domain Security
  slug: zus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zus
tags:
- Health
- FHIR
- Interoperability
- Patient Data
- Healthcare
website: https://zushealth.com
---
