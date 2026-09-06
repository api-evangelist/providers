---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The HTTP surface exposed by a Dara application. Dara is causaLens'' Apache-2.0 open-source Python framework built on FastAPI; each app serves a documented set of built-in routes (session verification, '
  name: Dara Application Framework HTTP API
  slug: dara-application-framework-http-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/causalens-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/causalens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://causalens.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dara.causalens.com
- group: docs
  title: ''
  type: Documentation
  url: https://dara.causalens.com/docs/generated/dara/docs/getting-started/whats-dara
- group: docs
  title: ''
  type: APIReference
  url: https://dara.causalens.com/docs/generated/dara/reference/dara/core/auth/routes
- group: start
  title: ''
  type: GettingStarted
  url: https://dara.causalens.com/docs/generated/dara/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/causalens
- group: operate
  title: ''
  type: Support
  url: https://github.com/causalens/dara/issues
- group: company
  title: ''
  type: Blog
  url: https://causalens.com/resource-hub
- group: start
  title: ''
  type: SignUp
  url: https://platform.causalens.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://causalens.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://causalens.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.causalens.com
- group: build
  title: ''
  type: Packages
  url: packages/causalens-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/causalens-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/causalens-cli.yml
- group: design
  title: ''
  type: Components
  url: components/causalens-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/causalens-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/causalens-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/causalens-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/causalens-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/causalens-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/causalens-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/causalens-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: causaLens is a London-headquartered enterprise AI company and a pioneer of Causal AI — machine intelligence that models cause-and-effect relationships rather than correlation alone. Its commercial platform, decisionOS, is a decision-making operating system that combines causal discovery, causal graph modelling, and multi-agent "Digital Knowledge Workers" that automate repetitive data-science and analyst workflows for enterprises. The platform is delivered as a hosted product plus a Python-first interface, and is distributed through the Microsoft Azure Marketplace and the UK G-Cloud Digital Marketplace. causaLens also maintains Dara, an Apache-2.0 open-source Python application framework for building interactive, decision-support web apps, published on GitHub with packages on PyPI and npm and full public documentation.
image: https://avatars.githubusercontent.com/u/40164755?s=200&v=4
layout: provider
mcp_servers:
- description: ''
  name: CausaLens MCP Server
  slug: causalens-mcp-server
modified: '2026-08-09'
name: CausaLens
nav: Providers
network: true
overview: 'CausaLens publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Causal AI, Machine-Learning, and Data Science.


  CausaLens'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 19 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 33.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/causalens/refs/heads/main/screenshots/causalens-2026-09-02T145021.png
security:
- kind: authentication
  name: Causalens Authentication
  slug: causalens-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Causalens Domain Security
  slug: causalens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: causalens
tags:
- Company
- Artificial Intelligence
- Causal AI
- Machine-Learning
- Data Science
- Decision Intelligence
- Analytics
- Agents
- Open-Source
- Python
website: https://causalens.com
---
