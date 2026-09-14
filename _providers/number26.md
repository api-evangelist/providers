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
- baseURL: https://xs2a.tech26.de/v1/berlin-group/v1
  baseurl_source: declared
  description: The default API from Number26 — 9 operation(s) for default.
  name: Number26 default API
  slug: number26-default-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: XS2A_N26 default API
  slug: open-number26-default-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/number26-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://n26.com/en-eu
- group: company
  title: ''
  type: Blog
  url: https://n26.com/en-eu/blog
- group: operate
  title: ''
  type: Support
  url: https://support.n26.com/en-eu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.n26.com/legal/06+EU/03+Privacy%20Policy/en/01privacy-policy-en.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://n26.com/en-eu/legal-documents
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/n26
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/n26/psd2-tpp-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/n26/psd2-tpp-docs
- group: build
  title: ''
  type: Postman
  url: https://github.com/n26/psd2-tpp-docs/tree/master/doc/assets/postman
- group: auth
  title: ''
  type: Authentication
  url: authentication/number26-xs2a-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/number26-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/number26-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/number26-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/number26-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/number26-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/number26-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/number26-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/number26-xs2a-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/number26-llms.txt
created: '2026-07-17'
description: Number26 — trading as N26 (legally N26 GmbH) — is a German licensed digital bank offering 100% mobile banking to more than 8 million customers across 24 European markets. Founded in Berlin in 2013 and holding a full banking licence from Germany's Federal Financial Supervisory Authority (BaFin), N26 provides current accounts with virtual and physical Mastercard debit cards, instant savings with variable interest, in-app stock/ETF and cryptocurrency investing, real-time spending insights, sub-accounts (Spaces), and travel features such as foreign-exchange and insurance, across a free tier and paid Smart, Go, and Metal plans plus matching business accounts. N26 is a consumer neobank and does not publish a public developer API, developer portal, or API documentation; this API Evangelist profile tracks the company's public web presence.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/number26.png
layout: provider
modified: '2026-07-20'
name: Number26
nav: Providers
network: true
overview: 'Number26 publishes 1 API on the [APIs.io](https://apis.io/) network: default API. Tagged areas include Company, Fintech, Banking, Neobank, and Mobile Banking.


  Number26''s developer surface includes engineering blog, support, documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 18
screenshot: https://raw.githubusercontent.com/api-evangelist/number26/refs/heads/main/screenshots/number26-2026-08-07T185726.png
security:
- kind: authentication
  name: Number26 Xs2A Authentication
  slug: number26-xs2a-authentication
  summary_line: http/mutualTLS · 2 schemes
- kind: domain-security
  name: Number26 Domain Security
  slug: number26-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: number26
tags:
- Company
- Fintech
- Banking
- Neobank
- Mobile Banking
- Payments
- Europe
- Germany
website: https://n26.com/en-eu
---
