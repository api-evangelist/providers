---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - plans
  - https://hashnode.com/pro
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Hashnode Public API is a GraphQL API that queries publication data, manages posts and drafts, and creates content via mutations. All requests are POSTed to a single endpoint at https://gql-beta.ha
  name: Hashnode GraphQL API
  slug: hashnode-graphql-api
artifact_total: 9
asyncapis:
- description: ''
  name: Hashnode Webhooks
  slug: hashnode-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://hashnode.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/Hashnode/gql-skill
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Hashnode/gql-skill/tree/main/skills/gql-api
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Hashnode/gql-skill/blob/main/skills/gql-api/references/queries.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Hashnode/gql-skill#using-the-api-directly
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hashnode
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Hashnode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hashnode
- group: other
  title: ''
  type: X
  url: https://x.com/hashnode
- group: company
  title: ''
  type: Blog
  url: https://hashnode.com/blog
- group: operate
  title: ''
  type: Support
  url: https://hashnode.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://hashnode.com/pro
- group: start
  title: ''
  type: SignUp
  url: https://hashnode.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hashnode.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hashnode.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hashnode.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://hashnode.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hashnode-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/hashnode-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hashnode-lifecycle.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/hashnode-gql-api.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/hashnode-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hashnode-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hashnode-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hashnode-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hashnode-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hashnode-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/hashnode-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hashnode-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hashnode-cli.yml
- group: design
  title: ''
  type: Components
  url: components/hashnode-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hashnode-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/hashnode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hashnode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hashnode-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hashnode-domain-security.yml
created: '2026-06-13'
description: Hashnode is a blogging platform for developers and engineering teams, offering publications on a custom domain, a headless CMS mode, and a public GraphQL API covering posts, drafts, publications, users, tags, series, comments and documentation projects. The API is a single GraphQL endpoint with anonymous introspection; authentication is a Personal Access Token in the Authorization header, with no OAuth and no scopes. Since 13 May 2026 the API has been a paid feature - anonymous public reads still work, but every publication-scoped read and every write mutation requires the target publication to hold an active Hashnode Pro plan. Hashnode publishes no OpenAPI and no MCP server, shipping an official Agent Skill instead.
finops:
- name: Hashnode Finops
  service_category: API
  slug: hashnode-finops
graphqls:
- description: The Hashnode API is a GraphQL API that allows developers to interact with the Hashnode blogging platform, manage posts, publications, and user data.
  name: Hashnode GraphQL API
  slug: hashnode-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hashnode.png
layout: provider
modified: '2026-08-13'
name: Hashnode
nav: Providers
network: true
overview: 'Hashnode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blogging, Developer Platform, GraphQL, Content Management, and Publications.


  The Hashnode catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hashnode''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Hashnode Plans Pricing
  plan_count: 3
  slug: hashnode-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Hashnode Rate Limits
  slug: hashnode-rate-limits
score:
  band: strong
  composite: 58.3
  delta: 0.7
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 52.2
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 57.6
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hashnode/refs/heads/main/screenshots/hashnode-2026-08-17T083521.png
security:
- kind: authentication
  name: Hashnode Authentication
  slug: hashnode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hashnode Domain Security
  slug: hashnode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hashnode Vulnerability Disclosure
  slug: hashnode-vulnerability-disclosure
  summary_line: Hackerone
slug: hashnode
tags:
- Blogging
- Developer Platform
- GraphQL
- Content Management
- Publications
- Newsletters
- Headless CMS
- Agent Skills
- Developer Community
- Documentation
website: https://hashnode.com
---
