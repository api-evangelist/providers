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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kickbox Agentic Access
  operation_count: 5
  slug: kickbox-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 5
apis:
- description: REST API for verifying the deliverability of email addresses in real time. Returns a result (deliverable, undeliverable, risky, unknown), a reason code, plus flags for role addresses, disposable domai
  name: Kickbox Email Verification API
  slug: verification-api
- description: Account balance and metadata.
  name: Kickbox Account API
  slug: kickbox-account-api
- description: Bulk CSV email verification.
  name: Kickbox Batch API
  slug: kickbox-batch-api
- description: Free disposable-domain lookup (no auth).
  name: Kickbox Open API
  slug: kickbox-open-api
- description: Real-time email verification.
  name: Kickbox Verification API
  slug: kickbox-verification-api
artifact_total: 9
collections:
- collection_type: open
  name: Kickbox Email Verification API
  slug: open-kickbox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kickbox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kickbox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kickbox-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kickbox
- group: company
  title: ''
  type: Website
  url: https://kickbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kickbox.com
- group: commercial
  title: ''
  type: Pricing
  url: https://kickbox.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.kickbox.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kickboxio
- group: operate
  title: ''
  type: Support
  url: https://kickbox.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kickbox.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.kickbox.com/rss/
created: '2026-05-11'
description: Kickbox is an email verification and list cleaning service that helps senders improve deliverability by detecting invalid, disposable, role-based, and risky email addresses before they enter mailing lists. The platform offers real-time single verification, bulk batch verification, and a deliverability monitoring suite. Kickbox provides a simple HTTPS REST API authenticated by API key returning structured verification results with reason codes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kickbox.png
layout: provider
modified: '2026-05-11'
name: Kickbox
nav: Providers
network: true
overview: 'Kickbox publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Batch API, Open API, and 1 more. Tagged areas include Email Verification, Email Validation, Deliverability, Data Quality, and Email.


  Kickbox''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 57.5
    developer_ergonomics: 26.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kickbox/refs/heads/main/screenshots/kickbox-2026-06-20T184032.png
security:
- kind: authentication
  name: Kickbox Authentication
  slug: kickbox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kickbox Domain Security
  slug: kickbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kickbox
tags:
- Email Verification
- Email Validation
- Deliverability
- Data Quality
- Email
website: https://kickbox.com
---
