---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dpla Agentic Access
  operation_count: 8
  slug: dpla-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 5
apis:
- description: Self-service API key registration endpoint that issues free access keys via email. Developers submit their email address via HTTP POST and receive an API key by email. The key is then passed as the ap
  name: DPLA API Key Registration
  slug: api-key-registration
- description: API key registration and management
  name: Digital Public Library of America Authentication API
  slug: dpla-authentication-api
- description: Search and retrieve cultural heritage item metadata records
  name: Digital Public Library of America Items API
  slug: dpla-items-api
- description: Search and retrieve primary source sets (PSS) for education
  name: Digital Public Library of America Primary Source Sets API
  slug: dpla-primary-source-sets-api
- description: Utility endpoints for health checks and random item retrieval
  name: Digital Public Library of America Utilities API
  slug: dpla-utilities-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Digital Public Library of America (DPLA) Authentication API
  slug: open-dpla-authentication-api
- collection_type: open
  name: Digital Public Library of America (DPLA) Authentication Items API
  slug: open-dpla-items-api
- collection_type: open
  name: Digital Public Library of America (DPLA) Authentication Primary Source Sets API
  slug: open-dpla-primary-source-sets-api
- collection_type: open
  name: Digital Public Library of America (DPLA) Authentication Utilities API
  slug: open-dpla-utilities-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/dpla/api/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dpla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dpla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dpla-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://dp.la/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pro.dp.la/developers
- group: docs
  title: ''
  type: Documentation
  url: https://pro.dp.la/developers/api-codex
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dpla
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dpla/api
- group: company
  title: ''
  type: Blog
  url: https://dp.la/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digital-public-library-of-america
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/dpla
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/dpla/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/dpla/refs/heads/main/plans/plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/dpla/refs/heads/main/finops/finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/dpla/refs/heads/main/json-ld/context.jsonld
created: '2026-06-13'
description: The Digital Public Library of America (DPLA) provides a free REST API that gives access to metadata for 50 million+ cultural heritage items aggregated from 4,000+ US libraries, archives, and museums. The API supports full-text search, field-specific queries, geographic and date range filtering, faceted browsing, and JSONP callbacks. All results are returned as JSON-LD. API keys are issued free of charge via a self-service email-based registration endpoint. DPLA aggregates contributions from cultural heritage institutions across the United States and makes the combined metadata freely available to researchers, developers, and the public.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dpla.png
jsonld:
- class_count: 47
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-06-13'
name: Digital Public Library of America
nav: Providers
network: true
overview: 'Digital Public Library of America publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Items API, Primary Source Sets API, and 1 more. Tagged areas include Cultural Heritage, Libraries, Archives, Museums, and Open Data.


  The Digital Public Library of America catalog on APIs.io includes 1 JSON-LD context.


  Digital Public Library of America''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 119
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Dpla Authentication
  slug: dpla-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Dpla Domain Security
  slug: dpla-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dpla
tags:
- Cultural Heritage
- Libraries
- Archives
- Museums
- Open Data
- Metadata
- Digital Collections
- Public Domain
website: https://dp.la/
---
