---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swept-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sweptworks.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swept
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sweptworks
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.sweptworks.com/knowledge/resources
- group: commercial
  title: ''
  type: Plans
  url: plans/swept-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://learn.sweptworks.com/rss.xml
created: '2026-07-04'
description: Swept (sweptworks.com) is workforce management software for commercial cleaning and janitorial businesses - scheduling, GPS-verified time tracking and payroll reporting, mobile crew messaging, quality inspections, supply requests, client portals, and one-time work order management. As of this catalog entry, Swept does NOT publish a documented, self-serve public or partner developer API. There is no developer portal, API reference, API key or OAuth signup, published OpenAPI/Swagger specification, or webhook documentation on sweptworks.com or in the Swept Support Center knowledge base. The only documented outbound data path is a one-way, manually-activated QuickBooks Online payroll sync set up per account by a Swept Customer Success Manager - not a self-serve developer integration. Swept's public GitHub organization contains only take-home coding-challenge repositories used for hiring, not a first-party API client, SDK, or spec. This entry is therefore an honest stub documenting
  the provider and its access model; no API definitions are asserted because none are publicly documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swept.png
layout: provider
modified: '2026-07-04'
name: Swept
nav: Providers
network: true
overview: 'Swept is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Janitorial, Commercial Cleaning, Workforce Management, Scheduling, and Time Tracking.


  Swept''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Swept Plans Pricing
  plan_count: 3
  slug: swept-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Swept Domain Security
  slug: swept-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swept
tags:
- Janitorial
- Commercial Cleaning
- Workforce Management
- Scheduling
- Time Tracking
- Payroll
- Inspections
- Field Service
- No Public API
website: https://sweptworks.com
---
