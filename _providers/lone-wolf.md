---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 174
  human_in_the_loop: 1
  name: Lone Wolf Agentic Access
  operation_count: 348
  slug: lone-wolf-agentic-access
  summary_line: 348 operations · 174 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: E-signature API for Authentisign, Lone Wolf's signing product. Creates and manages signings, signer roles, documents and signing status. Supports an optional CallbackUrl on a signing, and a PATCH endp
  name: Lone Wolf Authentisign API
  slug: lone-wolf-authentisign-api
- description: The Accounts API from Lone Wolf Technologies — 1 operation(s) for accounts.
  name: Lone Wolf Technologies Accounts API
  slug: lone-wolf-accounts-api
- description: The Authentication API from Lone Wolf Technologies — 6 operation(s) for authentication.
  name: Lone Wolf Technologies Authentication API
  slug: lone-wolf-authentication-api
- description: OAuth 2.0 client credentials token endpoint.
  name: Lone Wolf Technologies Authorization API
  slug: lone-wolf-authorization-api
- description: The Business Contact API from Lone Wolf Technologies — 8 operation(s) for business contact.
  name: Lone Wolf Technologies Business Contact API
  slug: lone-wolf-business-contact-api
- description: 'Business contacts represent a business or third party that is part of a transaction such as a home inspector or a lawyer. They do not represent the buyer or seller. For buyer and seller contacts, use '
  name: Lone Wolf Technologies Business Contacts API
  slug: lone-wolf-business-contacts-api
- description: The CCs API from Lone Wolf Technologies — 2 operation(s) for ccs.
  name: Lone Wolf Technologies C Cs API
  slug: lone-wolf-ccs-api
- description: The Classification API from Lone Wolf Technologies — 2 operation(s) for classification.
  name: Lone Wolf Technologies Classification API
  slug: lone-wolf-classification-api
- description: Classifications relate to the commission structure of a transaction.
  name: Lone Wolf Technologies Classifications API
  slug: lone-wolf-classifications-api
- description: The Client Contact API from Lone Wolf Technologies — 8 operation(s) for client contact.
  name: Lone Wolf Technologies Client Contact API
  slug: lone-wolf-client-contact-api
- description: Client contacts represent a buyer or seller that is part of a transaction. For all other types of contacts, use business contacts.
  name: Lone Wolf Technologies Client Contacts API
  slug: lone-wolf-client-contacts-api
- description: The Commission API from Lone Wolf Technologies — 2 operation(s) for commission.
  name: Lone Wolf Technologies Commission API
  slug: lone-wolf-commission-api
- description: Represents fees that are associated with commissions.
  name: Lone Wolf Technologies Commission Fees API
  slug: lone-wolf-commission-fees-api
- description: Represents the commissions and the related agent's within the brokerage that receive those commissions. For commissions related to agent's that are not part of the brokerage, use external commissions.
  name: Lone Wolf Technologies Commissions API
  slug: lone-wolf-commissions-api
- description: The Condition API from Lone Wolf Technologies — 2 operation(s) for condition.
  name: Lone Wolf Technologies Condition API
  slug: lone-wolf-condition-api
- description: The Condition Type API from Lone Wolf Technologies — 2 operation(s) for condition type.
  name: Lone Wolf Technologies Condition Type API
  slug: lone-wolf-condition-type-api
- description: Represents some common conditions that can be added to transactions.
  name: Lone Wolf Technologies Condition Types API
  slug: lone-wolf-condition-types-api
- description: Represents the conditions that exist on the transaction before it can be closed.
  name: Lone Wolf Technologies Conditions API
  slug: lone-wolf-conditions-api
- description: The Contact Type API from Lone Wolf Technologies — 2 operation(s) for contact type.
  name: Lone Wolf Technologies Contact Type API
  slug: lone-wolf-contact-type-api
- description: Represents the types of contacts for both business and client.
  name: Lone Wolf Technologies Contact Types API
  slug: lone-wolf-contact-types-api
- description: Manage transaction contacts.
  name: Lone Wolf Technologies Contacts API
  slug: lone-wolf-contacts-api
- description: The Deal API from Lone Wolf Technologies — 7 operation(s) for deal.
  name: Lone Wolf Technologies Deal API
  slug: lone-wolf-deal-api
- description: The Deposit API from Lone Wolf Technologies — 2 operation(s) for deposit.
  name: Lone Wolf Technologies Deposit API
  slug: lone-wolf-deposit-api
- description: Represents the deposits that have are required for the transaction.
  name: Lone Wolf Technologies Deposits API
  slug: lone-wolf-deposits-api
- description: The Documents API from Lone Wolf Technologies — 17 operation(s) for documents.
  name: Lone Wolf Technologies Documents API
  slug: lone-wolf-documents-api
- description: Represents a person that works at the brokerage. This includes the broker themselves, office admins, agent's, everyone.
  name: Lone Wolf Technologies Employees API
  slug: lone-wolf-employees-api
- description: The External Agent API from Lone Wolf Technologies — 8 operation(s) for external agent.
  name: Lone Wolf Technologies External Agent API
  slug: lone-wolf-external-agent-api
- description: Represents agents that are on the transaction but are not part of the brokerage.
  name: Lone Wolf Technologies External Agents API
  slug: lone-wolf-external-agents-api
- description: The External Commission API from Lone Wolf Technologies — 2 operation(s) for external commission.
  name: Lone Wolf Technologies External Commission API
  slug: lone-wolf-external-commission-api
- description: Represents the external commissions and the related external agent's that are not part of the brokerage that receive those commissions. For commissions related to agent's that are part of the brokerag
  name: Lone Wolf Technologies External Commissions API
  slug: lone-wolf-external-commissions-api
- description: Represents the different features that are enabled or disabled for a client.
  name: Lone Wolf Technologies Features API
  slug: lone-wolf-features-api
- description: Manage folders within transactions.
  name: Lone Wolf Technologies Folders API
  slug: lone-wolf-folders-api
- description: Browse form libraries and library forms (Forms Design service).
  name: Lone Wolf Technologies Form Libraries API
  slug: lone-wolf-form-libraries-api
- description: Manage forms and file documents within transactions.
  name: Lone Wolf Technologies Forms and Documents API
  slug: lone-wolf-forms-and-documents-api
- description: The History API from Lone Wolf Technologies — 1 operation(s) for history.
  name: Lone Wolf Technologies History API
  slug: lone-wolf-history-api
- description: The Layouts API from Lone Wolf Technologies — 3 operation(s) for layouts.
  name: Lone Wolf Technologies Layouts API
  slug: lone-wolf-layouts-api
- description: 'The Members resource is a RESTful web resource running on Microsoft''s Web API allowing third parties to access member data. The following actions are currently supported: - Retrieve a member or a coll'
  name: Lone Wolf Technologies Members API
  slug: lone-wolf-members-api
- description: Retrieve metadata and property specifications for API resources
  name: Lone Wolf Technologies Metadata API
  slug: lone-wolf-metadata-api
- description: Manage offers on transactions.
  name: Lone Wolf Technologies Offers API
  slug: lone-wolf-offers-api
- description: Represents the different physical offices that make up the brokerage.
  name: Lone Wolf Technologies Offices API
  slug: lone-wolf-offices-api
- description: Additional endpoints including users, form libraries, and transaction forms
  name: Lone Wolf Technologies Other Endpoints API
  slug: lone-wolf-other-endpoints-api
- description: The Participants API from Lone Wolf Technologies — 3 operation(s) for participants.
  name: Lone Wolf Technologies Participants API
  slug: lone-wolf-participants-api
- description: The Property Type API from Lone Wolf Technologies — 2 operation(s) for property type.
  name: Lone Wolf Technologies Property Type API
  slug: lone-wolf-property-type-api
- description: Represents the different property types that can be associated to a transaction.
  name: Lone Wolf Technologies Property Types API
  slug: lone-wolf-property-types-api
- description: Share transactions with groups of users and manage group membership.
  name: Lone Wolf Technologies Share Groups API
  slug: lone-wolf-share-groups-api
- description: The Signings API from Lone Wolf Technologies — 23 operation(s) for signings.
  name: Lone Wolf Technologies Signings API
  slug: lone-wolf-signings-api
- description: Generate one-time-use SSO links for the agent dashboard, transaction list, or a specific transaction
  name: Lone Wolf Technologies Single Sign On API
  slug: lone-wolf-single-sign-on-api
- description: The Source of Business API from Lone Wolf Technologies — 1 operation(s) for source of business.
  name: Lone Wolf Technologies Source of Business API
  slug: lone-wolf-source-of-business-api
- description: Represents the different sources of business that were used to find the buyers and sellers.
  name: Lone Wolf Technologies Sources of Business API
  slug: lone-wolf-sources-of-business-api
- description: The Sso API from Lone Wolf Technologies — 2 operation(s) for sso.
  name: Lone Wolf Technologies SSO API
  slug: lone-wolf-sso-api
- description: Manage team-based transaction access for agents in brokerage or team scenarios.
  name: Lone Wolf Technologies Teams API
  slug: lone-wolf-teams-api
- description: List and apply transaction templates.
  name: Lone Wolf Technologies Templates API
  slug: lone-wolf-templates-api
- description: The Tier API from Lone Wolf Technologies — 3 operation(s) for tier.
  name: Lone Wolf Technologies Tier API
  slug: lone-wolf-tier-api
- description: Represents a tier or sub-transaction for a given transaction. All transactions must have at least one tier.
  name: Lone Wolf Technologies Tiers API
  slug: lone-wolf-tiers-api
- description: Allow title partners to update title order status and manage notes on transactions.
  name: Lone Wolf Technologies Title Integration API
  slug: lone-wolf-title-integration-api
- description: Manage contact type definitions
  name: Lone Wolf Technologies Transaction Contact Types API
  slug: lone-wolf-transaction-contact-types-api
- description: Manage contacts associated with transaction files
  name: Lone Wolf Technologies Transaction Contacts API
  slug: lone-wolf-transaction-contacts-api
- description: Manage documents within transaction files
  name: Lone Wolf Technologies Transaction Documents API
  slug: lone-wolf-transaction-documents-api
- description: Manage forms attached to a transaction's form package (Forms Editor service).
  name: Lone Wolf Technologies Transaction Forms API
  slug: lone-wolf-transaction-forms-api
- description: Manage transaction status definitions
  name: Lone Wolf Technologies Transaction Statuses API
  slug: lone-wolf-transaction-statuses-api
- description: Create, read, update, and delete transaction files and their property details
  name: Lone Wolf Technologies Transaction Summary API
  slug: lone-wolf-transaction-summary-api
- description: Read transaction templates available to a user.
  name: Lone Wolf Technologies Transaction Templates API
  slug: lone-wolf-transaction-templates-api
- description: Manage transaction type definitions
  name: Lone Wolf Technologies Transaction Types API
  slug: lone-wolf-transaction-types-api
- description: Represents a transaction.
  name: Lone Wolf Technologies Transactions API
  slug: lone-wolf-transactions-api
- description: Users and offices belonging to a client account (Platform service).
  name: Lone Wolf Technologies Users and Offices API
  slug: lone-wolf-users-and-offices-api
artifact_total: 81
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lone-wolf-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lone-wolf-transact-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lone-wolf-deals-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lone-wolf-back-office-online-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lone-wolf-transactiondesk-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lone-wolf-zipform-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lone-wolf-wolfconnect-api-overlay.yaml
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
  name: Lone Wolf Technologies MCP Server
  slug: lone-wolf-technologies-mcp-server
- description: ''
  name: MCP server manifest and captured tools/list
  slug: mcp-server-manifest-and-captured-toolslist
modified: '2026-08-13'
name: Lone Wolf Technologies
nav: Providers
network: true
overview: 'Lone Wolf Technologies publishes 65 APIs on the [APIs.io](https://apis.io/) network, including Lone Wolf Authentisign API, Accounts API, Authentication API, and 62 more. Tagged areas include Real-Estate, United States, PropTech, Transaction, and Transaction Management.


  The Lone Wolf Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lone Wolf Technologies'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, engineering blog, changelog, and 58 more developer resources.'
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
  composite: 50.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 63.8
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Real-Estate
- United States
- PropTech
- Transaction
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
