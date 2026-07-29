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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Enrich So Agentic Access
  operation_count: 17
  slug: enrich-so-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 7
apis:
- description: Credit balance and transaction history.
  name: Enrich Account API
  slug: enrich-so-account-api
- description: IP-to-company resolution and LinkedIn company-follower scraping.
  name: Enrich Company Intelligence API
  slug: enrich-so-company-intelligence-api
- description: Find a professional email from a name and company domain.
  name: Enrich Email Finder API
  slug: enrich-so-email-finder-api
- description: Validate email addresses for deliverability.
  name: Enrich Email Verification API
  slug: enrich-so-email-verification-api
- description: Search and reveal leads across people and organizations.
  name: Enrich Lead Finder API
  slug: enrich-so-lead-finder-api
- description: Reverse email lookup returning a person's professional profile.
  name: Enrich Person Enrichment API
  slug: enrich-so-person-enrichment-api
- description: Find phone and mobile numbers for a person.
  name: Enrich Phone Finder API
  slug: enrich-so-phone-finder-api
artifact_total: 13
collections:
- collection_type: open
  name: Enrich API
  slug: open-enrich-so
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/enrich-so-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enrich-so-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enrich-so
- group: company
  title: ''
  type: Website
  url: https://www.enrich.so
- group: docs
  title: ''
  type: Documentation
  url: https://doc.enrich.so/introduction-1951028m0
- group: commercial
  title: ''
  type: Plans
  url: plans/enrich-so-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enrich-so-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/enrich-so-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.enrich.so/blog
created: '2026-07-11'
description: Enrich (enrich.so) is a person and company data enrichment API for B2B go-to-market, sales, and web intelligence teams. From a single REST interface it resolves a professional profile from an email address (reverse email lookup), finds and verifies professional email addresses, finds mobile and phone numbers, resolves a company and geolocation from an IP address, scrapes LinkedIn company followers, and searches a lead-finder database of people and organizations for contact discovery and lead enrichment. All endpoints share one base URL and are metered with a prepaid credit balance; unsuccessful ("not found") lookups are refunded.
finops:
- name: Enrich So Finops
  service_category: Data Enrichment and Intelligence
  slug: enrich-so-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enrich-so.png
layout: provider
modified: '2026-07-11'
name: Enrich
nav: Providers
network: true
overview: 'Enrich publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Company Intelligence API, Email Finder API, and 4 more. Tagged areas include Data Enrichment, Contact Discovery, Web Intelligence, B2B Data, and Lead Enrichment.


  Enrich''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Enrich So Plans Pricing
  plan_count: 5
  slug: enrich-so-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 12
  name: Enrich So Rate Limits
  slug: enrich-so-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/enrich-so/refs/heads/main/screenshots/enrich-so-2026-07-25T213424.png
security:
- kind: authentication
  name: Enrich So Authentication
  slug: enrich-so-authentication
  summary_line: apiKey/http · 2 schemes
slug: enrich-so
tags:
- Data Enrichment
- Contact Discovery
- Web Intelligence
- B2B Data
- Lead Enrichment
- Email Finder
- Email Verification
- Phone Numbers
- LinkedIn
- Reference Data
website: https://www.enrich.so
---
