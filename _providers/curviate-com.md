---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Agent-native LinkedIn infrastructure API.
  name: Curviate API
  slug: curviate-api
artifact_total: 6
asyncapis:
- description: ''
  name: Curviate Com Webhooks
  slug: curviate-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/curviate-com/plans/curviate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curviate-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/curviate-com/asyncapi/curviate-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/curviate-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/curviate-com/conventions/curviate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/curviate-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/curviate-com/authentication/curviate-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curviate-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/curviate-com/conformance/curviate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curviate-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/curviate-com/llms/curviate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/curviate-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/curviate-com/well-known/curviate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curviate-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/curviate-com/hosts/curviate-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curviate-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/curviate-com/packages/curviate-com-packages.yml
  title: ''
  type: Packages
  url: packages/curviate-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://curviate.com/resources/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curviate.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://curviate.com/product/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curviate.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.curviate.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.curviate.com/reference/mcp/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.curviate.com/reference
- group: auth
  href: https://artifacts.apis.io/curviate-com/security/curviate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curviate-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curviate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curviate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.curviate.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://curviate.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://curviate.com/blog
created: '2026-10-30'
description: Curviate provides a LinkedIn API for AI agents, offering REST, CLI, MCP and SDK interfaces. It enables agents to access LinkedIn data such as profiles, companies, jobs, posts, and messaging, with built-in caching, rate limits, and webhooks for real‑time events. The platform includes a CLI tool, SDKs for multiple languages, and an MCP agent‑native interface, all documented with an OpenAPI spec. Curviate aims to simplify building AI‑driven LinkedIn integrations while ensuring safety and compliance.
image: https://curviate.com/curviate-og-1200x630.png
layout: provider
modified: '2026-10-30'
name: curviate-com
nav: Providers
network: true
overview: 'curviate-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Curviate API. Tagged areas include AI, LinkedIn, API, Automation, and Agent.


  The curviate-com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  curviate-com''s developer surface includes authentication, changelog, getting-started guide, API reference, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Curviate Com Plans Pricing
  plan_count: 2
  slug: curviate-com-plans-pricing
random_paper: 7
scopes:
- name: Curviate Com Scopes
  scope_count: 0
  slug: curviate-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.2
    catalog_earned_first_party: 0.0
    catalog_gap: 70.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.5
    contract_governance: 16.4
    contract_quality: 39.0
    developer_ergonomics: 59.5
    discoverability: 66.1
    operational_transparency: 23.7
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Curviate Com Authentication
  slug: curviate-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Curviate Com Domain Security
  slug: curviate-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curviate-com
tags:
- AI
- LinkedIn
- API
- Automation
- Agent
website: https://curviate.com/
---
