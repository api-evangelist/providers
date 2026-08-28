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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'The SmartCustomer Business API (published under the pre-rebrand Sitejabber name at api.sitejabber.com) is the review-management API behind SmartCustomer''s business product. It covers business profile '
  name: SmartCustomer (Sitejabber) Business API
  slug: smartcustomer-sitejabber-business-api
artifact_total: 7
collections:
- collection_type: open
  name: SmartCustomer (Sitejabber) Business API
  slug: open-sitejabber-business-api
common:
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
mcp_servers:
- description: ''
  name: SiteJabber MCP Server
  slug: sitejabber-mcp-server
modified: '2026-08-13'
name: SiteJabber
nav: Providers
network: true
overview: 'SiteJabber publishes 1 API on the [APIs.io](https://apis.io/) network: SmartCustomer (Sitejabber) Business API. Tagged areas include Company, Reviews, Consumer Reviews, Product Reviews, and Reputation Management.


  SiteJabber''s developer surface includes pricing, support, documentation, signup flow, and 16 more developer resources.'
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
  composite: 47.4
  delta: 2.3
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 53.1
    developer_ergonomics: 25.6
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 45.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
