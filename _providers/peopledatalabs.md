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
- acting_count: 8
  human_in_the_loop: 0
  name: Peopledatalabs Agentic Access
  operation_count: 21
  slug: peopledatalabs-agentic-access
  summary_line: 21 operations · 8 acting
api_count: 7
apis:
- description: The Autocomplete API from People Data Labs — 1 operation(s) for autocomplete.
  name: People Data Labs Autocomplete API
  slug: peopledatalabs-autocomplete-api
- description: The Cleaner Endpoints API from People Data Labs — 3 operation(s) for cleaner endpoints.
  name: People Data Labs Cleaner Endpoints API
  slug: peopledatalabs-cleaner-endpoints-api
- description: The Company Endpoints API from People Data Labs — 2 operation(s) for company endpoints.
  name: People Data Labs Company Endpoints API
  slug: peopledatalabs-company-endpoints-api
- description: The IP Enrichment API from People Data Labs — 1 operation(s) for ip enrichment.
  name: People Data Labs IP Enrichment API
  slug: peopledatalabs-ip-enrichment-api
- description: The Job Title Enrichment API from People Data Labs — 1 operation(s) for job title enrichment.
  name: People Data Labs Job Title Enrichment API
  slug: peopledatalabs-job-title-enrichment-api
- description: The Person Endpoints API from People Data Labs — 5 operation(s) for person endpoints.
  name: People Data Labs Person Endpoints API
  slug: peopledatalabs-person-endpoints-api
- description: The Skill Enrichment API from People Data Labs — 1 operation(s) for skill enrichment.
  name: People Data Labs Skill Enrichment API
  slug: peopledatalabs-skill-enrichment-api
artifact_total: 13
collections:
- collection_type: open
  name: People Data Labs API
  slug: open-peopledatalabs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/peopledatalabs-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/peopledatalabs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peopledatalabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/people-data-labs
- group: company
  title: ''
  type: Website
  url: https://www.peopledatalabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.peopledatalabs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/peopledatalabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/peopledatalabs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/peopledatalabs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.peopledatalabs.com/blog
created: '2026-07-11'
description: People Data Labs (PDL) is a B2B data enrichment and web intelligence provider offering a REST API over a dataset of nearly three billion person profiles and tens of millions of company records. The api.peopledatalabs.com/v5 API lets developers enrich, identify, and search person and company data, resolve contacts and firmographics, look up companies from a domain or LinkedIn URL, and clean and standardize job titles, skills, schools, companies, and locations. Authentication is a single X-Api-Key header, all endpoints are HTTPS REST, and PDL publishes an official OpenAPI specification.
finops:
- name: Peopledatalabs Finops
  service_category: Data and Analytics
  slug: peopledatalabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peopledatalabs.png
layout: provider
modified: '2026-07-11'
name: People Data Labs
nav: Providers
network: true
overview: 'People Data Labs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Cleaner Endpoints API, Company Endpoints API, and 4 more. Tagged areas include Data Enrichment, Web Intelligence, Person Data, Company Data, and B2B Data.


  People Data Labs'' developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Peopledatalabs Plans Pricing
  plan_count: 4
  slug: peopledatalabs-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 7
  name: Peopledatalabs Rate Limits
  slug: peopledatalabs-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.9
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
security:
- kind: authentication
  name: Peopledatalabs Authentication
  slug: peopledatalabs-authentication
  summary_line: apiKey · 1 scheme
slug: peopledatalabs
tags:
- Data Enrichment
- Web Intelligence
- Person Data
- Company Data
- B2B Data
- Contact Discovery
- Reference Data
- Firmographics
- Identity Resolution
website: https://www.peopledatalabs.com
---
