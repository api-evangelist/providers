---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 174
  human_in_the_loop: 1
  name: Lone Wolf Agentic Access
  operation_count: 348
  slug: lone-wolf-agentic-access
  summary_line: 348 operations · 174 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Programmatic access to Lone Wolf's transaction management platform across the full transaction lifecycle — creating and updating transactions, managing offers, contacts, folders and documents, sharing
  name: Lone Wolf Transact API
  slug: lone-wolf-transact-api
- description: Partner-integration API (release 25.01.00) covering deal records across the Lone Wolf Foundation platform. All requests require an Authorization header carrying a Bearer JWT obtained by POSTing creden
  name: Lone Wolf Deals API
  slug: lone-wolf-deals-api
- description: Brokerage back-office and accounting API covering the money side of the transaction — commissions, commission fees and tiers, deposits, conditions and condition types, classifications, employees, offi
  name: Lone Wolf Back Office API
  slug: lone-wolf-back-office-api
- description: E-signature API for Authentisign, Lone Wolf's signing product. Creates and manages signings, signer roles, documents and signing status. Supports an optional CallbackUrl on a signing, and a PATCH endp
  name: Lone Wolf Authentisign API
  slug: lone-wolf-authentisign-api
- description: Partner API for the TransactionDesk edition of Lone Wolf Transactions, covering transaction summaries, documents, contacts and contact types, transaction types and statuses, single sign-on, and resour
  name: Lone Wolf TransactionDesk Partner API
  slug: lone-wolf-transactiondesk-api
- description: The zipForm REST web service (v5.1), exposing zipForm transaction data, PDF forms and selected zipForm application functionality for integration into partner applications. Explicitly made available on
  name: Lone Wolf zipForm Partner API
  slug: lone-wolf-zipform-api
- description: A collection of RESTful web resources giving third parties access to Lone Wolf data — members, transactions, classifications, conditions, contact types, property types and sources of business. Authent
  name: Lone Wolf WolfConnect API
  slug: lone-wolf-wolfconnect-api
artifact_total: 23
asyncapis:
- description: ''
  name: Lone Wolf Authentisign Webhooks
  slug: lone-wolf-authentisign-webhooks
collections:
- collection_type: open
  name: Authentisign API
  slug: open-lone-wolf-authentisign-api
- collection_type: open
  name: Back Office API
  slug: open-lone-wolf-back-office-online-api
- collection_type: open
  name: Deals API
  slug: open-lone-wolf-deals-api
- collection_type: open
  name: Transact API
  slug: open-lone-wolf-transact-api
- collection_type: open
  name: TransactionDesk Partner API
  slug: open-lone-wolf-transactiondesk-api
- collection_type: open
  name: WolfConnect API
  slug: open-lone-wolf-wolfconnect-api
- collection_type: open
  name: ZipForm Partner API
  slug: open-lone-wolf-zipform-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lone-wolf-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lone-wolf-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lone-wolf-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lone-wolf-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lone-wolf-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lone-wolf-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lone-wolf-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lone-wolf-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lone-wolf-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lone-wolf-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lone-wolf-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/lone-wolf-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lone-wolf-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lone-wolf-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lone-wolf-authentisign-webhooks.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lone-wolf-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lone-wolf-open-a-transaction.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lone-wolf-attach-forms-and-sign.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lone-wolf-back-office-commissions.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lone-wolf-wolfconnect-sync-members.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lone-wolf-authentisign-signing-lifecycle.md
- group: company
  title: ''
  type: Website
  url: https://www.lwolf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lwolf.com/api-portal
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.lwolf.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.lwolf.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.lwolf.com/api-getting-started
- group: start
  title: ''
  type: Signup
  url: https://www.lwolf.com/api-getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.lwolf.com/api-getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.lwolf.com/blog
- group: operate
  title: ''
  type: Changelog
  url: https://apidocs.lwolf.com/changes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lone-wolf-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lone-wolf-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://apidocs.lwolf.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lone-wolf-mcp.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://apidocs.lwolf.com/?format=md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lone-wolf-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: https://authentication.api.lwolf.com/v1/login
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: https://gateway.lwolf.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: TokenEndpoint
  url: https://gateway.lwolf.com/oauth/token
- group: other
  title: ''
  type: JWKS
  url: https://gateway.lwolf.com/.well-known/jwks.json
- group: start
  title: ''
  type: Login
  url: https://gateway.lwolf.com/u/login/identifier
- group: company
  title: ''
  type: About
  url: https://www.lwolf.com/about
- group: other
  title: ''
  type: Leadership
  url: https://www.lwolf.com/leadership
- group: operate
  title: ''
  type: Support
  url: https://www.lwolf.com/support
- group: operate
  title: ''
  type: Contact
  url: https://www.lwolf.com/contact
- group: company
  title: ''
  type: News
  url: https://www.lwolf.com/news-press
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lwolf.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lwolf.com/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getlwolf/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/GetLWolf
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/getlwolf
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/GetLWolf
- group: docs
  title: ''
  type: ProductDocumentation
  url: https://cloudcma.com/developers
- group: docs
  title: ''
  type: ProductDocumentation
  url: https://docs.homespotter.com/
- group: docs
  title: ''
  type: ProductDocumentation
  url: https://spac.io/docs/api/
- group: docs
  title: ''
  type: ProductDocumentation
  url: https://apidocs.propertybase.com/
- group: other
  title: ''
  type: Product
  url: https://signinkless.com/
created: '2026-07-26'
description: 'Lone Wolf Technologies is the dominant back-office, transaction-management and forms vendor in North American residential real estate, headquartered in Dallas, Texas and backed by Stone Point Capital. Its software runs the paperwork and money side of the deal rather than the listing feed: brokerage accounting and commission processing (Back Office, the brokerWOLF lineage), transaction management in two editions (zipForm Edition and TransactionDesk Edition), Authentisign and Inkless e-signature, Cloud CMA comparative market analysis, Boost digital advertising (HomeSpotter), Spacio open-house lead capture, and Propertybase/Relationships CRM. Its forms suites are distributed to agents as association member benefits through state REALTOR associations and MLSs, which places it between the MLS layer and the brokerage. On API posture it is one of the strongest surfaces in this sector and an instructive counter-example to the MLS data providers: on 2026-02-02 it launched a public API
  Portal for the Lone Wolf Foundation platform, and its documentation hub at apidocs.lwolf.com publishes seven complete, anonymously downloadable OpenAPI 3.0 definitions (Transact, Deals, Back Office, Authentisign, TransactionDesk, zipForm and WolfConnect) plus an MCP server endpoint. Documentation is genuinely open; credentials are not. Keys are issued only after an access-request form is reviewed by the integrations team, and the zipForm API is explicitly licensed to third-party application partners. Lone Wolf is not a RESO-certified data distributor and publishes no RESO Web API, Data Dictionary endpoint, OData $metadata document or Universal Property Identifier — RESO certification governs MLS listing feeds, which is not the layer Lone Wolf occupies; it consumes MLS data under MLS agreements (Cloud CMA documents RETS live queries) rather than redistributing it.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: MCP server manifest and captured tools/list
  slug: mcp-server-manifest-and-captured-toolslist
modified: '2026-08-13'
name: Lone Wolf Technologies
nav: Providers
network: true
overview: 'Lone Wolf Technologies publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Lone Wolf Transact API, Lone Wolf Deals API, Lone Wolf Back Office API, and 4 more. Tagged areas include Real Estate, United States, PropTech, Transactions, and Transaction Management.


  The Lone Wolf Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lone Wolf Technologies'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, engineering blog, changelog, and 51 more developer resources.'
plans:
- name: Lone Wolf Plans Pricing
  plan_count: 0
  slug: lone-wolf-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Lone Wolf Rate Limits
  slug: lone-wolf-rate-limits
scopes:
- name: Lone Wolf Scopes
  scope_count: 14
  slug: lone-wolf-scopes
  summary_line: 14 scopes
score:
  band: developing
  composite: 53.8
  delta: 1.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 65.4
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 71.4
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lone-wolf/refs/heads/main/screenshots/lone-wolf-2026-08-07T171753.png
security:
- kind: authentication
  name: Lone Wolf Authentication
  slug: lone-wolf-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Lone Wolf Domain Security
  slug: lone-wolf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lone-wolf
tags:
- Real Estate
- United States
- PropTech
- Transactions
- Transaction Management
- Brokerage Back Office
- Real Estate Accounting
- Commissions
- Forms
- zipForm
- TransactionDesk
- E-Signature
- CMA
- Valuation
- CRM
- MLS
- Real Estate Agents
- Brokers
website: https://www.lwolf.com/
---
