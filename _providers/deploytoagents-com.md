---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Deploy to Agents provides an MCP (Machine-Readable Catalog) for AI agents to discover and interact with deployed applications.
  name: Deploy to Agents API
  slug: deploy-to-agents-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/deploytoagents-com/plans/deploytoagents-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deploytoagents-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/deploytoagents-com/llms/deploytoagents-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deploytoagents-com-llms.txt
- group: other
  href: https://artifacts.apis.io/deploytoagents-com/a2a/deploytoagents-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deploytoagents-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/deploytoagents-com/well-known/deploytoagents-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deploytoagents-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/deploytoagents-com/hosts/deploytoagents-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deploytoagents-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/deploytoagents-com/packages/deploytoagents-com-packages.yml
  title: ''
  type: SDKs
  url: packages/deploytoagents-com-packages.yml
- group: build
  href: https://artifacts.apis.io/deploytoagents-com/packages/deploytoagents-com-packages.yml
  title: ''
  type: Packages
  url: packages/deploytoagents-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deploytoagents.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deploytoagents.com/privacy
- group: auth
  href: https://artifacts.apis.io/deploytoagents-com/security/deploytoagents-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deploytoagents-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deploytoagents.com/
- group: docs
  title: ''
  type: Documentation
  url: https://deploytoagents.com/#guides
- group: commercial
  title: ''
  type: Pricing
  url: https://deploytoagents.com/#pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://deploytoagents.com/onboarding
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite probing known spec endpoints and the MCP endpoint returned only a 406 error.
  evidence:
  - status: 406
    url: https://deploytoagents.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Deploy to Agents provides distribution infrastructure that makes software discoverable, verifiable, and invocable by AI agents. It offers free, pro, and business plans, enabling developers to publish their applications so AI agents can find and interact with them across platforms.
image: https://deploytoagents.com/opengraph-image.png?opengraph-image.03h-3tcuctd.c.png
layout: provider
modified: '2026-11-05'
name: We Are 14, Inc.
nav: Providers
network: true
overview: 'We Are 14, Inc. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Distribution, Platform, Software, and Agents.


  We Are 14, Inc.''s developer surface includes documentation, pricing, getting-started guide, and 11 more developer resources.'
plans:
- name: Deploytoagents Com Plans Pricing
  plan_count: 4
  slug: deploytoagents-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deploytoagents Com Domain Security
  slug: deploytoagents-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: deploytoagents-com
tags:
- Artificial Intelligence
- Distribution
- Platform
- Software
- Agents
website: https://deploytoagents.com/
---
