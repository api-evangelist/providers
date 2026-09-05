---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-04'
api_count: 138
apis:
- description: Remote Model Context Protocol server for impact.com. Fifteen documented tools give an AI assistant account-scoped access to performance analytics, invoices, partner and program discovery, promo codes,
  name: Impact MCP Server
  slug: mcp-server
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Account API from Impact — 2 operation(s) for account.
  name: Impact Account API
  slug: impact-account-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for managing partner company account information.
  name: Impact Accounts API
  slug: impact-accounts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Action Inquiries API from Impact — 4 operation(s) for action inquiries.
  name: Impact Action Inquiries API
  slug: impact-action-inquiries-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Action Updates API from Impact — 2 operation(s) for action updates.
  name: Impact Action Updates API
  slug: impact-action-updates-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Actions API from Impact — 10 operation(s) for actions.
  name: Impact Actions API
  slug: impact-actions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Ads API from Impact — 7 operation(s) for ads.
  name: Impact Ads API
  slug: impact-ads-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Advertiser accounts managed by this agency.
  name: Impact Advertisers API
  slug: impact-advertisers-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The API Submissions API from Impact — 2 operation(s) for api submissions.
  name: Impact API Submissions API
  slug: impact-api-submissions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Call Data API from Impact — 1 operation(s) for call data.
  name: Impact Call Data API
  slug: impact-call-data-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Catalog Items API from Impact — 3 operation(s) for catalog items.
  name: Impact Catalog Items API
  slug: impact-catalog-items-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Catalogs API from Impact — 8 operation(s) for catalogs.
  name: Impact Catalogs API
  slug: impact-catalogs-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The ClickExport API from Impact — 2 operation(s) for clickexport.
  name: Impact Click Export API
  slug: impact-clickexport-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Clicks API from Impact — 2 operation(s) for clicks.
  name: Impact Clicks API
  slug: impact-clicks-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Your agency's company profile, addresses, and key contacts.
  name: Impact Company Information API
  slug: impact-company-information-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Submit content for impact.com compliance monitoring and retrieve job status and results.
  name: Impact Compliance Content API
  slug: impact-compliance-content-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Contacts API from Impact — 2 operation(s) for contacts.
  name: Impact Contacts API
  slug: impact-contacts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Contracts API from Impact — 5 operation(s) for contracts.
  name: Impact Contracts API
  slug: impact-contracts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Conversions API from Impact — 2 operation(s) for conversions.
  name: Impact Conversions API
  slug: impact-conversions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Deals API from Impact — 4 operation(s) for deals.
  name: Impact Deals API
  slug: impact-deals-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Deferred Deep Linking API from Impact — 1 operation(s) for deferred deep linking.
  name: Impact Deferred Deep Linking API
  slug: impact-deferred-deep-linking-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Inbound webhook payloads that impact.com sends to a partner-configured URL when events occur.
  name: Impact Event Notifications API
  slug: impact-event-notifications-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Exception List Items API from Impact — 2 operation(s) for exception list items.
  name: Impact Exception List Items API
  slug: impact-exception-list-items-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Exception Lists API from Impact — 4 operation(s) for exception lists.
  name: Impact Exception Lists API
  slug: impact-exception-lists-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: 'Endpoints for working with bulk data exports: create a new export, look up the status of an existing export, download a completed export, and list recent exports.'
  name: Impact Export API
  slug: impact-export-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The FTP Submissions API from Impact — 3 operation(s) for ftp submissions.
  name: Impact FTP Submissions API
  slug: impact-ftp-submissions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoint for creating and resuming identity verification sessions.
  name: Impact Identity Verification API
  slug: impact-identity-verification-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Invoices API from Impact — 6 operation(s) for invoices.
  name: Impact Invoices API
  slug: impact-invoices-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Schedule, monitor, replay, and download large-scale asynchronous jobs.
  name: Impact Jobs API
  slug: impact-jobs-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Legal Entities API from Impact — 2 operation(s) for legal entities.
  name: Impact Legal Entities API
  slug: impact-legal-entities-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for listing, creating, retrieving, updating, and deleting partner media properties.
  name: Impact Media Properties API
  slug: impact-media-properties-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Notes API from Impact — 2 operation(s) for notes.
  name: Impact Notes API
  slug: impact-notes-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Special methods designed for Client-facing applications like the Mobile and Javascript SDKs.
  name: Impact Open Endpoint API
  slug: impact-open-endpoint-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Page Load API from Impact — 1 operation(s) for page load.
  name: Impact Page Load API
  slug: impact-page-load-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Partner Groups API from Impact — 2 operation(s) for partner groups.
  name: Impact Partner Groups API
  slug: impact-partner-groups-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Partners API from Impact — 2 operation(s) for partners.
  name: Impact Partners API
  slug: impact-partners-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Phone Numbers API from Impact — 2 operation(s) for phone numbers.
  name: Impact Phone Numbers API
  slug: impact-phone-numbers-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Programs API from Impact — 5 operation(s) for programs.
  name: Impact Programs API
  slug: impact-programs-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Promo Code Exception List Items API from Impact — 2 operation(s) for promo code exception list items.
  name: Impact Promo Code Exception List Items API
  slug: impact-promo-code-exception-list-items-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Promo Code Exception Lists API from Impact — 4 operation(s) for promo code exception lists.
  name: Impact Promo Code Exception Lists API
  slug: impact-promo-code-exception-lists-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Promo Codes API from Impact — 4 operation(s) for promo codes.
  name: Impact Promo Codes API
  slug: impact-promo-codes-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for listing and retrieving brand promotions available to your partner account.
  name: Impact Promotions API
  slug: impact-promotions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: A Referral tracks who has referred whom.
  name: Impact Referral API
  slug: impact-referral-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: 'Endpoints for working with referral codes: look up a code and its associated reward, or apply a code to a referred account. For background on what referral codes are, see the Referral Code Overview.'
  name: Impact Referral Code API
  slug: impact-referral-code-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Report Export API from Impact — 2 operation(s) for report export.
  name: Impact Report Export API
  slug: impact-report-export-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Asynchronously export reports through impact.com's Jobs system. Recommended for all report downloads.
  name: Impact Report Export API
  slug: impact-reportexport-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: List available reports, fetch their metadata, and run them synchronously.
  name: Impact Reports API
  slug: impact-reports-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Legacy synchronous reports endpoint. Subject to pagination limits — prefer `ReportExport` for large datasets.
  name: Impact Reports (Legacy) API
  slug: impact-reports-legacy-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: A Reward keeps track of a prize, discount or credit that someone has received. All reward types other than gift card integrated rewards can be cancelled using the impact.com API, or through the impact
  name: Impact Reward API
  slug: impact-reward-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Reward Balances summarizes the Rewards in someone's account.
  name: Impact Reward Balance API
  slug: impact-reward-balance-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Routing Rules API from Impact — 2 operation(s) for routing rules.
  name: Impact Routing Rules API
  slug: impact-routing-rules-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for retrieving the share links of a given user. Share links are organised by engagement medium and share medium. For background on how they work, see the Share Links Overview.
  name: Impact Share Links API
  slug: impact-share-links-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for browsing partner storefronts, their groups, and the catalog items inside them.
  name: Impact Stores API
  slug: impact-stores-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Tasks API from Impact — 4 operation(s) for tasks.
  name: Impact Tasks API
  slug: impact-tasks-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for creating, completing, and retrieving partner tax documents.
  name: Impact Tax Documents API
  slug: impact-tax-documents-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Tracking Links API from Impact — 2 operation(s) for tracking links.
  name: Impact Tracking Links API
  slug: impact-tracking-links-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Tracking Value Requests API from Impact — 2 operation(s) for tracking value requests.
  name: Impact Tracking Value Requests API
  slug: impact-tracking-value-requests-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Unsubscribed Contacts API from Impact — 1 operation(s) for unsubscribed contacts.
  name: Impact Unsubscribed Contacts API
  slug: impact-unsubscribed-contacts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: API for managing users, including creation, lookup, and blocking.
  name: Impact User API
  slug: impact-user-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for listing and retrieving partner-account users.
  name: Impact Users API
  slug: impact-users-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: 'Endpoints for managing webhook subscriptions: list current subscriptions, register new endpoint URLs, remove existing ones, and send a test event to verify a subscription.'
  name: Impact Webhook API
  slug: impact-webhook-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for retrieving and updating your bank account, PayPal, and payment scheduling settings.
  name: Impact Withdrawal Settings API
  slug: impact-withdrawal-settings-api
artifact_total: 73
asyncapis:
- description: ''
  name: Impact Webhooks
  slug: impact-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/impact-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/impact-brand-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/impact-partner-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/impact-agency-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/impact-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://impact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.impact.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ImpactInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/impactdotcom
- group: company
  title: ''
  type: Blog
  url: https://impact.com/press-releases/
- group: commercial
  title: ''
  type: Pricing
  url: https://impact.com/get-started/
- group: other
  title: ''
  type: X
  url: https://x.com/impactdotcom
- group: commercial
  title: ''
  type: Plans
  url: plans/impact-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/impact-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/impact-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/impact-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.impact.com/
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.impact.com/brand-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.impact.com/rest-apis/api-quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.impact.com/
- group: start
  title: ''
  type: SignUp
  url: https://impact.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impact.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impact.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.impact.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/impact-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impact-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/impact-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/impact-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/impact-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/impact-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/impact-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impact-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/impact-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/impact-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/impact-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/impact-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/impact-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/impact-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impact-packages.yml
- group: design
  title: ''
  type: Components
  url: components/impact-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/impact-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/impact-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impact-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impact-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/impact-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/impact-webhooks.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/impact-advocate-graphql.yml
created: '2026-06-13'
description: impact.com is a partnership management platform for affiliate, creator, influencer and customer-referral programs. It publishes four REST API personas - Brand v14, Partner v16, Agency v3 and Advocate v13 - across 69 OpenAPI 3.1 documents and 245 operations, a remote OAuth 2.1 MCP server at mcp.impact.com, first-party agent skills, an Advocate GraphQL endpoint, webhook and postback event delivery, and an agent-readable developer portal that serves llms.txt, per-page markdown and a live documentation question interface.
finops:
- name: Impact Finops
  service_category: ''
  slug: impact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impact.png
jsonld:
- class_count: 0
  name: Impact Context
  property_count: 2
  slug: impact-context
layout: provider
mcp_servers:
- description: First-party remote Model Context Protocol server for the impact.com partnership management platform. Exposes account-scoped tools for performance analytics, invoices, partner and program discovery, pr
  name: impact.com MCP Server
  slug: impactcom-mcp-server
modified: '2026-08-13'
name: Impact
nav: Providers
network: true
overview: 'Impact publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Action Inquiries API, and 58 more. Tagged areas include Affiliates, Partnerships, Performance Marketing, Commission, and Tracking.


  The Impact catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Impact''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, signup flow, and 43 more developer resources.'
plans:
- name: Impact Plans Pricing
  plan_count: 0
  slug: impact-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Impact Rate Limits
  slug: impact-rate-limits
scopes:
- name: Impact Scopes
  scope_count: 0
  slug: impact-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 12.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 4.5
    contract_quality: 63.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 94.7
  previous_composite: 65.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 61
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impact/refs/heads/main/screenshots/impact-2026-06-20T183254.png
security:
- kind: authentication
  name: Impact Authentication
  slug: impact-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Impact Domain Security
  slug: impact-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Impact Vulnerability Disclosure
  slug: impact-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Impact Trust Center
  slug: impact-trust-center
  summary_line: SOC 1 Type II, ISO/IEC 27001:2022, PCI DSS Level 4
slug: impact
tags:
- Affiliates
- Partnerships
- Performance Marketing
- Commission
- Tracking
- Creator Economy
- Partner Management
- Referral
- Attribution
- Payouts
- Marketing
- Advertising
- MCP
- Agents
website: https://impact.com/
---
