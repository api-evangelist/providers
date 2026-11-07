---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/airpim/hosts/airpim-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airpim-hosts.yml
- group: auth
  href: https://artifacts.apis.io/airpim/security/airpim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airpim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airpim.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.airpim.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.airpim.com/en/software/openbridge
- group: docs
  title: ''
  type: APIReference
  url: https://www.airpim.com/en/software/openbridge
- group: start
  title: ''
  type: GettingStarted
  url: https://www.airpim.com/en/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airpim.com/en/store/openbridge
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airpim.com/en/documents/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airpim.com/en/documents/privacy
coverage:
  checked: '2026-10-19'
  detail: No public API specification or developer program was found; attempts to fetch OpenAPI files returned errors.
  evidence:
  - status: 502
    url: https://api.airpim.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-19'
description: Openbridge, operating under the brand Airpim, provides intelligent software solutions that transform data into a competitive advantage. Their platform offers modular, scalable components for data integration, automation, and analytics, serving various industries such as sales, production, logistics, and supervision. The company emphasizes rapid deployment, flexibility, and user-friendly interfaces to help businesses maintain clean, structured data and adapt to evolving needs.
image: https://www.airpim.com/assets/web_site_airpim_v1/files/airpim-share.jpg
layout: provider
modified: '2026-10-19'
name: Openbridge
nav: Providers
network: true
overview: 'Openbridge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, Automation, Analytics, Modular Software, and Openbridge.


  Openbridge''s developer surface includes documentation, API reference, getting-started guide, pricing, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 18.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/airpim/airpim-2026-11-03T120532.png
security:
- kind: domain-security
  name: Airpim Domain Security
  slug: airpim-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: airpim
tags:
- Data Integration
- Automation
- Analytics
- Modular Software
- Openbridge
website: https://www.airpim.com/en/
---
