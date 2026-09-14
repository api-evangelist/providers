---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Google Gmail Agentic Access
  operation_count: 29
  slug: google-gmail-agentic-access
  summary_line: 29 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://gmail.googleapis.com
  baseurl_source: declared
  description: The Gmail API from Google Gmail — 19 operation(s) for gmail.
  name: Google Gmail Gmail API
  slug: google-gmail-gmail-api
artifact_total: 13
collections:
- collection_type: postman
  name: Google Gmail API
  slug: postman-google-gmail-gmail-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Gmail API
  slug: open-google-gmail-gmail-api
- collection_type: open
  name: Google Gmail API
  slug: open-openapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-gmail/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-gmail-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-gmail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-gmail-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/workspace/gmail
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/gmail/api/guides
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/gmail/api
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/workspace/gmail/api/auth/about-auth
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/workspace/gmail/api/guides/quota
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/workspace/gmail/api/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/gmail/rss/
created: '2026-03-13'
description: The Gmail API lets you view and manage Gmail mailbox data like threads, messages, and labels. It provides RESTful access to Gmail mailboxes, supporting message sending, drafting, organizing with labels, managing settings, and push notifications for mailbox changes. The API uses OAuth 2.0 for authorization and supports both user and service account authentication for Google Workspace domains.
finops:
- name: Google Gmail Finops
  service_category: API
  slug: google-gmail-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-gmail.png
jsonld:
- class_count: 6
  name: Json Ld Context
  property_count: 5
  slug: json-ld
layout: provider
modified: '2026-05-19'
name: Google Gmail
nav: Providers
network: true
overview: 'Google Gmail publishes 1 API on the [APIs.io](https://apis.io/) network: Gmail API. Tagged areas include Drafts, Email, Gmail, Google, and Google Workspace.


  The Google Gmail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Gmail''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 10 more developer resources.'
plans:
- name: Google Gmail Plans Pricing
  plan_count: 3
  slug: google-gmail-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Gmail Rate Limits
  slug: google-gmail-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Gmail API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-gmail-jsonschema-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/google-gmail/refs/heads/main/screenshots/google-gmail-2026-06-20T182205.png
security:
- kind: domain-security
  name: Google Gmail Domain Security
  slug: google-gmail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Gmail Vulnerability Disclosure
  slug: google-gmail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-gmail
tags:
- Drafts
- Email
- Gmail
- Google
- Google Workspace
- Labels
- Messaging
- Threads
website: https://www.google.com/
---
