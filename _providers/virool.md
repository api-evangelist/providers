---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virool-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://virool.com
- group: start
  title: ''
  type: SignUp
  url: https://virool.com/signup
- group: start
  title: ''
  type: Login
  url: https://virool.com/login
- group: operate
  title: ''
  type: Support
  url: https://virool.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.virool.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.virool.com/publisher-terms-and-conditions
- group: build
  title: ''
  type: Packages
  url: packages/virool-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virool-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virool-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/virool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virool-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virool-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Virool's marketing site is live but ships no developer surface at all — every developer path (/developers, /api, /docs, /openapi.json) 404s and the API host its old directory listings pointed at, api.virool.com, no longer resolves in DNS.
  evidence:
  - status: 404
    url: https://virool.com/developers
  - status: 404
    url: https://virool.com/api
  - status: 404
    url: https://virool.com/openapi.json
  - status: 404
    url: https://virool.com/.well-known/agent-card.json
  - status: 0
    url: http://api.virool.com/api/v1
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Virool is a native video advertising platform that distributes branded video content ("advertainment") across the web to help brands reach and grow targeted audiences. It pairs a proprietary data-management platform of roughly 450 million unique profiles for granular audience targeting with native video placement technology designed to minimize disruption to the user experience, and a real-time performance analytics dashboard that includes emotional insight tracking (eIQ). Virool serves advertisers and publishers through self-service campaign and monetization dashboards rather than a public developer API. The company was backed by 500 Global and a16z and has run campaigns for brands including Turkish Airlines, Under Armour, and WestJet.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/virool.png
layout: provider
modified: '2026-08-12'
name: Virool
nav: Providers
network: true
overview: 'Virool is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Video Advertising, Video, and AdTech.


  Virool''s developer surface includes signup flow, support, and 11 more developer resources.'
plans:
- name: Virool Plans Pricing
  plan_count: 0
  slug: virool-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Virool Rate Limits
  slug: virool-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.9
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Virool Domain Security
  slug: virool-domain-security
  summary_line: TLSv1.2
slug: virool
tags:
- Company
- Advertising
- Video Advertising
- Video
- AdTech
- Marketing
- Brand
- Media
website: https://virool.com
---
