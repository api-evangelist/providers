---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Snov Io Agentic Access
  operation_count: 65
  slug: snov-io-agentic-access
  summary_line: 65 operations · 32 acting
api_count: 16
apis:
- description: Verify the deliverability and validity of up to 10 email addresses per request using a two-step async API. Returns validity status, MX record checks, and disposable email detection results.
  name: Snov.io Email Verification API
  slug: snovio-email-verification-api
- description: Create, update, delete, and manage multi-channel outreach campaigns programmatically. Supports email step content management, recipient management, campaign state changes, and full analytics reporting
  name: Snov.io Campaigns API
  slug: snovio-campaigns-api
- description: Add, search, and manage prospect records and lists within Snov.io. Supports custom fields, list creation, CRM pipeline management, and do-not-email suppression list operations.
  name: Snov.io Prospect Management API
  slug: snovio-prospect-management-api
- description: Create and manage email warm-up campaigns to improve deliverability scores. Supports full CRUD operations on warm-up campaigns and provides statistical reporting on warm-up progress.
  name: Snov.io Email Warm-up API
  slug: snovio-email-warm-up-api
- description: Subscribe to real-time event notifications from the Snov.io platform. Supports listing, creating, updating, and deleting webhook subscriptions for automated event-driven integrations.
  name: Snov.io Webhooks API
  slug: snovio-webhooks-api
- description: OAuth 2.0 token management
  name: Snov.io Authentication API
  slug: snov-io-authentication-api
- description: Create and manage multi-channel outreach campaigns
  name: Snov.io Campaigns API
  slug: snov-io-campaigns-api
- description: CRM pipeline and stage management
  name: Snov.io CRM Pipeline API
  slug: snov-io-crm-pipeline-api
- description: Search for company information and email addresses by domain
  name: Snov.io Domain Search API
  slug: snov-io-domain-search-api
- description: Manage sender email accounts
  name: Snov.io Email Accounts API
  slug: snov-io-email-accounts-api
- description: Find email addresses by name, LinkedIn, or domain
  name: Snov.io Email Finder API
  slug: snov-io-email-finder-api
- description: Verify email deliverability and validity
  name: Snov.io Email Verification API
  slug: snov-io-email-verification-api
- description: Manage email warm-up campaigns for improved deliverability
  name: Snov.io Email Warm-up API
  slug: snov-io-email-warm-up-api
- description: Manage prospect records and lists
  name: Snov.io Prospects API
  slug: snov-io-prospects-api
- description: User account management
  name: Snov.io User API
  slug: snov-io-user-api
- description: Real-time event webhook subscriptions
  name: Snov.io Webhooks API
  slug: snov-io-webhooks-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snov-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snov-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snov-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://snov.io/
- group: docs
  title: ''
  type: Documentation
  url: https://snov.io/api
- group: other
  title: ''
  type: Knowledgebase
  url: https://snov.io/knowledgebase/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snovio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snovio
- group: company
  title: ''
  type: Blog
  url: https://snov.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://snov.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/snov_io
- group: auth
  title: ''
  type: Authentication
  url: https://snov.io/knowledgebase/how-to-use-snov-io-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/snov-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snov-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/snov-io-finops.yml
created: '2026-06-12'
description: Snov.io is a sales automation and lead generation platform serving over 300,000 companies across 180+ countries. The platform provides a REST API enabling developers to programmatically access email finding, domain search, email verification, drip campaign management, and LinkedIn prospect automation. Authentication uses OAuth 2.0 client credentials to obtain short-lived Bearer tokens, and all API operations consume credits from the account balance. The API covers the full sales outreach lifecycle from prospect discovery and contact enrichment through multi-channel campaign execution and CRM pipeline management.
finops:
- name: Snov Io Finops
  service_category: ''
  slug: snov-io-finops
graphqls:
- description: Snov.io is a sales automation and lead generation platform serving over 300,000 companies across 180+ countries. Its REST API covers the full outreach lifecycle — prospect discovery, email finding, em
  name: Snov.io GraphQL Schema
  slug: snov-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snov-io.png
jsonld:
- class_count: 11
  name: Snov Io Context
  property_count: 28
  slug: snov-io-context
layout: provider
modified: '2026-06-12'
name: Snov.io
nav: Providers
network: true
overview: 'Snov.io publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Campaigns API, CRM Pipeline API, and 8 more. Tagged areas include Sales Automation, Email Finder, Email Verification, Lead Generation, and Drip Campaigns.


  The Snov.io catalog on APIs.io includes 1 JSON-LD context.


  Snov.io''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Snov Io Plans Pricing
  plan_count: 7
  slug: snov-io-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 3
  name: Snov Io Rate Limits
  slug: snov-io-rate-limits
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 74.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snov-io/refs/heads/main/screenshots/snov-io-2026-06-20T194107.png
security:
- kind: authentication
  name: Snov Io Authentication
  slug: snov-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Snov Io Domain Security
  slug: snov-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snov-io
tags:
- Sales Automation
- Email Finder
- Email Verification
- Lead Generation
- Drip Campaigns
- CRM
- LinkedIn Automation
- Prospect Management
- Data Enrichment
- Cold Email
website: https://snov.io/
---
