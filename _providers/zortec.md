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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/zortec/hosts/zortec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zortec-hosts.yml
- group: auth
  href: https://artifacts.apis.io/zortec/security/zortec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zortec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zortec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zortec.com/
- group: operate
  title: ''
  type: Support
  url: https://support.zortec.com:8443
- group: docs
  title: ''
  type: Documentation
  url: https://zortec.com/developer-portal
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zortec.com/developer-portal
- group: start
  title: ''
  type: GettingStarted
  url: https://zortec.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://zortec.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://zortec.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://zortec.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://zortec.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zortec.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zortec.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://zortec.com/postman
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://zortec.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Zortec International provides enterprise software solutions focusing on data integration, application modernization, and digital transformation. Their platform offers tools for RAD development, legacy system modernization, and database independence, helping organizations streamline operations and accelerate innovation across various industries.
layout: provider
modified: '2026-10-21'
name: Zortec
nav: Providers
network: true
overview: 'Zortec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Modernization, Enterprise, and Software.


  Zortec''s developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zortec Domain Security
  slug: zortec-domain-security
  summary_line: no transport/DNS hardening detected
slug: zortec
tags:
- Company
- Integration
- Modernization
- Enterprise
- Software
website: https://zortec.com/
---
