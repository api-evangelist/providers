---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://erxes.io/pricing/self-service/frontline
  - https://erxes.io/pricing/community-edition
  - https://erxes.io/auth/signup
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: GraphQL Federation API powering the erxes XOS platform. An Apollo Router gateway federates one subgraph per plugin — core (contacts, companies, products, tags, documents, brands, organization structur
  name: Erxes GraphQL API
  slug: graphql-api
artifact_total: 9
asyncapis:
- description: ''
  name: Erxes Webhooks
  slug: erxes-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erxes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://erxes.io
- group: docs
  title: ''
  type: Documentation
  url: https://erxes.io/docs/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.erxes.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.erxes.io/self-hosting
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/erxes/erxes-skills/blob/main/agent-plugin/erxes-next/erxes-graphql-api.md
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/erxes
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/erxeshq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/erxes
- group: company
  title: ''
  type: Blog
  url: https://erxes.io/blogs
- group: operate
  title: ''
  type: Support
  url: https://erxes.io/discussions
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/aaGzy3gQK5
- group: operate
  title: ''
  type: Roadmap
  url: https://erxes.io/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://erxes.io/pricing/self-service/frontline
- group: start
  title: ''
  type: SignUp
  url: https://erxes.io/auth/signup
- group: start
  title: ''
  type: Login
  url: https://erxes.io/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://erxes.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://erxes.io/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.erxes.io
- group: auth
  title: ''
  type: Security
  url: https://github.com/erxes/erxes/blob/main/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/erxes-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/erxes-plans.md
- group: commercial
  title: ''
  type: Plans
  url: plans/erxes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/erxes-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/erxes-finops.md
- group: build
  title: ''
  type: Packages
  url: packages/erxes-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/erxes-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/erxes-cli.yml
- group: design
  title: ''
  type: Components
  url: components/erxes-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/erxes-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/erxes-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/erxes-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/erxes-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/erxes-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/erxes-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/erxes/erxes/blob/main/CHANGELOG.md
- group: design
  title: ''
  type: Conformance
  url: conformance/erxes-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/erxes-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/erxes-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/erxes-llms.txt
created: 2026-06-14
description: Open-source Experience Operating System (XOS) that unifies marketing, sales, operations and support in one self-hostable platform, positioned as a replacement for HubSpot, Zendesk, Linear and Wix. The machine surface is a GraphQL Federation API served by an Apollo Router gateway — there is no REST API and no OpenAPI — covering contacts, companies, products, tags, documents, brands, organization structure, team members and automations in the core subgraph, plus sales, frontline (inbox/tickets), operation (projects/tasks/cycles) and block plugin subgraphs. Authentication is OAuth 2.0 Device Authorization Grant with per-tenant clients and a documented 34-scope vocabulary. erxes ships the Community Edition under AGPL-3.0 alongside a proprietary Enterprise Edition, publishes its own agent plugin and agent skills, and releases roughly once per merge day.
graphqls:
- description: 'Erxes is an open-source experience operating system (XOS) built on a GraphQL Federation architecture using Apollo Router. The API is organized as a microservices monorepo where each plugin (contacts, '
  name: Erxes GraphQL API
  slug: erxes-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/erxes.png
layout: provider
modified: 2026-08-13
name: Erxes
nav: Providers
network: true
overview: 'Erxes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, CRM, Customer Experience, Open-Source, and Marketing Automation.


  The Erxes catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Erxes'' developer surface includes documentation, getting-started guide, API reference, engineering blog, support, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Erxes Plans Pricing
  plan_count: 5
  slug: erxes-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Erxes Rate Limits
  slug: erxes-rate-limits
scopes:
- name: Erxes Scopes
  scope_count: 34
  slug: erxes-scopes
  summary_line: 34 scopes · deviceCode
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 23
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 78.6
    discoverability: 83.3
    governance: 4.5
    operational_transparency: 81.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 63.0
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/erxes/refs/heads/main/screenshots/erxes-2026-06-20T180818.png
security:
- kind: authentication
  name: Erxes Authentication
  slug: erxes-authentication
  summary_line: oauth2/http · 5 schemes
- kind: domain-security
  name: Erxes Domain Security
  slug: erxes-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Erxes Vulnerability Disclosure
  slug: erxes-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: erxes
tags:
- GraphQL
- CRM
- Customer Experience
- Open-Source
- Marketing Automation
- Sales Pipeline
- Help Desk
- Ticketing
- Team Inbox
- Self-Hosted
- Apollo Federation
- Project Management
- Knowledge Base
- Webhook
- Agent Skills
website: https://erxes.io
---
