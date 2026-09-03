---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Complyadvantage Agentic Access
  operation_count: 19
  slug: complyadvantage-agentic-access
  summary_line: 19 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.mesh.complyadvantage.com
  baseurl_source: declared
  description: ComplyAdvantage's newer Mesh platform API, authenticated with OAuth2 bearer tokens (24-hour validity). Covers the full customer lifecycle - customer creation and screening (sync or async), risk scorin
  name: ComplyAdvantage Mesh Platform API
  slug: complyadvantage-mesh-platform-api
- baseURL: https://api.complyadvantage.com
  baseurl_source: declared
  description: Comments, tags, assignment, and match status workflow on searches.
  name: ComplyAdvantage Case Management API
  slug: complyadvantage-case-management-api
- baseURL: https://api.complyadvantage.com
  baseurl_source: declared
  description: Ongoing monitoring of searches, change differences, and acknowledgement.
  name: ComplyAdvantage Monitored Searches API
  slug: complyadvantage-monitored-searches-api
- baseURL: https://api.complyadvantage.com
  baseurl_source: declared
  description: Create and manage AML screening searches against sanctions, PEP, warning, and adverse media data.
  name: ComplyAdvantage Searches API
  slug: complyadvantage-searches-api
- baseURL: https://api.complyadvantage.com
  baseurl_source: declared
  description: Users on your ComplyAdvantage account.
  name: ComplyAdvantage Users API
  slug: complyadvantage-users-api
artifact_total: 20
asyncapis:
- description: ''
  name: Complyadvantage Webhooks
  slug: complyadvantage-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ComplyAdvantage Case Management API
  slug: open-complyadvantage-case-management-api
- collection_type: open
  name: ComplyAdvantage Case Management Monitored Searches API
  slug: open-complyadvantage-monitored-searches-api
- collection_type: open
  name: ComplyAdvantage Case Management Searches API
  slug: open-complyadvantage-searches-api
- collection_type: open
  name: ComplyAdvantage Case Management Users API
  slug: open-complyadvantage-users-api
- collection_type: open
  name: ComplyAdvantage API
  slug: open-complyadvantage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/complyadvantage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/complyadvantage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/complyadvantage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/complyadvantage
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/complyadvantage
- group: company
  title: ''
  type: Website
  url: https://complyadvantage.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.complyadvantage.com
- group: commercial
  title: ''
  type: Pricing
  url: https://complyadvantage.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/complyadvantage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/complyadvantage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/complyadvantage-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://complyadvantage.com/insights/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/complyadvantage-mesh-api-openapi.json
- group: build
  title: ''
  type: Packages
  url: packages/complyadvantage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/complyadvantage-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/complyadvantage-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/complyadvantage-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/complyadvantage-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/complyadvantage-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/complyadvantage-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/complyadvantage-mesh-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/complyadvantage-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/complyadvantage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/complyadvantage-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/complyadvantage-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/complyadvantage-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/complyadvantage-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/complyadvantage-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/complyadvantage-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/complyadvantage-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/teamcomplyadvantage/workspace/complyadvantage/collection/37100431-42eb1f77-1374-485d-999c-f2bea24f2bec
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mesh.complyadvantage.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mesh.complyadvantage.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mesh.complyadvantage.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.complyadvantage.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://complyadvantage.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://complyadvantage.com/privacy-notice/
- group: start
  title: ''
  type: SignUp
  url: https://complyadvantage.com/starter-plan/
- group: start
  title: ''
  type: Login
  url: https://mesh.complyadvantage.com/
created: '2026-07-11'
description: ComplyAdvantage provides AI-driven anti-money laundering (AML) and financial crime risk detection - screening people and companies against sanctions and watchlists, politically exposed persons (PEPs and RCAs), and adverse media, with ongoing monitoring that alerts you when a customer's risk profile changes. The REST API (api.complyadvantage.com, with US and APAC regional bases) exposes searches, monitored searches, case management, comments, tags, and users with api-key auth, plus webhooks for match and monitoring updates. The newer Mesh platform API adds customer lifecycle screening, cases and alerts, transaction monitoring, and fraud detection workflows. Used by banks, fintechs, payments, and crypto firms for KYC/AML compliance, sanctions screening, and fraud prevention.
finops:
- name: Complyadvantage Finops
  service_category: Security, Identity, and Compliance
  slug: complyadvantage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/complyadvantage.png
layout: provider
mcp_servers:
- description: 'ComplyAdvantage serves a live, anonymous, remote MCP server from its own Mesh documentation host. It is a spec-introspection server rather than a business-capability server: the four tools let an agen'
  name: ComplyAdvantage Mesh Documentation MCP Server
  slug: complyadvantage-mesh-documentation-mcp-server
modified: '2026-08-27'
name: ComplyAdvantage
nav: Providers
network: true
overview: 'ComplyAdvantage publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Mesh Platform API, Case Management API, Monitored Searches API, and 2 more. Tagged areas include Anti-Money Laundering, AML, Fraud Detection, Sanctions Screening, and Compliance.


  The ComplyAdvantage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ComplyAdvantage''s developer surface includes authentication, documentation, pricing, engineering blog, API reference, getting-started guide, support, and 33 more developer resources.'
plans:
- name: Complyadvantage Plans Pricing
  plan_count: 3
  slug: complyadvantage-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Complyadvantage Rate Limits
  slug: complyadvantage-rate-limits
scopes:
- name: Complyadvantage Scopes
  scope_count: 0
  slug: complyadvantage-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 23.2
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/complyadvantage/refs/heads/main/screenshots/complyadvantage-2026-07-25T210154.png
security:
- kind: authentication
  name: Complyadvantage Authentication
  slug: complyadvantage-authentication
  summary_line: oauth2-client-credentials/http-bearer/apiKey · 3 schemes
- kind: domain-security
  name: Complyadvantage Domain Security
  slug: complyadvantage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: complyadvantage
tags:
- Anti-Money Laundering
- AML
- Fraud Detection
- Sanctions Screening
- Compliance
- PEP Screening
- Adverse Media
- KYC
- Watchlist
- Transaction Monitoring
- Financial Crime
- RegTech
website: https://complyadvantage.com
---
