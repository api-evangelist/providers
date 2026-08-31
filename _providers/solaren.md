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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solaren-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solarenspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.solarenspace.com/news-events/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.solarenspace.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.solarenspace.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solarenspace.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solarenspace.com/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solaren-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/solaren-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solaren-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: Solaren generates and sells electricity from orbiting space solar power plants under utility power purchase agreements, and its single public site is a WordPress marketing brochure with no developer section — every OpenAPI, GraphQL and /.well-known/ path probed returned the theme's HTTP 500 error page, and the only machine-readable endpoint on the domain is the default WordPress core REST API at /wp-json/ (wp/v2 and friends, no company namespace).
  evidence:
  - status: 200
    url: https://www.solarenspace.com/
  - status: 500
    url: https://www.solarenspace.com/openapi.json
  - status: 500
    url: https://www.solarenspace.com/graphql
  - status: 500
    url: https://www.solarenspace.com/.well-known/agent-card.json
  - status: 200
    url: https://www.solarenspace.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: 'Solaren is a combination energy and aerospace company headquartered in Manhattan Beach, California, founded in 2001 by a team of satellite engineers and space scientists. Solaren designs, develops, integrates, deploys and operates space solar power (SSP) plants: solar arrays on a patented lightweight solar power satellite in geosynchronous orbit convert sunlight to electricity, convert that electricity to radio-frequency power, and beam it to an earth receiving station that returns it to the grid as baseload power. The company''s business model is to own and operate its SSP plants and sell continuous, zero-emission electricity to utility and government customers; it signed the world''s first power purchase agreement for space solar electricity, with Pacific Gas & Electric. Solaren is a hardware and energy-generation company and publishes no public developer program, API, or machine-readable API contract.'
image: https://www.solarenspace.com/wp-content/themes/solaren/img/logo.png
layout: provider
modified: '2026-08-28'
name: Solaren
nav: Providers
network: true
overview: 'Solaren is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Renewable Energy, and Space.


  Solaren''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Solaren Plans Pricing
  plan_count: 0
  slug: solaren-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Solaren Rate Limits
  slug: solaren-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Solaren Domain Security
  slug: solaren-domain-security
  summary_line: TLSv1.3
slug: solaren
tags:
- Company
- Energy
- Electricity
- Renewable Energy
- Space
- Aerospace
- Satellites
- Solar Power
- Utilities
website: https://www.solarenspace.com/
---
