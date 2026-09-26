---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 15
  human_in_the_loop: 15
  name: Ninox Agentic Access
  operation_count: 23
  slug: ninox-agentic-access
  summary_line: 23 operations · 15 acting · 15 human-in-the-loop
api_count: 1
apis:
- baseURL: https://go.ninox.com
  baseurl_source: declared
  description: The Fields API from Ninox — 3 operation(s) for fields.
  name: Ninox Fields API
  slug: ninox-fields-api
- baseURL: https://go.ninox.com
  baseurl_source: declared
  description: The Modules API from Ninox — 2 operation(s) for modules.
  name: Ninox Modules API
  slug: ninox-modules-api
- baseURL: https://go.ninox.com
  baseurl_source: declared
  description: The Records API from Ninox — 2 operation(s) for records.
  name: Ninox Records API
  slug: ninox-records-api
- baseURL: https://go.ninox.com
  baseurl_source: declared
  description: The Tables API from Ninox — 2 operation(s) for tables.
  name: Ninox Tables API
  slug: ninox-tables-api
- baseURL: https://go.ninox.com
  baseurl_source: declared
  description: The Workspace API from Ninox — 1 operation(s) for workspace.
  name: Ninox Workspace API
  slug: ninox-workspace-api
arazzos:
- description: Create a table in a module, add fields in batch, insert records, then read them back.
  name: Ninox — Create a table and add records
  slug: ninox-create-table-and-add-records
- description: Create a module in a workspace, add a table, and define its fields.
  name: Ninox — Provision a module with tables and fields
  slug: ninox-provision-module
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ninox Public Fields API
  slug: open-ninox-fields-api
- collection_type: open
  name: Ninox Public Fields Modules API
  slug: open-ninox-modules-api
- collection_type: open
  name: Ninox Public Fields Records API
  slug: open-ninox-records-api
- collection_type: open
  name: Ninox Public Fields Tables API
  slug: open-ninox-tables-api
- collection_type: open
  name: Ninox Public Fields Workspace API
  slug: open-ninox-workspace-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/overlays/ninox-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ninox-public-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ninox.com/ninox-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ninox.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ninox.com/ninox-api/api-reference/api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ninox.com/ninox-api/api-reference/introduction-to-ninox-public-api
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/authentication/ninox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ninox-authentication.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://go.ninox.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://go.ninox.com/user/signup
- group: start
  title: ''
  type: Login
  url: https://go.ninox.com/user/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://go.ninox.com/en/legal-notices/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://go.ninox.com/en/legal-notices/privacy
- group: operate
  title: ''
  type: Support
  url: https://go.ninox.com/en/resources/support
- group: company
  title: ''
  type: Blog
  url: https://go.ninox.com/en/resources/blog
- group: operate
  title: ''
  type: Community
  url: https://forum.ninox.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://forum.ninox.com/category/service-status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/changelog/ninox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ninox-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/lifecycle/ninox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ninox-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/llms/ninox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ninox-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/packages/ninox-packages.yml
  title: ''
  type: Packages
  url: packages/ninox-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/cli/ninox-cli.yml
  title: ''
  type: CLI
  url: cli/ninox-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/mcp/ninox-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ninox-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/conventions/ninox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ninox-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/errors/ninox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ninox-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/conformance/ninox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ninox-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/data-model/ninox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ninox-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/arazzo/ninox-create-table-and-add-records.yml
  title: ''
  type: Arazzo
  url: arazzo/ninox-create-table-and-add-records.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/arazzo/ninox-provision-module.yml
  title: ''
  type: Arazzo
  url: arazzo/ninox-provision-module.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/agentic-access/ninox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ninox-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/security/ninox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ninox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ninox.com/
created: '2026-07-17'
description: Ninox is an AI-native low-code database and application platform that lets business teams build custom apps, databases, and workflows without traditional coding. Teams model data as modules, tables, fields, and records, automate processes with the Ninox scripting language, generate documents, and collaborate across organizations and workspaces. The Ninox Public REST API provides programmatic access to workspace resources — creating and managing modules, tables, fields, and records, plus CSV import — authenticated with per-workspace API keys sent as bearer tokens. Ninox is delivered as public cloud, private cloud, and on-premises deployments, and is backed by Techstars.
image: https://ninox.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Ninox
nav: Providers
network: true
overview: 'Ninox publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Fields API, Modules API, Records API, and 2 more. Tagged areas include Company, Low-Code, Database, No-Code, and Application Development.


  Ninox''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, support, and 24 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 45.5
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/screenshots/ninox-2026-08-07T185329.png
security:
- kind: authentication
  name: Ninox Authentication
  slug: ninox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ninox Domain Security
  slug: ninox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ninox
tags:
- Company
- Low-Code
- Database
- No-Code
- Application Development
- Workflow Automation
- Business Apps
- Productivity
website: https://ninox.com/
---
