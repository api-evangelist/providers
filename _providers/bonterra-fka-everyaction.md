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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The EveryAction 8 (EA8) / NGP VAN REST API for nonprofit and campaign CRM data — people matching, contributions, recurring commitments, disbursements, events, survey questions, activist codes, canvass
  name: EveryAction (NGP VAN) API
  slug: everyaction-ngp-van-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bonterra-fka-everyaction-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.everyaction.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.everyaction.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.everyaction.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.everyaction.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.everyaction.com/recipes/first-api-call
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.everyaction.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NGPVAN
- group: auth
  title: ''
  type: Authentication
  url: authentication/bonterra-fka-everyaction-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bonterra-fka-everyaction-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bonterra-fka-everyaction-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bonterra-fka-everyaction-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bonterra-fka-everyaction-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bonterra-fka-everyaction-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bonterra-fka-everyaction-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/bonterra-fka-everyaction-packages.yml
created: '2026-07-17'
description: Bonterra (formerly EveryAction) is a social-good technology company whose EveryAction / NGP VAN platform powers fundraising, advocacy, organizing, and supporter engagement for nonprofits, unions, and political campaigns. The EveryAction 8 (EA8) REST API at api.securevan.com/v4 exposes people matching, contributions and recurring commitments, disbursements, events, survey questions, activist codes, canvass responses, bulk import and file-loading jobs, early-vote and voter-registration fields, employers/worksites, scores, printed lists, and MiniVAN exports. It uses HTTP Basic authentication with an application name and an API key scoped to a database mode (My Voters or My Campaign), and is documented on a ReadMe-hosted developer portal with a reference, recipes, changelog, and an llms.txt.
image: https://docs.everyaction.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Bonterra (fka EveryAction) MCP Server
  slug: bonterra-fka-everyaction-mcp-server
modified: '2026-07-18'
name: Bonterra (fka EveryAction)
nav: Providers
network: true
overview: 'Bonterra (fka EveryAction) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Non-Profit, Fundraising, and Advocacy.


  Bonterra (fka EveryAction)''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 17.1
  provenance:
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bonterra-fka-everyaction/refs/heads/main/screenshots/bonterra-fka-everyaction-2026-07-25T203601.png
security:
- kind: authentication
  name: Bonterra Fka Everyaction Authentication
  slug: bonterra-fka-everyaction-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bonterra Fka Everyaction Domain Security
  slug: bonterra-fka-everyaction-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonterra-fka-everyaction
tags:
- Company
- CRM
- Non-Profit
- Fundraising
- Advocacy
- Political
- Voter Engagement
- Donor Management
- Organizing
website: https://www.everyaction.com/
---
