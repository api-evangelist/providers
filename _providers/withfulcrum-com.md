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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/withfulcrum-com/llms/withfulcrum-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/withfulcrum-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/withfulcrum-com/well-known/withfulcrum-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/withfulcrum-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/withfulcrum-com/well-known/withfulcrum-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withfulcrum-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/withfulcrum-com/hosts/withfulcrum-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withfulcrum-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withfulcrum.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.withfulcrum.com/en/
- group: auth
  title: ''
  type: Security
  url: https://www.withfulcrum.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withfulcrum.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.withfulcrum.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.withfulcrum.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.withfulcrum.com/en/articles/14489589-applied-epic-integration-complete-setup-troubleshooting-guide
- group: docs
  title: ''
  type: Documentation
  url: https://help.withfulcrum.com/
- group: auth
  href: https://artifacts.apis.io/withfulcrum-com/security/withfulcrum-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withfulcrum-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.withfulcrum.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://app.withfulcrum.com/api/mcp
  - status: 200
    url: https://www.withfulcrum.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Fulcrum provides a platform that enables businesses to integrate and manage their data workflows, offering tools for data ingestion, transformation, and orchestration. The company focuses on simplifying complex data pipelines, delivering robust APIs for developers to build scalable solutions. Backed by CRV, Fulcrum aims to empower enterprises with flexible, secure, and performant data integration services across cloud and on-premises environments.
image: https://framerusercontent.com/assets/2QJHWsAMIAEe6Tvm24mfedocs.png
layout: provider
modified: '2026-10-25'
name: Fulcrum
nav: Providers
network: true
overview: 'Fulcrum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Integration, and Platform.


  Fulcrum''s developer surface includes support, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.3
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
screenshot: https://apis.io/screenshots/withfulcrum-com/withfulcrum-com-2026-11-03T150211.png
security:
- kind: domain-security
  name: Withfulcrum Com Domain Security
  slug: withfulcrum-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withfulcrum-com
tags:
- Company
- Data
- Integration
- Platform
website: https://www.withfulcrum.com/
---
