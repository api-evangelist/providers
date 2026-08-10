---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fullenrich Agentic Access
  operation_count: 7
  slug: fullenrich-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 3
apis:
- description: Workspace credit balance and API key checks.
  name: FullEnrich Account API
  slug: fullenrich-account-api
- description: Submit contacts for waterfall enrichment and retrieve results.
  name: FullEnrich Contact Enrichment API
  slug: fullenrich-contact-enrichment-api
- description: Resolve a person and company from an email address.
  name: FullEnrich Reverse Email Lookup API
  slug: fullenrich-reverse-email-lookup-api
artifact_total: 11
collections:
- collection_type: open
  name: FullEnrich API
  slug: open-fullenrich
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fullenrich-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fullenrich-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fullenrich-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fullenrich-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FullEnrich
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fullenrich
- group: company
  title: ''
  type: Website
  url: https://fullenrich.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fullenrich.com
- group: commercial
  title: ''
  type: Plans
  url: plans/fullenrich-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fullenrich-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fullenrich-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fullenrich.com/blog
created: '2026-07-01'
description: FullEnrich is a B2B contact enrichment platform that finds verified business emails and mobile phone numbers by running a waterfall across 15+ data vendors. Its API accepts contacts by name plus company (domain or company name) or LinkedIn URL, submits them for bulk enrichment, and returns the most probable work email, personal email, and mobile phone, billing credits only when data is found.
finops:
- name: Fullenrich Finops
  service_category: Data and Analytics
  slug: fullenrich-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fullenrich.png
layout: provider
modified: '2026-07-01'
name: FullEnrich
nav: Providers
network: true
overview: 'FullEnrich publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Contact Enrichment API, and Reverse Email Lookup API. Tagged areas include B2B Data, Contact Enrichment, Email Finder, Phone Finder, and Waterfall Enrichment.


  FullEnrich''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Fullenrich Plans Pricing
  plan_count: 5
  slug: fullenrich-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 3
  name: Fullenrich Rate Limits
  slug: fullenrich-rate-limits
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fullenrich/refs/heads/main/screenshots/fullenrich-2026-07-25T215257.png
security:
- kind: authentication
  name: Fullenrich Authentication
  slug: fullenrich-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fullenrich Domain Security
  slug: fullenrich-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fullenrich Trust Center
  slug: fullenrich-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: fullenrich
tags:
- B2B Data
- Contact Enrichment
- Email Finder
- Phone Finder
- Waterfall Enrichment
- Sales Intelligence
website: https://fullenrich.com
---
