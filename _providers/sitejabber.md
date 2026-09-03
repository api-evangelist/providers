---
access_model:
  confidence: high
  label: Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.smartcustomer.com/business/pricing
  - https://api.sitejabber.com/
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Authentication API from SiteJabber — 1 operation(s) for authentication.
  name: SiteJabber Authentication API
  slug: sitejabber-authentication-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Business Info API from SiteJabber — 2 operation(s) for business info.
  name: SiteJabber Business Info API
  slug: sitejabber-business-info-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Business Questions API from SiteJabber — 1 operation(s) for business questions.
  name: SiteJabber Business Questions API
  slug: sitejabber-business-questions-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Messages API from SiteJabber — 2 operation(s) for messages.
  name: SiteJabber Messages API
  slug: sitejabber-messages-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Partners API from SiteJabber — 2 operation(s) for partners.
  name: SiteJabber Partners API
  slug: sitejabber-partners-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Privacy API from SiteJabber — 2 operation(s) for privacy.
  name: SiteJabber Privacy API
  slug: sitejabber-privacy-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Product Questions API from SiteJabber — 1 operation(s) for product questions.
  name: SiteJabber Product Questions API
  slug: sitejabber-product-questions-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Product Review Requests API from SiteJabber — 2 operation(s) for product review requests.
  name: SiteJabber Product Review Requests API
  slug: sitejabber-product-review-requests-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Product Reviews API from SiteJabber — 5 operation(s) for product reviews.
  name: SiteJabber Product Reviews API
  slug: sitejabber-product-reviews-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Products API from SiteJabber — 4 operation(s) for products.
  name: SiteJabber Products API
  slug: sitejabber-products-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Resolution Attempts API from SiteJabber — 1 operation(s) for resolution attempts.
  name: SiteJabber Resolution Attempts API
  slug: sitejabber-resolution-attempts-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Review Comments API from SiteJabber — 2 operation(s) for review comments.
  name: SiteJabber Review Comments API
  slug: sitejabber-review-comments-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Review Requests API from SiteJabber — 2 operation(s) for review requests.
  name: SiteJabber Review Requests API
  slug: sitejabber-review-requests-api
- baseURL: https://api.smartcustomer.com/v1
  baseurl_source: declared
  description: The Reviews API from SiteJabber — 4 operation(s) for reviews.
  name: SiteJabber Reviews API
  slug: sitejabber-reviews-api
artifact_total: 19
collections:
- collection_type: open
  name: SmartCustomer (Sitejabber) Business API
  slug: open-sitejabber-business-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sitejabber-business-api-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sitejabber-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sitejabber-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartcustomer.com
- group: start
  title: ''
  type: Login
  url: https://www.smartcustomer.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartcustomer.com/business/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartcustomer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartcustomer.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.smartcustomer.com/contact-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sitejabber.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.sitejabber.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartcustomer-reviews
- group: start
  title: ''
  type: SignUp
  url: https://www.smartcustomer.com/registration
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.smartcustomer.com/faq
- group: build
  title: ''
  type: Packages
  url: packages/sitejabber-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sitejabber-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sitejabber-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sitejabber-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sitejabber-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sitejabber-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/sitejabber-components.yml
created: '2026-07-17'
description: 'SiteJabber is a consumer review platform, rebranded as SmartCustomer at smartcustomer.com, where shoppers read and write reviews about online businesses, services and products. Operating for over twenty years, it emphasizes consumer protection through review moderation and verification, and offers a browser extension that surfaces business ratings while users browse. On the business side it is an official Google Review Partner that distributes verified reviews to Google Seller Ratings, Google Business profiles and Google Shopping Ads, and it sells review sourcing, moderation, showcasing widgets, competitive intelligence and e-commerce integrations across four contact-sales packages. It was surfaced as a portfolio company of 500 Global and added to the API Evangelist network. It does publish a developer API: the SmartCustomer Business API, a 31-operation REST surface documented at api.sitejabber.com covering business ratings, consumer reviews and moderation, reviewer messaging,
  review requests by email and SMS, a full product-review and catalog surface, and two CCPA-shaped customer-privacy operations. A prior enrichment pass recorded no API; that was wrong — the reference is served from the pre-rebrand api.sitejabber.com host, which is not linked from the current consumer or business site navigation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sitejabber.png
layout: provider
modified: '2026-08-13'
name: SiteJabber
nav: Providers
network: true
overview: 'SiteJabber publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Business Info API, Business Questions API, and 11 more. Tagged areas include Company, Reviews, Consumer Reviews, Product Reviews, and Reputation Management.


  SiteJabber''s developer surface includes pricing, support, documentation, signup flow, and 18 more developer resources.'
plans:
- name: Sitejabber Plans Pricing
  plan_count: 4
  slug: sitejabber-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Sitejabber Rate Limits
  slug: sitejabber-rate-limits
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 52.9
    developer_ergonomics: 25.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 44.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sitejabber/refs/heads/main/screenshots/sitejabber-2026-08-17T081908.png
security:
- kind: authentication
  name: Sitejabber Authentication
  slug: sitejabber-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sitejabber Domain Security
  slug: sitejabber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sitejabber
tags:
- Company
- Reviews
- Consumer Reviews
- Product Reviews
- Reputation Management
- Reviews Management
- E-Commerce
- Trust and Safety
- Google Seller Ratings
- Customer Feedback
- Ratings
- Privacy
website: https://www.smartcustomer.com
---
