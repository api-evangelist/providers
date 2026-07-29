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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Mycase Agentic Access
  operation_count: 8
  slug: mycase-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 8
apis:
- description: MyCase Webhooks deliver event notifications when records change in the MyCase platform (for example case, event, task, and document lifecycle events). Webhook subscriptions are documented alongside th
  name: MyCase Webhooks
  slug: webhooks
- description: Configured case stages for the firm.
  name: MyCase Case Stages API
  slug: mycase-case-stages-api
- description: Cases (matters) for the firm, and case-scoped sub-resources.
  name: MyCase Cases API
  slug: mycase-cases-api
- description: Companies visible to the authorized user.
  name: MyCase Companies API
  slug: mycase-companies-api
- description: People and client relationships associated with cases.
  name: MyCase Contacts API
  slug: mycase-contacts-api
- description: Documents and document folders associated with a case.
  name: MyCase Documents API
  slug: mycase-documents-api
- description: Calendar events on the firm calendar.
  name: MyCase Events API
  slug: mycase-events-api
- description: The authorized firm of the current API user.
  name: MyCase Firm API
  slug: mycase-firm-api
artifact_total: 15
collections:
- collection_type: open
  name: MyCase Open API
  slug: open-mycase-open-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mycase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mycase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mycase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mycase.com/
- group: other
  title: ''
  type: Parent Company
  url: https://www.8am.com/
- group: other
  title: ''
  type: AffiniPay
  url: https://www.affinipay.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mycase.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.mycase.com/lp/free-trial/
- group: start
  title: ''
  type: Login
  url: https://auth.mycase.com/login
- group: start
  title: ''
  type: Portal
  url: https://mycaseapi.stoplight.io/
- group: docs
  title: ''
  type: Documentation
  url: https://mycaseapi.stoplight.io/docs/mycase-api-documentation/k5xpc4jyhkom7-getting-started
- group: docs
  title: ''
  type: Reference
  url: https://mycaseapi.stoplight.io/
- group: operate
  title: ''
  type: Support
  url: https://supportcenter.mycase.com/
- group: operate
  title: ''
  type: Support Article
  url: https://supportcenter.mycase.com/en/articles/9370198-open-api
- group: other
  title: ''
  type: Certified Consultants
  url: https://www.mycase.com/consultants/
- group: company
  title: ''
  type: Blog
  url: https://www.mycase.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.mycase.com/news/
- group: learn
  title: ''
  type: Webinars
  url: https://www.mycase.com/webinars/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.mycase.com/case-studies/
- group: other
  title: ''
  type: Customers
  url: https://www.mycase.com/customers/
- group: other
  title: ''
  type: Mobile
  url: https://www.mycase.com/features/mobile-app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mycase.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mycase.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://www.mycase.com/security/
- group: company
  title: ''
  type: Careers
  url: https://www.8am.com/careers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mycase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mycase-inc-
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/mycaseinc
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/mycaseinc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/MyCaseInc
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mycase-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/mycase-rules.yml
created: '2026-05-25'
description: MyCase is a cloud-based legal practice and case management platform used by more than 18,000 law firms for matter management, contacts and companies, calendaring, events, tasks, documents, time tracking, billing and invoicing, payments via LawPay, lead intake, eSignature, and client communications through a secure portal. MyCase was acquired by AffiniPay (now 8am, LLC — which also owns LawPay, CasePeer, and Docketwise) in 2022. In late 2023 MyCase released a public Open API available exclusively on its Advanced tier, with documentation hosted at mycaseapi.stoplight.io. The Open API exposes the firm, cases, contacts, companies, case stages, events, tasks, documents, client relationships, and webhook subscriptions, and is positioned as the integration surface for third-party software vendors building on MyCase.
graphqls:
- description: MyCase is a cloud-based legal practice management platform. The API covers cases/matters, contacts, time entries, invoices, payments, documents, calendar events, tasks, and communication threads for l
  name: MyCase GraphQL API
  slug: mycase-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mycase.png
jsonld:
- class_count: 0
  name: Mycase Context
  property_count: 8
  slug: mycase-context
layout: provider
modified: '2026-05-25'
name: MyCase
nav: Providers
network: true
overview: 'MyCase publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Case Stages API, Cases API, Companies API, and 4 more. Tagged areas include Billing, Calendaring, Case Management, Client Portal, and Document Management.


  The MyCase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MyCase''s developer surface includes authentication, pricing, signup flow, developer portal, documentation, support, engineering blog, and 25 more developer resources.'
random_paper: 26
rules:
- name: MyCase API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: mycase-rules
score:
  band: developing
  composite: 46.1
  delta: -4.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.4
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 15.8
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mycase/refs/heads/main/screenshots/mycase-2026-06-20T185916.png
security:
- kind: authentication
  name: Mycase Authentication
  slug: mycase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mycase Domain Security
  slug: mycase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mycase
tags:
- Billing
- Calendaring
- Case Management
- Client Portal
- Document Management
- Invoicing
- Law Firms
- Legal
- Legal Practice Management
- LegalTech
- Matter Management
- OAuth 2.0
- Payments
- Practice Management
- Time Tracking
- Webhooks
website: https://www.mycase.com/
---
