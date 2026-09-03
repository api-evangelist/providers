---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: The WPL API Plugin is a RESTful HTTP/JSON interface for the Realtyna WPL WordPress platform. It supports user account registration and management, authentication, retrieving active listing types, load
  name: Realtyna WPL API Plugin
  slug: wpl-api
- description: MLS Router API is an enterprise solution that aggregates and routes data across multiple MLS feeds, providing a single integration point for accessing normalized MLS listing data through a RESO-compli
  name: Realtyna MLS Router API
  slug: mls-router-api
- description: Organic RESO API provides standards-based access to real estate listing data using the RESO Web API specification, enabling developers to build applications consuming MLS data through a RESO-compliant
  name: Realtyna Organic RESO API
  slug: organic-reso-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realtyna-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://realtyna.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/realtyna
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/realtyna
- group: company
  title: ''
  type: Website
  url: https://realtyna.com
- group: docs
  title: ''
  type: Documentation
  url: https://realtyna.com/api
- group: agent
  title: ''
  type: LlmsText
  url: https://realtyna.com/llms.txt
created: '2026-03-16'
description: Realtyna provides real estate technology including IDX, RESO Web API integrations, MLS data routing, and a WordPress-based property platform (WPL). Their API Plugin exposes the WPL platform via a RESTful, JSON-based HTTP interface for building custom front-ends and mobile applications. Realtyna also offers MLS API, Organic RESO API, and the MLS Router API for enterprise MLS integration.
finops:
- name: Realtyna Finops
  service_category: API
  slug: realtyna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realtyna.png
layout: provider
modified: '2026-04-28'
name: Realtyna
nav: Providers
network: true
overview: 'Realtyna publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, MLS, IDX, RESO, and WordPress.


  Realtyna''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
plans:
- name: Realtyna Plans Pricing
  plan_count: 3
  slug: realtyna-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Realtyna Rate Limits
  slug: realtyna-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/realtyna/refs/heads/main/screenshots/realtyna-2026-06-20T192659.png
security:
- kind: domain-security
  name: Realtyna Domain Security
  slug: realtyna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: realtyna
tags:
- Real-Estate
- MLS
- IDX
- RESO
- WordPress
website: https://realtyna.com
---
