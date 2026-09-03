---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Monday Com Agentic Access
  operation_count: 1
  slug: monday-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: An expressive GraphQL API to interact with monday.com workflows, boards, items, users, and updates - automate processes, power integrations, and more.
  name: Monday.com API
  slug: monday-com
- baseURL: https://api.monday.com/v2
  baseurl_source: declared
  description: The Monday.com Platform GraphQL API API from Monday.com — 1 operation(s) for monday.com platform graphql api.
  name: Monday.com Monday.com Platform GraphQL API API
  slug: monday-com-monday-com-platform-graphql-api-api
artifact_total: 32
asyncapis:
- description: AsyncAPI 2.6 description of the monday.com webhook surface. monday.com webhooks deliver real-time board, item, subitem, column, and update events to a consumer-controlled HTTPS endpoint via HTTP POST.
  name: monday.com Webhooks
  slug: monday-com-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: monday.com Platform GraphQL Monday.com Platform GraphQL API API
  slug: open-monday-com-monday-com-platform-graphql-api-api
- collection_type: open
  name: monday.com Platform GraphQL API
  slug: open-monday-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monday-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/monday-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monday-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monday-com-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/monday-com-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mondaycom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mondaydotcom
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.monday.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://monday.com/blog
created: '2025-02-17'
description: An expressive API to interact with your workflows, automate processes, power integrations, and more!
features:
- Free for up to 2 users with 3 boards
- Basic at $9/seat/mo with unlimited items and viewers
- Standard at $12/seat/mo with 250 automation/integration actions
- Pro at $19/seat/mo with 25K automation/integration actions
- Enterprise with 250K actions, multi-level permissions, AI bundle
- GraphQL API at api.monday.com/v2
- 'Complexity budget: 5M points/min per account'
- Default 5K requests/day (raise via support)
- 10 concurrent requests cap
- Webhooks for board, item, column changes
- OAuth 2.0 and API tokens
- monday Apps Framework for marketplace apps
- Files API with S3-backed uploads
- Custom column types via Apps
- monday Forms and monday WorkForms
- monday CRM, Dev, Service product variants
finops:
- name: Monday Com Finops
  service_category: Work Management
  slug: monday-com-finops
graphqls:
- description: An expressive GraphQL API to interact with monday.com workflows, boards, items, users, and updates - automate processes, power integrations, and more.
  name: Monday.com GraphQL API
  slug: monday-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monday-com.png
layout: provider
modified: '2026-05-29'
name: Monday.com
nav: Providers
network: true
overview: 'Monday.com publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Monday.com Platform GraphQL API API, and 1 more. Tagged areas include Work Management, CRM, Automation, and GraphQL.


  The Monday.com catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Monday.com''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Monday Com Plans Pricing
  plan_count: 5
  slug: monday-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Monday Com Rate Limits
  slug: monday-com-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Monday.com API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: monday-com-asyncapi-spectral-rules
scopes:
- name: Monday Com Scopes
  scope_count: 7
  slug: monday-com-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 74.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 64.9
    developer_ergonomics: 13.1
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 14.5
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monday-com/refs/heads/main/screenshots/monday-com-2026-06-20T185722.png
security:
- kind: authentication
  name: Monday Com Authentication
  slug: monday-com-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Monday Com Domain Security
  slug: monday-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Monday Com Trust Center
  slug: monday-com-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: monday-com
tags:
- Work Management
- CRM
- Automation
- GraphQL
---
