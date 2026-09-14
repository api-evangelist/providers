---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://developers.sendinblue.com/docs'', ''status'': 301, ''note'': ''declared website redirects to https://developers.brevo.com/docs — a different registrable domain (sendinblue.com -> brevo.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://developers.sendinblue.com/docs
  baseurl_source: declared
  description: A service that provides solutions relating to marketing and/or transactional email and/or SMS
  name: Sendinblue
  slug: sendinblue
artifact_total: 4
asyncapis:
- description: AsyncAPI description of the outbound webhook surface for Brevo (formerly Sendinblue). Brevo delivers event notifications by issuing HTTP POST requests with a JSON body to a URL configured by the custo
  name: Brevo (Sendinblue) Webhooks
  slug: sendinblue-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendinblue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.sendinblue.com/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: A service that provides solutions relating to marketing and/or transactional email and/or SMS
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendinblue.png
layout: provider
modified: '2026-05-30'
name: Sendinblue
nav: Providers
network: true
overview: 'Sendinblue publishes 1 API on the [APIs.io](https://apis.io/) network: Sendinblue. Tagged areas include Email and Public APIs.


  The Sendinblue catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 15
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Sendinblue API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: sendinblue-asyncapi-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/sendinblue/refs/heads/main/screenshots/sendinblue-2026-06-20T193701.png
security:
- kind: domain-security
  name: Sendinblue Domain Security
  slug: sendinblue-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sendinblue
tags:
- Email
- Public APIs
website: https://developers.sendinblue.com/docs
---
