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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Google Suite Agentic Access
  operation_count: 11
  slug: google-suite-agentic-access
  summary_line: 11 operations · 6 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Google Meet API allows developers to build applications that integrate with Google Meet.
  name: Google Meet API
  slug: google-meet-api
- description: The Google Forms API provides programmatic access to create, modify, and retrieve form content and responses.
  name: Google Forms API
  slug: google-forms-api
- description: The Gmail API from Google Workspace (G Suite) — 10 operation(s) for gmail.
  name: Google Workspace (G Suite) Gmail API
  slug: google-suite-gmail-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gmail API
  slug: open-google-suite-gmail-api
- collection_type: open
  name: Gmail API
  slug: open-google-suite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-suite-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-suite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-suite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-suite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-suite-scopes.yml
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
  url: https://console.cloud.google.com/
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
  url: https://www.google.com/appsstatus/dashboard/
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default?alt=rss
created: '2024-01-15'
description: Google Workspace (formerly G Suite) is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google.
finops:
- name: Google Suite Finops
  service_category: API
  slug: google-suite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-suite.png
layout: provider
modified: '2026-04-28'
name: Google Workspace (G Suite)
nav: Providers
network: true
overview: 'Google Workspace (G Suite) publishes 1 API on the [APIs.io](https://apis.io/) network: Gmail API. Tagged areas include Cloud, Collaboration, Enterprise, Google, and Productivity.


  Google Workspace (G Suite)''s developer surface includes authentication, developer console, engineering blog, and 10 more developer resources.'
plans:
- name: Google Suite Plans Pricing
  plan_count: 3
  slug: google-suite-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Google Suite Rate Limits
  slug: google-suite-rate-limits
scopes:
- name: Google Suite Scopes
  scope_count: 5
  slug: google-suite-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 35.4
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 52.5
    developer_ergonomics: 19.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-suite/refs/heads/main/screenshots/google-suite-2026-06-20T182235.png
security:
- kind: authentication
  name: Google Suite Authentication
  slug: google-suite-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Suite Domain Security
  slug: google-suite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Suite Vulnerability Disclosure
  slug: google-suite-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-suite
tags:
- Cloud
- Collaboration
- Enterprise
- Google
- Productivity
- Workspace
website: https://workspace.google.com/
---
