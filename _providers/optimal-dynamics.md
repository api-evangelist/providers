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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/optimal-dynamics/a2a/optimal-dynamics-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/optimal-dynamics-a2a.yml
- group: agent
  href: https://artifacts.apis.io/optimal-dynamics/well-known/optimal-dynamics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/optimal-dynamics-well-known.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.incident.io/alerts/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.incident.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.incident.io/llms.txt
- group: other
  href: https://artifacts.apis.io/optimal-dynamics/hosts/optimal-dynamics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/optimal-dynamics-hosts.yml
- group: other
  href: https://artifacts.apis.io/optimal-dynamics/vendors/optimal-dynamics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/optimal-dynamics-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.optimaldynamics.com
- group: company
  title: ''
  type: About
  url: https://www.optimaldynamics.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.optimaldynamics.com/resources/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.incident.io/optimaldynamics
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimaldynamics.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.optimaldynamics.com/security
- group: auth
  href: https://artifacts.apis.io/optimal-dynamics/security/optimal-dynamics-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/optimal-dynamics-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/optimal-dynamics/security/optimal-dynamics-trust-center.yml
  title: ''
  type: Compliance
  url: security/optimal-dynamics-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/optimal-dynamics/security/optimal-dynamics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/optimal-dynamics-domain-security.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.optimaldynamics.com/request-a-demo
- group: operate
  title: ''
  type: Support
  url: https://support.optimaldynamics.com/hc/en-us
coverage:
  checked: '2026-10-20'
  detail: optimaldynamics.com sells the CORE.ai trucking decision platform by demo request only; /developers 404s, api.optimaldynamics.com does not resolve, and the only docs links found belong to its status-page vendor incident.io.
  evidence:
  - status: 404
    url: https://www.optimaldynamics.com/developers
  - status: 200
    url: https://www.optimaldynamics.com/request-a-demo
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Optimal Dynamics is the Decision Company for trucking. Its Transportation Decision System (TDS), CORE.ai, applies Artificial Decision Intelligence — born from 40 years of research at Princeton University — to automate and optimize strategic, tactical, and real-time planning for enterprise truckload carriers. The platform spans dispatch management, network management, bid analysis, and network simulation, using dynamic forecasting to simulate downstream impacts and drive highly automated operations that increase revenue per truck and reduce manual planning. Surfaced as a portfolio company of bessemer-venture-partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimal-dynamics.png
layout: provider
modified: '2026-10-20'
name: Optimal Dynamics
nav: Providers
network: true
overview: 'Optimal Dynamics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vertical Software, Logistics, Trucking, and Transportation.


  Optimal Dynamics'' developer surface includes getting-started guide, documentation, API reference, engineering blog, signup flow, support, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 55.4
    operational_transparency: 26.3
  previous_composite: 24.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/optimal-dynamics/optimal-dynamics-2026-08-07T190811.png
security:
- kind: domain-security
  name: Optimal Dynamics Domain Security
  slug: optimal-dynamics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Optimal Dynamics Trust Center
  slug: optimal-dynamics-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: optimal-dynamics
tags:
- Company
- Vertical Software
- Logistics
- Trucking
- Transportation
- Supply Chain
- Artificial Intelligence
- Decision Automation
website: https://www.optimaldynamics.com
---
