---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Memori API provides endpoints for agent memory, conversation, and management.
  name: Memori API
  slug: memori-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/memorilabs/plans/memorilabs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/memorilabs-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/memorilabs/authentication/memorilabs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/memorilabs-authentication.yml
- group: design
  href: https://artifacts.apis.io/memorilabs/conformance/memorilabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memorilabs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/memorilabs/llms/memorilabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memorilabs-llms.txt
- group: other
  href: https://artifacts.apis.io/memorilabs/hosts/memorilabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memorilabs-hosts.yml
- group: other
  href: https://artifacts.apis.io/memorilabs/vendors/memorilabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memorilabs-vendors.yml
- group: build
  href: https://artifacts.apis.io/memorilabs/packages/memorilabs-packages.yml
  title: ''
  type: SDKs
  url: packages/memorilabs-packages.yml
- group: build
  href: https://artifacts.apis.io/memorilabs/packages/memorilabs-packages.yml
  title: ''
  type: Packages
  url: packages/memorilabs-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://memorilabs.ai/playground/
- group: start
  title: ''
  type: GettingStarted
  url: https://memorilabs.ai/docs/memori-cloud/getting-started/python-quickstart
- group: auth
  href: https://artifacts.apis.io/memorilabs/security/memorilabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memorilabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memorilabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://memorilabs.ai/docs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memorilabs.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://memorilabs.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://memorilabs.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.memorilabs.ai/signup
created: '2026-10-18'
description: Memori Labs provides an agent‑native memory infrastructure that captures, classifies, and persists conversational state for production AI systems. It offers a LLM‑agnostic layer turning agent execution into structured data, with features like automatic remembering, customizable retention, and secure storage, enabling developers to build reliable, stateful AI applications.
image: https://memorilabs.ai/og-image.png
layout: provider
modified: '2026-10-18'
name: Memori Labs
nav: Providers
network: true
overview: 'Memori Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Memory, Agents, and Infrastructure.


  Memori Labs'' developer surface includes authentication, sandbox, getting-started guide, documentation, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Memorilabs Plans Pricing
  plan_count: 5
  slug: memorilabs-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 30.9
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Memorilabs Authentication
  slug: memorilabs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Memorilabs Domain Security
  slug: memorilabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: memorilabs
tags:
- Company
- Artificial Intelligence
- Memory
- Agents
- Infrastructure
website: https://memorilabs.ai/
---
