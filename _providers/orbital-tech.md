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
  score: 13.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.orbital.tech/security
- group: agent
  href: https://artifacts.apis.io/orbital-tech/llms/orbital-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orbital-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/orbital-tech/well-known/orbital-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orbital-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/orbital-tech/hosts/orbital-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orbital-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/orbital-tech/vendors/orbital-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orbital-tech-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.orbital.tech/security
- group: auth
  href: https://artifacts.apis.io/orbital-tech/security/orbital-tech-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/orbital-tech-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/orbital-tech/security/orbital-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orbital-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.orbital.tech
- group: company
  title: ''
  type: Blog
  url: https://www.orbital.tech/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orbital.tech/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.orbital.tech/about
- group: operate
  title: ''
  type: Contact
  url: https://www.orbital.tech/contact-us
coverage:
  checked: '2026-10-23'
  detail: The provider's website does not expose any machine‑readable API specification and developer documentation is behind a login page.
  evidence:
  - status: 200
    url: https://www.orbital.tech
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Orbital provides an AI platform for commercial real estate legal work, helping law firms, real estate businesses, and occupiers automate title, survey, lease analysis, and transaction coordination. The platform surfaces legal issues early, visualizes property data, and streamlines drafting and negotiation, accelerating deal timelines and reducing risk for commercial real estate transactions.
image: https://cdn.prod.website-files.com/6a462f7758e73e174119a505/6a8cae4a4e43bf78a635cf04_Preview.png
layout: provider
modified: '2026-10-23'
name: Orbital
nav: Providers
network: true
overview: 'Orbital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Real Estate, Legal Tech, Commercial, and Platform.


  Orbital''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/orbital-tech/orbital-tech-2026-11-03T140723.png
security:
- kind: domain-security
  name: Orbital Tech Domain Security
  slug: orbital-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Orbital Tech Trust Center
  slug: orbital-tech-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: orbital-tech
tags:
- Artificial Intelligence
- Real Estate
- Legal Tech
- Commercial
- Platform
- Company
website: https://www.orbital.tech
---
