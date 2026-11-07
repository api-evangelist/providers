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
api_count: 1
apis:
- description: API documented at the Echo Memory docs site
  name: Echo Memory API
  slug: echo-memory-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.echo-mem.com/security
- group: agent
  href: https://artifacts.apis.io/echo-mem-com/llms/echo-mem-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/echo-mem-com-llms.txt
- group: other
  href: https://artifacts.apis.io/echo-mem-com/hosts/echo-mem-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/echo-mem-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/echo-mem-com/vendors/echo-mem-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/echo-mem-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.echo-mem.com/security
- group: auth
  href: https://artifacts.apis.io/echo-mem-com/security/echo-mem-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/echo-mem-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/echo-mem-com/security/echo-mem-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/echo-mem-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/echo-mem-com/security/echo-mem-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/echo-mem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://echo-mem.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.echo-mem.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.echo-mem.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/echo-mem
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.echo-mem.com
- group: agent
  title: ''
  type: llms.txt
  url: https://www.echo-mem.com/llms.txt
- group: operate
  title: ''
  type: Contact
  url: https://www.echo-mem.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.echo-mem.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.echo-mem.com/terms
coverage:
  checked: '2026-11-06'
  detail: Docs page at https://www.echo-mem.com/docs is a JavaScript‑rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.echo-mem.com/docs
  - status: 404
    url: https://api.echo-mem.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: Echo Memory provides a graph‑based memory service for AI agents, enabling persistent, searchable fact storage that can be read and written by multiple agents. The platform offers both a hosted cloud version and a self‑hosted open‑source deployment, with an Apache 2.0 licensed Python package available on PyPI. It integrates via MCP over HTTP, supports easy key‑based authentication, and includes tooling for quick start, pricing, and extensive documentation.
image: https://www.echo-mem.com/opengraph-image?fb390782d069af70
layout: provider
modified: '2026-11-06'
name: Echo Memory
nav: Providers
network: true
overview: 'Echo Memory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Graph, Open Source, and MCP.


  Echo Memory''s developer surface includes documentation, engineering blog, and 15 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Echo Mem Com Domain Security
  slug: echo-mem-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Echo Mem Com Vulnerability Disclosure
  slug: echo-mem-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Echo Mem Com Trust Center
  slug: echo-mem-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: echo-mem-com
tags:
- Artificial Intelligence
- Memory
- Graph
- Open Source
- MCP
website: https://echo-mem.com/
---
