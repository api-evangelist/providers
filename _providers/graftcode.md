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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Self-hosted gateway (gg) that discovers public methods of a service and exposes them as Grafts over the Hypertube protocol, through Graftcode Vision, and as an MCP endpoint. It runs on the customer ma
  name: Graftcode Gateway
  slug: graftcode-gateway
artifact_total: 2
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/cli/graftcode-cli.yml
  title: ''
  type: CLI
  url: cli/graftcode-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/llms/graftcode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/graftcode-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/well-known/graftcode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/graftcode-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/hosts/graftcode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/graftcode-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/vendors/graftcode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/graftcode-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/packages/graftcode-packages.yml
  title: ''
  type: SDKs
  url: packages/graftcode-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/packages/graftcode-packages.yml
  title: ''
  type: Packages
  url: packages/graftcode-packages.yml
- group: company
  title: ''
  type: Website
  url: https://graftcode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://academy.graftcode.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.graftcode.com/reference/quick-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.graftcode.com/quick-start
- group: company
  title: ''
  type: Blog
  url: https://graftcode.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grft-dev
- group: start
  title: ''
  type: SignUp
  url: https://portal.graftcode.com/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/2tWb3BAE36
- group: commercial
  title: ''
  type: TermsOfService
  url: https://graftcode.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://graftcode.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graftcode/refs/heads/main/security/graftcode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graftcode-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://graftcode.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: 'Graftcode (Graftcode S.A.) builds an integration-free development layer: the Graftcode Gateway (gg) exposes the public classes and methods of a service written in Python, .NET, Java, JavaScript, Go, Ruby, PHP or C++ and lets other applications install a strongly-typed client (a Graft) through their own package manager, communicating over the binary Hypertube protocol instead of REST or gRPC. The gateway also serves the Graftcode Vision explorer and automatically exposes an MCP endpoint so AI agents can call the hosted methods. Graftcode publishes no public HTTP API or OpenAPI contract of its own.'
image: https://graftcode.com/assets/Integrations/pulsing-logo.png
layout: provider
modified: '2026-10-12'
name: Graftcode
nav: Providers
network: true
overview: 'Graftcode is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Integration, Cross-Language, and MCP.


  Graftcode''s developer surface includes CLI, documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Graftcode Domain Security
  slug: graftcode-domain-security
  summary_line: TLSv1.3 · DMARC
slug: graftcode
tags:
- Company
- Developer Tools
- Integration
- Cross-Language
- MCP
- Microservices
- Code Generation
website: https://graftcode.com/
---
