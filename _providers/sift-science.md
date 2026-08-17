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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Sift's REST API for Digital Trust & Safety — send behavioral and transaction Events, request risk Scores, apply Decisions and Labels, run Workflows, and verify users. Data is sent as JSON over HTTPS a
  name: Sift API
  slug: sift-api
artifact_total: 5
asyncapis:
- description: ''
  name: Sift Science Webhooks
  slug: sift-science-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sift-science-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sift.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.sift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sift.com/docs/curl/apis-overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.sift.com/docs/curl/apis-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://sift.com/developer-overview/
- group: operate
  title: ''
  type: Support
  url: https://sift.com/community
- group: company
  title: ''
  type: Blog
  url: https://sift.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SiftScience
- group: start
  title: ''
  type: SignUp
  url: https://console.sift.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sift.com/legal-and-compliance/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sift.com/legal-and-compliance/service-privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sift.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sift-science-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/sift-science-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sift-science-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sift-science-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sift-science-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sift-science-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sift-science-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sift.com/legal-and-compliance/trust-and-safety-security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://sift.com/legal-and-compliance/trust-and-safety-security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sift-science-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sift-science-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/sift-science-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sift-science-webhooks.yml
created: '2026-07-17'
description: Sift (formerly Sift Science) is a Digital Trust & Safety platform that uses machine learning to help online businesses stop payment fraud, account takeover, fake-account creation, and content abuse in real time. Developers integrate Sift through modern REST APIs (Events, Score, Labels, Decisions, Workflows, and Verification), a client-side JavaScript snippet, and mobile SDKs for iOS and Android. The platform scores users and transactions against a global network of over one trillion annual events, returns risk scores synchronously or asynchronously, and lets teams automate business actions via Decisions and Workflows. Sift is used by 700+ global brands including Hertz, Yelp, and Poshmark.
image: https://sift.com/wp-content/uploads/2026/07/Digital-Fraud-Prevention-Risk-Based-Authentication-Sift.png
layout: provider
modified: '2026-07-21'
name: Sift Science
nav: Providers
network: true
overview: 'Sift Science publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Fraud Detection, Fraud Prevention, and Machine Learning.


  The Sift Science catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sift Science''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 19 more developer resources.'
random_paper: 21
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 50.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Sift Science Authentication
  slug: sift-science-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sift Science Domain Security
  slug: sift-science-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sift Science Trust Center
  slug: sift-science-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: sift-science
tags:
- Company
- Enterprise Saas
- Fraud Detection
- Fraud Prevention
- Machine Learning
- Risk Scoring
- Payments
- Identity
- Security
- Digital Trust And Safety
website: https://sift.com
---
