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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.jitjatjo.com/
- group: operate
  title: ''
  type: Support
  url: https://help.jitjatjo.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terms.jitjatjo.com/terms/terms-client.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terms.jitjatjo.com/terms/privacy.html
- group: start
  title: ''
  type: SignUp
  url: https://ondemand.jitjatjo.com/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Jitjatjo-Technology
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jitjatjo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jitjatjo-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jitjatjo-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jitjatjo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jitjatjo-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: 'Jitjatjo ships software only as an end-user product — the Ondemand, Flex and Network apps — and publishes no developer surface of any kind: the production API host read out of its own JavaScript bundle, ondemandapi.dayforceflexwork.com, returns {"error":"Resource not found."} for /openapi.json, /swagger.json, /graphql, /api-docs, /docs and /redoc alike, and no developer portal, API reference, SDK or webhook catalog exists on any of the hosts enumerated from Certificate Transparency for jitjatjo.com, jjj.work or networkplatform.com.'
  evidence:
  - status: 404
    url: https://ondemandapi.dayforceflexwork.com/openapi.json
  - status: 404
    url: https://ondemandapi.dayforceflexwork.com/api-docs
  - status: 404
    url: https://ondemandapi.dayforceflexwork.com/graphql
  - status: 200
    url: https://help.jitjatjo.com/llms.txt
  - status: 0
    url: https://www.jitjatjo.com/
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'Jitjatjo is a New York City based on-demand staffing and workforce management platform operated by JJJ International, matching hospitality, healthcare, education, facilities, retail and logistics businesses with W2 temporary talent in real time. The company runs two consumer-facing products — "Ondemand by Jitjatjo" for businesses booking shifts and "Flex by Jitjatjo" for talent picking up gigs — alongside "Network", a frontline vendor management system (VMS) for contingent labor that is integrated with SAP Fieldglass. JJJ International was acquired by Dayforce in September 2025 and the platform is being rebranded as Dayforce Flex Work; the Jitjatjo web apps now call API hosts on dayforceflexwork.com. Jitjatjo publishes no public developer program: no developer portal, API reference, OpenAPI/GraphQL contract, SDK or webhook catalog was found on any host the company controls.'
image: https://cdn.prod.website-files.com/5feb460b9cc80b0a7898c766/5fecd7cdcfa4cb6f9cf69609_jitjatjo_webclip.png
layout: provider
modified: '2026-08-23'
name: Jitjatjo
nav: Providers
network: true
overview: 'Jitjatjo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Human Resources, Workforce Management, and Talent Marketplace.


  Jitjatjo''s developer surface includes support, signup flow, and 9 more developer resources.'
plans:
- name: Jitjatjo Plans Pricing
  plan_count: 0
  slug: jitjatjo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Jitjatjo Rate Limits
  slug: jitjatjo-rate-limits
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Jitjatjo Domain Security
  slug: jitjatjo-domain-security
  summary_line: HSTS · DMARC
slug: jitjatjo
tags:
- Company
- Staffing
- Human Resources
- Workforce Management
- Talent Marketplace
- Gig Economy
- Contingent Labor
- Vendor Management
- Hospitality
- Healthcare Staffing
website: https://www.jitjatjo.com/
---
