---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 13
  human_in_the_loop: 0
  name: Mailosaur Agentic Access
  operation_count: 28
  slug: mailosaur-agentic-access
  summary_line: 28 operations · 13 acting
api_count: 7
apis:
- description: Operations for analyzing the content and deliverability of an email, including SpamAssassin scoring and per-provider deliverability reports.
  name: Mailosaur Analysis API
  slug: mailosaur-analysis-api
- description: Operations for managing virtual security devices and retrieving their current one-time passwords (OTPs), used to automate testing of app-based multi-factor authentication.
  name: Mailosaur Devices API
  slug: mailosaur-devices-api
- description: Operations for downloading the raw content associated with a message — file attachments, the full EML source of an email, and rendered email previews.
  name: Mailosaur Files API
  slug: mailosaur-files-api
- description: Operations for finding, retrieving, creating, forwarding, replying to, and deleting the email and SMS messages received by your Mailosaur inboxes.
  name: Mailosaur Messages API
  slug: mailosaur-messages-api
- description: Operations for discovering the email clients available for generating email previews (screenshots of an email rendered in real clients).
  name: Mailosaur Previews API
  slug: mailosaur-previews-api
- description: Operations for creating and managing your Mailosaur inboxes (servers). Inboxes group your tests together, each with its own domain and SMTP/POP3/IMAP credentials.
  name: Mailosaur Servers API
  slug: mailosaur-servers-api
- description: Operations for inspecting your account's usage limits and recent transactional usage. These endpoints require authentication with an account-level API key.
  name: Mailosaur Usage API
  slug: mailosaur-usage-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailosaur-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mailosaur-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailosaur-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailosaur-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mailosaur.com
- group: docs
  title: ''
  type: Documentation
  url: https://mailosaur.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mailosaur
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailosaur
- group: other
  title: ''
  type: X
  url: https://x.com/mailosaur
- group: company
  title: ''
  type: Blog
  url: https://mailosaur.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://mailosaur.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mailosaur.com
- group: commercial
  title: ''
  type: Plans
  url: plans/mailosaur-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailosaur-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailosaur-finops.yml
created: 2026-06-13
description: Mailosaur is an email and SMS testing platform for developers and QA teams. It provides a REST API for creating test inboxes, capturing and retrieving messages, running assertions, performing deliverability analysis, and integrating email and SMS testing into CI/CD pipelines. The platform supports authentication testing (TOTP/2FA), spam analysis, SPF/DKIM/DMARC validation, and connects via SMTP, POP3, and IMAP protocols.
examples:
- key_count: 3
  name: Mailosaur Create Server Example
  slug: mailosaur-create-server-example
- key_count: 3
  name: Mailosaur Deliverability Report Example
  slug: mailosaur-deliverability-report-example
- key_count: 3
  name: Mailosaur Get Otp Example
  slug: mailosaur-get-otp-example
- key_count: 3
  name: Mailosaur Search Messages Example
  slug: mailosaur-search-messages-example
finops:
- name: Mailosaur Finops
  service_category: ''
  slug: mailosaur-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailosaur.png
json_schemas:
- name: Device
  property_count: 2
  slug: mailosaur-device
- name: Message
  property_count: 13
  slug: mailosaur-message
- name: Server
  property_count: 4
  slug: mailosaur-server
jsonld:
- class_count: 38
  name: Mailosaur Context
  property_count: 7
  slug: mailosaur-context
layout: provider
modified: 2026-06-13
name: Mailosaur
nav: Providers
network: true
overview: 'Mailosaur publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analysis API, Devices API, Files API, and 4 more. Tagged areas include Email Testing, SMS Testing, Developer Tools, QA Automation, and CI/CD.


  The Mailosaur catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mailosaur''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Mailosaur Plans Pricing
  plan_count: 3
  slug: mailosaur-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 0
  name: Mailosaur Rate Limits
  slug: mailosaur-rate-limits
rules:
- name: Mailosaur API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: mailosaur-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.0
  delta: -4.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailosaur/refs/heads/main/screenshots/mailosaur-2026-06-20T184900.png
security:
- kind: authentication
  name: Mailosaur Authentication
  slug: mailosaur-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mailosaur Domain Security
  slug: mailosaur-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mailosaur Trust Center
  slug: mailosaur-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: mailosaur
tags:
- Email Testing
- SMS Testing
- Developer Tools
- QA Automation
- CI/CD
- SMTP
- TOTP
- Deliverability
website: https://mailosaur.com
---
