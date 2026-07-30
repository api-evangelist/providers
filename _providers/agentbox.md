---
access_model:
  confidence: high
  label: Paid - integrator application required
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.agentbox.com.au/integrator-application
  - https://api.agentboxcrm.com.au/
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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The production Agentbox (Reapit Sales) REST API used by approved integration partners to read and write agency CRM data - contacts, listings, properties, staff and offices. The host is live and fronte
  name: Agentbox API
  slug: agentbox-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentbox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentbox-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agentbox-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agentbox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentbox-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentbox-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/agentbox-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agentbox-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.agentbox.com.au/future-releases
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentbox-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.agentbox.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.agentbox.com.au/blog
- group: operate
  title: ''
  type: SupportPage
  url: https://help.agentboxcrm.com.au/home
- group: docs
  title: ''
  type: Documentation
  url: https://help.agentboxcrm.com.au/reapit-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://help.agentboxcrm.com.au/portals
- group: start
  title: ''
  type: Onboarding
  url: https://www.agentbox.com.au/integrator-application
- group: commercial
  title: ''
  type: Plans
  url: https://www.agentbox.com.au/plans-inclusions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentbox.com.au/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentbox.com.au/privacy
- group: company
  title: ''
  type: About
  url: https://www.agentbox.com.au/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.agentbox.com.au/contact-us
- group: operate
  title: ''
  type: Support
  url: https://www.agentbox.com.au/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.agentboxcrm.com.au/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentbox.com.au/plans-inclusions
- group: start
  title: ''
  type: Login
  url: https://login.agentboxcrm.com.au/
- group: learn
  title: ''
  type: Training
  url: https://www.agentbox.com.au/training
- group: other
  title: ''
  type: Resources
  url: https://www.agentbox.com.au/resources
- group: other
  title: ''
  type: CaseStudies
  url: https://www.agentbox.com.au/case-studies
- group: company
  title: ''
  type: Careers
  url: https://www.agentbox.com.au/careers
- group: company
  title: ''
  type: Newsletter
  url: https://www.agentbox.com.au/subscribe
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/agentboxau
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agentbox/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/agentboxcrm
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/agentboxau
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AgentboxSoftware/featured
- group: other
  title: ''
  type: ParentCompany
  url: https://www.reapit.com.au/
created: '2026-07-26'
description: Agentbox - rebranded Reapit Sales after its acquisition by the UK-headquartered proptech group Reapit - is an Australian real estate CRM and sales platform used by residential sales agencies across Australia and New Zealand, covering contacts and prospecting, listing management, appraisals, vendor management, marketing, agency websites, and a mobile agent app. Its position in the value chain is the agency system of record and, critically, the portal uploader - Agentbox is the system that pushes an agency's for-sale and for-rent listings out to realestate.com.au, domain.com.au, allhomes, commercialrealestate.com.au and dozens of other Australian portals, which in the Australian market is the REAXML feed seam rather than an MLS. Its API posture is honest but closed - a production API gateway is live at api.agentboxcrm.com.au (Tyk, HTTP 401 "Authorization field missing" to anonymous callers, authenticated with an X-API-Key header alongside a Client ID and Office ID), but there
  is no public developer portal, no published reference, and no downloadable machine-readable contract. Access is application-approval only - every third party must complete the Reapit Sales Integrator Application and be reviewed before an agency's API Key, Client ID and Office ID are issued by support. There is no RESO Web API or Data Dictionary certification, no OData $metadata document, and no Universal Property Identifier - RESO is a North American MLS regime with no presence in this Australian vendor's surface - and no open data is published.
image: https://agentboxcdn.com.au/assets/img/agentbox/favicon-192x192.png
layout: provider
modified: '2026-07-26'
name: Agentbox
nav: Providers
network: true
overview: 'Agentbox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Australia, Property Listings, PropTech, and CRM.


  Agentbox''s developer surface includes authentication, changelog, engineering blog, documentation, support, pricing, training material, and 30 more developer resources.'
random_paper: 36
rate_limits:
- limit_count: 0
  name: Agentbox Rate Limits
  slug: agentbox-rate-limits
score:
  band: emerging
  composite: 25.3
  delta: -0.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 25.5
  provenance:
    conformance: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentbox/refs/heads/main/screenshots/agentbox-2026-07-27T125332.png
security:
- kind: authentication
  name: Agentbox Authentication
  slug: agentbox-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Agentbox Domain Security
  slug: agentbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentbox
tags:
- Real Estate
- Australia
- Property Listings
- PropTech
- CRM
- REAXML
- Portal Feeds
- Rentals
- Commercial Real Estate
- New Zealand
website: https://www.agentbox.com.au/
---
