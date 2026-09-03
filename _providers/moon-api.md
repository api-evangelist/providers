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
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Moon Api Agentic Access
  operation_count: 7
  slug: moon-api-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://moon-phase.p.rapidapi.com
  baseurl_source: spec
  description: The Advanced API from Moon-API — 1 operation(s) for advanced.
  name: Moon-API Advanced API
  slug: moon-api-advanced-api
- baseURL: https://moon-phase.p.rapidapi.com
  baseurl_source: spec
  description: The Astrology API from Moon-API — 1 operation(s) for astrology.
  name: Moon-API Astrology API
  slug: moon-api-astrology-api
- baseURL: https://moon-phase.p.rapidapi.com
  baseurl_source: spec
  description: The Basic API from Moon-API — 1 operation(s) for basic.
  name: Moon-API Basic API
  slug: moon-api-basic-api
- baseURL: https://moon-phase.p.rapidapi.com
  baseurl_source: spec
  description: The Calendar API from Moon-API — 1 operation(s) for calendar.
  name: Moon-API Calendar API
  slug: moon-api-calendar-api
- baseURL: https://moon-phase.p.rapidapi.com
  baseurl_source: spec
  description: The Emoji API from Moon-API — 1 operation(s) for emoji.
  name: Moon-API Emoji API
  slug: moon-api-emoji-api
- baseURL: https://moon-phase.p.rapidapi.com
  baseurl_source: spec
  description: The Phase API from Moon-API — 1 operation(s) for phase.
  name: Moon-API Phase API
  slug: moon-api-phase-api
- baseURL: https://moon-phase.p.rapidapi.com
  baseurl_source: spec
  description: The Plain Text API from Moon-API — 1 operation(s) for plain text.
  name: Moon-API Plain Text API
  slug: moon-api-plain-text-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Moon-API.com Advanced API
  slug: open-moon-api-advanced-api
- collection_type: open
  name: Moon-API.com Advanced Astrology API
  slug: open-moon-api-astrology-api
- collection_type: open
  name: Moon-API.com Advanced Basic API
  slug: open-moon-api-basic-api
- collection_type: open
  name: Moon-API.com Advanced Calendar API
  slug: open-moon-api-calendar-api
- collection_type: open
  name: Moon-API.com Advanced Emoji API
  slug: open-moon-api-emoji-api
- collection_type: open
  name: Moon-API.com Advanced Phase API
  slug: open-moon-api-phase-api
- collection_type: open
  name: Moon-API.com Advanced Plain Text API
  slug: open-moon-api-plain-text-api
- collection_type: open
  name: Moon-API.com
  slug: open-moon-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moon-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moon-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moon-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moon-api-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://moon-api.com/
- group: docs
  title: ''
  type: SwaggerUI
  url: https://moon-api.com/swagger.html
- group: start
  title: ''
  type: Signup
  url: https://rapidapi.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://moon-api.com/llms.txt
created: '2024-03-30'
description: Moon-API.com provides real-time lunar and astronomical data including moon phases, illumination, moonrise and moonset times, sun data, calendars, and astrology data such as natal charts, planetary positions, aspects, and house cusps. The API is offered through the RapidAPI marketplace with global edge caching for low-latency responses.
finops:
- name: Moon Api Finops
  service_category: API
  slug: moon-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moon-api.png
layout: provider
modified: '2026-05-19'
name: Moon-API
nav: Providers
network: true
overview: 'Moon-API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Advanced API, Astrology API, Basic API, and 4 more. Tagged areas include Astrology, Astronomy, Lunar, Moon, and Moon Phases.


  Moon-API''s developer surface includes authentication, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Moon Api Plans Pricing
  plan_count: 3
  slug: moon-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Moon Api Rate Limits
  slug: moon-api-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moon-api/refs/heads/main/screenshots/moon-api-2026-06-20T185757.png
security:
- kind: authentication
  name: Moon Api Authentication
  slug: moon-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Moon Api Domain Security
  slug: moon-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moon Api Vulnerability Disclosure
  slug: moon-api-vulnerability-disclosure
  summary_line: disclosure policy published
slug: moon-api
tags:
- Astrology
- Astronomy
- Lunar
- Moon
- Moon Phases
- Space
website: https://moon-api.com/
---
