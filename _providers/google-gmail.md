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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Google Gmail Agentic Access
  operation_count: 29
  slug: google-gmail-agentic-access
  summary_line: 29 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Gmail API from Google Gmail — 19 operation(s) for gmail.
  name: Google Gmail Gmail API
  slug: google-gmail-gmail-api
artifact_total: 11
collections:
- collection_type: postman
  name: Google Gmail API
  slug: postman-google-gmail-gmail-api
- collection_type: open
  name: Google Gmail API
  slug: open-openapi
common:
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


  Google Gmail''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Gmail Plans Pricing
  plan_count: 3
  slug: google-gmail-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Google Gmail Rate Limits
  slug: google-gmail-rate-limits
rules:
- name: Google Gmail API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-gmail-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.0
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 67.4
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
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
website: https://developers.google.com/workspace/gmail
---
