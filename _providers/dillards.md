---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dillards-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dillards-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dillards-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dillards-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dillards
- group: company
  title: ''
  type: Website
  url: https://www.dillards.com
- group: agent
  title: ''
  type: LlmsText
  url: https://www.dillards.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.dillards.com/c/customerservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dillards.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dillards.com/c/faqs-notices-policies?#q=int-policies-notices-question-legal-terms-of-use
coverage:
  checked: '2026-09-06'
  detail: Dillard's is a physical-goods department store with no developer program at all — every /.well-known/ and /openapi.json path on www.dillards.com returns the storefront SPA shell under HTTP 200, byte-for-byte the same class of response as a deliberate nonsense control path, and the only machine interface Dillard's actually operates is a supplier X12 EDI program whose implementation guide sits behind a vendor login on the ebiz.dillards.com extranet.
  evidence:
  - status: 200
    url: https://www.dillards.com/.well-known/api-catalog
  - status: 200
    url: https://www.dillards.com/openapi.json
  - status: 403
    url: https://ebiz.dillards.com/eBiz/
  - status: 200
    url: https://www.dillards.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-03-24'
description: Dillard's, Inc. is a Little Rock, Arkansas department store chain selling apparel, footwear, cosmetics, handbags, menswear and home goods through its stores across the United States and dillards.com. Dillard's publishes no developer program, no OpenAPI, GraphQL, AsyncAPI, gRPC or SOAP contract, and no MCP or A2A agent surface — contract discovery on 2026-09-06 found every /.well-known/ and /openapi.json path answering with the storefront single-page-app shell under HTTP 200, matching a nonsense control path. Its two real machine-facing surfaces are a first-party llms.txt at https://www.dillards.com/llms.txt that maps the retail catalog for language models, and an ANSI ASC X12 EDI trading-partner program (810/816/820/832/850/856/860/864/997 over the OpenText/GXS VAN) whose implementation guide and vendor portal are gated behind a login on the Dillard's eBiz extranet.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dillards.png
layout: provider
modified: '2026-09-06'
name: Dillard's
nav: Providers
network: true
overview: 'Dillard''s is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Department Store, Apparel, E-Commerce, and Fortune 500.


  Dillard''s'' developer surface includes support and 9 more developer resources.'
plans:
- name: Dillards Plans Pricing
  plan_count: 0
  slug: dillards-plans-pricing
press:
- date: '2026-05-25'
  title: Retail basics propel Dillard's in Q3
  url: https://www.retaildive.com/news/retail-basics-propel-dillards-q3-sales-up/805384/
- date: '2026-05-25'
  title: Dillard's, Inc. to Report Fourth Quarter and Fiscal Year Results
  url: https://www.barchart.com/story/news/374069/dillards-inc-to-report-fourth-quarter-and-fiscal-year-results
- date: '2026-05-25'
  title: Dillard's, Inc. Reports First Quarter Results | Markets Insider
  url: https://markets.businessinsider.com/news/stocks/dillard-s-inc-reports-first-quarter-results-1036155467
- date: '2026-05-25'
  title: Dillard's, Inc. Reports First Quarter Results - DDS
  url: https://www.stocktitan.net/news/DDS/dillard-s-inc-reports-first-quarter-v63n3of1e4jm.html
- date: '2026-05-25'
  title: Dillard's, Inc. Reports First Quarter Results | Thu, 05/14/2026
  url: https://investor.dillards.com/news-releases/news-release-details/dillards-inc-reports-first-quarter-results-6
random_paper: 7
rate_limits:
- limit_count: 0
  name: Dillards Rate Limits
  slug: dillards-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dillards/refs/heads/main/screenshots/dillards-2026-06-20T180028.png
security:
- kind: domain-security
  name: Dillards Domain Security
  slug: dillards-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dillards
tags:
- Retail
- Department Store
- Apparel
- E-Commerce
- Fortune 500
website: https://www.dillards.com
---
