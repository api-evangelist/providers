---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SkySpark is a native Project Haystack server. External applications integrate through the Haystack HTTP REST API, exposing operations such as about, read, hisRead, hisWrite, pointWrite, watchSub, watc
  name: SkySpark REST API (Project Haystack)
  slug: skyspark-rest-api-project-haystack
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/skyfoundry/conventions/skyfoundry-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/skyfoundry-conventions.yml
- group: other
  href: https://artifacts.apis.io/skyfoundry/hosts/skyfoundry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skyfoundry-hosts.yml
- group: build
  href: https://artifacts.apis.io/skyfoundry/integrations/skyfoundry-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/skyfoundry-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/skyfoundry/vendors/skyfoundry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skyfoundry-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://skyfoundry.com
- group: docs
  title: ''
  type: Documentation
  url: https://skyfoundry.com/product
- group: docs
  title: ''
  type: APIReference
  url: https://project-haystack.org/doc/docHaystack/HttpApi
- group: company
  title: ''
  type: Blog
  url: https://skyfoundry.com/blog
- group: start
  title: ''
  type: Login
  url: https://skyfoundry.com/user/login
- group: commercial
  title: ''
  type: Pricing
  url: https://skyfoundry.com/buy
- group: operate
  title: ''
  type: Support
  url: https://skyfoundry.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skyfoundry.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skyfoundry
- group: auth
  href: https://artifacts.apis.io/skyfoundry/authentication/skyfoundry-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skyfoundry-authentication.yml
- group: design
  href: https://artifacts.apis.io/skyfoundry/conventions/skyfoundry-conventions.yml
  title: ''
  type: Conventions
  url: conventions/skyfoundry-conventions.yml
- group: auth
  href: https://artifacts.apis.io/skyfoundry/security/skyfoundry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skyfoundry-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/skyfoundry/well-known/skyfoundry-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skyfoundry-well-known.yml
coverage:
  checked: '2026-10-20'
  detail: SkySpark is self-hosted per customer with no public API host, and SkyFoundry's own product documentation at skyfoundry.com/doc (and its forum) redirects to a customer login page; only the generic Project Haystack HTTP API spec is public.
  evidence:
  - status: 200
    url: https://skyfoundry.com/doc
  - status: 200
    url: https://skyfoundry.com/buy
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'SkyFoundry, founded in 2009 and headquartered in Glen Allen, Virginia, develops SkySpark, an analytics and informatics platform that connects, stores, analyzes, and visualizes data from smart devices, automation and control systems, meters, and sensors to "find what matters" in large equipment and facility datasets. SkySpark automatically detects issues, patterns, deviations, faults, and cost-reduction opportunities across intelligent buildings, industrial, agriculture, energy, government, and healthcare facilities, and has been applied to over 15,000 buildings spanning more than a billion square feet. SkySpark is a native Project Haystack server: external applications integrate through the Haystack HTTP REST API (ops such as read, hisRead, hisWrite, pointWrite, watchSub/watchPoll, eval, commit, and nav) with Zinc, JSON, Trio, and CSV data formats, and authenticate using the Haystack SCRAM (SHA-256) handshake with bearer authTokens. The company sells through a network of 140+
  OEM, systems-integrator, and value-added-distributor channel partners rather than a self-service public SaaS.'
image: https://skyfoundry.com/file/17/SkyFoundry-Logo.png
layout: provider
modified: '2026-07-21'
name: SkyFoundry
nav: Providers
network: true
overview: 'SkyFoundry is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Building Analytics, IoT, Energy Management, and Fault Detection.


  SkyFoundry''s developer surface includes documentation, API reference, engineering blog, pricing, support, authentication, and 11 more developer resources.'
plans:
- name: Skyfoundry Plans Pricing
  plan_count: 0
  slug: skyfoundry-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Skyfoundry Rate Limits
  slug: skyfoundry-rate-limits
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/skyfoundry/skyfoundry-2026-09-02T155802.png
security:
- kind: authentication
  name: Skyfoundry Authentication
  slug: skyfoundry-authentication
  summary_line: scram/http · 5 schemes
- kind: domain-security
  name: Skyfoundry Domain Security
  slug: skyfoundry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skyfoundry
tags:
- Company
- Building Analytics
- IoT
- Energy Management
- Fault Detection
- Smart Buildings
- Project Haystack
- Time Series
- Analytics
website: https://skyfoundry.com
---
