---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Gravity Forms Agentic Access
  operation_count: 16
  slug: gravity-forms-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 6
apis:
- description: WordPress-hosted REST API for managing Gravity Forms forms, entries, feeds, fields, notifications, submissions, and results. Uses Basic Auth or OAuth 1.0a with consumer keys generated in the Gravity F
  name: Gravity Forms REST API v2
  slug: rest-api-v2
- description: The Entries API from Gravity Forms — 2 operation(s) for entries.
  name: Gravity Forms Entries API
  slug: gravity-forms-entries-api
- description: The Feeds API from Gravity Forms — 1 operation(s) for feeds.
  name: Gravity Forms Feeds API
  slug: gravity-forms-feeds-api
- description: The Forms API from Gravity Forms — 4 operation(s) for forms.
  name: Gravity Forms Forms API
  slug: gravity-forms-forms-api
- description: The Notifications API from Gravity Forms — 1 operation(s) for notifications.
  name: Gravity Forms Notifications API
  slug: gravity-forms-notifications-api
- description: The Results API from Gravity Forms — 1 operation(s) for results.
  name: Gravity Forms Results API
  slug: gravity-forms-results-api
artifact_total: 12
collections:
- collection_type: open
  name: Gravity Forms REST API v2
  slug: open-gravity-forms
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gravity-forms-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gravity-forms-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gravity-forms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gravity-forms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gravity-forms-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gravityforms
- group: company
  title: ''
  type: Website
  url: https://www.gravityforms.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gravityforms.com
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.gravityforms.com/rest-api-v2/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gravityforms.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.gravityforms.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.gravityforms.com/my-account/
- group: operate
  title: ''
  type: Support
  url: https://www.gravityforms.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.gravityforms.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gravityforms
created: '2026-05-11'
description: Gravity Forms is a premium WordPress form plugin used to build advanced forms, surveys, quizzes, payment forms, and workflow applications on WordPress sites. The plugin provides drag-and-drop form building, conditional logic, add-on integrations with CRMs and marketing platforms, and entry management. The Gravity Forms REST API v2 exposes forms, entries, feeds, notifications, and submissions over HTTP using Basic Auth or OAuth 1.0a authentication scoped to API keys.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gravity-forms.png
layout: provider
modified: '2026-05-11'
name: Gravity Forms
nav: Providers
network: true
overview: 'Gravity Forms publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Entries API, Feeds API, Forms API, and 2 more. Tagged areas include WordPress, Forms, Form Builder, Surveys, and Workflow.


  Gravity Forms'' developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 9 more developer resources.'
random_paper: 94
score:
  band: thin
  composite: 33.8
  delta: -0.5
  facets:
    commercial_clarity: 31.6
    contract_quality: 51.5
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gravity-forms/refs/heads/main/screenshots/gravity-forms-2026-06-20T182350.png
security:
- kind: authentication
  name: Gravity Forms Authentication
  slug: gravity-forms-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Gravity Forms Domain Security
  slug: gravity-forms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gravity Forms Vulnerability Disclosure
  slug: gravity-forms-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Gravity Forms Trust Center
  slug: gravity-forms-trust-center
  summary_line: HIPAA, GDPR
slug: gravity-forms
tags:
- WordPress
- Forms
- Form Builder
- Surveys
- Workflow
- Plugins
website: https://www.gravityforms.com
---
