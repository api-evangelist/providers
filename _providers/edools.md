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
  - '{''url'': ''https://edools.com'', ''status'': 301, ''note'': ''declared website redirects to https://herospark.com/ — a different registrable domain (edools.com -> herospark.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Token-authenticated REST API for managing an Edools school — team and role administration, content (courses, learning paths, lessons, media), student management and engagement triggers, and school pro
  name: Edools Core API
  slug: edools-core-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://edools.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plataforma.edools.com/desenvolvedores
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edools.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.edools.com/file.05_api.html
- group: operate
  title: ''
  type: Support
  url: https://ajuda.herospark.com/
- group: company
  title: ''
  type: Blog
  url: https://herospark.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://herospark.com/calculadora-de-taxas
- group: start
  title: ''
  type: SignUp
  url: https://app.herospark.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.herospark.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://herospark.com/termos-de-uso-herospark/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://herospark.com/politicas-de-privacidade/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Edools
- group: operate
  title: ''
  type: StatusPage
  url: https://status.herospark.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/edools-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edools-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edools-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edools-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/edools-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/edools-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/edools-cli.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edools-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edools-llms.txt
created: '2026-07-17'
description: Edools is a Brazilian e-learning and digital-education platform for creating, hosting, and selling online courses, learning paths, and training programs under a white-label school (LMS) with a Netflix-style members area, video hosting, and student engagement tools. The platform is now delivered as HeroSpark (edools.com redirects to herospark.com), a digital-product sales suite for course creators covering checkout, payments (SparkPay), members areas, and a student mobile app. Edools exposes a token-authenticated REST API (base host per-school on myedools.com) for team, content, and student management, plus first-party Ruby and PHP client libraries and theme development tooling, letting integrators sync courses, students, enrollments, and school products with external systems.
image: https://herospark.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Edools
nav: Providers
network: true
overview: 'Edools publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, E-Learning, LMS, and Online Courses.


  Edools'' developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 15 more developer resources.'
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/edools/refs/heads/main/screenshots/edools-2026-07-25T212856.png
security:
- kind: authentication
  name: Edools Authentication
  slug: edools-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Edools Domain Security
  slug: edools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edools
tags:
- Company
- Education
- E-Learning
- LMS
- Online Courses
- EdTech
- Content Management
- Digital Products
- Brazil
- REST
website: https://edools.com
---
