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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Uplead Agentic Access
  operation_count: 21
  slug: uplead-agentic-access
  summary_line: 21 operations · 11 acting
api_count: 8
apis:
- description: Account and credit management.
  name: UpLead Account API
  slug: uplead-account-api
- description: Combined person and company lookup.
  name: UpLead Combined API
  slug: uplead-combined-api
- description: Company search and enrichment operations.
  name: UpLead Company API
  slug: uplead-company-api
- description: Contact list management operations.
  name: UpLead Lists API
  slug: uplead-lists-api
- description: Person/contact search and enrichment operations.
  name: UpLead Person API
  slug: uplead-person-api
- description: Prospector search operations for discovering contacts.
  name: UpLead Prospector API
  slug: uplead-prospector-api
- description: Reference data lookups.
  name: UpLead Reference API
  slug: uplead-reference-api
- description: General search operations.
  name: UpLead Search API
  slug: uplead-search-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uplead-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uplead-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uplead-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uplead.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uplead.com/
- group: company
  title: ''
  type: Blog
  url: https://www.uplead.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uplead.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uplead.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uplead-com/
- group: other
  title: ''
  type: X
  url: https://x.com/UpLeadHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/uplead-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uplead-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uplead-finops.yml
created: '2026-06-13'
description: UpLead is a B2B contact and company data platform providing a REST API for searching leads, verifying emails, accessing company profiles, and enriching contact information. The API enables developers to look up verified contacts by email or name, search companies by domain or name, run prospector queries to find contacts by job title or function, and perform combined person-plus-company lookups in a single call. UpLead operates on a credit-based billing model where charges only apply when verified data is returned.
examples:
- key_count: 2
  name: Company Search Response
  slug: company-search-response
- key_count: 2
  name: Credits Response
  slug: credits-response
- key_count: 2
  name: Person Search Response
  slug: person-search-response
- key_count: 7
  name: Prospector Search Request
  slug: prospector-search-request
- key_count: 3
  name: Prospector Search Response
  slug: prospector-search-response
finops:
- name: Uplead Finops
  service_category: ''
  slug: uplead-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uplead.png
json_schemas:
- name: UpLead Company
  property_count: 32
  slug: company
- name: UpLead Contact List
  property_count: 3
  slug: list
- name: UpLead Person
  property_count: 20
  slug: person
jsonld:
- class_count: 42
  name: Uplead Context
  property_count: 13
  slug: uplead-context
layout: provider
modified: '2026-06-13'
name: UpLead
nav: Providers
network: true
overview: 'UpLead publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Combined API, Company API, and 5 more. Tagged areas include B2B, Lead Generation, Contact Data, Company Data, and Email Verification.


  The UpLead catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UpLead''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Uplead Plans Pricing
  plan_count: 6
  slug: uplead-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 1
  name: Uplead Rate Limits
  slug: uplead-rate-limits
rules:
- name: UpLead API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uplead-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.5
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uplead/refs/heads/main/screenshots/uplead-2026-06-20T200445.png
security:
- kind: authentication
  name: Uplead Authentication
  slug: uplead-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uplead Domain Security
  slug: uplead-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uplead
tags:
- B2B
- Lead Generation
- Contact Data
- Company Data
- Email Verification
- Data Enrichment
- Sales Intelligence
website: https://www.uplead.com/
---
