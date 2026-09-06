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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Google Suite Docs Sheets Slides Gmail Agentic Access
  operation_count: 21
  slug: google-suite-docs-sheets-slides-gmail-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- baseURL: https://docs.googleapis.com
  baseurl_source: declared
  description: The Docs API from Google Workspace Suite — 3 operation(s) for docs.
  name: Google Workspace Suite Docs API
  slug: google-suite-docs-sheets-slides-gmail-docs-api
- baseURL: https://docs.googleapis.com
  baseurl_source: declared
  description: The Gmail API from Google Workspace Suite — 8 operation(s) for gmail.
  name: Google Workspace Suite Gmail API
  slug: google-suite-docs-sheets-slides-gmail-gmail-api
- baseURL: https://docs.googleapis.com
  baseurl_source: declared
  description: The Sheets API from Google Workspace Suite — 4 operation(s) for sheets.
  name: Google Workspace Suite Sheets API
  slug: google-suite-docs-sheets-slides-gmail-sheets-api
- baseURL: https://docs.googleapis.com
  baseurl_source: declared
  description: The Slides API from Google Workspace Suite — 3 operation(s) for slides.
  name: Google Workspace Suite Slides API
  slug: google-suite-docs-sheets-slides-gmail-slides-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Workspace Suite (, Sheets, Slides, Gmail) Docs API
  slug: open-google-suite-docs-sheets-slides-gmail-docs-api
- collection_type: open
  name: Google Workspace Suite (, Sheets, Slides, ) Docs Gmail API
  slug: open-google-suite-docs-sheets-slides-gmail-gmail-api
- collection_type: open
  name: Google Workspace Suite (, , Slides, Gmail) Docs Sheets API
  slug: open-google-suite-docs-sheets-slides-gmail-sheets-api
- collection_type: open
  name: Google Workspace Suite (, Sheets, , Gmail) Docs Slides API
  slug: open-google-suite-docs-sheets-slides-gmail-slides-api
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
random_paper: 5
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
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 31.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
