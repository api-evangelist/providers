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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
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
artifact_total: 16
collections:
- collection_type: open
  name: People Data Labs API
  slug: open-people-data-labs
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
- group: auth
  title: ''
  type: TrustCenter
  url: security/peopledatalabs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peopledatalabs-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.peopledatalabs.com/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.peopledatalabs.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.peopledatalabs.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.peopledatalabs.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peopledatalabs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peopledatalabs.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://docs.peopledatalabs.com/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.peopledatalabs.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.peopledatalabs.com/llms.txt
created: '2026-07-11'
description: People Data Labs (PDL) is a B2B data enrichment and web intelligence provider offering a REST API over a dataset of nearly three billion person profiles and tens of millions of company records. The api.peopledatalabs.com/v5 API lets developers enrich, identify, and search person and company data, resolve contacts and firmographics, look up companies from a domain or LinkedIn URL, and clean and standardize job titles, skills, schools, companies, and locations. Authentication is a single X-Api-Key header, all endpoints are HTTPS REST, and PDL publishes an official OpenAPI specification.
finops:
- name: Peopledatalabs Finops
  service_category: Data and Analytics
  slug: peopledatalabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peopledatalabs.png
layout: provider
modified: '2026-08-08'
name: People Data Labs
nav: Providers
network: true
overview: 'People Data Labs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Cleaner Endpoints API, Company Endpoints API, and 4 more. Tagged areas include Data Enrichment, Web Intelligence, Person Data, Company Data, and B2B Data.


  People Data Labs'' developer surface includes authentication, documentation, engineering blog, developer portal, signup flow, pricing, support, and 14 more developer resources.'
plans:
- name: Peopledatalabs Plans Pricing
  plan_count: 4
  slug: peopledatalabs-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 7
  name: Peopledatalabs Rate Limits
  slug: peopledatalabs-rate-limits
score:
  band: developing
  composite: 53.0
  delta: 15.2
  facets:
    commercial_clarity: 92.1
    contract_quality: 53.6
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/peopledatalabs/refs/heads/main/screenshots/peopledatalabs-2026-06-20T191552.png
security:
- kind: authentication
  name: Peopledatalabs Authentication
  slug: peopledatalabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Peopledatalabs Domain Security
  slug: peopledatalabs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Peopledatalabs Trust Center
  slug: peopledatalabs-trust-center
  summary_line: SOC 2, ISO 27001, FIPS 140
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
