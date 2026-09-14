---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.postman-echo.com'', ''status'': 302, ''note'': ''declared website redirects to https://www.postman.com/postman/workspace/published-postman-templates/documentation/631643-f695cab7-6878-eb55-7943-ad88e1ccfd65?ctx=documentation — a different registrable domain (postman-echo.com -> postman.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Test api server to receive and return value from HTTP method
  name: Postman Echo
  slug: postman-echo
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postman-echo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.postman-echo.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Test api server to receive and return value from HTTP method
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postman-echo.png
layout: provider
modified: '2026-05-28'
name: Postman Echo
nav: Providers
network: true
overview: Postman Echo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Validation and Public APIs.
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/postman-echo/refs/heads/main/screenshots/postman-echo-2026-06-20T192007.png
security:
- kind: domain-security
  name: Postman Echo Domain Security
  slug: postman-echo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postman-echo
tags:
- Data Validation
- Public APIs
website: https://www.postman-echo.com
---
