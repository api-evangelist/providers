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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 61
  human_in_the_loop: 0
  name: Lobcom Agentic Access
  operation_count: 105
  slug: lobcom-agentic-access
  summary_line: 105 operations · 61 acting
api_count: 30
apis:
- description: The Accounts API from Lob.com — 1 operation(s) for accounts.
  name: Lob.com Accounts API
  slug: lobcom-accounts-api
- description: To add an address to your address book, you create a new address object. You can retrieve and delete individual addresses as well as get a list of addresses. Addresses are identified by a unique rando
  name: Lob.com Addresses API
  slug: lobcom-addresses-api
- description: Bank Accounts allow you to store your bank account securely in our system. The API provides endpoints for creating bank accounts, deleting bank accounts, verifying bank accounts, retrieving individual
  name: Lob.com Bank Accounts API
  slug: lobcom-bank-accounts-api
- description: The Billing Groups API allows you to create and view labels that can be attached to certain consumption-based usages of Letters, Checks, Postcards and Self-Mailers to customize your bill. Please check
  name: Lob.com Billing Groups API
  slug: lobcom-billing-groups-api
- description: The Booklets API from Lob.com — 2 operation(s) for booklets.
  name: Lob.com Booklets API
  slug: lobcom-booklets-api
- description: The Buckslip Orders endpoint allows you to easily create buckslip orders for existing buckslips. The API provides endpoints for creating buckslip orders and listing buckslip orders for a given bucksli
  name: Lob.com Buckslip Orders API
  slug: lobcom-buckslip-orders-api
- description: 'The Buckslips endpoint allows you to easily create buckslips that can later be used as add-ons for Letters Campaigns. Note that a Letter Campaign with Buckslip add-on requires a minimum send quantity '
  name: Lob.com Buckslips API
  slug: lobcom-buckslips-api
- description: The campaigns endpoint allows you to create and view campaigns that can be used to send multiple letters or postcards. The API provides endpoints for creating campaigns, updating campaigns, retrieving
  name: Lob.com Campaigns API
  slug: lobcom-campaigns-api
- description: The card orders endpoint allows you to easily create card orders for existing cards. The API provides endpoints for creating card orders and listing card orders for a given card. <div class="back-to-t
  name: Lob.com Card Orders API
  slug: lobcom-card-orders-api
- description: The cards endpoint allows you to easily create cards that can later be affixed to Letters. The API provides endpoints for creating cards, retrieving individual cards, creating card orders, and retriev
  name: Lob.com Cards API
  slug: lobcom-cards-api
- description: Checks allow you to send payments via physical checks. The API provides endpoints for creating checks, retrieving individual checks, canceling checks, and retrieving a list of checks. <div class="back
  name: Lob.com Checks API
  slug: lobcom-checks-api
- description: The creatives endpoint allows you to create and view creatives. Creatives are used to create reusable letter and postcard templates. The API provides endpoints for creating creatives, updating creativ
  name: Lob.com Creatives API
  slug: lobcom-creatives-api
- description: Validates whether a given name is associated with an address. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Identity Validation API
  slug: lobcom-identity-validation-api
- description: The Informed Delivery campaigns API allows you to create and view Informed Delivery campaigns. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Informed Delivery Campaign API
  slug: lobcom-informed-delivery-campaign-api
- description: 'Address verification for non-US addresses <br> <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div> ## Intl Verifications Test Env When verifying international addresses, '
  name: Lob.com Intl Verifications API
  slug: lobcom-intl-verifications-api
- description: The letters endpoint allows you to easily print and mail letters. The API provides endpoints for creating letters, retrieving individual letters, canceling letters, and retrieving a list of letters. <
  name: Lob.com Letters API
  slug: lobcom-letters-api
- description: The Lob Credits API from Lob.com — 1 operation(s) for lob credits.
  name: Lob.com Lob Credits API
  slug: lobcom-lob-credits-api
- description: 'The postcards endpoint allows you to easily print and mail postcards. The API provides endpoints for creating postcards, retrieving individual postcards, canceling postcards, and retrieving a list of '
  name: Lob.com Postcards API
  slug: lobcom-postcards-api
- description: Lob QR codes allow you to generate a QR code that is unique to each mailpiece, thereby allowing each and every customers to receive a personalized link. See the Create endpoint for <a href="#tag/Lette
  name: Lob.com QR Codes API
  slug: lobcom-qr-codes-api
- description: The resource proofs endpoint allows you to create a final rendering of any template. This is best practice to ensure that you are visually validating your creative before any mail pieces use the templ
  name: Lob.com Resource Proofs API
  slug: lobcom-resource-proofs-api
- description: Find a list of zip codes associated with a valid US location via latitude and longitude. <br> <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Reverse Geocode Lookups API
  slug: lobcom-reverse-geocode-lookups-api
- description: The self mailer endpoint allows you to easily print and mail self mailers. The API provides endpoints for creating self mailers, retrieving individual self mailers, canceling self mailers, and retriev
  name: Lob.com Self Mailers API
  slug: lobcom-self-mailers-api
- description: The Snap Packs API from Lob.com — 2 operation(s) for snap packs.
  name: Lob.com Snap Packs API
  slug: lobcom-snap-packs-api
- description: These API endpoints allow you to create, retrieve, update and delete versions of reusable HTML templates for use with the Print & Mail API. <div class="back-to-top" ><a href="#" onclick="toTopLink()">
  name: Lob.com Template Versions API
  slug: lobcom-template-versions-api
- description: These API endpoints allow you to create, retrieve, update and delete reusable HTML templates for use with the Print & Mail API. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top<
  name: Lob.com Templates API
  slug: lobcom-templates-api
- description: The uploads endpoint allows you to upload audience files that are then associated with a given campaign. At this time, only CSV files are allowed. The API provides endpoints for creating uploads, uplo
  name: Lob.com Uploads API
  slug: lobcom-uploads-api
- description: Lob's URL shortener allows you to generate unique short links, either with Lob's own domain or your own custom domains. Each custom link enables Lob to track mail individually and provide customers th
  name: Lob.com URL Shortener API
  slug: lobcom-url-shortener-api
- description: 'Given partial address information, this endpoint returns up to 10 address suggestions. <br> <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div> ## Autocompletion Test Env'
  name: Lob.com US Autocompletions API
  slug: lobcom-us-autocompletions-api
- description: Validate, automatically correct, and standardize the addresses in your address book based on USPS's <a href="https://postalpro.usps.com/certifications/cass" target="_blank">Coding Accuracy Support Sys
  name: Lob.com US Verifications API
  slug: lobcom-us-verifications-api
- description: Find a list of cities, states and associated information about a US ZIP code. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Zip Lookups API
  slug: lobcom-zip-lookups-api
artifact_total: 35
asyncapis:
- description: ''
  name: Lobcom Webhooks
  slug: lobcom-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lob.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lob.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lob.com/#tag/Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://help.lob.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lob.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lob
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lob.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.lob.com/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.lob.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lob.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lob.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lob.com/
- group: build
  title: ''
  type: Packages
  url: packages/lobcom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lobcom-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lobcom-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lobcom-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lobcom-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/lobcom-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lobcom-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lobcom-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lobcom-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.lob.com/#tag/Versioning-and-Changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lobcom-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lobcom-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lobcom-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lobcom-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lobcom-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lobcom-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lobcom-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lobcom-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lobcom-agentic-access.yml
created: '2026-07-17'
description: Lob is the direct-mail and address-verification API for developers. Its REST API lets teams programmatically create and mail postcards, letters, checks, self-mailers, snap packs, booklets, buckslips and cards; verify and autocomplete US and international addresses; run direct-mail and USPS Informed Delivery campaigns; manage HTML templates; and track physical delivery through USPS scan events surfaced over webhooks. The API is organized around REST with resource-oriented URLs, HTTP Basic authentication using test_/live_ API keys, cursor pagination, Idempotency-Key support, and standard rate-limit headers. Lob was surfaced as an a16z portfolio company and enriched into the API Evangelist network from its public OpenAPI, docs, SDKs, and registries.
image: https://www.lob.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: lobcom-mcp.yml
  slug: lobcom-mcpyml
modified: '2026-07-20'
name: Lob.com
nav: Providers
network: true
overview: 'Lob.com publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Addresses API, Bank Accounts API, and 27 more. Tagged areas include Company, Direct Mail, Print, Address Verification, and Mail.


  The Lob.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lob.com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 4
score:
  band: strong
  composite: 57.0
  delta: -1.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.1
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lobcom/refs/heads/main/screenshots/lobcom-2026-07-25T225441.png
security:
- kind: authentication
  name: Lobcom Authentication
  slug: lobcom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lobcom Domain Security
  slug: lobcom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lobcom
tags:
- Company
- Direct Mail
- Print
- Address Verification
- Mail
- Postcards
- Letters
- Checks
- Campaigns
- USPS
- Deliverability
website: https://docs.lob.com/
---
