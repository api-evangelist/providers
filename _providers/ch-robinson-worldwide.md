---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Ch Robinson Worldwide Agentic Access
  operation_count: 35
  slug: ch-robinson-worldwide-agentic-access
  summary_line: 35 operations · 24 acting
api_count: 2
apis:
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: C.H. Robinson uses OAuth v2.0 to secure connections to its APIs. oAuth v2 works by delegating user authentication to the service that hosts the user account and authorizing third-party applications to
  name: C.H. Robinson Authentication API
  slug: ch-robinson-worldwide-authentication-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: C.H. Robinson's Documents product allows our partners to generate, post, and retrieve documents. C.H. Robinson currently offers customers the ability to generate blank BOLs and retrieve signed BOLs, P
  name: C.H. Robinson Documents API
  slug: ch-robinson-worldwide-documents-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: C.H. Robinson's Events product gives complete, near real-time order and shipment information, including all transportation updates. Integrating with C.H. Robinson's Events API give partners near visib
  name: C.H. Robinson Events API
  slug: ch-robinson-worldwide-events-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: C.H. Robinson's financial product provides customers and carriers insight into their invoicing. Currently, customers can retrieve their invoice information from the Financials product. C.H. Robinson g
  name: C.H. Robinson Financials API
  slug: ch-robinson-worldwide-financials-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: 'A service for generating small parcel shipping labels. An associated C.H. Robinson order is also created to track the package updates through Navisphere®. Note: Configuration of your company’s parcel '
  name: C.H. Robinson Labels API
  slug: ch-robinson-worldwide-labels-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: C.H. Robinson’s Orders and Bookings products are the starting point for all freight execution in Navisphere®. They provide a unified gateway for customers to submit and manage shipment and booking det
  name: C.H. Robinson Orders and Booking API
  slug: ch-robinson-worldwide-orders-and-booking-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: C.H. Robinson's rating product allows our customers to retrieve contractual or transactional quotes. Customers can generate quotes with nothing more than weights and zip codes! However, the more detai
  name: C.H. Robinson Rating API
  slug: ch-robinson-worldwide-rating-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: C.H. Robinson's Shipments product allows our partner base to access C.H. Robinson's available shipments, send offers on those shipments, and book those shipments. Additionally, our partners can update
  name: C.H. Robinson Shipments API
  slug: ch-robinson-worldwide-shipments-api
- baseURL: https://api.navisphere.com
  baseurl_source: declared
  description: Navisphere® Vision and Visibility tool is a global visibility technology that allows select customers to view and proactively manage their supply chain movements from a single platform. The tool combi
  name: C.H. Robinson Visibility API
  slug: ch-robinson-worldwide-visibility-api
artifact_total: 61
asyncapis:
- description: ''
  name: Ch Robinson Worldwide Webhooks
  slug: ch-robinson-worldwide-webhooks
collections:
- collection_type: postman
  name: Customer API Onboarding Collection - Public
  slug: postman-ch-robinson-worldwide-customer-api-onboarding
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/agentic-access/ch-robinson-worldwide-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ch-robinson-worldwide-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/authentication/ch-robinson-worldwide-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ch-robinson-worldwide-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/security/ch-robinson-worldwide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ch-robinson-worldwide-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ch-robinson
- group: company
  title: ''
  type: Website
  url: https://www.chrobinson.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.chrobinson.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chrobinson.com/en-us/shippers/lean-ai-supply-chains/connectivity-integrations/
- group: other
  title: ''
  type: Technology
  url: https://www.chrobinson.com/en-us/technology/
- group: other
  title: ''
  type: Navisphere
  url: https://www.chrobinson.com/en-us/technology/shipper-technology/navisphere/
- group: start
  title: ''
  type: CarrierPortal
  url: https://www.chrobinson.com/en-us/carriers/api-connectivity/
- group: company
  title: ''
  type: About
  url: https://www.chrobinson.com/en-us/about-us/
- group: company
  title: ''
  type: Careers
  url: https://jobs.chrobinson.com/
- group: company
  title: ''
  type: News
  url: https://www.chrobinson.com/en-us/about-us/newsroom/
- group: company
  title: ''
  type: Investors
  url: https://investor.chrobinson.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chrobinson.com/en-us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chrobinson.com/en-us/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/c-h-robinson/
- group: other
  title: ''
  type: X
  url: https://x.com/CHRobinsonInc
- group: other
  title: ''
  type: Services
  url: ''
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/llms/ch-robinson-worldwide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ch-robinson-worldwide-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/openapi/_original/ch-robinson-worldwide-rest-apis-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/ch-robinson-worldwide-rest-apis-openapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.chrobinson.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.chrobinson.com/carrier
- group: operate
  title: ''
  type: Support
  url: https://developer.chrobinson.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.chrobinson.com/en-us/resources/blog/
- group: build
  title: ''
  type: Postman
  url: https://api.navisphere.com/api/B2B/Portal/v1/documents/customerApiOnboardingCollectionPublic.json
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.chrobinson.com/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/lifecycle/ch-robinson-worldwide-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ch-robinson-worldwide-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/conventions/ch-robinson-worldwide-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ch-robinson-worldwide-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/errors/ch-robinson-worldwide-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ch-robinson-worldwide-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/conformance/ch-robinson-worldwide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ch-robinson-worldwide-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/data-model/ch-robinson-worldwide-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ch-robinson-worldwide-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/packages/ch-robinson-worldwide-packages.yml
  title: ''
  type: Packages
  url: packages/ch-robinson-worldwide-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/sandbox/ch-robinson-worldwide-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ch-robinson-worldwide-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/asyncapi/ch-robinson-worldwide-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ch-robinson-worldwide-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/mcp/ch-robinson-worldwide-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ch-robinson-worldwide-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/overlays/ch-robinson-worldwide-rest-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ch-robinson-worldwide-rest-apis-overlay.yaml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/rate-limits/ch-robinson-worldwide-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ch-robinson-worldwide-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/plans/ch-robinson-worldwide-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ch-robinson-worldwide-plans-pricing.yml
created: '2025-01-01'
description: C.H. Robinson is one of the world's largest third-party logistics (3PL) providers, offering global freight transportation, supply chain management, customs brokerage, and sourcing of fresh produce. Its Navisphere transportation management system provides end-to-end supply chain planning, purchase order management, execution, freight payment, and business intelligence. C.H. Robinson exposes APIs that allow shippers and carriers to integrate quoting, booking, tracking, documents, and payment workflows directly into their own TMS or ERP platforms.
features:
- name: Rate Quoting
- name: Load Booking
- name: Load Tendering
- name: Shipment Tracking
- name: Real-Time Visibility
- name: Document Exchange
- name: Payment Status
- name: Freight Audit
- name: Freight Payment
- name: Business Intelligence
- name: EDI
- name: XML
- name: API Connectivity
- name: Carrier Onboarding
- name: Load Matching
- name: Capacity Search
- name: Automated Booking
- name: Tracking Webhooks
- name: Proof of Delivery
- name: Invoice Upload
finops:
- name: Ch Robinson Worldwide Finops
  service_category: Logistics / Freight
  slug: ch-robinson-worldwide-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ch-robinson-worldwide.png
integrations:
- name: Navisphere
- name: Axele
- name: Beyond Trucks
- name: SmartHop
- name: Geotab
- name: SOS Trucking
- name: SAP
- name: Oracle
- name: NetSuite
- name: Microsoft Dynamics
- name: Manhattan Associates
- name: Blue Yonder
- name: MercuryGate
- name: Kuebix
layout: provider
modified: '2026-09-16'
name: C.H. Robinson
nav: Providers
network: true
overview: 'C.H. Robinson publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Events API, and 6 more. Tagged areas include Freight, Logistics, Shipping, Supply Chain, and Transportation.


  The C.H. Robinson catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  C.H. Robinson''s developer surface includes authentication, documentation, product news, API reference, getting-started guide, support, engineering blog, and 32 more developer resources.'
plans:
- name: Ch Robinson Worldwide Plans Pricing
  plan_count: 2
  slug: ch-robinson-worldwide-plans-pricing
press:
- date: '2026-05-25'
  title: More than 100 trillion data points fuel ...
  url: https://www.chrobinson.com/en-us/about-us/newsroom/press-releases/2026/100-trillion-data-points-fuel-chrobinson-agentic-supply-chains/
- date: '2026-05-25'
  title: C.H. Robinson Worldwide, Inc. - Search Results
  url: https://investor.chrobinson.com/Search-Results/default.aspx?SearchTerm=&PageNumber=4
- date: '2026-05-25'
  title: Artificial Intelligence
  url: https://www.chrobinson.com/en-us/about-us/newsroom/tags/artificial-intelligence/
- date: '2026-05-25'
  title: C.H. Robinson Launches AI Agents to Combat ...
  url: https://investor.chrobinson.com/News-and-Events/Press-Releases/press-release-details/2026/C-H--Robinson-Launches-AI-Agents-to-Combat-Industrywide-Problem-of-Missed-LTL-Pickups/default.aspx
- date: '2026-05-25'
  title: In-House Tech and AI Agents Expand Impact
  url: https://www.chrobinson.com/en-us/about-us/newsroom/news/2026/lean-ai-growing-shipper-impact/
random_paper: 10
rate_limits:
- limit_count: 2
  name: Ch Robinson Worldwide Rate Limits
  slug: ch-robinson-worldwide-rate-limits
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 63.9
    developer_ergonomics: 37.5
    discoverability: 75.9
    operational_transparency: 31.6
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/screenshots/ch-robinson-worldwide-2026-06-20T174153.png
security:
- kind: authentication
  name: Ch Robinson Worldwide Authentication
  slug: ch-robinson-worldwide-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Ch Robinson Worldwide Domain Security
  slug: ch-robinson-worldwide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ch-robinson-worldwide
tags:
- Freight
- Logistics
- Shipping
- Supply Chain
- Transportation
- Transportation Management
- Fortune 500
use_cases:
- name: TMS Integration
- name: Carrier Load Booking
- name: Shipper Rate Shopping
- name: Multi-Modal Transportation
- name: Customs Brokerage
- name: Global Forwarding
- name: Produce Sourcing
- name: Managed Transportation
- name: Supply Chain Consulting
- name: Fresh Produce Logistics
website: https://www.chrobinson.com
---
