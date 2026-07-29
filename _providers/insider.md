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
api_count: 1
apis:
- description: Send user profiles, attributes and events into Insider One's Unified Customer Database. POST JSON to the upsert endpoint authenticated with an API key (X-REQUEST-TOKEN) and partner name (X-PARTNER-NAM
  name: Insider Upsert User Data API
  slug: insider-upsert-user-data-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://insiderone.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://academy.insiderone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://academy.insiderone.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://academy.insiderone.com/docs/upsert-user-data-api-integration-wizard-2
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.insiderone.com/docs/user-guides-welcome
- group: operate
  title: ''
  type: Support
  url: https://useinsiderhelp.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://insiderone.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useinsider
- group: commercial
  title: ''
  type: Pricing
  url: https://insiderone.com/request-a-demo/
- group: start
  title: ''
  type: SignUp
  url: https://inone.useinsider.com/login
- group: start
  title: ''
  type: Login
  url: https://inone.useinsider.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insiderone.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insiderone.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insider-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/insider-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/insider-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insider-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/insider-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insider-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insider-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/insider-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/insider-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insider-domain-security.yml
created: '2026-07-17'
description: Insider (rebranded Insider One, useinsider.com now redirects to insiderone.com) is an AI-native customer engagement and personalization platform used by 2,000+ global brands. It unifies a Customer Data Platform (CDP), cross-channel journey orchestration (Architect), personalization, predictive segmentation, and behavioral analytics, delivering across Web, Email, SMS/RCS, WhatsApp, Web Push, Mobile App, Site Search, InStory and conversational CX. For developers it exposes a Unified Customer Database via the Upsert User Data API (POST unification.useinsider.com/api/user/v1/upsert, authenticated with X-REQUEST-TOKEN and X-PARTNER-NAME headers), a Product Catalog API, Web and Mobile (iOS, Android, React Native, Flutter, Cordova) SDKs, and an outbound "Call an API" journey channel. Recognized by Gartner and Forrester as a leader in personalization engines, CDP and omnichannel marketing platforms.
image: https://logo.clearbit.com/useinsider.com
layout: provider
modified: '2026-07-19'
name: Insider
nav: Providers
network: true
overview: 'Insider publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Engagement, Personalization, Customer Data Platform, and Marketing.


  Insider''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 34.7
  delta: 0.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 33.8
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insider/refs/heads/main/screenshots/insider-2026-07-25T222527.png
security:
- kind: authentication
  name: Insider Authentication
  slug: insider-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Insider Domain Security
  slug: insider-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Insider Trust Center
  slug: insider-trust-center
  summary_line: SOC 2, ISO 27001:2013, ISO 27701, CSA STAR
slug: insider
tags:
- Company
- Customer Engagement
- Personalization
- Customer Data Platform
- Marketing
- Journey Orchestration
- Omnichannel
- CDP
- Artificial Intelligence
website: https://insiderone.com
---
