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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'HomeBox API as documented publicly: 93 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: HomeBox API
  slug: homebox-software-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/homebox-software/rules/homebox-software-rules.yml
  title: ''
  type: Spectral
  url: rules/homebox-software-rules.yml
- group: design
  href: https://artifacts.apis.io/homebox-software/vocabulary/homebox-software-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/homebox-software-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/sysadminsmedia/homebox/blob/main/SECURITY.md
- group: design
  href: https://artifacts.apis.io/homebox-software/conformance/homebox-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/homebox-software-conformance.yml
- group: agent
  href: https://artifacts.apis.io/homebox-software/llms/homebox-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/homebox-software-llms.txt
- group: auth
  href: https://artifacts.apis.io/homebox-software/well-known/homebox-software-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/homebox-software-security.txt
- group: auth
  href: https://artifacts.apis.io/homebox-software/well-known/homebox-software-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/homebox-software-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/homebox-software/well-known/homebox-software-demo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/homebox-software-demo-security.txt
- group: auth
  href: https://artifacts.apis.io/homebox-software/well-known/homebox-software-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/homebox-software-community-security.txt
- group: auth
  href: https://artifacts.apis.io/homebox-software/well-known/homebox-software-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/homebox-software-blog-security.txt
- group: agent
  href: https://artifacts.apis.io/homebox-software/well-known/homebox-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/homebox-software-well-known.yml
- group: other
  href: https://artifacts.apis.io/homebox-software/hosts/homebox-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/homebox-software-hosts.yml
- group: other
  href: https://artifacts.apis.io/homebox-software/vendors/homebox-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/homebox-software-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://community.homebox.software/login
- group: auth
  href: https://artifacts.apis.io/homebox-software/security/homebox-software-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/homebox-software-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/homebox-software/security/homebox-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/homebox-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://homebox.software/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://git.homebox.software
- group: docs
  title: ''
  type: Documentation
  url: https://homebox.software/en/
- group: docs
  title: ''
  type: APIReference
  url: https://homebox.software/en/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://homebox.software/en/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://discord.homebox.software
- group: company
  title: ''
  type: Blog
  url: https://blog.homebox.software
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation page https://homebox.software/en/api/ returns HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://homebox.software/en/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: HomeBox provides a simple, open‑source home inventory management system. It lets users catalog items, locations, and collections with a lightweight Go backend, supporting SQLite or PostgreSQL, Docker deployment, and self‑hosting. The software emphasizes privacy, low resource usage (under 50 MB RAM), and extensibility through templates and labels, making it suitable for personal households and small teams.
layout: provider
modified: '2026-10-28'
name: HomeBox
nav: Providers
network: true
overview: 'HomeBox is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Homes, Inventory, Open Source, Self-Hosted, and Go.


  The HomeBox catalog on APIs.io includes 1 Spectral governance ruleset.


  HomeBox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: HomeBox API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: homebox-software-rules
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 11.8
    developer_ergonomics: 22.6
    discoverability: 60.7
    operational_transparency: 5.3
  previous_composite: 24.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/homebox-software/homebox-software-2026-11-03T133432.png
security:
- kind: domain-security
  name: Homebox Software Domain Security
  slug: homebox-software-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Homebox Software Vulnerability Disclosure
  slug: homebox-software-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: homebox-software
tags:
- Homes
- Inventory
- Open Source
- Self-Hosted
- Go
website: https://homebox.software/
---
