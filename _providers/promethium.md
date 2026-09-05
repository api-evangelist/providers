---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for Promethium's agentic data platform — tenant-scoped OAuth2 authentication, datamap search and creation, bulk metadata import, audit logs, and federated SQL execution via the Trino Stream U
  name: Promethium API
  slug: promethium-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://promethium.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.promethium.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.promethium.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.promethium.ai/docs/api-intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.promethium.ai/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://promethium.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://promethium.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://promethium.ai/trial
- group: operate
  title: ''
  type: Support
  url: https://promethium.ai/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://promethium.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promethium.ai/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/promethium-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/promethium-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/promethium-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/promethium-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/promethium-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/promethium-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Promethium is an open agentic data platform that gives analysts, business users, and AI agents trusted access to all enterprise data through a single governed layer without moving, copying, or consolidating data. Its AI Insights Fabric combines a zero-copy federated Universal Query Engine (Trino) across cloud warehouses, relational databases, SaaS apps and on-prem systems, an Insights Context Graph that assembles business definitions and semantic models, and a Trust Harness that validates answers before delivery. Promethium exposes governed data to any agent, copilot, or application through a single MCP server or REST API, with its Mantra engine powering plain-English agentic analytics. Backed by Insight Partners; led by CEO Prat Moghe.
image: https://promethium.ai/wp-content/themes/promethium/assets/images/src/favicon.png
layout: provider
modified: '2026-07-20'
name: Promethium
nav: Providers
network: true
overview: 'Promethium publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Fabric, Agentic Analytics, Semantic Layer, and Enterprise Data.


  Promethium''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 11 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 29.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/promethium/refs/heads/main/screenshots/promethium-2026-09-02T152139.png
security:
- kind: authentication
  name: Promethium Authentication
  slug: promethium-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Promethium Domain Security
  slug: promethium-domain-security
  summary_line: TLSv1.3 · DMARC
slug: promethium
tags:
- Company
- Data Fabric
- Agentic Analytics
- Semantic Layer
- Enterprise Data
- MCP
- Federated Query
- Data Governance
website: https://promethium.ai/
---
