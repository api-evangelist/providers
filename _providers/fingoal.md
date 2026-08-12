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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-11'
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
- group: other
  title: ''
  type: Overlay
  url: overlays/fingoal-insights-overlay.yaml
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


  FinGoal''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, sandbox, and 20 more developer resources.'
random_paper: 40
scopes:
- name: Fingoal Scopes
  scope_count: 3
  slug: fingoal-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 53.5
  delta: -1.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.3
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 55.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fingoal/refs/heads/main/screenshots/fingoal-2026-07-25T214520.png
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
