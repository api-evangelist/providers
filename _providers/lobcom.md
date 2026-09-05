---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 61
  human_in_the_loop: 0
  name: Lobcom Agentic Access
  operation_count: 105
  slug: lobcom-agentic-access
  summary_line: 105 operations · 61 acting
api_count: 1
apis:
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The Accounts API from Lob.com — 1 operation(s) for accounts.
  name: Lob.com Accounts API
  slug: lobcom-accounts-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: To add an address to your address book, you create a new address object. You can retrieve and delete individual addresses as well as get a list of addresses. Addresses are identified by a unique rando
  name: Lob.com Addresses API
  slug: lobcom-addresses-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Bank Accounts allow you to store your bank account securely in our system. The API provides endpoints for creating bank accounts, deleting bank accounts, verifying bank accounts, retrieving individual
  name: Lob.com Bank Accounts API
  slug: lobcom-bank-accounts-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The Billing Groups API allows you to create and view labels that can be attached to certain consumption-based usages of Letters, Checks, Postcards and Self-Mailers to customize your bill. Please check
  name: Lob.com Billing Groups API
  slug: lobcom-billing-groups-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The Booklets API from Lob.com — 2 operation(s) for booklets.
  name: Lob.com Booklets API
  slug: lobcom-booklets-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The Buckslip Orders endpoint allows you to easily create buckslip orders for existing buckslips. The API provides endpoints for creating buckslip orders and listing buckslip orders for a given bucksli
  name: Lob.com Buckslip Orders API
  slug: lobcom-buckslip-orders-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: 'The Buckslips endpoint allows you to easily create buckslips that can later be used as add-ons for Letters Campaigns. Note that a Letter Campaign with Buckslip add-on requires a minimum send quantity '
  name: Lob.com Buckslips API
  slug: lobcom-buckslips-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The campaigns endpoint allows you to create and view campaigns that can be used to send multiple letters or postcards. The API provides endpoints for creating campaigns, updating campaigns, retrieving
  name: Lob.com Campaigns API
  slug: lobcom-campaigns-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The card orders endpoint allows you to easily create card orders for existing cards. The API provides endpoints for creating card orders and listing card orders for a given card. <div class="back-to-t
  name: Lob.com Card Orders API
  slug: lobcom-card-orders-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The cards endpoint allows you to easily create cards that can later be affixed to Letters. The API provides endpoints for creating cards, retrieving individual cards, creating card orders, and retriev
  name: Lob.com Cards API
  slug: lobcom-cards-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Checks allow you to send payments via physical checks. The API provides endpoints for creating checks, retrieving individual checks, canceling checks, and retrieving a list of checks. <div class="back
  name: Lob.com Checks API
  slug: lobcom-checks-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The creatives endpoint allows you to create and view creatives. Creatives are used to create reusable letter and postcard templates. The API provides endpoints for creating creatives, updating creativ
  name: Lob.com Creatives API
  slug: lobcom-creatives-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Validates whether a given name is associated with an address. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Identity Validation API
  slug: lobcom-identity-validation-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The Informed Delivery campaigns API allows you to create and view Informed Delivery campaigns. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Informed Delivery Campaign API
  slug: lobcom-informed-delivery-campaign-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: 'Address verification for non-US addresses <br> <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div> ## Intl Verifications Test Env When verifying international addresses, '
  name: Lob.com Intl Verifications API
  slug: lobcom-intl-verifications-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The letters endpoint allows you to easily print and mail letters. The API provides endpoints for creating letters, retrieving individual letters, canceling letters, and retrieving a list of letters. <
  name: Lob.com Letters API
  slug: lobcom-letters-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The Lob Credits API from Lob.com — 1 operation(s) for lob credits.
  name: Lob.com Lob Credits API
  slug: lobcom-lob-credits-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: 'The postcards endpoint allows you to easily print and mail postcards. The API provides endpoints for creating postcards, retrieving individual postcards, canceling postcards, and retrieving a list of '
  name: Lob.com Postcards API
  slug: lobcom-postcards-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Lob QR codes allow you to generate a QR code that is unique to each mailpiece, thereby allowing each and every customers to receive a personalized link. See the Create endpoint for <a href="#tag/Lette
  name: Lob.com QR Codes API
  slug: lobcom-qr-codes-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The resource proofs endpoint allows you to create a final rendering of any template. This is best practice to ensure that you are visually validating your creative before any mail pieces use the templ
  name: Lob.com Resource Proofs API
  slug: lobcom-resource-proofs-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Find a list of zip codes associated with a valid US location via latitude and longitude. <br> <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Reverse Geocode Lookups API
  slug: lobcom-reverse-geocode-lookups-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The self mailer endpoint allows you to easily print and mail self mailers. The API provides endpoints for creating self mailers, retrieving individual self mailers, canceling self mailers, and retriev
  name: Lob.com Self Mailers API
  slug: lobcom-self-mailers-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The Snap Packs API from Lob.com — 2 operation(s) for snap packs.
  name: Lob.com Snap Packs API
  slug: lobcom-snap-packs-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: These API endpoints allow you to create, retrieve, update and delete versions of reusable HTML templates for use with the Print & Mail API. <div class="back-to-top" ><a href="#" onclick="toTopLink()">
  name: Lob.com Template Versions API
  slug: lobcom-template-versions-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: These API endpoints allow you to create, retrieve, update and delete reusable HTML templates for use with the Print & Mail API. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top<
  name: Lob.com Templates API
  slug: lobcom-templates-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: The uploads endpoint allows you to upload audience files that are then associated with a given campaign. At this time, only CSV files are allowed. The API provides endpoints for creating uploads, uplo
  name: Lob.com Uploads API
  slug: lobcom-uploads-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Lob's URL shortener allows you to generate unique short links, either with Lob's own domain or your own custom domains. Each custom link enables Lob to track mail individually and provide customers th
  name: Lob.com URL Shortener API
  slug: lobcom-url-shortener-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: 'Given partial address information, this endpoint returns up to 10 address suggestions. <br> <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div> ## Autocompletion Test Env'
  name: Lob.com US Autocompletions API
  slug: lobcom-us-autocompletions-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Validate, automatically correct, and standardize the addresses in your address book based on USPS's <a href="https://postalpro.usps.com/certifications/cass" target="_blank">Coding Accuracy Support Sys
  name: Lob.com US Verifications API
  slug: lobcom-us-verifications-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: Find a list of cities, states and associated information about a US ZIP code. <div class="back-to-top" ><a href="#" onclick="toTopLink()">back to top</a></div>
  name: Lob.com Zip Lookups API
  slug: lobcom-zip-lookups-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: When various notable things happen within the Lob architecture, Events will be created. To get these events sent to your server automatically when they occur, you can set up [Webhooks](#tag/Webhooks).
  name: Lob.com Events API
  slug: lobcom-events-api
- baseURL: https://api.lob.com/v1
  baseurl_source: declared
  description: As mailpieces travel through the mail stream, USPS scans their unique barcodes, and Lob processes these mail scans to generate tracking events. <h3>Certified Tracking Event Details</h3> Letters sent w
  name: Lob.com Tracking Events API
  slug: lobcom-tracking-events-api
artifact_total: 72
asyncapis:
- description: ''
  name: Lobcom Webhooks
  slug: lobcom-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lob Accounts API
  slug: open-lobcom-accounts-api
- collection_type: open
  name: Lob Addresses API
  slug: open-lobcom-addresses-api
- collection_type: open
  name: Lob Bank Accounts API
  slug: open-lobcom-bank-accounts-api
- collection_type: open
  name: Lob Billing Groups API
  slug: open-lobcom-billing-groups-api
- collection_type: open
  name: Lob Booklets API
  slug: open-lobcom-booklets-api
- collection_type: open
  name: Lob Buckslip Orders API
  slug: open-lobcom-buckslip-orders-api
- collection_type: open
  name: Lob Buckslips API
  slug: open-lobcom-buckslips-api
- collection_type: open
  name: Lob Campaigns API
  slug: open-lobcom-campaigns-api
- collection_type: open
  name: Lob Card Orders API
  slug: open-lobcom-card-orders-api
- collection_type: open
  name: Lob Cards API
  slug: open-lobcom-cards-api
- collection_type: open
  name: Lob Checks API
  slug: open-lobcom-checks-api
- collection_type: open
  name: Lob Creatives API
  slug: open-lobcom-creatives-api
- collection_type: open
  name: Lob Events API
  slug: open-lobcom-events-api
- collection_type: open
  name: Lob Identity Validation API
  slug: open-lobcom-identity-validation-api
- collection_type: open
  name: Lob Informed Delivery Campaign API
  slug: open-lobcom-informed-delivery-campaign-api
- collection_type: open
  name: Lob Intl Verifications API
  slug: open-lobcom-intl-verifications-api
- collection_type: open
  name: Lob Letters API
  slug: open-lobcom-letters-api
- collection_type: open
  name: Lob Lob Credits API
  slug: open-lobcom-lob-credits-api
- collection_type: open
  name: Lob Postcards API
  slug: open-lobcom-postcards-api
- collection_type: open
  name: Lob QR Codes API
  slug: open-lobcom-qr-codes-api
- collection_type: open
  name: Lob Resource Proofs API
  slug: open-lobcom-resource-proofs-api
- collection_type: open
  name: Lob Reverse Geocode Lookups API
  slug: open-lobcom-reverse-geocode-lookups-api
- collection_type: open
  name: Lob Self Mailers API
  slug: open-lobcom-self-mailers-api
- collection_type: open
  name: Lob Snap Packs API
  slug: open-lobcom-snap-packs-api
- collection_type: open
  name: Lob Template Versions API
  slug: open-lobcom-template-versions-api
- collection_type: open
  name: Lob Templates API
  slug: open-lobcom-templates-api
- collection_type: open
  name: Lob Tracking Events API
  slug: open-lobcom-tracking-events-api
- collection_type: open
  name: Lob Uploads API
  slug: open-lobcom-uploads-api
- collection_type: open
  name: Lob URL Shortener API
  slug: open-lobcom-url-shortener-api
- collection_type: open
  name: Lob US Autocompletions API
  slug: open-lobcom-us-autocompletions-api
- collection_type: open
  name: Lob US Verifications API
  slug: open-lobcom-us-verifications-api
- collection_type: open
  name: Lob Zip Lookups API
  slug: open-lobcom-zip-lookups-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/lob/lob-openapi/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lobcom-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lobcom-openapi-overlay.yaml
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
  url: https://www.lob.com/privacy
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
  type: X-MCPServerCandidate
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
- group: build
  title: ''
  type: Postman
  url: https://raw.githubusercontent.com/lob/lob-openapi/main/dist/lob-api-postman.json
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/lob/lob-openapi
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.lob.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/lobcom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lobcom-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/lobcom-components.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lobcom-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/lobcom-trust-center.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lobcom-tool-crosswalk.yml
created: '2026-07-17'
description: Lob is the direct-mail and address-verification API for developers. Its REST API lets teams programmatically create and mail postcards, letters, checks, self-mailers, snap packs, booklets, buckslips and cards; verify and autocomplete US and international addresses; run direct-mail and USPS Informed Delivery campaigns; manage HTML templates; and track physical delivery through USPS scan events surfaced over webhooks. The API is organized around REST with resource-oriented URLs, HTTP Basic authentication using test_/live_ API keys, cursor pagination, Idempotency-Key support, and standard rate-limit headers. Lob was surfaced as an a16z portfolio company and enriched into the API Evangelist network from its public OpenAPI, docs, SDKs, and registries.
image: https://www.lob.com/favicon.ico
layout: provider
modified: '2026-08-13'
name: Lob.com
nav: Providers
network: true
overview: 'Lob.com publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Addresses API, Bank Accounts API, and 29 more. Tagged areas include Company, Direct Mail, Print, Address Verification, and Mail.


  The Lob.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lob.com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Lobcom Plans Pricing
  plan_count: 4
  slug: lobcom-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Lobcom Rate Limits
  slug: lobcom-rate-limits
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.0
    catalog_earned_first_party: 24.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 64.9
    developer_ergonomics: 72.0
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 77.6
  previous_composite: 63.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- kind: trust-center
  name: Lobcom Trust Center
  slug: lobcom-trust-center
  summary_line: SOC 2 Type 2, HIPAA, GDPR, CCPA/CPRA
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
