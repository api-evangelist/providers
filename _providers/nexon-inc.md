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
- description: Programmatic access to per-game data (character, ranking, match, and metadata) for Nexon titles. Authenticated with a per-application API key sent in the x-nxopen-api-key HTTP header. Versioned resour
  name: NEXON Open API
  slug: nexon-open-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.nexon.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi.nexon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://openapi.nexon.com/guide/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.nexon.com/guide/request-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://openapi.nexon.com/guide/prepare-in-advance/
- group: start
  title: ''
  type: SignUp
  url: https://openapi.nexon.com/my-application/create-app/
- group: operate
  title: ''
  type: Support
  url: https://openapi.nexon.com/support/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openapi.nexon.com/support/terms/
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexon-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexon-inc-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexon-inc-domain-security.yml
created: '2026-07-17'
description: Nexon (operated by Nexon Korea Co., Ltd.) is a global video game publisher whose NEXON Open API platform at openapi.nexon.com gives developers programmatic access to per-game data such as character, ranking, and match information. Requests are authenticated with a per-application API key sent in the x-nxopen-api-key HTTP header and served from open.api.nexon.com; the developer portal provides application registration, usage analytics, per-game API references, and integration guides.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nexon-inc.png
layout: provider
modified: '2026-07-20'
name: Nexon Inc
nav: Providers
network: true
overview: 'Nexon Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Video Games, and Game Data.


  Nexon Inc''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 5 more developer resources.'
random_paper: 8
screenshot: https://raw.githubusercontent.com/api-evangelist/nexon-inc/refs/heads/main/screenshots/nexon-inc-2026-08-07T185157.png
security:
- kind: authentication
  name: Nexon Inc Authentication
  slug: nexon-inc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nexon Inc Domain Security
  slug: nexon-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nexon-inc
tags:
- Company
- Consumer
- Gaming
- Video Games
- Game Data
- Developer API
- OpenAPI
website: http://www.nexon.net/
---
