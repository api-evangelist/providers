---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Mailpace Agentic Access
  operation_count: 11
  slug: mailpace-agentic-access
  summary_line: 11 operations · 7 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Delivers outbound, Ed25519-signed event callbacks (email.queued, email.delivered, email.deferred, email.bounced, email.spam) to your endpoints. Configured per domain in the MailPace dashboard; the pub
  name: MailPace Webhooks API
  slug: mailpace-webhooks-api
- description: Manage per-domain API tokens.
  name: MailPace API Tokens API
  slug: mailpace-api-tokens-api
- description: Manage sending domains and DKIM verification.
  name: MailPace Domains API
  slug: mailpace-domains-api
- description: Send transactional email.
  name: MailPace Send API
  slug: mailpace-send-api
artifact_total: 11
collections:
- collection_type: open
  name: MailPace API
  slug: open-mailpace
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailpace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailpace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailpace-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailpace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailpace
- group: company
  title: ''
  type: Website
  url: https://mailpace.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mailpace.com
- group: commercial
  title: ''
  type: Plans
  url: plans/mailpace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailpace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailpace-finops.yml
created: '2026-06-20'
description: MailPace is a fast, privacy-focused transactional email API for developers. It delivers application email - password resets, receipts, notifications - over a simple HTTPS REST API and SMTP, with DKIM-verified sending domains, Ed25519-signed webhooks, and EU-based hosting.
finops:
- name: Mailpace Finops
  service_category: Email and Messaging
  slug: mailpace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailpace.png
layout: provider
modified: '2026-06-20'
name: MailPace
nav: Providers
network: true
overview: 'MailPace publishes 3 APIs on the [APIs.io](https://apis.io/) network: API Tokens API, Domains API, and Send API. Tagged areas include Email, Transactional Email, Messaging, SMTP, and Privacy.


  MailPace''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Mailpace Plans Pricing
  plan_count: 2
  slug: mailpace-plans-pricing
random_paper: 108
rate_limits:
- limit_count: 3
  name: Mailpace Rate Limits
  slug: mailpace-rate-limits
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailpace/refs/heads/main/screenshots/mailpace-2026-06-20T184903.png
security:
- kind: authentication
  name: Mailpace Authentication
  slug: mailpace-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mailpace Domain Security
  slug: mailpace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mailpace
tags:
- Email
- Transactional Email
- Messaging
- SMTP
- Privacy
website: https://mailpace.com
---
