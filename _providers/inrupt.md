---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The ESS Pod Storage Service implements the Solid Protocol over HTTP — LDP-style container and resource CRUD in RDF (Turtle, JSON-LD) and binary form, with Access Control Policy (ACP) resources, canoni
  name: Inrupt Pod Storage API (Solid Protocol)
  slug: pod-storage
- description: Inrupt's hosted Solid-OIDC identity provider for PodSpaces WebIDs. It publishes a standard OpenID Connect discovery document at /.well-known/openid-configuration advertising authorization, token, user
  name: Inrupt Solid OpenID Provider
  slug: solid-oidc
- description: The ESS Access Grant Service issues, queries, verifies, derives and status-checks W3C Verifiable Credentials that carry Access Requests and Access Grants — the consent receipts that authorize one agen
  name: Inrupt Access Grant Service (VC API)
  slug: access-grant
- description: 'Added in ESS 3.0, the MCP Resource Service exposes four Model Context Protocol tools — requestAccess, checkAccessRequestStatus, hasMatchingAccessGrant and getResource — over streamable HTTP, so an AI '
  name: Inrupt ESS MCP Resource Service
  slug: mcp-resource
- description: 'The Platform Management service hosts the ESS Admin API used to provision users before they first log in — creating a provisioning account, attaching a WebID and a storage container, setting identity '
  name: Inrupt ESS Platform Management API
  slug: platform-management
- baseURL: https://notification.inrupt.com
  baseurl_source: declared
  description: WebSocket Discovery
  name: Inrupt Discovery API
  slug: inrupt-discovery-api
- baseURL: https://notification.inrupt.com
  baseurl_source: declared
  description: Public JSON Web Keys
  name: Inrupt Jsonkeys API
  slug: inrupt-jsonkeys-api
- baseURL: https://notification.inrupt.com
  baseurl_source: declared
  description: Subscription Management
  name: Inrupt Subscription API
  slug: inrupt-subscription-api
artifact_total: 17
asyncapis:
- description: ''
  name: Inrupt Notifications Webhooks
  slug: inrupt-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.inrupt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.inrupt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inrupt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inrupt.com/ess/services/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inrupt.com/sdk/javascript-sdk/tutorial/
- group: operate
  title: ''
  type: Support
  url: https://inrupt.atlassian.net/servicedesk
- group: company
  title: ''
  type: Blog
  url: https://www.inrupt.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inrupt
- group: start
  title: ''
  type: SignUp
  url: https://start.inrupt.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inrupt.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inrupt.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inrupt.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.inrupt.com/maintenance-policy
- group: auth
  title: ''
  type: Security
  url: https://www.inrupt.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.inrupt.com/trust
- group: auth
  title: ''
  type: Compliance
  url: conformance/inrupt-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inrupt-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/inrupt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/inrupt-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/inrupt-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inrupt-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/inrupt-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inrupt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inrupt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inrupt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/inrupt-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/inrupt-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inrupt-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inrupt-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/inrupt-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/inrupt-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inrupt-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inrupt-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/inrupt-notifications-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/inrupt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inrupt-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/inrupt-notification-overlay.yaml
created: '2026-08-23'
description: Inrupt is the enterprise company founded by Sir Tim Berners-Lee and John Bruce to commercialize Solid, the open decentralized-data specification he created at MIT. Its flagship product is the Enterprise Solid Server (ESS), a Kubernetes-deployed platform of cooperating services that gives each person or organization a Pod — a personal data store with fine-grained access control, auditing, and W3C Verifiable-Credential-based Access Requests and Grants. ESS ships an Access Grant service, an Authorization service using Access Control Policies (ACP), a Pod Storage service implementing the Solid Protocol, a Notification Delivery service that pushes signed webhooks to remote HTTPS endpoints, a Platform Management service with a token-exchange and admin provisioning API, an optional hybrid keyword-plus-semantic Search service, and — since ESS 3.0 — an MCP Resource Service exposing consent-mediated tools to AI agents. Inrupt also runs PodSpaces, a hosted developer-preview deployment
  of ESS, and publishes first-party JavaScript and Java client SDKs.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Inrupt ships a first-party MCP server as an ESS service. The MCP Resource Service exposes four tools that let an AI agent ask a person for consent to their Pod data, watch for the approval, verify the
  name: Inrupt ESS MCP Resource Service
  slug: inrupt-ess-mcp-resource-service
modified: '2026-08-23'
name: Inrupt
nav: Providers
network: true
overview: 'Inrupt publishes 3 APIs on the [APIs.io](https://apis.io/) network: Discovery API, Jsonkeys API, and Subscription API. Tagged areas include Company, Solid, Personal Data Stores, Decentralized Identity, and Data Privacy.


  The Inrupt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Inrupt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 31 more developer resources.'
plans:
- name: Inrupt Plans Pricing
  plan_count: 0
  slug: inrupt-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Inrupt Rate Limits
  slug: inrupt-rate-limits
scopes:
- name: Inrupt Scopes
  scope_count: 0
  slug: inrupt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 66.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inrupt/refs/heads/main/screenshots/inrupt-2026-09-02T145900.png
security:
- kind: authentication
  name: Inrupt Authentication
  slug: inrupt-authentication
  summary_line: openIdConnect/oauth2/http/mutualTLS · 7 schemes
- kind: domain-security
  name: Inrupt Domain Security
  slug: inrupt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Inrupt Vulnerability Disclosure
  slug: inrupt-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Inrupt Trust Center
  slug: inrupt-trust-center
  summary_line: ISO/IEC 27001:2022
slug: inrupt
tags:
- Company
- Solid
- Personal Data Stores
- Decentralized Identity
- Data Privacy
- Access Control
- Verifiable Credentials
- Linked Data
- RDF
- Consent Management
- Data Wallets
- Agent Infrastructure
- MCP
- Enterprise Software
website: https://www.inrupt.com/
---
