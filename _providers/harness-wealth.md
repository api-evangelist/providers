---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harness-wealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.harness.co/
- group: company
  title: ''
  type: About
  url: https://www.harness.co/about
- group: company
  title: ''
  type: Blog
  url: https://www.harness.co/articles
- group: operate
  title: ''
  type: Support
  url: https://help.harness.co/
- group: operate
  title: ''
  type: Roadmap
  url: https://harness.canny.io/
- group: start
  title: ''
  type: Login
  url: https://app.harness.co/app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harness-wealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harness.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harness.co/privacy-policy
- group: auth
  title: ''
  type: Disclosures
  url: https://www.harness.co/regulatory-disclosures
- group: company
  title: ''
  type: Press
  url: https://www.harness.co/press
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/harnesswealth
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/harnesswealth/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harness-wealth-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Harness ships its tax-advisory platform only as an end-user web application at app.harness.co — api.harness.co, docs.harness.co and developer.harness.co do not resolve in DNS, the marketing site returns a hard 404 for /llms.txt, /openapi.json and every /.well-known/ path, and the only host that answers a spec probe is the client SPA, which returns the same 18,352-byte HTML shell for every unmatched path.
  evidence:
  - status: 404
    url: https://www.harness.co/openapi.json
  - status: 404
    url: https://www.harness.co/llms.txt
  - status: 404
    url: https://www.harness.co/.well-known/agent-card.json
  - status: 200
    url: https://app.harness.co/openapi.json
  - status: 404
    url: https://app.harness.co/.well-known/agent-card.json
  - status: 200
    url: https://harnesswealth.com/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'Harness — the company that launched as Harness Wealth, and today a wholly owned business of Multiplier, Inc. — is a New York City firm that runs an advisory platform for tax and wealth practices. It operates three connected surfaces: a marketplace that matches individuals with complex financial situations (equity compensation, liquidity events, business owners, real estate, high net worth) to vetted tax advisors; a client portal and workflow platform that tax firms run their engagements, documents, questionnaires and e-file on; and Harness Wealth Advisers, LLC, an SEC-registered investment adviser that recommends third-party advisers. Harness publishes no public developer program — there is no developer portal, API reference, OpenAPI/GraphQL/AsyncAPI specification, SDK, CLI or webhook documentation on any Harness host, and the product is delivered entirely as an end-user web application at app.harness.co.'
image: https://www.harness.co/assets/logo.svg
layout: provider
modified: '2026-08-22'
name: Harness Wealth
nav: Providers
network: true
overview: 'Harness Wealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Tax, Wealth Management, and Accounting.


  Harness Wealth''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 18
screenshot: https://raw.githubusercontent.com/api-evangelist/harness-wealth/refs/heads/main/screenshots/harness-wealth-2026-09-02T145705.png
security:
- kind: domain-security
  name: Harness Wealth Domain Security
  slug: harness-wealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harness-wealth
tags:
- Company
- Financial-Services
- Tax
- Wealth Management
- Accounting
- Investment Advisory
- Marketplace
- Professional Services
- Fintech
website: https://www.harness.co/
---
