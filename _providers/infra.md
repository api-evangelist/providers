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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-11'
api_count: 8
apis:
- description: The Authentication API from Infra — 9 operation(s) for authentication.
  name: Infra Authentication API
  slug: infra-authentication-api
- description: The Destinations API from Infra — 3 operation(s) for destinations.
  name: Infra Destinations API
  slug: infra-destinations-api
- description: The Grants API from Infra — 2 operation(s) for grants.
  name: Infra Grants API
  slug: infra-grants-api
- description: The Groups API from Infra — 3 operation(s) for groups.
  name: Infra Groups API
  slug: infra-groups-api
- description: The Organizations API from Infra — 3 operation(s) for organizations.
  name: Infra Organizations API
  slug: infra-organizations-api
- description: The Providers API from Infra — 2 operation(s) for providers.
  name: Infra Providers API
  slug: infra-providers-api
- description: The Settings API from Infra — 2 operation(s) for settings.
  name: Infra Settings API
  slug: infra-settings-api
- description: The Users API from Infra — 4 operation(s) for users.
  name: Infra Users API
  slug: infra-users-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create an identity for automation and issue an access key it can use for CI/CD or API calls.
  name: Create a user and issue an access key
  slug: infra-issue-access-key
- description: Create a user, put them in a group, and grant the group access to a destination.
  name: Onboard a user and grant destination access
  slug: infra-onboard-and-grant
artifact_total: 14
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infra-mcp.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/infrahq/infra/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/infrahq/infra/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/infrahq/infra/blob/main/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://infrahq.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/infrahq/infra/tree/main/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/infrahq/infra/blob/main/docs/reference/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/infrahq/infra/blob/main/docs/quickstart.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infrahq
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/infrahq/infra
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/infra-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/infra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infra-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/infra-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infra-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infra-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infra-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infra-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infra-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infra-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infra-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infra-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/infra-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infra-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/infra-onboard-and-grant.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/infra-issue-access-key.yml
created: '2026-07-17'
description: 'Infra is open-source authentication and access management for infrastructure. It grants short-lived, identity-based access to Kubernetes clusters, servers, and databases by connecting an organization''s OIDC identity providers (Okta, Google, Azure AD, and others) to fine-grained grants on destination resources. Users and groups receive least-privilege roles, access keys are issued for CI/CD and API automation, and the `infra` CLI lets engineers list and switch into destinations. The project was originally added to the API Evangelist network as an 8vc portfolio lead; the hosted service at api.infrahq.com has since wound down (infrahq.com now redirects to the GitHub repository), but the source, OpenAPI spec, CLI, and Go client remain available under the Elastic License 2.0 (core) and MIT (SDK and connectors). Final release: v0.21.0.'
image: https://avatars.githubusercontent.com/u/85984819
layout: provider
mcp_servers:
- description: ''
  name: infra-mcp.yml
  slug: infra-mcpyml
modified: '2026-07-19'
name: Infra
nav: Providers
network: true
overview: 'Infra publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Destinations API, Grants API, and 5 more. Tagged areas include Company, Identity, Access Management, Authentication, and Authorization.


  Infra''s developer surface includes documentation, API reference, getting-started guide, CLI, authentication, changelog, and 21 more developer resources.'
random_paper: 64
score:
  band: thin
  composite: 35.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 50.6
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 35.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infra/refs/heads/main/screenshots/infra-2026-07-25T222422.png
security:
- kind: authentication
  name: Infra Authentication
  slug: infra-authentication
  summary_line: http-bearer · 4 schemes
- kind: domain-security
  name: Infra Domain Security
  slug: infra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: infra
tags:
- Company
- Identity
- Access Management
- Authentication
- Authorization
- Infrastructure
- Kubernetes
- OIDC
- Security
- Open Source
website: https://infrahq.com
---
