---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Polycode Co Uk Agentic Access
  operation_count: 50
  slug: polycode-co-uk-agentic-access
  summary_line: 50 operations · 24 acting
api_count: 2
apis:
- baseURL: https://marginalia.polycode.co.uk/api
  baseurl_source: declared
  description: 'Public read + chat REST API for marginalia, the memory-graph chat agent operated by Polycode Limited. 50 operations under /api: async one-turn chat with task polling, an OpenAI-shaped mechanical compl'
  name: marginalia public API
  slug: marginalia-public-api
- description: 'Agent2Agent (A2A) surface for marginalia: an agent card served from https://marginalia.polycode.co.uk/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC, version 0.2.0) advertising three skil'
  name: marginalia A2A Agent
  slug: marginalia-a2a-agent
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://marginalia.polycode.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://marginalia.polycode.co.uk/developers
- group: docs
  title: ''
  type: Documentation
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://marginalia.polycode.co.uk/api/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/README.md#talk-to-it--the-a2a-api
- group: start
  title: ''
  type: Login
  url: https://marginalia.polycode.co.uk/auth/login
- group: operate
  title: ''
  type: Support
  url: mailto:antony@polycode.co.uk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marginalia.polycode.co.uk/#legal-text-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marginalia.polycode.co.uk/#legal-text-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/_developers/ETHICS.md
- group: commercial
  title: ''
  type: License
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/LICENSE
- group: other
  title: ''
  type: OpenSource
  url: https://gitlab.com/polycode-projects/marginalia
- group: build
  title: ''
  type: GitLabRepositories
  url: https://gitlab.com/polycode-projects/marginalia
- group: build
  title: ''
  type: GitLabOrganizations
  url: https://gitlab.com/polycode-projects
- group: operate
  title: ''
  type: RoadMap
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/NEXT.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/a2a/polycode-co-uk-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/polycode-co-uk-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/well-known/polycode-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/polycode-co-uk-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/llms/polycode-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/polycode-co-uk-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/authentication/polycode-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/polycode-co-uk-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/conventions/polycode-co-uk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/polycode-co-uk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/errors/polycode-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/polycode-co-uk-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/lifecycle/polycode-co-uk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/polycode-co-uk-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/conformance/polycode-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/polycode-co-uk-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/data-model/polycode-co-uk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/polycode-co-uk-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/sandbox/polycode-co-uk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/polycode-co-uk-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/plans/polycode-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/polycode-co-uk-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/rate-limits/polycode-co-uk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/polycode-co-uk-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/packages/polycode-co-uk-packages.yml
  title: ''
  type: Packages
  url: packages/polycode-co-uk-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/cli/polycode-co-uk-cli.yml
  title: ''
  type: CLI
  url: cli/polycode-co-uk-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/agentic-access/polycode-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/polycode-co-uk-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/security/polycode-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polycode-co-uk-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/polycode-co-uk/refs/heads/main/security/polycode-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/polycode-co-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/_developers/ETHICS.md
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/_developers/ETHICS.md
- group: other
  title: ''
  type: AITransparency
  url: https://marginalia.polycode.co.uk/
- group: other
  title: ''
  type: NoticeAndAction
  url: https://marginalia.polycode.co.uk/
- group: other
  title: ''
  type: DataResidency
  url: https://gitlab.com/polycode-projects/marginalia/-/blob/main/README.md#operating
created: '2026-09-19'
description: 'Polycode Limited is a UK information-technology consultancy (Companies House 10172940, Leeds, incorporated 2016) that operates marginalia, a small public chat experiment built on a shared, provenance-tracked memory graph: a language model synthesises conversations into an OWL-typed graph and questions are answered by narrowing that graph with SPARQL. marginalia publishes a public REST API (OpenAPI 3.0.3, 50 operations at https://marginalia.polycode.co.uk/api — async chat with task polling, session search and history, insights, projects, usage and budget, key-authed private graphs; no key for reads and chat), an A2A 0.3.0 agent card at /.well-known/agent-card.json with a live JSON-RPC endpoint (message/send, message/stream, tasks/get) advertising chat, recall-memory and research-projects skills, an OpenAI-shaped zero-token completion shim, a first-party CLI and the AGPL-3.0 source on GitLab. Visitor contributions are PII-redacted at ingest and republished under CC-BY-SA 4.0;
  a volatile flag keeps a turn out of shared memory. The corporate apex polycode.co.uk did not resolve when profiled; the product host is the live web presence.'
image: https://marginalia.polycode.co.uk/favicon.svg
layout: provider
modified: '2026-09-19'
name: Polycode
nav: Providers
network: true
overview: 'Polycode publishes 1 API on the [APIs.io](https://apis.io/) network: marginalia public API. Tagged areas include Chat, Memory, Agents, A2A, and Knowledge Graph.


  Polycode''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, CLI, and 31 more developer resources.'
plans:
- name: Polycode Co Uk Plans Pricing
  plan_count: 0
  slug: polycode-co-uk-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Polycode Co Uk Rate Limits
  slug: polycode-co-uk-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 35.4
    developer_ergonomics: 70.8
    discoverability: 68.5
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Polycode Co Uk Authentication
  slug: polycode-co-uk-authentication
  summary_line: none/apiKey/openIdConnect/hmac · 4 schemes
- kind: domain-security
  name: Polycode Co Uk Domain Security
  slug: polycode-co-uk-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Polycode Co Uk Vulnerability Disclosure
  slug: polycode-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: polycode-co-uk
tags:
- Chat
- Memory
- Agents
- A2A
- Knowledge Graph
- Research
- Artificial Intelligence
- Open Source
- Consulting
- United Kingdom
website: https://marginalia.polycode.co.uk/
---
