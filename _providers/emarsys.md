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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Emarsys Agentic Access
  operation_count: 9
  slug: emarsys-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 5
apis:
- description: The Contact Lists API from SAP Emarsys — 1 operation(s) for contact lists.
  name: SAP Emarsys Contact Lists API
  slug: emarsys-contact-lists-api
- description: The Contacts API from SAP Emarsys — 2 operation(s) for contacts.
  name: SAP Emarsys Contacts API
  slug: emarsys-contacts-api
- description: The Email API from SAP Emarsys — 2 operation(s) for email.
  name: SAP Emarsys Email API
  slug: emarsys-email-api
- description: The Events API from SAP Emarsys — 1 operation(s) for events.
  name: SAP Emarsys Events API
  slug: emarsys-events-api
- description: The Segments API from SAP Emarsys — 1 operation(s) for segments.
  name: SAP Emarsys Segments API
  slug: emarsys-segments-api
artifact_total: 12
collections:
- collection_type: open
  name: SAP Emarsys Core API
  slug: open-emarsys
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emarsys-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/emarsys-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emarsys-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emarsys-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/emarsys-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://emarsys.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.emarsys.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.emarsys.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.emarsys.com/docs/core-api-reference
- group: auth
  title: ''
  type: Authentication
  url: https://dev.emarsys.com/docs/core-api-reference/b3c3a1eba8515-authentication-in-v3-api
- group: start
  title: ''
  type: SAP Help Portal
  url: https://help.sap.com/docs/SAP_EMARSYS
- group: other
  title: ''
  type: API Credentials
  url: https://help.sap.com/docs/SAP_EMARSYS/5d44574160f44536b0130abf58cb87cc/fdf4b58974c110149353957a3e7ef453.html
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/emartech/Emarsys-postman-collection
- group: commercial
  title: ''
  type: Pricing
  url: https://emarsys.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://login.emarsys.net/
- group: operate
  title: ''
  type: Support
  url: https://emarsys.com/support/
- group: company
  title: ''
  type: Blog
  url: https://emarsys.com/learn/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emarsys.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emarsys.com/legal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emartech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emarsys
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/emarsys
created: '2026-05-11'
description: SAP Emarsys (formerly Emarsys) is an omnichannel customer engagement and marketing automation platform that helps brands run personalized email, mobile, web, SMS, and ads campaigns powered by a unified customer data layer and AI-driven segmentation. The Emarsys API surface exposes contacts, segments, campaigns, automation programs, event triggers, external events, and analytics so marketing and engineering teams can integrate Emarsys with the rest of the stack. Authentication uses OAuth 2.0 / OIDC with JWT for the v3 API, while legacy endpoints continue to use WSSE (being phased out by end of 2026).
graphqls:
- description: SAP Emarsys is an omnichannel customer engagement platform. The API covers contact management, email campaigns, automation programs, segmentation, personalization, event triggers, and marketing analyt
  name: SAP Emarsys GraphQL API
  slug: emarsys-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emarsys.png
layout: provider
modified: '2026-05-11'
name: SAP Emarsys
nav: Providers
network: true
overview: 'SAP Emarsys publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contact Lists API, Contacts API, Email API, and 2 more. Tagged areas include Marketing Automation, Customer Engagement, Email Marketing, Omnichannel, and Customer Data Platform.


  SAP Emarsys'' developer surface includes authentication, documentation, API reference, pricing, support, engineering blog, and 16 more developer resources.'
random_paper: 12
scopes:
- name: Emarsys Scopes
  scope_count: 156
  slug: emarsys-scopes
  summary_line: 156 scopes · clientCredentials
score:
  band: thin
  composite: 40.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.4
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emarsys/refs/heads/main/screenshots/emarsys-2026-06-20T180628.png
security:
- kind: authentication
  name: Emarsys Authentication
  slug: emarsys-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Emarsys Domain Security
  slug: emarsys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Emarsys Vulnerability Disclosure
  slug: emarsys-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: emarsys
tags:
- Marketing Automation
- Customer Engagement
- Email Marketing
- Omnichannel
- Customer Data Platform
- SAP
website: https://emarsys.com
---
