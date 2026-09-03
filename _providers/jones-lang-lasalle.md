---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Jones Lang Lasalle Agentic Access
  operation_count: 5
  slug: jones-lang-lasalle-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- baseURL: https://am-ce98c.corrigo.com/api/v1
  baseurl_source: declared
  description: Track and manage facility assets and equipment.
  name: Jones Lang LaSalle Assets API
  slug: jones-lang-lasalle-assets-api
- baseURL: https://am-ce98c.corrigo.com/api/v1
  baseurl_source: declared
  description: Manage contacts including vendors and tenants.
  name: Jones Lang LaSalle Contacts API
  slug: jones-lang-lasalle-contacts-api
- baseURL: https://am-ce98c.corrigo.com/api/v1
  baseurl_source: declared
  description: Manage building and space locations.
  name: Jones Lang LaSalle Locations API
  slug: jones-lang-lasalle-locations-api
- baseURL: https://am-ce98c.corrigo.com/api/v1
  baseurl_source: declared
  description: Create and manage work orders for facility maintenance.
  name: Jones Lang LaSalle Work Orders API
  slug: jones-lang-lasalle-work-orders-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JLL Corrigo Enterprise REST Assets API
  slug: open-jones-lang-lasalle-assets-api
- collection_type: open
  name: JLL Corrigo Enterprise REST Assets Contacts API
  slug: open-jones-lang-lasalle-contacts-api
- collection_type: open
  name: JLL Corrigo Enterprise REST API
  slug: open-jones-lang-lasalle-corrigo-rest-api
- collection_type: open
  name: JLL Corrigo Enterprise REST Assets Locations API
  slug: open-jones-lang-lasalle-locations-api
- collection_type: open
  name: JLL Corrigo Enterprise REST Assets Work Orders API
  slug: open-jones-lang-lasalle-work-orders-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/jones-lang-lasalle-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jones-lang-lasalle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jones-lang-lasalle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jones-lang-lasalle-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JLL-IT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jll
- group: company
  title: ''
  type: Website
  url: https://www.jll.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.corrigo.com/
created: '2026-03-21'
description: Jones Lang LaSalle Incorporated (JLL) is a global commercial real estate services company offering investment management, property management, and facility services. Through JLL Technologies (JLLT), the company delivers technology solutions including the Corrigo Enterprise platform for facility management with a REST API enabling integration with work order management, asset tracking, procurement, billing, and vendor management systems.
finops:
- name: Jones Lang Lasalle Finops
  service_category: Commercial Real Estate / Facility Management
  slug: jones-lang-lasalle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jones-lang-lasalle.png
layout: provider
modified: '2026-05-19'
name: Jones Lang LaSalle
nav: Providers
network: true
overview: 'Jones Lang LaSalle publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Contacts API, Locations API, and 1 more. Tagged areas include Commercial Real Estate, Facility Management, Asset Management, Work Orders, and Fortune 500.


  Jones Lang LaSalle''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Jones Lang Lasalle Plans Pricing
  plan_count: 1
  slug: jones-lang-lasalle-plans-pricing
press:
- date: '2026-05-25'
  title: JLL unveils first GPT model for commercial real estate
  url: https://www.prnewswire.com/news-releases/jll-unveils-first-gpt-model-for-commercial-real-estate-301890405.html
- date: '2026-05-25'
  title: Decode your building's story with JLL Azara, powered ...
  url: https://www.facebook.com/jll/posts/decode-your-buildings-story-with-jll-azara-powered-by-jll-falconreal-time-intell/1296376262523390/
- date: '2026-05-25'
  title: JLL Falcon kicks off new era of AI-powered CRE innovation
  url: https://ir.jll.com/news-releases/press-release-details/2024/JLL-Falcon-kicks-off-new-era-of-AI-powered-CRE-innovation/default.aspx
- date: '2026-05-25'
  title: Jones Lang LaSalle (JLL) Gains Analyst Confidence Amid ...
  url: https://finance.yahoo.com/news/jones-lang-lasalle-jll-gains-134305389.html
- date: '2026-05-25'
  title: JLL News and Press Releases
  url: https://www.prnewswire.com/news/jll/
random_paper: 0
rate_limits:
- limit_count: 1
  name: Jones Lang Lasalle Rate Limits
  slug: jones-lang-lasalle-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Jones Lang Lasalle Authentication
  slug: jones-lang-lasalle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jones Lang Lasalle Domain Security
  slug: jones-lang-lasalle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jones-lang-lasalle
tags:
- Commercial Real Estate
- Facility Management
- Asset Management
- Work Orders
- Fortune 500
website: https://www.jll.com/
---
