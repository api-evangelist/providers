---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Toolrouter API for secure endpoint integration
  name: Toolrouter API
  slug: toolrouter-api
- baseURL: https://api.toolrouter.ai
  baseurl_source: declared
  description: Toolrouter API for secure endpoint integration
  name: Toolrouter API Api-reference API
  slug: toolrouter-api-api-reference-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/toolrouter/rules/toolrouter-rules.yml
  title: ''
  type: Spectral
  url: rules/toolrouter-rules.yml
- group: design
  href: https://artifacts.apis.io/toolrouter/conformance/toolrouter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toolrouter-conformance.yml
- group: auth
  href: https://artifacts.apis.io/toolrouter/authentication/toolrouter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toolrouter-authentication.yml
- group: design
  href: https://artifacts.apis.io/toolrouter/errors/toolrouter-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/toolrouter-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/toolrouter/llms/toolrouter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toolrouter-llms.txt
- group: other
  href: https://artifacts.apis.io/toolrouter/a2a/toolrouter-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/toolrouter-a2a.yml
- group: agent
  href: https://artifacts.apis.io/toolrouter/well-known/toolrouter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/toolrouter-well-known.yml
- group: other
  href: https://artifacts.apis.io/toolrouter/hosts/toolrouter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toolrouter-hosts.yml
- group: other
  href: https://artifacts.apis.io/toolrouter/vendors/toolrouter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toolrouter-vendors.yml
- group: build
  href: https://artifacts.apis.io/toolrouter/packages/toolrouter-packages.yml
  title: ''
  type: SDKs
  url: packages/toolrouter-packages.yml
- group: build
  href: https://artifacts.apis.io/toolrouter/packages/toolrouter-packages.yml
  title: ''
  type: Packages
  url: packages/toolrouter-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.toolrouter.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.toolrouter.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://toolrouter.ai/blog/toolrouter-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.toolrouter.ai/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.toolrouter.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.toolrouter.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/toolrouter/security/toolrouter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toolrouter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toolrouter.ai/
created: '2026-10-19'
description: ToolRouter is an AI‑powered workflow platform designed to help founders and early‑stage startups turn ideas into repeatable actions. The service offers a library of pre‑built templates and custom command capabilities that automate product‑market‑fit analysis, user‑behavior tracking, and growth‑stage planning. By integrating with popular tools and providing a collaborative environment, ToolRouter aims to accelerate the journey from concept validation to scaling for ambitious entrepreneurs.
image: https://www.toolrouter.ai/images/home-og.png
layout: provider
modified: '2026-10-19'
name: ToolRouter
nav: Providers
network: true
overview: 'ToolRouter publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Api-reference API, and 1 more. Tagged areas include Artificial Intelligence, Workflows, Startups, Automation, and Founders.


  The ToolRouter catalog on APIs.io includes 1 Spectral governance ruleset.


  ToolRouter''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 14 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ToolRouter API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: toolrouter-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Toolrouter Authentication
  slug: toolrouter-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Toolrouter Domain Security
  slug: toolrouter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toolrouter
tags:
- Artificial Intelligence
- Workflows
- Startups
- Automation
- Founders
website: https://toolrouter.ai/
---
