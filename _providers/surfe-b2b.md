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
- acting_count: 7
  human_in_the_loop: 0
  name: Surfe B2B Agentic Access
  operation_count: 10
  slug: surfe-b2b-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 4
apis:
- description: Credit balance and account utilities.
  name: Surfe Account API
  slug: surfe-b2b-account-api
- description: Search and enrich organizations.
  name: Surfe Companies API
  slug: surfe-b2b-companies-api
- description: Search and enrich individual contacts.
  name: Surfe People API
  slug: surfe-b2b-people-api
- description: ICP definition and lookalike account recommendations.
  name: Surfe Recommendations API
  slug: surfe-b2b-recommendations-api
artifact_total: 11
collections:
- collection_type: open
  name: Surfe API
  slug: open-surfe-b2b
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/surfe-b2b-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surfe-b2b-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/surfe-b2b-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/surfe
- group: company
  title: ''
  type: Website
  url: https://surfe.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.surfe.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/surfe-b2b-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/surfe-b2b-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/surfe-b2b-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.surfe.com/blog/feed/
created: '2026-07-11'
description: Surfe (formerly Leadjet) is a B2B contact-discovery and data-enrichment platform whose REST API turns partial signals - a LinkedIn URL, a name plus a company, a domain, or an email - into verified professional email addresses, mobile phone numbers, company firmographics, and lookalike account recommendations. It is the web-intelligence and contact-discovery layer that sits behind Surfe's LinkedIn and CRM experiences, exposed to developers under https://api.surfe.com/v2 with Bearer API-key auth and a credit-based model. Bulk people and company enrichment run as asynchronous jobs (start with POST, then poll the GET job endpoint or receive a webhook callback). This entry focuses on the contact-discovery, data-enrichment, and B2B/sales-intelligence use cases (people search, people enrichment, company search, company enrichment).
finops:
- name: Surfe B2B Finops
  service_category: Data and Analytics
  slug: surfe-b2b-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surfe-b2b.png
layout: provider
modified: '2026-07-11'
name: Surfe
nav: Providers
network: true
overview: 'Surfe publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Companies API, People API, and 1 more. Tagged areas include Contact Discovery, Data Enrichment, B2B Data, Sales Intelligence, and Lead Enrichment.


  Surfe''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Surfe B2B Plans Pricing
  plan_count: 4
  slug: surfe-b2b-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Surfe B2B Rate Limits
  slug: surfe-b2b-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Surfe B2B Authentication
  slug: surfe-b2b-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Surfe B2B Domain Security
  slug: surfe-b2b-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: surfe-b2b
tags:
- Contact Discovery
- Data Enrichment
- B2B Data
- Sales Intelligence
- Lead Enrichment
- Web Intelligence
- Contact Data
- People Enrichment
- Company Enrichment
- Prospecting
website: https://surfe.com
---
