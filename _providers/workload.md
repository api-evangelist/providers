---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/workload/hosts/workload-hosts.yml
  title: ''
  type: Hosts
  url: hosts/workload-hosts.yml
- group: other
  href: https://artifacts.apis.io/workload/vendors/workload-vendors.yml
  title: ''
  type: Vendors
  url: vendors/workload-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.workload.co/security/
- group: auth
  href: https://artifacts.apis.io/workload/security/workload-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/workload-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/workload/security/workload-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workload-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://workload.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.workload.co/developer-platform
- group: docs
  title: ''
  type: Documentation
  url: https://www.workload.co/developer-platform
- group: docs
  title: ''
  type: APIReference
  url: https://www.workload.co/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.workload.co/agents/
- group: operate
  title: ''
  type: Support
  url: https://www.workload.co/contact
- group: company
  title: ''
  type: Blog
  url: https://www.workload.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workload.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workload.co/privacy/
coverage:
  checked: '2026-10-21'
  detail: The developer platform provides only HTML pages without any OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.workload.co/developer-platform
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Workload provides AI‑driven agents and self‑healing automation platforms that enable businesses to automate workflows across their existing software stack. By connecting to popular SaaS applications, Workload orchestrates tasks, monitors execution, and automatically repairs failures, ensuring continuous operation without manual intervention. The solution targets enterprises seeking to reduce manual effort, improve reliability, and accelerate digital transformation through intelligent automation.
layout: provider
modified: '2026-10-21'
name: Workload
nav: Providers
network: true
overview: 'Workload is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Automation, SaaS, and Integration.


  Workload''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Workload Domain Security
  slug: workload-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workload Vulnerability Disclosure
  slug: workload-vulnerability-disclosure
  summary_line: no policy recorded
slug: workload
tags:
- Company
- AI
- Automation
- SaaS
- Integration
website: https://workload.co/
---
