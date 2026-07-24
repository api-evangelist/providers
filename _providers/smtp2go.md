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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Smtp2Go Agentic Access
  operation_count: 52
  slug: smtp2go-agentic-access
  summary_line: 52 operations · 52 acting
api_count: 11
apis:
- description: REST API for sending transactional emails and SMS, managing sender domains, SMTP users, API keys, templates, webhooks, suppressions, and accessing delivery reports and activity statistics.
  name: SMTP2GO Email API
  slug: smtp2go-email-api
- description: Email activity search
  name: SMTP2GO Activity API
  slug: smtp2go-activity-api
- description: API key management
  name: SMTP2GO API Keys API
  slug: smtp2go-api-keys-api
- description: Sender domain management
  name: SMTP2GO Domains API
  slug: smtp2go-domains-api
- description: Send and receive SMS messages
  name: SMTP2GO SMS API
  slug: smtp2go-sms-api
- description: SMTP user account management
  name: SMTP2GO SMTP Users API
  slug: smtp2go-smtp-users-api
- description: Email delivery statistics and reports
  name: SMTP2GO Stats API
  slug: smtp2go-stats-api
- description: Subaccount management
  name: SMTP2GO Subaccounts API
  slug: smtp2go-subaccounts-api
- description: Suppression list management
  name: SMTP2GO Suppressions API
  slug: smtp2go-suppressions-api
- description: Email template management
  name: SMTP2GO Templates API
  slug: smtp2go-templates-api
- description: Webhook configuration
  name: SMTP2GO Webhooks API
  slug: smtp2go-webhooks-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smtp2go-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smtp2go-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smtp2go-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smtp2go.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smtp2go.com/docs/introduction-guide
- group: docs
  title: ''
  type: APIReference
  url: https://developers.smtp2go.com/reference/general-api-resources
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/smtp2go-oss
- group: company
  title: ''
  type: Blog
  url: https://www.smtp2go.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smtp2go.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://smtp2gostatus.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smtp2go
- group: other
  title: ''
  type: X
  url: https://x.com/smtp2go
- group: operate
  title: ''
  type: Support
  url: https://support.smtp2go.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/smtp2go-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smtp2go-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smtp2go-finops.yml
created: '2026-06-13'
description: Email delivery platform with a REST API for sending transactional emails, managing SMTP accounts, tracking delivery, viewing email statistics, and suppressing addresses.
examples:
- key_count: 4
  name: Add Suppression Example
  slug: add-suppression-example
- key_count: 4
  name: Send Email Example
  slug: send-email-example
- key_count: 4
  name: Send Sms Example
  slug: send-sms-example
finops:
- name: Smtp2Go Finops
  service_category: ''
  slug: smtp2go-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smtp2go.png
json_schemas:
- name: SMTP2GO Send Email Request
  property_count: 15
  slug: smtp2go-send-email
- name: SMTP2GO Suppression
  property_count: 6
  slug: smtp2go-suppression
jsonld:
- class_count: 9
  name: Smtp2Go Context
  property_count: 66
  slug: smtp2go-context
layout: provider
modified: '2026-06-13'
name: SMTP2GO
nav: Providers
network: true
overview: 'SMTP2GO publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Email API, Activity API, API Keys API, and 8 more. Tagged areas include Email, Email Delivery, Transactional Email, SMTP, and SMS.


  The SMTP2GO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SMTP2GO''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: Smtp2Go Plans Pricing
  plan_count: 4
  slug: smtp2go-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Smtp2Go Rate Limits
  slug: smtp2go-rate-limits
rules:
- name: SMTP2GO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smtp2go-jsonschema-spectral-rules
score:
  band: developing
  composite: 57.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.0
    developer_ergonomics: 32.6
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 57.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smtp2go/refs/heads/main/screenshots/smtp2go-2026-06-20T194102.png
security:
- kind: authentication
  name: Smtp2Go Authentication
  slug: smtp2go-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Smtp2Go Domain Security
  slug: smtp2go-domain-security
  summary_line: TLSv1.3 · DMARC
slug: smtp2go
tags:
- Email
- Email Delivery
- Transactional Email
- SMTP
- SMS
- Email API
- Deliverability
website: https://www.smtp2go.com/
---
