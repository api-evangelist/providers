---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Suites Agentic Access
  operation_count: 14
  slug: google-suites-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 4
apis:
- description: Manage video conferencing.
  name: Google Meet API
  slug: google-meet-api
- description: The Calendar API from Google Workspace APIs — 3 operation(s) for calendar.
  name: Google Workspace APIs Calendar API
  slug: google-suites-calendar-api
- description: The Drive API from Google Workspace APIs — 2 operation(s) for drive.
  name: Google Workspace APIs Drive API
  slug: google-suites-drive-api
- description: The Gmail API from Google Workspace APIs — 4 operation(s) for gmail.
  name: Google Workspace APIs Gmail API
  slug: google-suites-gmail-api
artifact_total: 13
collections:
- collection_type: open
  name: Google Workspace APIs (Gmail, Calendar, Drive)
  slug: open-google-suites
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-suites-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-suites-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-suites-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-suites-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-suites-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/googleworkspace
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/workspace/guides/auth-overview
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://workspace.google.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://workspace.google.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/workspace/guides/client-libraries
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default?alt=rss
created: '2024-01-01'
description: Collection of APIs for Google Workspace (formerly G Suite) services including Gmail, Calendar, Drive, Docs, Sheets, and more.
finops:
- name: Google Suites Finops
  service_category: API
  slug: google-suites-finops
image: https://workspace.google.com/static/img/logo-workspace.svg
layout: provider
modified: '2026-04-28'
name: Google Workspace APIs
nav: Providers
network: true
overview: 'Google Workspace APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Calendar API, Drive API, and Gmail API. Tagged areas include Cloud Storage, Collaboration, Email, Office Suite, and Productivity.


  Google Workspace APIs'' developer surface includes authentication, developer console, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Suites Plans Pricing
  plan_count: 3
  slug: google-suites-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Google Suites Rate Limits
  slug: google-suites-rate-limits
scopes:
- name: Google Suites Scopes
  scope_count: 6
  slug: google-suites-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 42.7
  delta: -1.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.0
    developer_ergonomics: 30.4
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-suites/refs/heads/main/screenshots/google-suites-2026-06-20T182240.png
security:
- kind: authentication
  name: Google Suites Authentication
  slug: google-suites-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Suites Domain Security
  slug: google-suites-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Suites Vulnerability Disclosure
  slug: google-suites-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-suites
tags:
- Cloud Storage
- Collaboration
- Email
- Office Suite
- Productivity
website: https://workspace.google.com/
---
