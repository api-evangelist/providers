---
access_model:
  confidence: high
  label: Paid consumption · Self-serve developer registration · SBOX sandbox · production data requires AppMarket review and customer install
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - documentation
  - authentication
  - developer-terms-and-conditions
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: 'The core Foundations REST API over the Reapit agency CRM data platform. It is documented as a hypermedia REST API with date-based versioning (the `api-version: 2020-01-31` header is required), optimis'
  name: Reapit Foundations Platform REST API
  slug: reapit-foundations-platform-rest-api
- description: A GraphQL proxy over the Foundations Platform REST API, released publicly out of internal beta and used in production by Reapit's own Geo Diary AppMarket app. The stated objective is a schema identica
  name: Reapit Foundations GraphQL API
  slug: reapit-foundations-graphql-api
- description: Real-time outbound event delivery from the Reapit CRM to an endpoint you host. Webhooks are created either in the developer portal UI at developers.reapit.cloud/webhooks/new or programmatically throug
  name: Reapit Foundations Webhooks
  slug: reapit-foundations-webhooks
- description: An alpha Model Context Protocol server exposing the Foundations platform to AI agents over Streamable HTTP at a single endpoint. Authentication is a Reapit Connect JWT that must carry the `agencyCloud
  name: Reapit Foundations MCP Server (Alpha)
  slug: reapit-foundations-mcp-server
- description: Reapit's hosted OpenID Connect identity service, which fronts every other Foundations API. It supports the authorization code flow for user-context applications and the client credentials flow for ser
  name: Reapit Connect
  slug: reapit-connect
- description: An inbound API that lets a third-party application push real-time event notifications into Reapit products for display to named CRM users. Requests POST to /notifications using an envelope-and-payload
  name: Reapit Foundations Notifications API
  slug: reapit-foundations-notifications-api
- description: A custom URI-scheme API, not an HTTP API, used by AppMarket web applications hosted inside the AgencyCloud desktop CRM to drive the desktop from the embedded app. Links prefixed `agencycloud:` are str
  name: Reapit AgencyCloud Desktop API
  slug: reapit-agencycloud-desktop-api
artifact_total: 14
asyncapis:
- description: ''
  name: Reapit Foundations Webhooks
  slug: reapit-foundations-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reapit-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reapit-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reapit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/reapit-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reapit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/reapit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reapit-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reapit-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reapit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://foundations-documentation.reapit.cloud/api/api-documentation#deprecation
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/reapit-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/reapit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reapit-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/reapit-cli.yml
- group: design
  title: ''
  type: Components
  url: components/reapit-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/reapit-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reapit-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reapit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.reapit.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/reapit-trust-center.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://foundations-documentation.reapit.cloud/developer-portal
- group: docs
  title: ''
  type: APIReference
  url: https://developers.reapit.cloud/swagger
- group: operate
  title: ''
  type: SLA
  url: https://www.reapit.com/legal/terms-and-conditions/reapit-partner-business-service-catalogue
- group: company
  title: ''
  type: Website
  url: https://www.reapit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://foundations-documentation.reapit.cloud/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.reapit.cloud/
- group: start
  title: ''
  type: SignUp
  url: https://developers.reapit.cloud/register
- group: auth
  title: ''
  type: Authentication
  url: https://foundations-documentation.reapit.cloud/api/reapit-connect
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundations-documentation.reapit.cloud/developer-terms-and-conditions
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.reapit.cloud/apps
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.reapit.com/company/partner-program
- group: other
  title: ''
  type: Platform
  url: https://www.reapit.com/platform
- group: operate
  title: ''
  type: Support
  url: https://foundations-documentation.reapit.cloud/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reapit.com/
- group: operate
  title: ''
  type: Changelog
  url: https://foundations-documentation.reapit.cloud/whats-new
- group: operate
  title: ''
  type: FAQ
  url: https://foundations-documentation.reapit.cloud/faqs
- group: agent
  title: ''
  type: LLMsTxt
  url: https://foundations-documentation.reapit.cloud/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reapit
- group: build
  title: ''
  type: SDK
  url: https://foundations-documentation.reapit.cloud/app-development/foundations-ts-defintions
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/reapit/foundations-code-examples
- group: company
  title: ''
  type: Blog
  url: https://www.reapit.com/resources/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reapit.com/legal/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.reapit.com/company/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reapit
created: '2026-07-26'
description: 'Reapit is a United Kingdom-headquartered supplier of agency CRM and property management software for estate and letting agents, best known for AgencyCloud and Property Cloud, and operating across the UK and Ireland, Australia and New Zealand, and Denmark (through Mindworking). In a market with no MLS, Reapit sits in the middle of the value chain: listings are created and maintained in the agent''s CRM and pushed outward to the two dominant consumer portals, Rightmove and Zoopla, so the CRM — not any cooperative database — is where the machine-readable property record actually lives. Its API posture is unusually open for this sector and is the counter-example to "certified but unreachable": Reapit Foundations is a genuine developer platform with a public documentation site at foundations-documentation.reapit.cloud, a self-serve registration form at developers.reapit.cloud/register behind published Developer Terms and Conditions, an immediately usable SBOX sandbox, OpenID Connect
  authentication through Reapit Connect with a live anonymous discovery document, a REST API covering roughly thirty CRM resource domains, a public GraphQL proxy, a real webhooks system with sixty-plus event topics, and an alpha Model Context Protocol server. The contract is split rather than absent: the Swagger/OpenAPI document that powers the Interactive API Explorer is served from platform.reapit.cloud/docs behind a bearer token, so no REST spec is harvestable anonymously — but full GraphQL introspection against graphql.reapit.cloud succeeds without credentials and yields a real machine-readable contract of 190 types, 63 queries and 58 mutations, which is the widest public description of the platform that exists. The MCP server''s tools/list is auth-gated, so its 43 tools are known only from the docs. Reaching any real agency''s data still requires the app to pass Reapit''s AppMarket listing review and then be installed by that customer, who grants the scopes. There is no RESO Web API
  or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier anywhere in Reapit''s stack — RESO is a North American, NAR-driven construct and the UK has no MLS to certify against. Reapit publishes no open data; the open UK property layer belongs to HM Land Registry and Ordnance Survey, not to the CRM vendors.'
image: https://cdn.prod.website-files.com/65cc1dfdc4913d1034befe43/65f4ec800a019f1d78665d75_webclip-reapit.png
layout: provider
mcp_servers:
- description: The Reapit Foundations MCP server is a real, hosted, first-party Model Context Protocol server that exposes the agency CRM platform to agents over a single Streamable HTTP endpoint. It is in alpha and
  name: Reapit MCP Server
  slug: reapit-mcp-server
modified: '2026-07-26'
name: Reapit
nav: Providers
network: true
overview: 'Reapit publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, United Kingdom, PropTech, CRM, and Estate Agents.


  The Reapit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Reapit''s developer surface includes authentication, changelog, CLI, sandbox, getting-started guide, API reference, documentation, and 38 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 3
  name: Reapit Rate Limits
  slug: reapit-rate-limits
scopes:
- name: Reapit Scopes
  scope_count: 0
  slug: reapit-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 55.3
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 58.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reapit/refs/heads/main/screenshots/reapit-2026-08-17T081459.png
security:
- kind: authentication
  name: Reapit Authentication
  slug: reapit-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Reapit Domain Security
  slug: reapit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reapit Trust Center
  slug: reapit-trust-center
  summary_line: ISO 27001
slug: reapit
tags:
- Real-Estate
- United Kingdom
- PropTech
- CRM
- Estate Agents
- Property Listings
- Property Management
- Rentals
- Conveyancing
- Australia
website: https://www.reapit.com/
---
