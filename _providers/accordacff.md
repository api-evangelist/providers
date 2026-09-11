---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-10'
api_count: 2
apis:
- description: A single GraphQL endpoint exposing the Accord data model — accords, stages, steps, stakeholders, playbooks, resources, summaries, engagement and CRM sync objects. The public reference documents 461 qu
  name: Accord Developer API (GraphQL)
  slug: accord-developer-api-graphql
- description: Hosted, remote Model Context Protocol server that wraps the Accord Developer API and exposes its read surface to any MCP client (Claude, Claude Code, Cursor, Gemini CLI, ChatGPT). Streamable HTTP tran
  name: Accord MCP Server
  slug: accord-mcp-server
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accordacff-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inaccord.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.inaccord.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.inaccord.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.inaccord.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.inaccord.com/quickstarts/accords
- group: operate
  title: ''
  type: Support
  url: https://collaboration.inaccord.com/knowledge
- group: operate
  title: ''
  type: HelpCenter
  url: https://collaboration.inaccord.com/knowledge
- group: company
  title: ''
  type: Blog
  url: https://inaccord.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://inaccord.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://inaccord.com/book-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inaccord.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inaccord.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inaccord
- group: auth
  title: ''
  type: Authentication
  url: authentication/accordacff-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/accordacff-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accordacff-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accordacff-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accordacff-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accordacff-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/accordacff-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/accordacff-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accordacff-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accordacff-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accordacff-rate-limits.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accordacff-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/accordacff-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accordacff-llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/accordacff-graphql-operations.yml
created: '2026-09-06'
description: Accord is a San Francisco-based revenue excellence platform for B2B sales, onboarding and customer success teams, founded in 2020 by Ross Rich and Ryan Rich. It turns a company's winning sales process into enforceable playbooks, mutual action plans and shared buyer workspaces, with stakeholder mapping, deal reviews, execution scoring and bi-directional CRM sync. Its developer surface is a single GraphQL endpoint at api2.inaccord.com/graphql covering 20+ objects (Accords, Stages, Steps, Contacts, Members, Resources, Summaries, Engagements) behind a workspace-scoped bearer API key, plus a hosted, OAuth 2.1 + PKCE Model Context Protocol server at api.inaccord.com that exposes the same read surface to MCP clients such as Claude, Cursor and ChatGPT.
image: https://cdn.prod.website-files.com/68d3df3714cf3a122c1640dd/6916517cbf54f093700a336d_Home%20Page_OG-min.png
layout: provider
mcp_servers:
- description: Hosted, remote Model Context Protocol server published by Accord. Per Accord's own announcement it "wraps our Developer API and exposes the same read endpoints through a secure, standardized interface
  name: Accord MCP Server
  slug: accord-mcp-server
- description: ''
  name: Accord MCP Server
  slug: accord-mcp-server-2
modified: '2026-09-06'
name: Accord
nav: Providers
network: true
overview: 'Accord publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Enablement, Revenue Operations, Customer Collaboration, Sales Engagement, and Customer Onboarding.


  Accord''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Accordacff Plans Pricing
  plan_count: 3
  slug: accordacff-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Accordacff Rate Limits
  slug: accordacff-rate-limits
scopes:
- name: Accordacff Scopes
  scope_count: 0
  slug: accordacff-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 39.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Accordacff Authentication
  slug: accordacff-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Accordacff Domain Security
  slug: accordacff-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Accordacff Vulnerability Disclosure
  slug: accordacff-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Accordacff Trust Center
  slug: accordacff-trust-center
  summary_line: SOC 2 Type II, SSO Authentication, GCP Secure
slug: accordacff
tags:
- Sales Enablement
- Revenue Operations
- Customer Collaboration
- Sales Engagement
- Customer Onboarding
- Mutual Action Plans
- CRM
- GraphQL
- MCP
- agent-native
- SaaS
- Company
website: https://inaccord.com/
---
