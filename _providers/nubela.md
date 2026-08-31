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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nubela Agentic Access
  operation_count: 11
  slug: nubela-agentic-access
  summary_line: 11 operations
api_count: 4
apis:
- description: The Company API from Nubela — 6 operation(s) for company.
  name: Nubela Company API
  slug: nubela-company-api
- description: The Competitor API from Nubela — 1 operation(s) for competitor.
  name: Nubela Competitor API
  slug: nubela-competitor-api
- description: The Customer API from Nubela — 1 operation(s) for customer.
  name: Nubela Customer API
  slug: nubela-customer-api
- description: The Employee API from Nubela — 3 operation(s) for employee.
  name: Nubela Employee API
  slug: nubela-employee-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nubela Proxycurl Company API
  slug: open-nubela-company-api
- collection_type: open
  name: Nubela Proxycurl Company Competitor API
  slug: open-nubela-competitor-api
- collection_type: open
  name: Nubela Proxycurl Company Customer API
  slug: open-nubela-customer-api
- collection_type: open
  name: Nubela Proxycurl Company Employee API
  slug: open-nubela-employee-api
- collection_type: open
  name: Nubela Proxycurl API
  slug: open-nubela
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nubela-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nubela-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nubela-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nubela
- group: company
  title: ''
  type: Website
  url: https://nubela.co/proxycurl/
- group: docs
  title: ''
  type: Documentation
  url: https://nubela.co/proxycurl/docs
- group: agent
  title: ''
  type: LlmsText
  url: https://nubela.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://nubela.co/blog/feed
created: '2025-02-08'
description: Build and scale data-driven applications on people and companies with Nubela's Proxycurl API without worrying about scaling a web scraping and data-science team.
finops:
- name: Nubela Finops
  service_category: API
  slug: nubela-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nubela.png
layout: provider
modified: '2026-05-19'
name: Nubela
nav: Providers
network: true
overview: 'Nubela publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Company API, Competitor API, Customer API, and 1 more. Tagged areas include Companies, Data, People, and Scraping.


  Nubela''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Nubela Plans Pricing
  plan_count: 3
  slug: nubela-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Nubela Rate Limits
  slug: nubela-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 23.8
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nubela/refs/heads/main/screenshots/nubela-2026-06-20T190506.png
security:
- kind: authentication
  name: Nubela Authentication
  slug: nubela-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nubela Domain Security
  slug: nubela-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nubela
tags:
- Companies
- Data
- People
- Scraping
website: https://nubela.co/proxycurl/
---
