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
- acting_count: 10
  human_in_the_loop: 0
  name: Google Suite Docs Sheets Slides Gmail Agentic Access
  operation_count: 21
  slug: google-suite-docs-sheets-slides-gmail-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 4
apis:
- description: The Docs API from Google Workspace Suite — 3 operation(s) for docs.
  name: Google Workspace Suite Docs API
  slug: google-suite-docs-sheets-slides-gmail-docs-api
- description: The Gmail API from Google Workspace Suite — 8 operation(s) for gmail.
  name: Google Workspace Suite Gmail API
  slug: google-suite-docs-sheets-slides-gmail-gmail-api
- description: The Sheets API from Google Workspace Suite — 4 operation(s) for sheets.
  name: Google Workspace Suite Sheets API
  slug: google-suite-docs-sheets-slides-gmail-sheets-api
- description: The Slides API from Google Workspace Suite — 3 operation(s) for slides.
  name: Google Workspace Suite Slides API
  slug: google-suite-docs-sheets-slides-gmail-slides-api
artifact_total: 13
collections:
- collection_type: open
  name: Google Workspace Suite (Docs, Sheets, Slides, Gmail)
  slug: open-google-suite-docs-sheets-slides-gmail
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-suite-docs-sheets-slides-gmail-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-suite-docs-sheets-slides-gmail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-suite-docs-sheets-slides-gmail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-suite-docs-sheets-slides-gmail-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-suite-docs-sheets-slides-gmail-scopes.yml
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
  url: https://developers.google.com/identity/protocols/oauth2
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com
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
  url: https://www.google.com/appsstatus
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default?alt=rss
created: '2024-01-01'
description: Collection of Google Workspace APIs including Docs, Sheets, Slides, and Gmail.
finops:
- name: Google Suite Docs Sheets Slides Gmail Finops
  service_category: API
  slug: google-suite-docs-sheets-slides-gmail-finops
image: https://workspace.google.com/static/img/logo.png
layout: provider
modified: '2026-04-28'
name: Google Workspace Suite
nav: Providers
network: true
overview: 'Google Workspace Suite publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Docs API, Gmail API, Sheets API, and 1 more. Tagged areas include Cloud, Collaboration, Documents, Google, and Productivity.


  Google Workspace Suite''s developer surface includes authentication, developer console, engineering blog, and 10 more developer resources.'
plans:
- name: Google Suite Docs Sheets Slides Gmail Plans Pricing
  plan_count: 3
  slug: google-suite-docs-sheets-slides-gmail-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Google Suite Docs Sheets Slides Gmail Rate Limits
  slug: google-suite-docs-sheets-slides-gmail-rate-limits
scopes:
- name: Google Suite Docs Sheets Slides Gmail Scopes
  scope_count: 6
  slug: google-suite-docs-sheets-slides-gmail-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 42.6
  delta: -1.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.0
    developer_ergonomics: 19.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-suite-docs-sheets-slides-gmail/refs/heads/main/screenshots/google-suite-docs-sheets-slides-gmail-2026-06-20T182236.png
security:
- kind: authentication
  name: Google Suite Docs Sheets Slides Gmail Authentication
  slug: google-suite-docs-sheets-slides-gmail-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Suite Docs Sheets Slides Gmail Domain Security
  slug: google-suite-docs-sheets-slides-gmail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Suite Docs Sheets Slides Gmail Vulnerability Disclosure
  slug: google-suite-docs-sheets-slides-gmail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-suite-docs-sheets-slides-gmail
tags:
- Cloud
- Collaboration
- Documents
- Google
- Productivity
- Workspace
website: https://workspace.google.com
---
