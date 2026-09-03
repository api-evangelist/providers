---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 13.3
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://havenenergy.com/
- group: company
  title: ''
  type: Blog
  url: https://havenenergy.com/blog
- group: operate
  title: ''
  type: Support
  url: https://resources.havenenergy.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://resources.havenenergy.com/
- group: start
  title: ''
  type: Login
  url: https://havenenergy.com/documents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://havenenergy.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://havenenergy.com/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/haven-energy-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/haven-energy-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/haven-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/haven-energy-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/haven-energy-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Haven Energy is a direct-to-consumer home battery and VPP operator whose entire product is a quote-to-install funnel plus utility program enrollment; contract discovery found no developer subdomain at all (api., developer., docs., portal. and app.havenenergy.com have no DNS record), every spec and well-known path 404s on the apex, and the only "partner" program on the site is a channel program for local electrical contractors, not an API integration program.
  evidence:
  - status: 404
    url: https://havenenergy.com/openapi.json
  - status: 404
    url: https://havenenergy.com/docs
  - status: 404
    url: https://havenenergy.com/.well-known/api-catalog
  - status: 404
    url: https://havenenergy.com/.well-known/agent-card.json
  - status: 200
    url: https://landing.havenenergy.com/partners
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Haven Energy is an Austin, Texas based residential clean-energy company that sells, finances, installs and operates home battery storage and solar systems, and then aggregates those systems into one of the largest virtual power plant (VPP) networks in the United States. Homeowners get an instant online quote, a fixed monthly payment over a ten-year term, end-to-end permitting and certified installation through Haven's Channel Partner network of local electricians, and ongoing remote monitoring. Haven then enrolls the installed batteries into utility and grid programs - California SGIP, PG&E, and Massachusetts ConnectedSolutions among them - so customers can monetize grid participation while utilities and community choice aggregators gain flexible local capacity. Founded in 2022 by Jeff Chapin, Philip Krim and Vinnie Campos, the company raised a $40M Series B in December 2025 led by Giant Ventures. Haven operates as a direct-to-consumer and utility-partner business; it publishes
  no public developer program, API, or machine-readable API contract.
layout: provider
modified: '2026-08-22'
name: Haven Energy
nav: Providers
network: true
overview: 'Haven Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Energy Storage, Solar, Virtual Power Plant, and Distributed Energy Resources.


  Haven Energy''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Haven Energy Plans Pricing
  plan_count: 0
  slug: haven-energy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Haven Energy Rate Limits
  slug: haven-energy-rate-limits
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/haven-energy/refs/heads/main/screenshots/haven-energy-2026-09-02T145708.png
security:
- kind: domain-security
  name: Haven Energy Domain Security
  slug: haven-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: haven-energy
tags:
- Energy
- Energy Storage
- Solar
- Virtual Power Plant
- Distributed Energy Resources
- Home Battery
- Clean Energy
- Utilities
- Climate Tech
- Company
website: https://havenenergy.com/
---
