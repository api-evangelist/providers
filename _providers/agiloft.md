---
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-09-24'
api_count: 3
apis:
- description: The Agiloft REST interface, served from every Agiloft knowledgebase under /ewws/. It exposes twenty documented operations — EWCreate, EWRead, EWUpdate, EWDelete, EWUpsert, EWSelect, EWSearch, EWLogin,
  name: Agiloft CLM REST API
  slug: rest
- description: Agiloft's outbound event surface. A webhook is registered per table and event type (Create, Update or Delete), optionally filtered by a record-filter expression and by modification type (Email, Web or
  name: Agiloft CLM Webhooks
  slug: webhooks
- description: Agiloft's SCIM 2.0 user provisioning endpoint, served per knowledgebase at /scim/v2 and authenticated with a bearer token generated from the KB's SCIM profile. An identity provider that speaks SCIM 2.
  name: Agiloft CLM SCIM 2.0 Service
  slug: scim
artifact_total: 10
asyncapis:
- description: ''
  name: Agiloft Webhooks
  slug: agiloft-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/security/agiloft-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agiloft-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/security/agiloft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agiloft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agiloft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.agiloft.com/space/HELP/43716366/API%20Web%20Services
- group: docs
  title: ''
  type: Documentation
  url: https://help.agiloft.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.agiloft.com/space/HELP/43715778/REST%20Interface
- group: start
  title: ''
  type: GettingStarted
  url: https://help.agiloft.com/space/HELP/929595396/OpenAPI%20Interface
- group: operate
  title: ''
  type: Support
  url: https://community.agiloft.com/home
- group: company
  title: ''
  type: Blog
  url: https://www.agiloft.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agiloft.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.agiloft.com/lets-talk
- group: start
  title: ''
  type: Login
  url: https://community.agiloft.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agiloft.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agiloft.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.agiloft.com/terms-policies/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/llms/agiloft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agiloft-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/authentication/agiloft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agiloft-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/scopes/agiloft-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agiloft-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/conventions/agiloft-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agiloft-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/conventions/agiloft-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agiloft-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/errors/agiloft-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/agiloft-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/lifecycle/agiloft-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agiloft-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/changelog/agiloft-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agiloft-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/conformance/agiloft-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agiloft-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/rate-limits/agiloft-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agiloft-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/plans/agiloft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agiloft-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/packages/agiloft-packages.yml
  title: ''
  type: Packages
  url: packages/agiloft-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/asyncapi/agiloft-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agiloft-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/mcp/agiloft-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/agiloft-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/data-model/agiloft-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agiloft-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/agiloft/refs/heads/main/sandbox/agiloft-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agiloft-sandbox.yml
created: '2026-09-12'
description: 'Agiloft is a Redwood City, California software company that sells an enterprise Contract Lifecycle Management (CLM) platform built on a no-code business process engine, used by legal, procurement, finance and IT teams to request, author, negotiate, approve, execute, store and report on agreements. Every deployment is a customer-specific knowledgebase (KB) whose tables and fields are configured per tenant, so the API surface is generated from that live configuration rather than published as one fixed catalog contract. Agiloft exposes three machine interfaces on each KB: an OpenAPI/Swagger interface generated from the tenant''s own tables (browsable and downloadable inside the KB at Setup > System > View REST documentation), a stable operation-style REST interface under /ewws/ covering create, read, update, delete, upsert, select, search, attachment, lock, table introspection and action-button execution, and a legacy SOAP interface whose WSDL is likewise generated per knowledgebase.
  Authorization is OAuth 2.0 (authorization code, authorization code with PKCE, and client credentials) or JWT bearer tokens, with a REST operation scope list and group permissions layered on top. Agiloft also ships an outbound webhook service with URL verification and retry, and SCIM 2.0 user provisioning at /scim/v2.'
image: https://cdn.prod.website-files.com/69df514a8d0f4dbcfa25740b/6a749eebcf2b3e9c0d935735_logo%20(1).svg
layout: provider
modified: '2026-09-12'
name: Agiloft
nav: Providers
network: true
overview: 'Agiloft publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Contract Lifecycle Management, Contract Management, Legal, Procurement, and Enterprise Software.


  The Agiloft catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agiloft''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Agiloft Plans Pricing
  plan_count: 0
  slug: agiloft-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Agiloft Rate Limits
  slug: agiloft-rate-limits
scopes:
- name: Agiloft Scopes
  scope_count: 1
  slug: agiloft-scopes
  summary_line: 1 scope · authorizationCode/authorizationCodePKCE/clientCredentials
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 81.5
    operational_transparency: 23.7
  previous_composite: 49.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agiloft Authentication
  slug: agiloft-authentication
  summary_line: oauth2/http/apiKey · 7 schemes
- kind: domain-security
  name: Agiloft Domain Security
  slug: agiloft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Agiloft Trust Center
  slug: agiloft-trust-center
  summary_line: SOC 1, SOC 2, ISO 27001, ISO 27701
slug: agiloft
tags:
- Contract Lifecycle Management
- Contract Management
- Legal
- Procurement
- Enterprise Software
- No-Code
- Workflow Automation
- Document Automation
- Webhook
- SCIM
- Company
website: https://www.agiloft.com/
---
