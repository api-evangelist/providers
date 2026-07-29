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
- acting_count: 5
  human_in_the_loop: 0
  name: 6Sense Agentic Access
  operation_count: 7
  slug: 6sense-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 3
apis:
- description: The Company API from 6sense — 1 operation(s) for company.
  name: 6sense Company API
  slug: 6sense-company-api
- description: The Enrichment API from 6sense — 2 operation(s) for enrichment.
  name: 6sense Enrichment API
  slug: 6sense-enrichment-api
- description: The People API from 6sense — 4 operation(s) for people.
  name: 6sense People API
  slug: 6sense-people-api
artifact_total: 22
collections:
- collection_type: open
  name: 6sense Company Firmographics API
  slug: open-6sense-company-firmographics-api
- collection_type: open
  name: 6sense Company Identification API
  slug: open-6sense-company-identification-api
- collection_type: open
  name: 6sense Lead Scoring API
  slug: open-6sense-lead-scoring-api
- collection_type: open
  name: 6sense Lead Scoring And Firmographics API
  slug: open-6sense-lead-scoring-firmographics-api
- collection_type: open
  name: 6sense People Enrichment API
  slug: open-6sense-people-enrichment-api
- collection_type: open
  name: 6sense People Search API
  slug: open-6sense-people-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/6sense-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/6sense-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/6sense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/6sense-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://6sense.com
- group: docs
  title: ''
  type: Documentation
  url: https://6sense.com/platform
- group: start
  title: ''
  type: Portal
  url: https://api.6sense.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://support.6sense.com/docs/6sense-api-overview
- group: operate
  title: ''
  type: Support
  url: https://support.6sense.com
- group: other
  title: ''
  type: CaseStudies
  url: https://6sense.com/customers
- group: company
  title: ''
  type: Blog
  url: https://6sense.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/6sense
- group: build
  title: ''
  type: Github
  url: https://github.com/6si
- group: commercial
  title: ''
  type: Pricing
  url: https://6sense.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/6sense-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/6sense-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/6sense-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/6sense-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/6sense-context.jsonld
finops:
- name: 6Sense Finops
  service_category: Sales and Marketing Technology
  slug: 6sense-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the 6sense Revenue AI Platform, covering account-based marketing (ABM), intent data, predictive scoring, firmographic and technographic enrichme
  name: 6sense GraphQL Schema
  slug: 6sense-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/6sense.png
json_schemas:
- name: 6sense Company
  property_count: 20
  slug: 6sense-company
- name: 6sense Enriched Contact
  property_count: 17
  slug: 6sense-contact
- name: 6sense Product Score
  property_count: 10
  slug: 6sense-score
jsonld:
- class_count: 0
  name: 6Sense Context
  property_count: 4
  slug: 6sense-context
layout: provider
name: 6sense
nav: Providers
network: true
overview: '6sense publishes 3 APIs on the [APIs.io](https://apis.io/) network: Company API, Enrichment API, and People API. Tagged areas include ABM, Account-Based Marketing, Intent Data, B2B, and Predictive Analytics.


  The 6sense catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  6sense''s developer surface includes authentication, documentation, developer portal, support, engineering blog, GitHub presence, pricing, and 12 more developer resources.'
plans:
- name: 6Sense Plans Pricing
  plan_count: 4
  slug: 6sense-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 6
  name: 6Sense Rate Limits
  slug: 6sense-rate-limits
rules:
- name: 6sense API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: 6sense-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.4
  delta: -2.8
  facets:
    commercial_clarity: 57.9
    contract_quality: 75.7
    developer_ergonomics: 34.8
    discoverability: 55.6
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/6sense/refs/heads/main/screenshots/6sense-2026-06-20T162740.png
security:
- kind: authentication
  name: 6Sense Authentication
  slug: 6sense-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 6Sense Domain Security
  slug: 6sense-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: 6Sense Trust Center
  slug: 6sense-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: 6sense
tags:
- ABM
- Account-Based Marketing
- Intent Data
- B2B
- Predictive Analytics
- Revenue
- Sales Intelligence
- AI
- Marketing Technology
website: https://6sense.com
---
