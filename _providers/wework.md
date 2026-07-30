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
api_count: 2
apis:
- description: 'The WeWork Partner API exposes the company''s global workspace inventory to integrators so that Supply Partners (third-party operators contributing spaces to WeWork) and Demand Partners (resellers and '
  name: WeWork Partner API
  slug: partner-api
- description: WeWork Workplace is the company's SaaS workplace-management platform sold to enterprises and landlords to manage flexible-office space across owned, leased, and partner locations. The product is refer
  name: WeWork Workplace
  slug: workplace
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wework-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.wework.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wework.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.wework.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.wework.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.wework.com/docs/quick-start
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.wework.com/docs/release-notes
- group: auth
  title: ''
  type: Authentication
  url: https://developers.wework.com/how-to-guides/how-to-create-service-tokens
- group: start
  title: ''
  type: Signup
  url: https://developers.wework.com/quick-start/request-access/submit-app-for-review
- group: company
  title: ''
  type: Partners
  url: https://www.wework.com/info/partner-with-us
- group: start
  title: ''
  type: Login
  url: https://members.wework.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.wework.com
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.wework.com
- group: operate
  title: ''
  type: Contact
  url: https://www.wework.com/contact-us
- group: commercial
  title: ''
  type: Privacy
  url: https://www.wework.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wework.com/legal/terms-of-service
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.wework.com/legal/cookie-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.wework.com/legal/accessibility
- group: company
  title: ''
  type: Careers
  url: https://careers.wework.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wework
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wework
created: '2026-05-23'
description: WeWork is a global flexible-workspace provider operating ~600 owned locations plus a Coworking Partner Network of 2,000+ partner spaces across 20+ countries. The company filed for Chapter 11 bankruptcy on November 6, 2023 and emerged on May 30, 2024 as a private company majority-owned by real estate technology vendor Yardi Systems. WeWork exposes a Partner API ("Partner API will help bring WeWork space bookings to your apps and websites") for Supply and Demand partners covering identity, locations, inventory, availability/calendaring, booking, and keycard access, but the full API reference sits behind Auth0 authentication and is not publicly catalogable. No public OpenAPI, AsyncAPI, SDKs, CLIs, status page, RSS feed, or rate-limit documentation could be located.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wework.png
layout: provider
modified: '2026-05-23'
name: WeWork
nav: Providers
network: true
overview: 'WeWork publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Coworking, Flexible Workspace, Real Estate, Workspace Booking, and Workplace Management.


  WeWork''s developer surface includes developer portal, documentation, API reference, getting-started guide, release notes, authentication, signup flow, and 14 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 25.5
  delta: -2.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wework/refs/heads/main/screenshots/wework-2026-06-20T201418.png
security:
- kind: domain-security
  name: Wework Domain Security
  slug: wework-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wework
tags:
- Coworking
- Flexible Workspace
- Real Estate
- Workspace Booking
- Workplace Management
- Bookings
- Inventory
website: https://developers.wework.com
---
