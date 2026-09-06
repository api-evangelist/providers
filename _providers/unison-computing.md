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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
  score: 10.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The API powering the Unison Share web application, including the APIs for syncing code with UCM and browsing projects, branches, and definitions. Unison Share also acts as the OAuth2 (with PKCE) and O
  name: Unison Share API
  slug: unison-share-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/unisoncomputing/share-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/unisoncomputing/share-api/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unison-computing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unison-lang.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.unison.cloud
- group: docs
  title: ''
  type: Documentation
  url: https://www.unison-lang.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.unison-lang.org/docs/at-a-glance/
- group: operate
  title: ''
  type: Support
  url: https://www.unison-lang.org/community/
- group: company
  title: ''
  type: Blog
  url: https://www.unison-lang.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unisonweb
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unison.cloud/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.unison.cloud/signup/?plan=Free
- group: start
  title: ''
  type: Login
  url: https://app.unison.cloud
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unison.cloud/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unison.cloud/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/unison-computing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unison-computing-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unison-computing-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unison-computing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unison-computing-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/unison-computing-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unison-computing-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unison-computing-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unison-computing-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/unison-computing-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unison-computing-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unison Computing, PBC is a public benefit corporation building the Unison programming language, Unison Cloud, and Unison Share. Unison is a statically-typed functional language where code is content-addressed and immutable; Unison Cloud deploys Unison services to the cloud with a function call, with typed service-to-service calls and typed durable storage; Unison Share is the community code host and package registry. Unison Share's open-source backend also serves as the OAuth2 (PKCE) and OpenID Connect authentication server for UCM and Unison Cloud, and UCM ships a built-in MCP server plus official LLM coding-assistant instructions for AI agents.
image: https://github.com/unisonweb.png
layout: provider
mcp_servers:
- description: ''
  name: Unison Computing MCP Server
  slug: unison-computing-mcp-server
modified: '2026-07-21'
name: Unison Computing
nav: Providers
network: true
overview: 'Unison Computing publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Programming Languages, Cloud Computing, Developer Tools, and Functional Programming.


  Unison Computing''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 0.0
  previous_composite: 30.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unison-computing/refs/heads/main/screenshots/unison-computing-2026-09-02T164915.png
security:
- kind: authentication
  name: Unison Computing Authentication
  slug: unison-computing-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Unison Computing Domain Security
  slug: unison-computing-domain-security
  summary_line: TLSv1.3 · HSTS
slug: unison-computing
tags:
- Company
- Programming Languages
- Cloud Computing
- Developer Tools
- Functional Programming
- Distributed Systems
- Platform-as-a-Service
website: https://www.unison-lang.org/
---
