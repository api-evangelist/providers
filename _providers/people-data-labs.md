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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: People Data Labs Agentic Access
  operation_count: 9
  slug: people-data-labs-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 5
apis:
- description: Autocomplete suggestions for fields like skills and titles.
  name: People Data Labs Autocomplete API
  slug: people-data-labs-autocomplete-api
- description: Company enrichment and search operations.
  name: People Data Labs Company API
  slug: people-data-labs-company-api
- description: IP-based enrichment operations.
  name: People Data Labs IP API
  slug: people-data-labs-ip-api
- description: Job posting search operations.
  name: People Data Labs Jobs API
  slug: people-data-labs-jobs-api
- description: Person enrichment, search, and identification operations.
  name: People Data Labs Person API
  slug: people-data-labs-person-api
artifact_total: 13
collections:
- collection_type: open
  name: People Data Labs API
  slug: open-people-data-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/people-data-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/people-data-labs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/people-data-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/people-data-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peopledatalabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peopledatalabs
- group: start
  title: ''
  type: Portal
  url: https://www.peopledatalabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.peopledatalabs.com/
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
- group: company
  title: ''
  type: Website
  url: https://www.peopledatalabs.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.peopledatalabs.com/llms.txt
created: '2026-03-16'
description: People Data Labs provides a people data API for enriching and building people profiles at scale. The API provides access to professional profiles, company data, and identity resolution for B2B applications.
finops:
- name: People Data Labs Finops
  service_category: API
  slug: people-data-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/people-data-labs.png
layout: provider
modified: '2026-05-19'
name: People Data Labs
nav: Providers
network: true
overview: 'People Data Labs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Company API, IP API, and 2 more. Tagged areas include B2B, Identity Resolution, and People Data.


  People Data Labs'' developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, and 11 more developer resources.'
plans:
- name: People Data Labs Plans Pricing
  plan_count: 3
  slug: people-data-labs-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: People Data Labs Rate Limits
  slug: people-data-labs-rate-limits
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 51.3
    developer_ergonomics: 32.6
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/people-data-labs/refs/heads/main/screenshots/people-data-labs-2026-06-20T191552.png
security:
- kind: authentication
  name: People Data Labs Authentication
  slug: people-data-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: People Data Labs Domain Security
  slug: people-data-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: People Data Labs Trust Center
  slug: people-data-labs-trust-center
  summary_line: SOC 2, ISO 27001, FIPS 140
slug: people-data-labs
tags:
- B2B
- Identity Resolution
- People Data
website: https://www.peopledatalabs.com/
---
