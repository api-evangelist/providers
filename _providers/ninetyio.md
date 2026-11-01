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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 15
  name: Ninetyio Agentic Access
  operation_count: 25
  slug: ninetyio-agentic-access
  summary_line: 25 operations · 15 acting · 15 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.public.ninety.io/v1
  baseurl_source: declared
  description: The Issues API from Ninety.io — 3 operation(s) for issues.
  name: Ninety.io Issues API
  slug: ninetyio-issues-api
- baseURL: https://api.public.ninety.io/v1
  baseurl_source: declared
  description: The Milestones API from Ninety.io — 2 operation(s) for milestones.
  name: Ninety.io Milestones API
  slug: ninetyio-milestones-api
- baseURL: https://api.public.ninety.io/v1
  baseurl_source: declared
  description: The Rocks API from Ninety.io — 3 operation(s) for rocks.
  name: Ninety.io Rocks API
  slug: ninetyio-rocks-api
- baseURL: https://api.public.ninety.io/v1
  baseurl_source: declared
  description: The Scorecard API from Ninety.io — 5 operation(s) for scorecard.
  name: Ninety.io Scorecard API
  slug: ninetyio-scorecard-api
- baseURL: https://api.public.ninety.io/v1
  baseurl_source: declared
  description: The Teams API from Ninety.io — 1 operation(s) for teams.
  name: Ninety.io Teams API
  slug: ninetyio-teams-api
- baseURL: https://api.public.ninety.io/v1
  baseurl_source: declared
  description: The To-Dos API from Ninety.io — 3 operation(s) for to-dos.
  name: Ninety.io To-Dos API
  slug: ninetyio-to-dos-api
- baseURL: https://api.public.ninety.io/v1
  baseurl_source: declared
  description: The Users API from Ninety.io — 1 operation(s) for users.
  name: Ninety.io Users API
  slug: ninetyio-users-api
arazzos:
- description: Resolve a team, create a quarterly Rock, and attach a Milestone to it.
  name: Create a Ninety Rock with Milestones
  slug: ninetyio-create-rock-with-milestones
- description: Resolve a team, create an Issue on its list, then mark it solved.
  name: Log and Solve a Ninety Issue
  slug: ninetyio-log-and-solve-issue
artifact_total: 27
collections:
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
- group: commercial
  href: https://artifacts.apis.io/ninetyio/plans/ninetyio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ninetyio-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ninety.io/eos/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ninety.io/eos/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/ninetyio/capabilities/ninetyio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ninetyio-capability-edges.yml
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
  href: https://artifacts.apis.io/ninetyio/authentication/ninetyio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ninetyio-authentication.yml
- group: design
  href: https://artifacts.apis.io/ninetyio/conventions/ninetyio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ninetyio-conventions.yml
- group: design
  href: https://artifacts.apis.io/ninetyio/errors/ninetyio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ninetyio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ninetyio/lifecycle/ninetyio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ninetyio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ninetyio/conformance/ninetyio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ninetyio-conformance.yml
- group: design
  href: https://artifacts.apis.io/ninetyio/data-model/ninetyio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ninetyio-data-model.yml
- group: operate
  href: https://artifacts.apis.io/ninetyio/changelog/ninetyio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ninetyio-changelog.yml
- group: agent
  href: https://artifacts.apis.io/ninetyio/mcp/ninetyio-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ninetyio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ninetyio/llms/ninetyio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ninetyio-llms.txt
- group: other
  href: https://artifacts.apis.io/ninetyio/overlays/ninetyio-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ninetyio-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ninetyio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ninetyio/arazzo/ninetyio-create-rock-with-milestones.yml
  title: ''
  type: Arazzo
  url: arazzo/ninetyio-create-rock-with-milestones.yml
- group: design
  href: https://artifacts.apis.io/ninetyio/arazzo/ninetyio-log-and-solve-issue.yml
  title: ''
  type: Arazzo
  url: arazzo/ninetyio-log-and-solve-issue.yml
- group: agent
  href: https://artifacts.apis.io/ninetyio/agentic-access/ninetyio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ninetyio-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ninetyio/security/ninetyio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ninetyio-domain-security.yml
created: '2026-07-17'
description: Ninety.io (Ninety) is a software platform for implementing the Entrepreneurial Operating System (EOS). It gives founders and leadership teams purpose-built tools for the Accountability Chart, the Vision/Traction Organizer (V/TO), quarterly Rocks, the weekly Scorecard, To-Dos, the Issues List, and EOS meeting rhythms such as the Level 10 meeting. Ninety exposes a REST Public API (v1) at api.public.ninety.io authenticated with per-user Personal Access Tokens, giving programmatic create/read/update/delete access to To-Dos, Issues, Rocks, Milestones, Scorecard measurables (KPIs, scores, notes), Teams, and Users.
finops:
- has_sources: true
  method: derived
  name: Ninetyio Finops
  primary_unit: user
  service_category: ''
  slug: ninetyio-finops
  template: false
image: https://www.ninety.io/hubfs/LI_Thumb_Home.jpg
layout: provider
modified: '2026-10-06'
name: Ninety.io
nav: Providers
network: true
overview: 'Ninety.io publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Issues API, Milestones API, Rocks API, and 4 more. Tagged areas include Company, EOS, Entrepreneurial Operating System, Business Management, and Meetings.


  Ninety.io''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Ninetyio Plans Pricing
  plan_count: 4
  slug: ninetyio-plans-pricing
- name: Ninetyio Price Estimates
  plan_count: 0
  slug: ninetyio-price-estimates
random_paper: 15
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 41.3
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 44.8
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ninetyio/ninetyio-2026-08-07T185322.png
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
skill_count: 4
skills:
- name: Manage Ninety Issues
  slug: ninetyio-manage-issues
- name: Manage Ninety Rocks and Milestones
  slug: ninetyio-manage-rocks-milestones
- name: Manage Ninety To-Dos
  slug: ninetyio-manage-todos
- name: Update Ninety Scorecard
  slug: ninetyio-update-scorecard
slug: ninetyio
tags:
- Company
- EOS
- Entrepreneurial Operating System
- Business Management
- Meetings
- Productivity
- Scorecards
- Team Management
- Goal Tracking
website: https://www.ninety.io/
---
