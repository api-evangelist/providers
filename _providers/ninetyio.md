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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 19
  name: Ninetyio Agentic Access
  operation_count: 25
  slug: ninetyio-agentic-access
  summary_line: 25 operations · 19 acting · 19 human-in-the-loop
api_count: 7
apis:
- description: The Issues API from Ninety.io — 3 operation(s) for issues.
  name: Ninety.io Issues API
  slug: ninetyio-issues-api
- description: The Milestones API from Ninety.io — 2 operation(s) for milestones.
  name: Ninety.io Milestones API
  slug: ninetyio-milestones-api
- description: The Rocks API from Ninety.io — 3 operation(s) for rocks.
  name: Ninety.io Rocks API
  slug: ninetyio-rocks-api
- description: The Scorecard API from Ninety.io — 5 operation(s) for scorecard.
  name: Ninety.io Scorecard API
  slug: ninetyio-scorecard-api
- description: The Teams API from Ninety.io — 1 operation(s) for teams.
  name: Ninety.io Teams API
  slug: ninetyio-teams-api
- description: The To-Dos API from Ninety.io — 3 operation(s) for to-dos.
  name: Ninety.io To-Dos API
  slug: ninetyio-to-dos-api
- description: The Users API from Ninety.io — 1 operation(s) for users.
  name: Ninety.io Users API
  slug: ninetyio-users-api
arazzos:
- description: Resolve a team, create a quarterly Rock, and attach a Milestone to it.
  name: Create a Ninety Rock with Milestones
  slug: ninetyio-create-rock-with-milestones
- description: Resolve a team, create an Issue on its list, then mark it solved.
  name: Log and Solve a Ninety Issue
  slug: ninetyio-log-and-solve-issue
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ninety Public Issues API
  slug: open-ninetyio-issues-api
- collection_type: open
  name: Ninety Public Issues Milestones API
  slug: open-ninetyio-milestones-api
- collection_type: open
  name: Ninety Public Issues Rocks API
  slug: open-ninetyio-rocks-api
- collection_type: open
  name: Ninety Public Issues Scorecard API
  slug: open-ninetyio-scorecard-api
- collection_type: open
  name: Ninety Public Issues Teams API
  slug: open-ninetyio-teams-api
- collection_type: open
  name: Ninety Public Issues To-Dos API
  slug: open-ninetyio-to-dos-api
- collection_type: open
  name: Ninety Public Issues Users API
  slug: open-ninetyio-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.ninety.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.ninety.io/en/articles/15505694-api-reference-and-access
- group: docs
  title: ''
  type: APIReference
  url: https://api.public.ninety.io/v1/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ninety.io/en/articles/15505694-api-reference-and-access
- group: operate
  title: ''
  type: Support
  url: https://help.ninety.io/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ninety.io/
- group: operate
  title: ''
  type: Community
  url: https://community.ninety.io/
- group: company
  title: ''
  type: Blog
  url: https://www.ninety.io/updates
- group: operate
  title: ''
  type: Roadmap
  url: https://www.ninety.io/product-updates
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ninety.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.ninety.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.ninety.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ninety.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ninety.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ninety.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ninety.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ninetyio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ninetyio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ninetyio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ninetyio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ninetyio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ninetyio-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ninetyio-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ninetyio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ninetyio-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/ninetyio-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ninetyio-create-rock-with-milestones.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ninetyio-log-and-solve-issue.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ninetyio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ninetyio-domain-security.yml
created: '2026-07-17'
description: Ninety.io (Ninety) is a software platform for implementing the Entrepreneurial Operating System (EOS). It gives founders and leadership teams purpose-built tools for the Accountability Chart, the Vision/Traction Organizer (V/TO), quarterly Rocks, the weekly Scorecard, To-Dos, the Issues List, and EOS meeting rhythms such as the Level 10 meeting. Ninety exposes a REST Public API (v1) at api.public.ninety.io authenticated with per-user Personal Access Tokens, giving programmatic create/read/update/delete access to To-Dos, Issues, Rocks, Milestones, Scorecard measurables (KPIs, scores, notes), Teams, and Users.
image: https://www.ninety.io/hubfs/LI_Thumb_Home.jpg
layout: provider
mcp_servers:
- description: ''
  name: ninetyio-mcp.yml
  slug: ninetyio-mcpyml
modified: '2026-07-20'
name: Ninety.io
nav: Providers
network: true
overview: 'Ninety.io publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Issues API, Milestones API, Rocks API, and 4 more. Tagged areas include Company, EOS, Entrepreneurial Operating System, Business Management, and Meetings.


  Ninety.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 46.7
  delta: 0.1
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 16.7
    contract_quality: 50.6
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ninetyio/refs/heads/main/screenshots/ninetyio-2026-08-07T185322.png
security:
- kind: authentication
  name: Ninetyio Authentication
  slug: ninetyio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ninetyio Domain Security
  slug: ninetyio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ninetyio Trust Center
  slug: ninetyio-trust-center
  summary_line: trust center published
slug: ninetyio
tags:
- Company
- EOS
- Entrepreneurial Operating System
- Business Management
- Meetings
- Productivity
- Scorecard
- Team Management
- Goal Tracking
website: https://www.ninety.io/
---
