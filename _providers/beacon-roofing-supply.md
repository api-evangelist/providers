---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - '{''url'': ''https://www.becn.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.qxo.com/. RESOLVED 2026-09-04: this is an acquisition, not a stale domain — QXO, Inc. completed its acquisition of Beacon Roofing Supply on 2025-04-29 and folded the PRO+ web app into qxo.com. The API host did NOT move: https://beaconproplus.com/swagger/ and the /v1|/v2|/v3 REST bases still serve from the Beacon domain.''}'
  - '{''url'': ''https://go.qxo.com/qxoapi'', ''status'': 200, ''note'': ''API access is sales-gated: requester must already be a QXO customer and accept the API licence terms. No self-serve signup, no published price.''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-04'
api_count: 11
apis:
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: 'The primary Beacon Rest Services surface — 187 published operations covering the product catalog, account-specific real-time pricing, branch and region availability, cart and order submission, quotes '
  name: Beacon PRO+ API (V2, OAuth)
  slug: beacon-pro-plus
- baseURL: https://beaconproplus.com
  baseurl_source: declared
  description: The combined Beacon Rest Services document — 145 operations spanning the V1, V2, V3 and V4 tags plus the Integrations and Beacon Stack surfaces. It is the ONLY Beacon document that assigns operationId
  name: Beacon External Rest Service (all_api)
  slug: beacon-rest-all-api
- baseURL: https://beaconproplus.com/v3/rest/com/becn
  baseurl_source: declared
  description: Beacon's integration surface — bulk catalog, SKU, branch and product-availability extracts designed for ERP, PIM and estimating-system synchronisation, plus the Mincron ERP product mapping endpoint an
  name: Beacon Rest Services V3 (Public / Integrations)
  slug: beacon-rest-v3
- baseURL: https://beaconproplus.com/v1/rest/com/becn
  baseurl_source: declared
  description: The original Beacon PRO+ API surface — login and logout, account switching, branch list, jobs, order history and detail, catalog item lookup, pricing, cart items, order submission and templates. Ninet
  name: Beacon Rest Services V1 (session)
  slug: beacon-rest-v1
- baseURL: https://beaconproplus.com/rest/model/REST/oauth
  baseurl_source: declared
  description: Beacon's OAuth 2.0 token service, implementing the refresh_token grant and linking to https://oauth.net/2/grant-types/refresh-token/ in its own description. Returns access_token, token_type, expires_i
  name: Beacon OAuth Rest Service
  slug: beacon-oauth
- baseURL: https://beaconproplus.com/v2/rest/com/becn/public
  baseurl_source: declared
  description: A small unauthenticated-user surface published at /v2/rest/com/becn/public. Beacon documents it as APIs that "do not require the user to login", though a bearer token is still required to be authorize
  name: Beacon Rest Services Public
  slug: beacon-rest-public
- baseURL: https://beaconproplus.com/v2/rest/com/becn
  baseurl_source: declared
  description: An internal-facing Beacon service that is nonetheless listed on the same public Swagger index and whose documentation is served without authentication — user and internal-user administration, EagleVie
  name: Beacon Internal Rest Service
  slug: beacon-rest-internal
artifact_total: 27
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/beacon-roofing-supply-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beacon-roofing-supply-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beacon-building-products
- group: company
  title: ''
  type: Website
  url: https://www.becn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qxo.com/customapi
- group: docs
  title: ''
  type: Documentation
  url: https://beaconproplus.com/swagger/
- group: docs
  title: ''
  type: APIReference
  url: https://beaconproplus.com/swagger/v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://go.qxo.com/qxoapi
- group: start
  title: ''
  type: SignUp
  url: https://www.qxo.com/open-an-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qxo.com/integrations/api-license-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qxo.com/privacy-policy-and-cookie-notice
- group: operate
  title: ''
  type: Support
  url: https://www.qxo.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.qxo.com/qxo-blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://beaconproplus.com/swagger/dev/index.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/beacon-roofing-supply-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beacon-roofing-supply-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beacon-roofing-supply-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beacon-roofing-supply-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/beacon-roofing-supply-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beacon-roofing-supply-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/beacon-roofing-supply-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beacon-roofing-supply-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beacon-roofing-supply-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/beacon-roofing-supply-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beacon-roofing-supply-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/beacon-roofing-supply-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beacon-roofing-supply-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/beacon-roofing-supply-finops.yml
created: '2026-03-23'
description: 'Beacon Roofing Supply (formerly NASDAQ: BECN) is one of the largest distributors of residential and non-residential roofing materials and complementary building products in North America, operating roughly 600 branches. QXO, Inc. completed its acquisition of Beacon on 2025-04-29 and the business now trades under the QXO brand. Its contractor commerce platform, Beacon PRO+, publishes an unusually complete REST surface: eleven OpenAPI 3.0 documents totalling 424 operations, indexed at https://beaconproplus.com/swagger/ and covering catalog search, account-specific real-time pricing, branch availability, cart and order submission, quotes and approval workflows, order history, delivery tracking, invoices, manufacturer rebates, permission management and the EagleView, GAF QuickMeasure and Hover measurement integrations, plus an OAuth 2.0 token service and a change log covering 72 releases. Access is sales-gated at https://www.qxo.com/customapi; contracts are public.'
features:
- description: Access live product inventory levels and pricing across Beacon locations for accurate contractor quoting.
  name: Real-Time Inventory and Pricing
- description: Place, manage, and track roofing material orders programmatically through the Beacon PRO+ API.
  name: Online Ordering
- description: Real-time delivery status updates and tracking for all Beacon material orders.
  name: Delivery Tracking
- description: Manage contractor account details, billing, and payment information through the API.
  name: Account Management
- description: Receive storm event notifications to proactively reach out to customers in affected areas.
  name: Storm Tracking Alerts
- description: Track manufacturer rebate programs and earned rebates through the API.
  name: Rebate Tracking
finops:
- name: Beacon Roofing Supply Finops
  service_category: Construction Distribution / E-Commerce APIs
  slug: beacon-roofing-supply-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beacon-roofing-supply.png
integrations:
- description: Roofing contractor management software with native Beacon PRO+ integration for material ordering.
  name: AccuLynx
- description: Contractor CRM and project management platform with Beacon PRO+ material order integration.
  name: JobNimbus
- description: Roofing manufacturer partnership enabling GAF product ordering through Beacon PRO+ e-commerce.
  name: GAF
- description: EDI integration service enabling electronic purchase orders, ASNs, and invoices with Beacon Roofing Supply.
  name: TrueCommerce EDI
layout: provider
modified: '2026-09-04'
name: Beacon Roofing Supply
nav: Providers
network: true
overview: 'Beacon Roofing Supply publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Beacon PRO+ API (V2, OAuth), Beacon External Rest Service (all_api), Beacon Rest Services V3 (Public / Integrations), and 4 more. Tagged areas include Construction, Distribution, Roofing, Building Materials, and E-Commerce.


  Beacon Roofing Supply''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 22 more developer resources.'
plans:
- name: Beacon Roofing Supply Plans Pricing
  plan_count: 0
  slug: beacon-roofing-supply-plans-pricing
press:
- date: '2026-05-25'
  title: QXO completes the acquisition of Beacon Roofing Supply ...
  url: https://news.mergerlinks.com/daily-review/qxo-completes-the-acquisition-of-beacon-roofing-supply-for-$-11bn
- date: '2026-05-25'
  title: BEACON ROOFING SUPPLY, INC. QUEEN MERGERCO, INC ...
  url: https://d18rn0p25nwr6d.cloudfront.net/CIK-0001124941/30855609-2f78-44b5-a21b-d4113cd5aee5.pdf
- date: '2026-05-25'
  title: 'In case you missed it: From private label roofing products ...'
  url: https://www.facebook.com/RoofingContractor/posts/in-case-you-missed-it-from-private-label-roofing-products-%EF%B8%8F-to-ai-powered-logist/1405757331590241/
- date: '2026-05-25'
  title: How QXO is Using AI to Streamline Distribution
  url: https://www.roofingcontractor.com/articles/101320-how-qxo-is-using-ai-to-streamline-distribution
- date: '2026-05-25'
  title: QXO launches $11 billion tender offer for Beacon Roofing ...
  url: https://www.investing.com/news/company-news/qxo-launches-11-billion-tender-offer-for-beacon-roofing-supply-93CH-3831708
random_paper: 5
rate_limits:
- limit_count: 0
  name: Beacon Roofing Supply Rate Limits
  slug: beacon-roofing-supply-rate-limits
scopes:
- name: Beacon Roofing Supply Scopes
  scope_count: 0
  slug: beacon-roofing-supply-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.1
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 58.9
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 20.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/screenshots/beacon-roofing-supply-2026-06-20T173105.png
security:
- kind: authentication
  name: Beacon Roofing Supply Authentication
  slug: beacon-roofing-supply-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Beacon Roofing Supply Domain Security
  slug: beacon-roofing-supply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beacon-roofing-supply
tags:
- Construction
- Distribution
- Roofing
- Building Materials
- E-Commerce
- Fortune 1000
- Supply Chain
- Order
- Catalog
- Delivery
use_cases:
- description: Integrate Beacon PRO+ with AccuLynx, JobNimbus, or other contractor management platforms to enable in-app material ordering.
  name: Contractor Management Software Integration
- description: Connect enterprise ERP systems with Beacon ordering and inventory for automated procurement workflows.
  name: ERP Integration
- description: Build custom ordering interfaces for roofing contractors that pull live Beacon pricing and inventory.
  name: Custom Ordering Portals
- description: Integrate Beacon delivery tracking into construction project management and scheduling tools.
  name: Delivery Logistics
website: https://www.becn.com/
---
