---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: Qwil's private, authenticated production REST API (Django REST Framework). Requires a bearer token; no public OpenAPI specification is published.
  name: Qwil API
  slug: qwil-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://qwil.co
- group: start
  title: ''
  type: Login
  url: https://app.qwil.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/qwil-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwil-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qwil-llms.txt
created: '2026-07-17'
description: Qwil (qwil.co) is a financial-technology company and a 500 Global portfolio company. It operates a consumer-facing web and mobile application ("Qwil WebApp" at app.qwil.com) backed by a private, authenticated REST API at api.qwil.co. The platform connects to users' bank accounts through Plaid and uses Firebase Authentication (Google Identity Platform) for identity, with bearer tokens presented to a Django REST Framework API. Qwil does not publish a public API specification, developer portal, or SDK documentation; the API is private and partner-gated. Note that qwil.co is distinct from Qwil Messenger (qwil.io), an unrelated secure client-collaboration platform. This profile was enriched by live probing of Qwil's public network surface; most standard developer artifacts are unavailable because Qwil exposes no public developer program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qwil.png
layout: provider
modified: '2026-07-20'
name: Qwil
nav: Providers
network: true
overview: 'Qwil publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial-Services, Payments, and Banking.


  Qwil''s developer surface includes authentication and 4 more developer resources.'
random_paper: 4
security:
- kind: authentication
  name: Qwil Authentication
  slug: qwil-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qwil Domain Security
  slug: qwil-domain-security
  summary_line: DMARC
slug: qwil
tags:
- Company
- Fintech
- Financial-Services
- Payments
- Banking
- Plaid
website: https://qwil.co
---
