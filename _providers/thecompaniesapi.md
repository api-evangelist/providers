---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
- acting_count: 15
  human_in_the_loop: 0
  name: Thecompaniesapi Agentic Access
  operation_count: 44
  slug: thecompaniesapi-agentic-access
  summary_line: 44 operations · 15 acting
api_count: 12
apis:
- description: The actions API from The Companies API — 2 operation(s) for actions.
  name: The Companies API actions API
  slug: thecompaniesapi-actions-api
- description: The analytics API from The Companies API — 2 operation(s) for analytics.
  name: The Companies API analytics API
  slug: thecompaniesapi-analytics-api
- description: The companies API from The Companies API — 13 operation(s) for companies.
  name: The Companies API companies API
  slug: thecompaniesapi-companies-api
- description: The industries API from The Companies API — 2 operation(s) for industries.
  name: The Companies API industries API
  slug: thecompaniesapi-industries-api
- description: The job-titles API from The Companies API — 1 operation(s) for job-titles.
  name: The Companies API job-titles API
  slug: thecompaniesapi-job-titles-api
- description: The lists API from The Companies API — 5 operation(s) for lists.
  name: The Companies API lists API
  slug: thecompaniesapi-lists-api
- description: The locations API from The Companies API — 5 operation(s) for locations.
  name: The Companies API locations API
  slug: thecompaniesapi-locations-api
- description: The prompts API from The Companies API — 4 operation(s) for prompts.
  name: The Companies API prompts API
  slug: thecompaniesapi-prompts-api
- description: The teams API from The Companies API — 1 operation(s) for teams.
  name: The Companies API teams API
  slug: thecompaniesapi-teams-api
- description: The technologies API from The Companies API — 1 operation(s) for technologies.
  name: The Companies API technologies API
  slug: thecompaniesapi-technologies-api
- description: The users API from The Companies API — 1 operation(s) for users.
  name: The Companies API users API
  slug: thecompaniesapi-users-api
- description: The utilities API from The Companies API — 2 operation(s) for utilities.
  name: The Companies API utilities API
  slug: thecompaniesapi-utilities-api
artifact_total: 18
collections:
- collection_type: open
  name: The Companies API
  slug: open-thecompaniesapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thecompaniesapi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thecompaniesapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thecompaniesapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thecompaniesapi
- group: company
  title: ''
  type: Website
  url: https://www.thecompaniesapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.thecompaniesapi.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/thecompaniesapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thecompaniesapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thecompaniesapi-finops.yml
created: '2026-07-11'
description: The Companies API is a company data and enrichment platform offering programmatic access to firmographic, technographic, and web-intelligence data on 50M+ companies. Its REST API (base https://api.thecompaniesapi.com, all resources under /v2) covers company search and segmentation, company enrichment by domain, email, or social profile, similar-company lookup, industry and technology reference data, location reference data, saved lists, and asynchronous bulk actions. Requests are authenticated with an API token passed in the Authorization header, billing is credit-based, and the full OpenAPI 3.1 description is published at /v2/openapi.
finops:
- name: Thecompaniesapi Finops
  service_category: Data and Analytics
  slug: thecompaniesapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thecompaniesapi.png
layout: provider
modified: '2026-07-11'
name: The Companies API
nav: Providers
network: true
overview: 'The Companies API publishes 12 APIs on the [APIs.io](https://apis.io/) network, including actions API, analytics API, companies API, and 9 more. Tagged areas include Company Data, Data Enrichment, Firmographics, Web Intelligence, and B2B Data.


  The Companies API''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Thecompaniesapi Plans Pricing
  plan_count: 4
  slug: thecompaniesapi-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 5
  name: Thecompaniesapi Rate Limits
  slug: thecompaniesapi-rate-limits
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Thecompaniesapi Authentication
  slug: thecompaniesapi-authentication
  summary_line: http · 1 scheme
slug: thecompaniesapi
tags:
- Company Data
- Data Enrichment
- Firmographics
- Web Intelligence
- B2B Data
- Reference Data
- Company Search
website: https://www.thecompaniesapi.com
---
