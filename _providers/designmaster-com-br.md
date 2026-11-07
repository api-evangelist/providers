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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/designmaster-com-br/llms/designmaster-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/designmaster-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/designmaster-com-br/well-known/designmaster-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/designmaster-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/designmaster-com-br/hosts/designmaster-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/designmaster-com-br-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://whmcs.designmaster.com.br/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.designmaster.com.br/
- group: auth
  href: https://artifacts.apis.io/designmaster-com-br/security/designmaster-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/designmaster-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.designmaster.com.br/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://commerce.designmaster.com.br/mcp
  - status: 200
    url: https://designmaster.com.br/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: DesignMaster is a Brazilian software company with 22 years of experience developing custom systems, mobile apps, websites and virtual stores. It offers domain registration and hosting services for businesses that cannot afford downtime, focusing on tailored digital solutions for the Brazilian market.
image: https://www.designmaster.com.br/og-image.jpg
layout: provider
modified: '2026-11-05'
name: DesignMaster
nav: Providers
network: true
overview: DesignMaster is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Web Development, E-Commerce, Brazil, and Software.
random_paper: 11
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Designmaster Com Br Domain Security
  slug: designmaster-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: designmaster-com-br
tags:
- Design
- Web Development
- E-Commerce
- Brazil
- Software
website: https://www.designmaster.com.br/
---
