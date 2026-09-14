---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.truveta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.truveta.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.truveta.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truveta.com/privacy-notice/
- group: start
  title: ''
  type: Login
  url: https://studio.truveta.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TruvetaPublic
- group: auth
  title: ''
  type: Compliance
  url: https://trust.truveta.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truveta-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/truveta-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truveta-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/truveta-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truveta-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/truveta-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/truveta-cli.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/truveta-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truveta-domain-security.yml
coverage:
  checked: '2026-08-05'
  detail: Truveta ships no developer surface at all — developer.truveta.com and docs.truveta.com do not resolve, and the only product entry point, studio.truveta.com, 302s straight into an Auth0 universal login at login.truveta.com, so the API reference (if one exists) requires a signed health-system or life-science subscription to reach.
  evidence:
  - status: 302
    url: https://studio.truveta.com/
  - status: 0
    url: https://developer.truveta.com/
  - status: 0
    url: https://docs.truveta.com/
  - status: 404
    url: https://api.truveta.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: 'Truveta is a health-system-led data and analytics company founded in 2020 and headquartered in Bellevue, Washington, jointly owned by 30 US health systems. It aggregates daily-updated, de-identified electronic health record data covering more than 120 million US patients, links it with claims, mortality and genomic data, and delivers it as regulatory-grade real-world evidence through Truveta Data and Truveta Studio, a HIPAA-compliant analytics workspace combining serverless SQL with Jupyter notebooks in R and Python. The Truveta Language Model normalizes unstructured clinical text into research-ready concepts, and the Truveta Genome Project links de-identified genetic data to the same longitudinal records. Truveta publishes no public API, developer portal or machine-readable specification: Truveta Studio is reachable only through an authenticated customer tenant at studio.truveta.com.'
image: https://www.truveta.com/wp-content/uploads/2025/01/Truveta-home-featured-image-1.png
layout: provider
modified: '2026-08-05'
name: Truveta
nav: Providers
network: true
overview: 'Truveta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Data, Electronic Health Records, and Real-World Evidence.


  Truveta''s developer surface includes engineering blog, support, authentication, CLI, and 12 more developer resources.'
random_paper: 2
scopes:
- name: Truveta Scopes
  scope_count: 14
  slug: truveta-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
screenshot: https://raw.githubusercontent.com/api-evangelist/truveta/refs/heads/main/screenshots/truveta-2026-09-02T164431.png
security:
- kind: authentication
  name: Truveta Authentication
  slug: truveta-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Truveta Domain Security
  slug: truveta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Truveta Trust Center
  slug: truveta-trust-center
  summary_line: HITRUST R2, ISO/IEC 27001, ISO/IEC 27018:2019, ISO/IEC 27701, SOC 2 Type 2
slug: truveta
tags:
- Company
- Healthcare
- Health Data
- Electronic Health Records
- Real-World Evidence
- Clinical Research
- Life Sciences
- Genomics
- Analytics
- Artificial Intelligence
- Data Platform
website: https://www.truveta.com/
---
