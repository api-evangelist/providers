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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/navan-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navan-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://navan.com
- group: other
  title: ''
  type: Product
  url: https://navan.com/products/business-travel
- group: other
  title: ''
  type: Product
  url: https://navan.com/products/expense
- group: other
  title: ''
  type: Product
  url: https://navan.com/products/payments
- group: other
  title: ''
  type: Product
  url: https://navan.com/products/navan-edge
- group: docs
  title: ''
  type: Documentation
  url: https://app.navan.com/app/helpcenter/articles/travel/admin/other-integrations/navan-tmc-api-integration-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://app.navan.com/app/helpcenter/articles/travel/admin/other-integrations/booking-data-integration
- group: auth
  title: ''
  type: Authentication
  url: https://api.navan.com/auth/v1/token
- group: other
  title: ''
  type: BaseURL
  url: https://api.navan.com
- group: auth
  title: ''
  type: Security
  url: https://navan.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.navan.com
- group: operate
  title: ''
  type: Status
  url: https://status.navan.com
- group: company
  title: ''
  type: Blog
  url: https://navan.com/blog
- group: company
  title: ''
  type: EngineeringBlog
  url: https://navan.com/blog/navan-tech-blog
- group: company
  title: ''
  type: Careers
  url: https://navan.com/careers
- group: other
  title: ''
  type: RandD
  url: https://navan.com/research-and-development-team
- group: commercial
  title: ''
  type: Pricing
  url: https://navan.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://navan.com/contact
- group: company
  title: ''
  type: Press
  url: https://navan.com/press
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://navan.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://navan.com/legal/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navan
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Navan
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@navan
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/navan
created: '2026-05-25'
description: Navan (formerly TripActions until its February 2023 rebrand) is a Palo Alto, California corporate travel and expense management platform that combines business travel booking, expense management, and corporate cards into a single product. Navan operates a global travel inventory with 24/7 agent support, a swipe-to-reconciliation expense flow with AI-assisted categorization and policy enforcement, and Navan Connect, a card-link network compatible with Visa, Mastercard, and American Express. Newer offerings include Navan Edge, a frequent-traveler assistant, and a Rewards program that incentivizes policy-compliant bookings. The company serves more than 10,000 organizations including Canva, DoorDash, and Duolingo. Navan exposes a partner-grade integration surface — a Booking Data API, an Expense API, a User Management REST API, a SCIM 2.0 provisioning endpoint, and an OAuth 2.0 client-credentials token endpoint — all under api.navan.com. Credentials and reference documentation are
  provisioned through the Admin portal (Settings → Integrations → API and Admin → SCIM settings) rather than a public developer portal, so the API contracts are not currently published as a downloadable OpenAPI specification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navan-com.png
layout: provider
modified: '2026-05-25'
name: Navan
nav: Providers
network: true
overview: 'Navan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Corporate Travel, Travel Management, Expense Management, Corporate Cards, and Payments.


  Navan''s developer surface includes documentation, authentication, status page, engineering blog, pricing, YouTube channel, and 21 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 21.7
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/navan-com/refs/heads/main/screenshots/navan-com-2026-06-20T190100.png
security:
- kind: domain-security
  name: Navan Com Domain Security
  slug: navan-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Navan Com Trust Center
  slug: navan-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR, CSA STAR
slug: navan-com
tags:
- Corporate Travel
- Travel Management
- Expense Management
- Corporate Cards
- Payments
- Spend Management
- Booking
- SCIM
- User Management
- FinTech
- SaaS
- TripActions
website: https://navan.com
---
