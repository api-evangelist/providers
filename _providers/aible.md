---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: The Aible API server (self-reported version 2.0.0) is the control plane behind the Aible platform. Its published route index lists 394 routes under the /v1 prefix across 29 modules — account, project,
  name: Aible API
  slug: aible-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/security/aible-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aible-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aible.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.iamaible.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aible.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.aible.com/partner_support
- group: start
  title: ''
  type: Login
  url: https://www.iamaible.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-77t5fm3cysegw
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aible.com/aible-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aible.com/privacy-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/changelog/aible-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aible-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/plans/aible-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aible-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/rate-limits/aible-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aible-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/authentication/aible-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aible-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/errors/aible-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aible-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/conventions/aible-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aible-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/data-model/aible-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aible-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/lifecycle/aible-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aible-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/conformance/aible-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aible-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/packages/aible-packages.yml
  title: ''
  type: Packages
  url: packages/aible-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aible/refs/heads/main/llms/aible-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aible-llms.txt
created: '2026-09-14'
description: Aible is an enterprise AI company founded in 2018 and headquartered in Pleasanton, California, that lets business users build and run AI agents, AutoML models and generative-AI analytics against data that stays inside the customer's own AWS, Azure, GCP or on-premise account. The platform is organized around projects, segments, scenarios, training data, jobs, models, deployments and content-generation collections, and is operated through a public REST API served at api.iamaible.com. That API server publishes its own route index — 394 routes across 29 modules at /v1, protected by bearer user, tenant and STS tokens — but Aible ships no OpenAPI, AsyncAPI, MCP server, agent card, SDK or public developer portal. Commercial access is sold as prepaid Flex Credits through the AWS and Google Cloud marketplaces.
image: https://www.aible.com/hubfs/Aible_Corp_Logo_Orange_White.svg
layout: provider
modified: '2026-09-14'
name: Aible
nav: Providers
network: true
overview: 'Aible publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine-Learning, AutoML, Analytics, and Data Science.


  Aible''s developer surface includes API reference, engineering blog, support, pricing, changelog, authentication, and 14 more developer resources.'
plans:
- name: Aible Plans Pricing
  plan_count: 4
  slug: aible-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Aible Rate Limits
  slug: aible-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 28.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aible Authentication
  slug: aible-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aible Domain Security
  slug: aible-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aible
tags:
- Artificial Intelligence
- Machine-Learning
- AutoML
- Analytics
- Data Science
- AI Agents
- Generative AI
- Enterprise Software
- Cloud
- Company
website: https://www.aible.com/
---
