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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 56.7
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The Insights API's transaction enrichment endpoints enable developers to clean and enhance their transaction data. This process includes standardizing merchant names, categorizing transactions, and ad
  name: FinGoal Enrichment API
  slug: fingoal-enrichment-api
- description: markdown/tagging.md
  name: FinGoal User Tagging API
  slug: fingoal-user-tagging-api
- description: Manage webhook callback URLs for your client. Supports default and tenant-specific configurations per webhook type.
  name: FinGoal Webhook Configurations API
  slug: fingoal-webhook-configurations-api
artifact_total: 9
asyncapis:
- description: ''
  name: Fingoal Webhooks
  slug: fingoal-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fingoal.com/developer-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fingoal.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fingoal.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fingoal.dev/
- group: build
  title: ''
  type: Postman
  url: https://fingoal.dev/FinGoal%20Enrichment.postman_collection.json
- group: start
  title: ''
  type: SignUp
  url: https://fingoal.com/request-developer-account
- group: company
  title: ''
  type: Blog
  url: https://fingoal.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fingoal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fingoal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fingoal.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://fingoal.com/fingoal-privacy-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/fingoal-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fingoal-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fingoal-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fingoal-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fingoal-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fingoal-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fingoal-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fingoal-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fingoal-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fingoal-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fingoal-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fingoal-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fingoal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fingoal.com/
created: '2026-07-17'
description: 'FinGoal provides financial data insights for banks, credit unions, and fintechs. Its Insights API enriches raw bank and card transaction data with clean merchant names, categorization, and behavioral "Persona Tags" that power personalized recommendations, targeted offers, and better banking features. The API is batch-oriented: developers submit transactions, receive a batch_request_id, and collect enriched results by polling or via ENRICHMENT_DATA and USER_TAGS_DATA webhooks. FinGoal also offers Link Money for account aggregation and verification across 17,000+ financial institutions. Authentication uses a JWT minted from client_id/client_secret; developer credentials are issued on request. FinGoal is SOC 2 Type II and GDPR compliant.'
image: https://cdn.prod.website-files.com/61d89a2cbc85dcbc83bb0f7c/637402586ca49d150ef97dc2_Website%20Open%20Graph%20%20Thumbnail.png
layout: provider
mcp_servers:
- description: ''
  name: fingoal-mcp.yml
  slug: fingoal-mcpyml
modified: '2026-07-19'
name: FinGoal
nav: Providers
network: true
overview: 'FinGoal publishes 3 APIs on the [APIs.io](https://apis.io/) network: Enrichment API, User Tagging API, and Webhook Configurations API. Tagged areas include Financial Services, Fintech, Transaction Enrichment, Data Enrichment, and Personal Financial Management.


  The FinGoal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FinGoal''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, sandbox, and 19 more developer resources.'
random_paper: 22
scopes:
- name: Fingoal Scopes
  scope_count: 3
  slug: fingoal-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 58.7
  delta: 5.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.0
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 53.7
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 87.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Fingoal Authentication
  slug: fingoal-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fingoal Domain Security
  slug: fingoal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fingoal Trust Center
  slug: fingoal-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: fingoal
tags:
- Financial Services
- Fintech
- Transaction Enrichment
- Data Enrichment
- Personal Financial Management
- Banking
- Categorization
- Webhooks
website: https://fingoal.com/
---
