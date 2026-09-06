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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Silverfin''s public v4 REST API and SyncAPI for accountancy automation: companies, periods, accounts, reconciliations, reports, adjustments, budgets, workflows, users, permanent documents, exports, and'
  name: Silverfin API v4
  slug: silverfin-api-v4
artifact_total: 5
asyncapis:
- description: ''
  name: Silverfin Webhooks
  slug: silverfin-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://silverfin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.silverfin.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.silverfin.com/docs/where-to-start
- group: docs
  title: ''
  type: APIReference
  url: https://developer.silverfin.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.silverfin.com/reference/get-started-1
- group: auth
  title: ''
  type: Authentication
  url: authentication/silverfin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/silverfin-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/silverfin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/silverfin-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silverfin-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.silverfin.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.silverfin.com/docs/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/silverfin-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/silverfin-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/silverfin-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/silverfin-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/silverfin-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/silverfin-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/silverfin-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silverfin-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/silverfin
- group: build
  title: ''
  type: Postman
  url: https://developer.silverfin.com/reference/postman-library-setup
- group: operate
  title: ''
  type: Support
  url: https://community.silverfin.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silverfin-domain-security.yml
created: '2026-07-17'
description: Silverfin is a cloud connected-accounting platform for accountancy firms and finance teams that standardises and automates the financial close. It pulls ledger data from bookkeeping systems, runs working papers, reconciliations and analytical review through a Liquid-based templating language, and produces reports, PDF exports and compliance filings. Founded in Ghent, Belgium and now part of Visma, Silverfin exposes a v4 REST API plus a dedicated SyncAPI that let third-party bookkeeping software and integrators submit transactions, manage companies, periods and accounts, drive workflows, generate exports, and subscribe to webhooks — all over OAuth 2.0.
image: https://github.com/silverfin.png
layout: provider
modified: '2026-07-21'
name: Silverfin
nav: Providers
network: true
overview: 'Silverfin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Accounting, Financial Close, and Bookkeeping.


  The Silverfin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Silverfin''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, CLI, support, and 18 more developer resources.'
random_paper: 12
scopes:
- name: Silverfin Scopes
  scope_count: 19
  slug: silverfin-scopes
  summary_line: 19 scopes · authorizationCode
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 38.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 31.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silverfin/refs/heads/main/screenshots/silverfin-2026-09-02T155512.png
security:
- kind: authentication
  name: Silverfin Authentication
  slug: silverfin-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Silverfin Domain Security
  slug: silverfin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silverfin
tags:
- Company
- Business Applications
- Accounting
- Financial Close
- Bookkeeping
- Reporting
- Compliance
- Fintech
- Software-as-a-Service
- Belgium
website: https://silverfin.com
---
