---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-09-16'
api_count: 12
apis:
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Event management API from CrossEngage — 1 operation(s) for event management.
  name: CrossEngage Event management API
  slug: crossenagage-event-management-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Lead management API from CrossEngage — 1 operation(s) for lead management.
  name: CrossEngage Lead management API
  slug: crossenagage-lead-management-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Opt-out management API from CrossEngage — 3 operation(s) for opt-out management.
  name: CrossEngage Opt-out management API
  slug: crossenagage-opt-out-management-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The product-feed API from CrossEngage — 2 operation(s) for product-feed.
  name: CrossEngage Product Feed API
  slug: crossenagage-product-feed-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The User Attribute Management API from CrossEngage — 2 operation(s) for user attribute management.
  name: CrossEngage User Attribute Management API
  slug: crossenagage-user-attribute-management-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The User profile management API from CrossEngage — 5 operation(s) for user profile management.
  name: CrossEngage User profile management API
  slug: crossenagage-user-profile-management-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Destination API from CrossEngage — 2 operation(s) for destination.
  name: CrossEngage Destination API
  slug: crossenagage-destination-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Detailed API from CrossEngage — 1 operation(s) for detailed.
  name: CrossEngage Detailed API
  slug: crossenagage-detailed-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Event Class API from CrossEngage — 1 operation(s) for event class.
  name: CrossEngage Event Class API
  slug: crossenagage-event-class-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Export API from CrossEngage — 2 operation(s) for export.
  name: CrossEngage Export API
  slug: crossenagage-export-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Files API from CrossEngage — 1 operation(s) for files.
  name: CrossEngage Files API
  slug: crossenagage-files-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Kpi API from CrossEngage — 2 operation(s) for kpi.
  name: CrossEngage Kpi API
  slug: crossenagage-kpi-api
- baseURL: https://api.crossengage.io
  baseurl_source: declared
  description: The Overall API from CrossEngage — 1 operation(s) for overall.
  name: CrossEngage Overall API
  slug: crossenagage-overall-api
artifact_total: 26
asyncapis:
- description: ''
  name: Crossenagage Webhooks
  slug: crossenagage-webhooks
collections:
- collection_type: open
  name: File Attachment API
  slug: open-crossenagage-file-attachments-v1
- collection_type: open
  name: Product Feed API
  slug: open-crossenagage-product-feed
- collection_type: open
  name: Raw Export API
  slug: open-crossenagage-raw-export-v1
- collection_type: open
  name: Statistics API
  slug: open-crossenagage-statistics-v1
- collection_type: open
  name: User Management API v1
  slug: open-crossenagage-user-management-v1
- collection_type: open
  name: User Management API v2
  slug: open-crossenagage-user-management-v2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/overlays/crossenagage-user-management-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crossenagage-user-management-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/overlays/crossenagage-user-management-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crossenagage-user-management-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/overlays/crossenagage-product-feed-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crossenagage-product-feed-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/overlays/crossenagage-raw-export-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crossenagage-raw-export-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/overlays/crossenagage-statistics-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crossenagage-statistics-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/overlays/crossenagage-file-attachments-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crossenagage-file-attachments-v1-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/authentication/crossenagage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crossenagage-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/security/crossenagage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossenagage-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.documentation.crossengage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.crossengage.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.documentation.crossengage.io/
- group: start
  title: ''
  type: Login
  url: https://app.crossengage.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://spotler.com/en-de/pricing
- group: company
  title: ''
  type: Blog
  url: https://spotler.com/en-de/resources
- group: operate
  title: ''
  type: Support
  url: https://documentation.crossengage.io/data-and-engagement-platform/help-and-support/reach-out-to-customer-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://spotler.com/en-de/help-centers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.spotler.com/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crossengage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.spotler.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.spotler.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/security/crossenagage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossenagage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.spotler.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/conformance/crossenagage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crossenagage-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/lifecycle/crossenagage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/crossenagage-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/conventions/crossenagage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crossenagage-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/llms/crossenagage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crossenagage-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/packages/crossenagage-packages.yml
  title: ''
  type: Packages
  url: packages/crossenagage-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/packages/crossenagage-packages.yml
  title: ''
  type: SDKs
  url: packages/crossenagage-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/mcp/crossenagage-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/crossenagage-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/errors/crossenagage-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/crossenagage-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/asyncapi/crossenagage-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/crossenagage-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/data-model/crossenagage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crossenagage-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/components/crossenagage-components.yml
  title: ''
  type: Components
  url: components/crossenagage-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/plans/crossenagage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crossenagage-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/rate-limits/crossenagage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crossenagage-rate-limits.yml
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/7f6c14ba49835c19dbd7
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrossEngage
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.crossengage.io/documentation-guide
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.spotler.com/general-terms-and-conditions-de
created: '2026-07-17'
description: CrossEngage is a Berlin-based customer data and cross-channel marketing platform (a Customer Data Platform / CDP) founded in 2015 and backed by Earlybird Venture Capital. It unifies first-party customer data into 360-degree profiles, builds no-code predictive AI/ML models for customer lifetime value and behavior, manages audiences with drag-and-drop segmentation, and orchestrates real-time cross-channel customer journeys across email, push, SMS, WhatsApp and webhooks. Following its acquisition by Spotler, the product is sold as Spotler Activate Pro. CrossEngage exposes six REST APIs on api.crossengage.io — User Management v1 and v2, Product Feed, Raw Export, Statistics and File Attachments — totalling 37 operations. Five are published as API Blueprint documents and one (Product Feed) as Swagger 2.0, all served from Apiary and embedded in the reference site at api.documentation.crossengage.io. Authentication is a static X-XNG-AuthToken header paired with a required X-XNG-ApiVersion
  header; there is no OAuth surface. Product documentation is published at documentation.crossengage.io, which serves a first-party llms.txt index of all 219 pages.
image: https://api.documentation.crossengage.io/wp-content/uploads/cropped-favicon-96x96-1-192x192.png
layout: provider
modified: '2026-08-13'
name: CrossEngage
nav: Providers
network: true
overview: 'CrossEngage publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Event management API, Lead management API, Opt-out management API, and 10 more. Tagged areas include Company, Customer Data Platform, Marketing, Customer Engagement, and Marketing Automation.


  The CrossEngage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CrossEngage''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, getting-started guide, and 33 more developer resources.'
plans:
- name: Crossenagage Plans Pricing
  plan_count: 0
  slug: crossenagage-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Crossenagage Rate Limits
  slug: crossenagage-rate-limits
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.1
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 52.8
    developer_ergonomics: 70.8
    discoverability: 81.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 47.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/screenshots/crossenagage-2026-07-25T210755.png
security:
- kind: authentication
  name: Crossenagage Authentication
  slug: crossenagage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crossenagage Domain Security
  slug: crossenagage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crossenagage Vulnerability Disclosure
  slug: crossenagage-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Crossenagage Trust Center
  slug: crossenagage-trust-center
  summary_line: ISO/IEC 27001:2022, CSA STAR Certification, GDPR
slug: crossenagage
tags:
- Company
- Customer Data Platform
- Marketing
- Customer Engagement
- Marketing Automation
- Cross-Channel
- Personalization
- Predictive Analytics
- Segmentation
- Campaign Management
- Product Feeds
- Data Export
- Webhook
- Web Tracking
- Germany
website: https://api.documentation.crossengage.io/
---
