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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Openfigi Agentic Access
  operation_count: 4
  slug: openfigi-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: The Filter API from OpenFIGI — 1 operation(s) for filter.
  name: OpenFIGI Filter API
  slug: openfigi-filter-api
- description: The Mapping API from OpenFIGI — 2 operation(s) for mapping.
  name: OpenFIGI Mapping API
  slug: openfigi-mapping-api
- description: The Search API from OpenFIGI — 1 operation(s) for search.
  name: OpenFIGI Search API
  slug: openfigi-search-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFIGI Filter API
  slug: open-openfigi-filter-api
- collection_type: open
  name: OpenFIGI Filter Mapping API
  slug: open-openfigi-mapping-api
- collection_type: open
  name: OpenFIGI Filter Search API
  slug: open-openfigi-search-api
- collection_type: open
  name: OpenFIGI API
  slug: open-openfigi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openfigi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openfigi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openfigi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenFIGI
- group: company
  title: ''
  type: About
  url: https://www.openfigi.com/about
- group: company
  title: ''
  type: News
  url: https://www.openfigi.com/about/news
- group: start
  title: ''
  type: Login
  url: https://www.openfigi.com/user/login
- group: start
  title: ''
  type: Signup
  url: https://www.openfigi.com/user/signup
- group: operate
  title: ''
  type: Contact
  url: https://www.openfigi.com/feedback
- group: operate
  title: ''
  type: FAQ
  url: https://www.openfigi.com/docs/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.openfigi.com/about/news
created: 2024-09-27 00:00:00+00:00
description: OpenFIGI is your entry point to multiple tools for identifying, mapping and requesting a free Financial Instrument Global Identifier (FIGI). OpenFIGI is an open system for identifying instruments globally across all asset classes. Combining the FIGI with additional descriptive meta-data, firms are able to link fragmented proprietary symbologies, fill the gaps that remain to create a data lineage, streamline the trade workflow and reduce operational risk.
finops:
- name: Openfigi Finops
  service_category: API
  slug: openfigi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openfigi.png
layout: provider
modified: '2026-05-19'
name: OpenFIGI
nav: Providers
network: true
overview: 'OpenFIGI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Filter API, Mapping API, and Search API. Tagged areas include Financial and Instruments.


  OpenFIGI''s developer surface includes authentication, product news, signup flow, FAQ, engineering blog, and 6 more developer resources.'
plans:
- name: Openfigi Plans Pricing
  plan_count: 3
  slug: openfigi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Openfigi Rate Limits
  slug: openfigi-rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openfigi/refs/heads/main/screenshots/openfigi-2026-06-20T191005.png
security:
- kind: authentication
  name: Openfigi Authentication
  slug: openfigi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openfigi Domain Security
  slug: openfigi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openfigi
tags:
- Financial
- Instruments
---
