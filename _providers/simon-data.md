---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Simon Data Agentic Access
  operation_count: 2
  slug: simon-data-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 4
apis:
- description: 'A premium API feature that fetches data from an external API at send time to enable dynamic, personalized content delivery across marketing channels. Powers real-time personalization at the moment of '
  name: Simon Data Real-Time Content API
  slug: simon-data-real-time-content-api
- description: Enables Simon Data to push customer segment and event data to external systems via webhooks. Supports payload specifications, best practices, and outbound integration authentication for downstream mar
  name: Simon Data Outbound Webhooks API
  slug: simon-data-outbound-webhooks-api
- description: The Contacts API from Simon Data — 1 operation(s) for contacts.
  name: Simon Data Contacts API
  slug: simon-data-contacts-api
- description: The Events API from Simon Data — 1 operation(s) for events.
  name: Simon Data Events API
  slug: simon-data-events-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simon-data-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/simon-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simon-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simon-data-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/simon-data-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.simon.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simondata.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Radico
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simon-data
- group: other
  title: ''
  type: X
  url: https://x.com/simon_data
- group: company
  title: ''
  type: Blog
  url: https://www.simon.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simon.ai/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.simondata.com/docs/operational-status
- group: commercial
  title: ''
  type: Plans
  url: plans/simon-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simon-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simon-data-finops.yml
created: '2026-06-13'
description: Simon Data is an AI-first customer data platform (CDP) that empowers marketing teams with faster, more precise segmentation and personalization. It provides a REST API for managing audiences, activating segments across channels, tracking events via the Simon Signal event collection API, and syncing customer data with downstream marketing tools including Salesforce, Klaviyo, Google Ads, and Facebook.
examples:
- key_count: 2
  name: Simon Data Get Contact Example
  slug: simon-data-get-contact-example
- key_count: 8
  name: Simon Data Identify Example
  slug: simon-data-identify-example
- key_count: 9
  name: Simon Data Track Transaction Example
  slug: simon-data-track-transaction-example
finops:
- name: Simon Data Finops
  service_category: ''
  slug: simon-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simon-data.png
json_schemas:
- name: Simon Data Contact
  property_count: 2
  slug: simon-data-contact
- name: Simon Data Event Payload
  property_count: 12
  slug: simon-data-event-payload
jsonld:
- class_count: 4
  name: Simon Data Context
  property_count: 40
  slug: simon-data-context
layout: provider
modified: '2026-06-13'
name: Simon Data
nav: Providers
network: true
overview: 'Simon Data publishes 2 APIs on the [APIs.io](https://apis.io/) network: Contacts API and Events API. Tagged areas include Customer Data Platform, CDP, Marketing Automation, Audience Segmentation, and Event Tracking.


  The Simon Data catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Simon Data''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Simon Data Plans Pricing
  plan_count: 1
  slug: simon-data-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 0
  name: Simon Data Rate Limits
  slug: simon-data-rate-limits
rules:
- name: Simon Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: simon-data-jsonschema-spectral-rules
scopes:
- name: Simon Data Scopes
  scope_count: 0
  slug: simon-data-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 69.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 52.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simon-data/refs/heads/main/screenshots/simon-data-2026-06-20T193927.png
security:
- kind: authentication
  name: Simon Data Authentication
  slug: simon-data-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Simon Data Domain Security
  slug: simon-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Simon Data Trust Center
  slug: simon-data-trust-center
  summary_line: SOC 2, GDPR
slug: simon-data
tags:
- Customer Data Platform
- CDP
- Marketing Automation
- Audience Segmentation
- Event Tracking
- Data Ingestion
- Personalization
- Marketing Technology
website: https://www.simon.ai/
---
