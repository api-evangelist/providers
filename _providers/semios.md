---
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The authenticated service behind the Semios Hub grower application at hub.semios.com. The host is live and answers on HTTPS, but every anonymous path returns an application-level "Path not Found" and '
  name: Semios Hub API
  slug: semios-hub-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://semios.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.semios.com/
- group: operate
  title: ''
  type: Support
  url: https://semios.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/semiosBIO
- group: start
  title: ''
  type: Login
  url: https://hub.semios.com/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/semios-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/semios-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/semios-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/semios-lifecycle.yml
coverage:
  checked: '2026-08-26'
  detail: Semios runs a live production API host at hub-api.semios.com that answers every anonymous path with an application-level "Path not Found", and the only human entry point is the Semios Hub login at hub.semios.com - there is no developer portal, no API reference and no machine-readable contract anywhere on semios.com, so the Hub API is reachable only with an active grower tenant arranged through customer success or a partner agreement.
  evidence:
  - status: 404
    url: https://hub-api.semios.com/openapi.json
  - status: 404
    url: https://semios.com/developers/
  - status: 200
    url: https://hub.semios.com/login
  - status: 404
    url: https://semios.com/.well-known/api-catalog
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Semios (legally SemiosBio Technologies Inc., Vancouver, British Columbia, founded 2010 by Michael Gilbert) is a precision-agriculture company that operates a large in-canopy IoT sensor network for permanent crops - almonds, apples, cherries, citrus, grapes, pears, pistachios, stone fruit and walnuts. Its sensors report climate, soil moisture, insect trap counts and plant-stress readings on roughly ten-minute intervals, and its platform layers degree-day models, disease and frost risk models and machine learning on top of that feed to drive insect pest management (including variable-rate aerosol mating disruption), disease management, frost management, irrigation and water management, plant-stress monitoring, and alerting and reporting. Growers and agronomists consume it through the Semios Hub web and mobile applications, backed by the hub-api.semios.com service. Semios acquired Agworld, Altrac and Centricity, and in October 2024 the group unified those brands under the Almanac
  name, with Semios continuing as the sensing and crop-protection brand. Semios does not operate a public developer portal - the Hub API is customer and partner authenticated, and integrations such as the WiseConn irrigation integration are arranged directly.
image: https://semios.com/wp-content/uploads/2020/10/logo.svg
layout: provider
modified: '2026-08-26'
name: Semios
nav: Providers
network: true
overview: 'Semios publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Precision Agriculture, Crop Management, and Pest Management.


  Semios'' developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Semios Plans Pricing
  plan_count: 0
  slug: semios-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Semios Rate Limits
  slug: semios-rate-limits
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.3
  provenance:
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Semios Domain Security
  slug: semios-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: semios
tags:
- Agriculture
- AgTech
- Precision Agriculture
- Crop Management
- Pest Management
- IoT
- Sensors
- Irrigation
- Weather
- Canada
website: https://semios.com/
---
