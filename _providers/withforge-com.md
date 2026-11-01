---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/withforge-com/authentication/withforge-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/withforge-com-authentication.yml
- group: other
  href: https://artifacts.apis.io/withforge-com/hosts/withforge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withforge-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/withforge-com/vendors/withforge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withforge-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poetic.com/terms
- group: operate
  title: ''
  type: Support
  url: https://poetic.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poetic.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/github-cli/github-cli/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.poetic.com/
- group: auth
  href: https://artifacts.apis.io/withforge-com/security/withforge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withforge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poetic.com/
coverage:
  checked: '2026-10-24'
  detail: Documentation site loads via JavaScript and provides no machine‑readable spec.
  evidence:
  - status: 200
    url: https://poetic.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Poetic is an AI-powered automation platform that transforms business processes into software. It learns organizational rules, automates repetitive tasks, and enables end‑to‑end workflow orchestration across teams, boosting efficiency and scalability. The platform offers a no‑code interface, integrations, and a developer API for custom extensions, positioning Poetic as a modern solution for digital transformation.
image: https://poetic.com/og.jpg
layout: provider
modified: '2026-10-24'
name: Poetic
nav: Providers
network: true
overview: 'Poetic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Automation, KYC, Dispute Management, Enterprise Workflow, and Security.


  Poetic''s developer surface includes authentication, support, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Withforge Com Authentication
  slug: withforge-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Withforge Com Domain Security
  slug: withforge-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: withforge-com
tags:
- AI Automation
- KYC
- Dispute Management
- Enterprise Workflow
- Security
website: https://poetic.com/
---
