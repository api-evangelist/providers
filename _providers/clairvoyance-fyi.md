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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/clairvoyance-fyi/security/clairvoyance-fyi-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/clairvoyance-fyi-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/clairvoyance-fyi/llms/clairvoyance-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clairvoyance-fyi-llms.txt
- group: agent
  href: https://artifacts.apis.io/clairvoyance-fyi/mcp/clairvoyance-fyi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clairvoyance-fyi-mcp.yml
- group: auth
  href: https://artifacts.apis.io/clairvoyance-fyi/well-known/clairvoyance-fyi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clairvoyance-fyi-security.txt
- group: agent
  href: https://artifacts.apis.io/clairvoyance-fyi/well-known/clairvoyance-fyi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clairvoyance-fyi-well-known.yml
- group: other
  href: https://artifacts.apis.io/clairvoyance-fyi/hosts/clairvoyance-fyi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clairvoyance-fyi-hosts.yml
- group: other
  href: https://artifacts.apis.io/clairvoyance-fyi/vendors/clairvoyance-fyi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clairvoyance-fyi-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codybrom
- group: auth
  href: https://artifacts.apis.io/clairvoyance-fyi/security/clairvoyance-fyi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clairvoyance-fyi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clairvoyance-fyi/security/clairvoyance-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clairvoyance-fyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clairvoyance.fyi/
- group: docs
  title: ''
  type: Documentation
  url: https://clairvoyance.fyi/install
- group: start
  title: ''
  type: GettingStarted
  url: https://clairvoyance.fyi/install
- group: operate
  title: ''
  type: Support
  url: https://clairvoyance.fyi/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clairvoyance.fyi/privacy
coverage:
  checked: '2026-11-03'
  detail: No machine‑readable API contract (OpenAPI/GraphQL/AsyncAPI) was found on the provider’s site.
  evidence:
  - status: 200
    url: https://clairvoyance.fyi/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Clairvoyance provides a free, open-source collection of software design skills for AI coding agents. It offers structured modules on structure, abstraction, clarity, process, and diagnostics, inspired by John Ousterhout’s design principles. The project is maintained by Cody Bromley and released under the MIT License, aiming to give AI agents “extrasensory perspective” to improve software design decisions.
image: https://clairvoyance.fyi/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at clairvoyance.fyi.
  name: Clairvoyance MCP Server
  slug: clairvoyance-fyi-mcp-yml
modified: '2026-11-03'
name: Clairvoyance
nav: Providers
network: true
overview: 'Clairvoyance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software Design, Open Source, Skills, and Education.


  Clairvoyance''s developer surface includes documentation, getting-started guide, support, and 12 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.3
    operational_transparency: 13.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clairvoyance Fyi Domain Security
  slug: clairvoyance-fyi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Clairvoyance Fyi Vulnerability Disclosure
  slug: clairvoyance-fyi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clairvoyance-fyi
tags:
- Artificial Intelligence
- Software Design
- Open Source
- Skills
- Education
website: https://clairvoyance.fyi/
---
