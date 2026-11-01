---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Example section for showcasing API endpoints
  name: Lytix API
  slug: lytix-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/lytix/cli/lytix-cli.yml
  title: ''
  type: CLI
  url: cli/lytix-cli.yml
- group: auth
  href: https://artifacts.apis.io/lytix/authentication/lytix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lytix-authentication.yml
- group: agent
  href: https://artifacts.apis.io/lytix/llms/lytix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lytix-llms.txt
- group: other
  href: https://artifacts.apis.io/lytix/a2a/lytix-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lytix-a2a.yml
- group: agent
  href: https://artifacts.apis.io/lytix/well-known/lytix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lytix-well-known.yml
- group: other
  href: https://artifacts.apis.io/lytix/hosts/lytix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lytix-hosts.yml
- group: other
  href: https://artifacts.apis.io/lytix/vendors/lytix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lytix-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lytix-Labs
- group: auth
  href: https://artifacts.apis.io/lytix/security/lytix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lytix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lytix.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lytix.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lytix.co/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lytix.co/quickstart/openai-integration
- group: company
  title: ''
  type: Blog
  url: https://blog.lytix.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lytix.co/pricing
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are rendered via Mintlify JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.lytix.co/api-reference/introduction
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Lytix provides an open‑source evaluations layer for LLMOps, offering continuous monitoring, custom evaluation workflows, and real‑time scoring to ensure AI model performance, accuracy, and empathy. The platform includes a console, playground, and integrations for medical and other domain‑specific use cases, helping teams assess and improve their AI systems.
layout: provider
modified: '2026-10-18'
name: Lytix
nav: Providers
network: true
overview: 'Lytix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLMOps, Evaluation, Monitoring, and Open Source.


  Lytix''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 53.6
    operational_transparency: 5.3
  previous_composite: 17.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lytix Authentication
  slug: lytix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lytix Domain Security
  slug: lytix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lytix
tags:
- Artificial Intelligence
- LLMOps
- Evaluation
- Monitoring
- Open Source
website: https://lytix.co/
---
