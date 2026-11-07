---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Salsify Agentic Access
  operation_count: 43
  slug: salsify-agentic-access
  summary_line: 43 operations · 33 acting
api_count: 3
apis:
- description: Early-access public GraphQL API for operating on Salsify accounts, organizations, configuration manifests and organization provisioning requests. Authenticated with a bearer API token; introspection r
  name: Salsify GraphQL API
  slug: graphql
- description: First-party remote Model Context Protocol server hosted by Salsify at app.salsify.com/mcp. Streamable HTTP transport, protected by OAuth 2.1 with RFC 9728 protected-resource metadata pointing at the a
  name: Salsify MCP Server
  slug: mcp
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Digital Assets API from Salsify — 5 operation(s) for digital assets.
  name: Salsify Digital Assets API
  slug: salsify-digital-assets-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Export Runs API from Salsify — 2 operation(s) for export runs.
  name: Salsify Export Runs API
  slug: salsify-export-runs-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Imports API from Salsify — 5 operation(s) for imports.
  name: Salsify Imports API
  slug: salsify-imports-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Lists API from Salsify — 1 operation(s) for lists.
  name: Salsify Lists API
  slug: salsify-lists-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The <org ID> API from Salsify — 1 operation(s) for <org id>.
  name: Salsify <org ID> API
  slug: salsify-org-id-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Products API from Salsify — 5 operation(s) for products.
  name: Salsify Products API
  slug: salsify-products-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Properties API from Salsify — 4 operation(s) for properties.
  name: Salsify Properties API
  slug: salsify-properties-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Record Types API from Salsify — 1 operation(s) for record types.
  name: Salsify Record Types API
  slug: salsify-record-types-api
- baseURL: https://app.salsify.com/api/v1/orgs
  baseurl_source: declared
  description: The Records API from Salsify — 6 operation(s) for records.
  name: Salsify Records API
  slug: salsify-records-api
artifact_total: 36
asyncapis:
- description: ''
  name: Salsify Webhooks
  slug: salsify-webhooks
collections:
- collection_type: open
  name: Salsify Digital Assets API
  slug: open-salsify-digital-assets-api
- collection_type: open
  name: Non-v1 endpoints Export Runs API
  slug: open-salsify-export-runs-api
- collection_type: open
  name: Non-v1 endpoints Imports API
  slug: open-salsify-imports-api
- collection_type: open
  name: No API Explorer (for destructive calls & not well defined parameters) Lists API
  slug: open-salsify-lists-api
- collection_type: open
  name: Settings <org ID> <org ID> API
  slug: open-salsify-org-id-api
- collection_type: open
  name: Salsify Products API
  slug: open-salsify-products-api
- collection_type: open
  name: Salsify Properties API
  slug: open-salsify-properties-api
- collection_type: open
  name: No API Explorer (for destructive calls & not well defined parameters) Record Types API
  slug: open-salsify-record-types-api
- collection_type: open
  name: Salsify Records API
  slug: open-salsify-records-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.salsify.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/salsify/capabilities/salsify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/salsify-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/salsify/security/salsify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/salsify-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.salsify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.salsify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.salsify.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.salsify.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.salsify.com/docs/integration-with-salsify
- group: auth
  href: https://artifacts.apis.io/salsify/authentication/salsify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/salsify-authentication.yml
- group: auth
  href: https://artifacts.apis.io/salsify/scopes/salsify-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/salsify-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://help.salsify.com/ProductXM/s/
- group: company
  title: ''
  type: Blog
  url: https://www.salsify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salsify
- group: start
  title: ''
  type: SignUp
  url: https://www.salsify.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.salsify.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salsify.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salsify.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salsify.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.salsify.com/security-and-reliability
- group: auth
  href: https://artifacts.apis.io/salsify/security/salsify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/salsify-trust-center.yml
- group: operate
  href: https://artifacts.apis.io/salsify/changelog/salsify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/salsify-changelog.yml
- group: build
  href: https://artifacts.apis.io/salsify/packages/salsify-packages.yml
  title: ''
  type: Packages
  url: packages/salsify-packages.yml
- group: build
  href: https://artifacts.apis.io/salsify/packages/salsify-packages.yml
  title: ''
  type: SDKs
  url: packages/salsify-packages.yml
- group: agent
  href: https://artifacts.apis.io/salsify/well-known/salsify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/salsify-well-known.yml
- group: design
  href: https://artifacts.apis.io/salsify/conformance/salsify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/salsify-conformance.yml
- group: design
  href: https://artifacts.apis.io/salsify/errors/salsify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/salsify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/salsify/lifecycle/salsify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/salsify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/salsify/conventions/salsify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/salsify-conventions.yml
- group: design
  href: https://artifacts.apis.io/salsify/data-model/salsify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/salsify-data-model.yml
- group: operate
  href: https://artifacts.apis.io/salsify/rate-limits/salsify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/salsify-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/salsify/asyncapi/salsify-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/salsify-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/salsify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/salsify/agentic-access/salsify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/salsify-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/salsify/security/salsify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/salsify-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.salsify.com/responsible-disclosure
- group: other
  href: https://artifacts.apis.io/salsify/overlays/salsify-api-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/salsify-api-settings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/salsify/overlays/salsify-write-operations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/salsify-write-operations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/salsify/overlays/salsify-non-v1-endpoints-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/salsify-non-v1-endpoints-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/salsify/llms/salsify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/salsify-llms.txt
created: '2026-08-02'
description: Salsify is a product experience management (PXM) and supplier experience management (SXM) platform used by brands, distributors and retailers to centralize product content, digital assets and syndication to the digital shelf. The Salsify platform exposes a REST API at app.salsify.com/api/v1/orgs covering products, records, properties, digital assets, list membership, imports and export runs, an early-access GraphQL API at api.salsify.com/graphql for accounts, organizations and configuration manifests, a webhook surface for product, digital asset, channel and import events with X.509/SHA-256 signature verification, and an OAuth 2.0 authorization server plus a first-party Model Context Protocol server at app.salsify.com/mcp.
graphqls:
- description: 'updatedAt: 2026-05-19T13:41:04.000Z'
  name: GraphQL Schema Overview
  slug: salsify-graphql-schema-overview
image: https://www.salsify.com/hubfs/Salsify%20-%20Product%20Experience%20Management%20PXM%20-%20Feature%20Image.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.salsify.com over HTTP.
  name: Salsify MCP Server
  slug: salsify
modified: '2026-10-06'
name: Salsify
nav: Providers
network: true
overview: 'Salsify publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Digital Assets API, Export Runs API, Imports API, and 8 more. Tagged areas include Company, Product Experience Management, Product Information Management, Digital Asset Management, and Commerce.


  The Salsify catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Salsify''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 32 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 2
  name: Salsify Rate Limits
  slug: salsify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Salsify API Rules
  rule_count: 45
  severity_counts:
    error: 37
    hint: 0
    info: 3
    warn: 5
  slug: salsify-rules
scopes:
- name: Salsify Scopes
  scope_count: 2
  slug: salsify-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 64.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 55.6
    developer_ergonomics: 66.1
    discoverability: 80.0
    operational_transparency: 73.7
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/salsify/salsify-2026-08-17T081714.png
security:
- kind: authentication
  name: Salsify Authentication
  slug: salsify-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Salsify Domain Security
  slug: salsify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Salsify Vulnerability Disclosure
  slug: salsify-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Salsify Trust Center
  slug: salsify-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2013
skill_count: 5
skills:
- name: Bulk upsert Salsify products
  slug: salsify-bulk-upsert-products
- name: Export a Salsify catalog and collect the result
  slug: salsify-export-catalog
- name: Manage Salsify digital assets
  slug: salsify-manage-digital-assets
- name: Model Salsify records and properties
  slug: salsify-model-records-and-properties
- name: Run a Salsify JSON import end to end
  slug: salsify-run-json-import
slug: salsify
tags:
- Company
- Product Experience Management
- Product Information Management
- Digital Asset Management
- Commerce
- Retail
- Syndication
- Data Management
- Software-as-a-Service
website: https://www.salsify.com/
---
