---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Github Enterprise Agentic Access
  operation_count: 17
  slug: github-enterprise-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Actions API from GitHub Enterprise — 2 operation(s) for actions.
  name: GitHub Enterprise Actions API
  slug: github-enterprise-actions-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Code Scanning API from GitHub Enterprise — 1 operation(s) for code scanning.
  name: GitHub Enterprise Code Scanning API
  slug: github-enterprise-code-scanning-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Enterprise Admin API from GitHub Enterprise — 1 operation(s) for enterprise admin.
  name: GitHub Enterprise Enterprise Admin API
  slug: github-enterprise-enterprise-admin-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Issues API from GitHub Enterprise — 1 operation(s) for issues.
  name: GitHub Enterprise Issues API
  slug: github-enterprise-issues-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Organizations API from GitHub Enterprise — 1 operation(s) for organizations.
  name: GitHub Enterprise Organizations API
  slug: github-enterprise-organizations-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Pull Requests API from GitHub Enterprise — 1 operation(s) for pull requests.
  name: GitHub Enterprise Pull Requests API
  slug: github-enterprise-pull-requests-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Repositories API from GitHub Enterprise — 2 operation(s) for repositories.
  name: GitHub Enterprise Repositories API
  slug: github-enterprise-repositories-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The SCIM API from GitHub Enterprise — 1 operation(s) for scim.
  name: GitHub Enterprise SCIM API
  slug: github-enterprise-scim-api
- baseURL: https://api.github.com
  baseurl_source: declared
  description: The Users API from GitHub Enterprise — 2 operation(s) for users.
  name: GitHub Enterprise Users API
  slug: github-enterprise-users-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions API
  slug: open-github-enterprise-actions-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Code Scanning API
  slug: open-github-enterprise-code-scanning-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Enterprise Admin API
  slug: open-github-enterprise-enterprise-admin-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Issues API
  slug: open-github-enterprise-issues-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Organizations API
  slug: open-github-enterprise-organizations-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Pull Requests API
  slug: open-github-enterprise-pull-requests-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Repositories API
  slug: open-github-enterprise-repositories-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions SCIM API
  slug: open-github-enterprise-scim-api
- collection_type: open
  name: GitHub Enterprise Cloud REST Actions Users API
  slug: open-github-enterprise-users-api
- collection_type: open
  name: GitHub Enterprise Cloud REST API
  slug: open-github-enterprise
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/github-enterprise-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/github-enterprise-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/github-enterprise
- group: company
  title: ''
  type: Website
  url: https://github.com/enterprise
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/enterprise-cloud@latest
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/enterprise/pricing
- group: start
  title: ''
  type: Signup
  url: https://github.com/enterprise/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://www.githubstatus.com
- group: docs
  title: ''
  type: OpenAPI Repository
  url: https://github.com/github/rest-api-description
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.github.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://github.blog/feed/
created: '2026-05-11'
description: 'GitHub Enterprise is GitHub''s offering for organizations that need advanced security, compliance, identity, and scale on top of the GitHub platform. It ships in two flavors: GitHub Enterprise Cloud, a hosted multi-tenant service on api.github.com with enterprise-managed users and SAML SSO; and GitHub Enterprise Server (GHES), a self-hosted appliance with the same REST and GraphQL APIs served from a customer''s domain at /api/v3 and /api/graphql. Both expose the full GitHub REST API for repositories, issues, pull requests, actions, packages, advanced security, audit log, SCIM, and admin operations, authenticated with personal access tokens or GitHub App tokens.'
graphqls:
- description: Hosted GitHub Enterprise Cloud REST API. Provides full access to repositories, issues, pull requests, GitHub Actions, packages, code scanning, secret scanning, Dependabot, audit log, SCIM provisioning
  name: GitHub Enterprise GraphQL API
  slug: github-enterprise-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/github-enterprise.png
layout: provider
modified: '2026-05-11'
name: GitHub Enterprise
nav: Providers
network: true
overview: 'GitHub Enterprise publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Code Scanning API, Enterprise Admin API, and 6 more. Tagged areas include Source Control, DevOps, CI/CD, Code Hosting, and Enterprise.


  GitHub Enterprise''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/github-enterprise/refs/heads/main/screenshots/github-enterprise-2026-06-20T181846.png
security:
- kind: authentication
  name: Github Enterprise Authentication
  slug: github-enterprise-authentication
  summary_line: apiKey/http · 2 schemes
slug: github-enterprise
tags:
- Source Control
- DevOps
- CI/CD
- Code Hosting
- Enterprise
- Self-Hosted
- SAML SSO
- SCIM
- Advanced Security
---
