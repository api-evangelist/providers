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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Emailoctopus Agentic Access
  operation_count: 25
  slug: emailoctopus-agentic-access
  summary_line: 25 operations · 15 acting
api_count: 6
apis:
- description: The Automation API from EmailOctopus — 1 operation(s) for automation.
  name: EmailOctopus Automation API
  slug: emailoctopus-automation-api
- description: The Campaign API from EmailOctopus — 5 operation(s) for campaign.
  name: EmailOctopus Campaign API
  slug: emailoctopus-campaign-api
- description: The Contact API from EmailOctopus — 3 operation(s) for contact.
  name: EmailOctopus Contact API
  slug: emailoctopus-contact-api
- description: The Field API from EmailOctopus — 2 operation(s) for field.
  name: EmailOctopus Field API
  slug: emailoctopus-field-api
- description: The List API from EmailOctopus — 2 operation(s) for list.
  name: EmailOctopus List API
  slug: emailoctopus-list-api
- description: The Tag API from EmailOctopus — 2 operation(s) for tag.
  name: EmailOctopus Tag API
  slug: emailoctopus-tag-api
artifact_total: 13
collections:
- collection_type: open
  name: EmailOctopus v2 API
  slug: open-emailoctopus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emailoctopus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emailoctopus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emailoctopus-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emailoctopus
- group: company
  title: ''
  type: Website
  url: https://emailoctopus.com
- group: docs
  title: ''
  type: Documentation
  url: https://emailoctopus.com/api-documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/emailoctopus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emailoctopus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/emailoctopus-finops.yml
created: '2026-06-25'
description: EmailOctopus is an affordable email-marketing platform for newsletters, campaigns, automations, and audience management. Its REST API (v2 at https://api.emailoctopus.com, Bearer authenticated) lets developers manage lists, contacts, custom fields, tags, campaigns, automations, and campaign reports programmatically.
finops:
- name: Emailoctopus Finops
  service_category: Marketing and Communications
  slug: emailoctopus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emailoctopus.png
layout: provider
modified: '2026-06-25'
name: EmailOctopus
nav: Providers
network: true
overview: 'EmailOctopus publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Automation API, Campaign API, Contact API, and 3 more. Tagged areas include Email, Email Marketing, Newsletters, Campaigns, and Automation.


  EmailOctopus'' developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Emailoctopus Plans Pricing
  plan_count: 3
  slug: emailoctopus-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 4
  name: Emailoctopus Rate Limits
  slug: emailoctopus-rate-limits
score:
  band: thin
  composite: 36.5
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emailoctopus/refs/heads/main/screenshots/emailoctopus-2026-07-25T213222.png
security:
- kind: authentication
  name: Emailoctopus Authentication
  slug: emailoctopus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Emailoctopus Domain Security
  slug: emailoctopus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emailoctopus
tags:
- Email
- Email Marketing
- Newsletters
- Campaigns
- Automation
website: https://emailoctopus.com
---
