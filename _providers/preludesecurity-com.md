---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 11.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Prelude Security observability platform
  name: Prelude API
  slug: prelude-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/preludesecurity-com/plans/preludesecurity-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/preludesecurity-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/preludesecurity-com/cli/preludesecurity-com-cli.yml
  title: ''
  type: CLI
  url: cli/preludesecurity-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/preludesecurity-com/changelog/preludesecurity-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/preludesecurity-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/preludesecurity-com/authentication/preludesecurity-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/preludesecurity-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/preludesecurity-com/llms/preludesecurity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/preludesecurity-com-llms.txt
- group: other
  href: https://artifacts.apis.io/preludesecurity-com/a2a/preludesecurity-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/preludesecurity-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/preludesecurity-com/hosts/preludesecurity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/preludesecurity-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/preludesecurity-com/vendors/preludesecurity-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/preludesecurity-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.originhq.com:443/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.originhq.com:443/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.originhq.com:443/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.originhq.com:443/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://support.preludesecurity.com/microsoft-automated-integration-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.preludesecurity.com/
- group: auth
  href: https://artifacts.apis.io/preludesecurity-com/security/preludesecurity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/preludesecurity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.originhq.com/preludesecurity
coverage:
  checked: '2026-10-22'
  detail: Access to OpenAPI spec URLs returns HTTP 403, indicating a sales or authentication gate.
  evidence:
  - status: 403
    url: https://www.originhq.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-10-22'
description: Prelude Security, now operating as Origin Technology, provides an endpoint AI observability platform. It helps organizations monitor, trace, and analyze AI model endpoints, offering insights into performance, errors, and usage patterns. Former Prelude customers are directed to Origin for continued support and product evolution.
image: https://www.originhq.com/preludesecurity/opengraph-image?d8bae3764b52a2c5
layout: provider
modified: '2026-10-22'
name: Prelude
nav: Providers
network: true
overview: 'Prelude is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Observability, Monitoring, and Platform.


  Prelude''s developer surface includes CLI, changelog, authentication, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Preludesecurity Com Plans Pricing
  plan_count: 4
  slug: preludesecurity-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Preludesecurity Com Authentication
  slug: preludesecurity-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Preludesecurity Com Domain Security
  slug: preludesecurity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: preludesecurity-com
tags:
- Company
- AI
- Observability
- Monitoring
- Platform
website: https://www.originhq.com/preludesecurity
---
