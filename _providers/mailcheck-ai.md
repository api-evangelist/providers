---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.mailcheck.ai/#documentation'', ''status'': 301, ''note'': ''declared website redirects to https://www.usercheck.com/?ref=mailcheck — a different registrable domain (mailcheck.ai -> usercheck.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Prevent users to sign up with temporary email addresses
  name: MailCheck.ai
  slug: mailcheckai
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailcheck-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mailcheck.ai/#documentation
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Prevent users to sign up with temporary email addresses
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailcheck-ai.png
layout: provider
modified: '2026-05-28'
name: MailCheck.ai
nav: Providers
network: true
overview: MailCheck.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email and Public APIs.
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/mailcheck-ai/refs/heads/main/screenshots/mailcheck-ai-2026-06-20T184854.png
security:
- kind: domain-security
  name: Mailcheck Ai Domain Security
  slug: mailcheck-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mailcheck-ai
tags:
- Email
- Public APIs
website: https://www.mailcheck.ai/#documentation
---
