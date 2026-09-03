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
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Bitly Agentic Access
  operation_count: 94
  slug: bitly-agentic-access
  summary_line: 94 operations · 27 acting
api_count: 2
apis:
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: List the branded short domains (BSDs) available to the authenticated account. 1 operation(s), extracted verbatim from the OpenAPI Bitly publishes at https://dev.bitly.com/v4/v4.json.
  name: Bitly BSDs API
  slug: bitly-bsds-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Create, expand, update, archive and delete Bitlinks, list them by group, and read per-link click, engagement, country, city, device and referrer metrics. 21 operation(s), extracted verbatim from the O
  name: Bitly Bitlinks API
  slug: bitly-bitlinks-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Manage marketing campaigns and the channels inside them, grouping Bitlinks for attribution. 8 operation(s), extracted verbatim from the OpenAPI Bitly publishes at https://dev.bitly.com/v4/v4.json.
  name: Bitly Campaigns API
  slug: bitly-campaigns-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Create and update custom back-halves on existing Bitlinks and read clicks by destination for A/B rotations. 5 operation(s), extracted verbatim from the OpenAPI Bitly publishes at https://dev.bitly.com
  name: Bitly Custom Bitlinks API
  slug: bitly-custom-bitlinks-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Manage groups (workspaces) — preferences, tags, shorten counts, exports, feature usage and historical usage — plus the full group-level click, scan and engagement analytics surface. 28 operation(s), e
  name: Bitly Groups API
  slug: bitly-groups-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Read organizations, their plan limits, and shorten counts overall and by group. 5 operation(s), extracted verbatim from the OpenAPI Bitly publishes at https://dev.bitly.com/v4/v4.json.
  name: Bitly Organizations API
  slug: bitly-organizations-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Create dynamic and static QR Codes, customize their render, fetch the image, upgrade a code to a Bitlink, and read scan metrics by browser, city, country and device OS. 16 operation(s), extracted verb
  name: Bitly QR Codes API
  slug: bitly-qr-codes-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Read and update the authenticated user profile and read the platform limits applied to the account. 3 operation(s), extracted verbatim from the OpenAPI Bitly publishes at https://dev.bitly.com/v4/v4.j
  name: Bitly User API
  slug: bitly-user-api
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: Create, read, update, delete and verify webhook endpoints that receive Bitly engagement events. 6 operation(s), extracted verbatim from the OpenAPI Bitly publishes at https://dev.bitly.com/v4/v4.json.
  name: Bitly Webhooks API
  slug: bitly-webhooks-api
- description: Bitly's official remote Model Context Protocol server, exposing 25 tools for link creation, QR Codes, analytics, groups, custom domains and bulk upload. Hosted by Bitly at https://api-ssl.bitly.com/v4
  name: Bitly MCP Server
  slug: bitly-mcp-server
- baseURL: https://api-ssl.bitly.com/v4
  baseurl_source: declared
  description: The Apps API from Bitly — 1 operation(s) for apps.
  name: Bitly Apps API
  slug: bitly-apps-api
artifact_total: 33
asyncapis:
- description: ''
  name: Bitly Engagement Webhooks
  slug: bitly-engagement-webhooks
collections:
- collection_type: open
  name: Bitly Bitlinks API
  slug: open-bitly-bitlinks-api
- collection_type: open
  name: Bitly BSDs API
  slug: open-bitly-bsds-api
- collection_type: open
  name: Bitly Campaigns API
  slug: open-bitly-campaigns-api
- collection_type: open
  name: Bitly Custom Bitlinks API
  slug: open-bitly-custom-bitlinks-api
- collection_type: open
  name: Bitly Groups API
  slug: open-bitly-groups-api
- collection_type: open
  name: Bitly OAuth Apps API
  slug: open-bitly-oauth-apps-api
- collection_type: open
  name: Bitly Organizations API
  slug: open-bitly-organizations-api
- collection_type: open
  name: Bitly QR Codes API
  slug: open-bitly-qr-codes-api
- collection_type: open
  name: Bitly User API
  slug: open-bitly-user-api
- collection_type: open
  name: Bitly Webhooks API
  slug: open-bitly-webhooks-api
- collection_type: open
  name: Bitly API v4
  slug: open-bitly
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bitly-oauth-apps-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bitly-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitly-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitly
- group: company
  title: ''
  type: Website
  url: https://bitly.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bitly.com
- group: docs
  title: ''
  type: APIReference
  url: https://dev.bitly.com/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://bitly.com/pages/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.bitly.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.bitly.com/sign_in
- group: auth
  title: ''
  type: Authentication
  url: https://dev.bitly.com/docs/getting-started/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://dev.bitly.com/docs/getting-started/rate-limits
- group: operate
  title: ''
  type: Support
  url: https://support.bitly.com
- group: operate
  title: ''
  type: StatusPage
  url: https://bitly.statuspage.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitly
- group: company
  title: ''
  type: Blog
  url: https://bitly.com/blog/
- group: build
  title: ''
  type: Packages
  url: packages/bitly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitly-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitly-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bitly-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitly-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bitly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/bitly-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitly-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitly-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitly-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bitly-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitly-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bitly-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bitly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitly-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bitly-engagement-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/bitly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bitly-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.bitly.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.bitly.com
- group: operate
  title: ''
  type: Changelog
  url: https://dev.bitly.com/bitly-mcp/overview/mcp-changelog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitly.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitly.com/pages/privacy
- group: agent
  title: ''
  type: MCPServer
  url: https://dev.bitly.com/bitly-mcp/
- group: build
  title: ''
  type: PostmanCollection
  url: collections/bitly.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/bitly.opencollection.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bitly-shorten-and-brand-a-link.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bitly-report-link-performance.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bitly-create-and-measure-a-qr-code.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bitly-subscribe-to-engagement-events.md
created: '2026-05-11'
description: Bitly is a link management platform for creating, branding, routing and measuring short links, QR Codes and link-in-bio pages at scale. The Bitly v4 REST API is a 94-operation, bearer-authenticated JSON API at https://api-ssl.bitly.com/v4 covering Bitlink creation and expansion, custom back-halves, branded short domains, groups (workspaces) and organizations, campaigns and channels, dynamic and static QR Codes, bulk shortening, engagement webhooks, and a deep click/scan analytics surface sliced by country, city, device, OS, browser and referrer. Bitly publishes its own OpenAPI 3.0 definition and operates an official remote Model Context Protocol server, making it directly callable by AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitly.png
layout: provider
mcp_servers:
- description: ''
  name: Bitly MCP Server
  slug: bitly-mcp-server
- description: ''
  name: Bitly MCP Server
  slug: bitly-mcp-server-2
modified: '2026-08-13'
name: Bitly
nav: Providers
network: true
overview: 'Bitly publishes 10 APIs on the [APIs.io](https://apis.io/) network, including BSDs API, Bitlinks API, Campaigns API, and 7 more. Tagged areas include Links, URL Shortener, QR Codes, Analytics, and Marketing.


  The Bitly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bitly''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 43 more developer resources.'
plans:
- name: Bitly Plans Pricing
  plan_count: 5
  slug: bitly-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Bitly Rate Limits
  slug: bitly-rate-limits
scopes:
- name: Bitly Scopes
  scope_count: 0
  slug: bitly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 24
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 68.8
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 84.2
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitly/refs/heads/main/screenshots/bitly-2026-06-20T173312.png
security:
- kind: authentication
  name: Bitly Authentication
  slug: bitly-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bitly Domain Security
  slug: bitly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bitly Vulnerability Disclosure
  slug: bitly-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bitly Trust Center
  slug: bitly-trust-center
  summary_line: SOC 2 Type 2, GDPR, CCPA
slug: bitly
tags:
- Links
- URL Shortener
- QR Codes
- Analytics
- Marketing
- Link Management
- Webhook
- Attribution
- Agents
- MCP
website: https://bitly.com
---
