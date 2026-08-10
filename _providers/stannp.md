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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Stannp Agentic Access
  operation_count: 32
  slug: stannp-agentic-access
  summary_line: 32 operations · 23 acting
api_count: 7
apis:
- description: Account balance and user information
  name: Stannp Account API
  slug: stannp-account-api
- description: Manage batch direct mail campaigns
  name: Stannp Campaigns API
  slug: stannp-campaigns-api
- description: Record recipient engagement and conversion events
  name: Stannp Events API
  slug: stannp-events-api
- description: Manage recipient groups
  name: Stannp Groups API
  slug: stannp-groups-api
- description: Create, post, retrieve, and cancel letter mailpieces
  name: Stannp Letters API
  slug: stannp-letters-api
- description: Create, retrieve, and cancel postcard mailpieces
  name: Stannp Postcards API
  slug: stannp-postcards-api
- description: Manage individual recipients and bulk imports
  name: Stannp Recipients API
  slug: stannp-recipients-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stannp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stannp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stannp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stannp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.stannp.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.stannp.com/us/direct-mail-api/guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stannp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stannp-com-postcard-bulk-mailer
- group: other
  title: ''
  type: X
  url: https://twitter.com/stannpdm
- group: company
  title: ''
  type: Blog
  url: https://go.stannp.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stannp.com/us/pricing-tiers
- group: commercial
  title: ''
  type: Plans
  url: plans/stannp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stannp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stannp-finops.yml
created: '2026-06-12'
description: Stannp is a direct mail platform that enables businesses to send physical postcards and letters programmatically via a REST API. The platform lets developers create campaigns, upload recipient lists, trigger individual mail pieces in real time, and track print and delivery status through webhooks and event endpoints. Authentication uses API key-based HTTP Basic Auth over HTTPS, and the API follows a simple JSON response envelope with success/data or success/error fields. Stannp serves businesses across the UK, US, and Canada with per-item pricing for letters and postcards at scale, and supports no-code integrations through Zapier and Make as well as official SDKs for PHP, Go, and C#.
examples:
- key_count: 8
  name: Create Postcard Request
  slug: create-postcard-request
- key_count: 2
  name: Create Postcard Response
  slug: create-postcard-response
- key_count: 5
  name: Webhook Payload
  slug: webhook-payload
finops:
- name: Stannp Finops
  service_category: ''
  slug: stannp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stannp.png
json_schemas:
- name: Campaign
  property_count: 8
  slug: campaign
- name: Mailpiece
  property_count: 8
  slug: mailpiece
- name: Recipient
  property_count: 22
  slug: recipient
jsonld:
- class_count: 45
  name: Stannp Context
  property_count: 9
  slug: stannp-context
layout: provider
modified: '2026-06-12'
name: Stannp
nav: Providers
network: true
overview: 'Stannp publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Campaigns API, Events API, and 4 more. Tagged areas include Direct Mail, Postcards, Letters, Print, and Physical Mail.


  The Stannp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stannp''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Stannp Plans Pricing
  plan_count: 5
  slug: stannp-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 4
  name: Stannp Rate Limits
  slug: stannp-rate-limits
rules:
- name: Stannp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stannp-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 78.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stannp/refs/heads/main/screenshots/stannp-2026-06-20T194506.png
security:
- kind: authentication
  name: Stannp Authentication
  slug: stannp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stannp Domain Security
  slug: stannp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stannp Trust Center
  slug: stannp-trust-center
  summary_line: trust center published
slug: stannp
tags:
- Direct Mail
- Postcards
- Letters
- Print
- Physical Mail
- Marketing Automation
- Campaigns
website: https://www.stannp.com
---
