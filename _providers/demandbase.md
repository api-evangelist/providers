---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Demandbase Agentic Access
  operation_count: 54
  slug: demandbase-agentic-access
  summary_line: 54 operations · 24 acting
api_count: 16
apis:
- description: Hosted remote Model Context Protocol server exposing Demandbase account, person, intent, buying-group, account-brief, global company/contact and reference capabilities to AI assistants. OAuth 2.1 auth
  name: Demandbase MCP Server
  slug: demandbase-mcp-server
- description: 'Real-time visitor identification: resolves a visitor IP address to a Demandbase company ID, firmographics and corporate hierarchy for web personalization, forms enrichment and analytics integrations. '
  name: Demandbase IP-API v3
  slug: demandbase-ip-api-v3
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Activities Management API from Demandbase — 3 operation(s) for activities management.
  name: Demandbase Activities Management API
  slug: demandbase-activities-management-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: Asynchronous bulk jobs for high-volume data retrieval and matching.
  name: Demandbase Asynchronous (Batch) API
  slug: demandbase-asynchronous-batch-api-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Auth API from Demandbase — 1 operation(s) for auth.
  name: Demandbase Auth API
  slug: demandbase-auth-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: Retrieve company-level intent signals and research activity.
  name: Demandbase Company Intent API
  slug: demandbase-company-intent-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Create Export Job API from Demandbase — 3 operation(s) for create export job.
  name: Demandbase Create Export Job API
  slug: demandbase-create-export-job-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Credit Usage API from Demandbase — 1 operation(s) for credit usage.
  name: Demandbase Credit Usage API
  slug: demandbase-credit-usage-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: Create and manage custom sources.
  name: Demandbase Custom Sources API
  slug: demandbase-custom-sources-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: Configure field mappings for a source and object type.
  name: Demandbase Field Mappings API
  slug: demandbase-field-mappings-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Get Fields API from Demandbase — 1 operation(s) for get fields.
  name: Demandbase Get Fields API
  slug: demandbase-get-fields-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Get Job Details API from Demandbase — 2 operation(s) for get job details.
  name: Demandbase Get Job Details API
  slug: demandbase-get-job-details-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Get Reference Data API from Demandbase — 2 operation(s) for get reference data.
  name: Demandbase Get Reference Data API
  slug: demandbase-get-reference-data-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The Import Job API from Demandbase — 5 operation(s) for import job.
  name: Demandbase Import Job API
  slug: demandbase-import-job-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: Reference schemas and allowed values used by the B2B API.
  name: Demandbase Reference Tables API
  slug: demandbase-reference-tables-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: Subscription creation, updates, status, alerts, and lifecycle operations.
  name: Demandbase Subscription API
  slug: demandbase-subscription-api-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: Synchronous company, contact, matching, news, and logo operations.
  name: Demandbase Sync API
  slug: demandbase-sync-api-api
- baseURL: https://uapi.demandbase.com/data/b2b/v1
  baseurl_source: declared
  description: The User Management API from Demandbase — 3 operation(s) for user management.
  name: Demandbase User Management API
  slug: demandbase-user-management-api
artifact_total: 36
asyncapis:
- description: ''
  name: Demandbase Webhooks
  slug: demandbase-webhooks
collections:
- collection_type: open
  name: Admin API
  slug: open-demandbase-admin
- collection_type: open
  name: Demandbase Auth API
  slug: open-demandbase-auth
- collection_type: open
  name: B2B API
  slug: open-demandbase-b2b
- collection_type: open
  name: Custom Sources API
  slug: open-demandbase-custom-sources
- collection_type: open
  name: Data Export API
  slug: open-demandbase-data-export
- collection_type: open
  name: Data Import API
  slug: open-demandbase-data-import
- collection_type: open
  name: Intent API
  slug: open-demandbase-intent
- collection_type: open
  name: Usage API
  slug: open-demandbase-usage
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-b2b-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-data-export-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-data-import-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-intent-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-admin-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-usage-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-custom-sources-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/demandbase-auth-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/demandbase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/demandbase-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demandbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/demandbase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demandbase
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demandbase.com/
- group: operate
  title: ''
  type: Support
  url: https://support.demandbase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.demandbase.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.demandbase.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/demandbase/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Demandbase
- group: start
  title: ''
  type: Portal
  url: https://developer.demandbase.com
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.demandbase.com/hc/en-us
- group: company
  title: ''
  type: Partners
  url: https://partners.demandbase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demandbase.com/terms-of-use/
- group: start
  title: ''
  type: Signup
  url: https://www.demandbase.com/products/data/api-integration/api-trial/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/demandbase-vocabulary.yml
- group: build
  title: ''
  type: Packages
  url: packages/demandbase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/demandbase-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/demandbase-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/demandbase-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/demandbase-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demandbase-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/demandbase-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.demandbase.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/demandbase-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/demandbase-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demandbase-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.demandbase.com/docs/migrating-from-legacy-tokens-to-api-keysets
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/demandbase-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/demandbase-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/demandbase-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/demandbase-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/demandbase-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/demandbase-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/demandbase-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/demandbase-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.demandbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.demandbase.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.demandbase.com/reference/generate_access_token
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.demandbase.com/docs/api-getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demandbase.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.demandbase.com/products/data/api-integration/api-trial/
- group: start
  title: ''
  type: Login
  url: https://web.demandbase.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.demandbase.com/hc/en-us
- group: build
  title: ''
  type: SDK
  url: https://pypi.org/project/demandbase-sdk/
- group: operate
  title: ''
  type: Contact
  url: https://www.demandbase.com/company/contact-us/
created: '2024-01-20'
description: Demandbase is a B2B go-to-market platform that unifies account intelligence, intent data, advertising, orchestration, personalization and sales intelligence into a single pipeline engine. Its developer surface is eight OpenAPI-documented REST APIs on uapi.demandbase.com — B2B company/contact intelligence, Data Export, Data Import, Admin, Intent (beta), Usage, Custom Sources and Auth — plus a hosted, OAuth-protected Model Context Protocol server that exposes account, person, intent, buying-group and account-brief capabilities to AI assistants, an official Python SDK, and a change-subscription webhook surface.
finops:
- name: Demandbase Finops
  service_category: B2B Marketing / Sales Intelligence
  slug: demandbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demandbase.png
layout: provider
mcp_servers:
- description: ''
  name: Demandbase MCP Server
  slug: demandbase-mcp-server
modified: '2026-08-13'
name: Demandbase
nav: Providers
network: true
overview: 'Demandbase publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Activities Management API, Asynchronous (Batch) API, Auth API, and 13 more. Tagged areas include Account Based Marketing, Advertising, AI Agents, B2B Marketing, and Company Data.


  The Demandbase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Demandbase''s developer surface includes authentication, support, engineering blog, developer portal, signup flow, changelog, documentation, and 49 more developer resources.'
plans:
- name: Demandbase Plans Pricing
  plan_count: 0
  slug: demandbase-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 15
  name: Demandbase Rate Limits
  slug: demandbase-rate-limits
scopes:
- name: Demandbase Scopes
  scope_count: 4
  slug: demandbase-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 25
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 63.2
    developer_ergonomics: 50.6
    discoverability: 75.9
    governance: 22.0
    operational_transparency: 69.7
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demandbase/refs/heads/main/screenshots/demandbase-2026-06-20T175908.png
security:
- kind: authentication
  name: Demandbase Authentication
  slug: demandbase-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Demandbase Domain Security
  slug: demandbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Demandbase Trust Center
  slug: demandbase-trust-center
  summary_line: SOC 2, ISO 27001
slug: demandbase
tags:
- Account Based Marketing
- Advertising
- AI Agents
- B2B Marketing
- Company Data
- Contact Data
- Data Enrichment
- Intent Data
- MCP
- Personalization
- Sales Intelligence
- Technographics
website: https://developer.demandbase.com
---
