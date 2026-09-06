---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: https://findmoney.fingoal.com/v3
  baseurl_source: declared
  description: The Insights API's transaction enrichment endpoints enable developers to clean and enhance their transaction data. This process includes standardizing merchant names, categorizing transactions, and ad
  name: FinGoal Enrichment API
  slug: fingoal-enrichment-api
- baseURL: https://findmoney.fingoal.com/v3
  baseurl_source: declared
  description: markdown/tagging.md
  name: FinGoal User Tagging API
  slug: fingoal-user-tagging-api
- baseURL: https://findmoney.fingoal.com/v3
  baseurl_source: declared
  description: Manage webhook callback URLs for your client. Supports default and tenant-specific configurations per webhook type.
  name: FinGoal Webhook Configurations API
  slug: fingoal-webhook-configurations-api
- baseURL: https://findmoney.fingoal.com/v3
  baseurl_source: declared
  description: 'There are three kinds of people who interact with Link Money: - **Users** are the people who use the Link Money application. They are the people who log in, view their accounts, and make transactions.'
  name: FinGoal Client Management API
  slug: fingoal-client-management-api
- baseURL: https://findmoney.fingoal.com/v3
  baseurl_source: declared
  description: The Link Money API permits end users to link and get data from their bank accounts. But of course, that requires a front-end interface. That's where the Fastlink comes in. The Fastlink is an example o
  name: FinGoal Fastlink API
  slug: fingoal-fastlink-api
- baseURL: https://findmoney.fingoal.com/v3
  baseurl_source: declared
  description: The Oauth API from FinGoal — 1 operation(s) for oauth.
  name: FinGoal OAUTH API
  slug: fingoal-oauth-api
- baseURL: https://findmoney.fingoal.com/v3
  baseurl_source: declared
  description: 'Webhook payload schemas for all webhook types. Configure which webhooks you receive using the Webhook Configurations endpoints. **Available Webhook Types:** - `ENRICHMENT_DATA`: Data-rich Transaction '
  name: FinGoal Webhooks API
  slug: fingoal-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Fingoal Link Money Webhooks
  slug: fingoal-link-money-webhooks
- description: ''
  name: Fingoal Webhooks
  slug: fingoal-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Insights Enrichment API
  slug: open-fingoal-enrichment-api
- collection_type: open
  name: Insights Enrichment User Tagging API
  slug: open-fingoal-user-tagging-api
- collection_type: open
  name: Insights Enrichment Webhook Configurations API
  slug: open-fingoal-webhook-configurations-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fingoal-link-money-overlay.yaml
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
  type: X-MCPServerCandidate
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
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fingoal-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/fingoal-components.yml
- group: operate
  title: ''
  type: Support
  url: https://fingoal.com/contact
- group: company
  title: ''
  type: Website
  url: https://fingoal.com/
created: '2026-07-17'
description: 'FinGoal provides financial data insights for banks, credit unions, and fintechs. Its Insights API enriches raw bank and card transaction data with clean merchant names, categorization, and behavioral "Persona Tags" that power personalized recommendations, targeted offers, and better banking features. The API is batch-oriented: developers submit transactions, receive a batch_request_id, and collect enriched results by polling or via ENRICHMENT_DATA and USER_TAGS_DATA webhooks. FinGoal also offers Link Money for account aggregation and verification across 17,000+ financial institutions. Authentication uses a JWT minted from client_id/client_secret; developer credentials are issued on request. FinGoal is SOC 2 Type II and GDPR compliant.'
image: https://cdn.prod.website-files.com/61d89a2cbc85dcbc83bb0f7c/637402586ca49d150ef97dc2_Website%20Open%20Graph%20%20Thumbnail.png
layout: provider
modified: '2026-08-14'
name: FinGoal
nav: Providers
network: true
overview: 'FinGoal publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Enrichment API, User Tagging API, Webhook Configurations API, and 4 more. Tagged areas include Financial-Services, Fintech, Transaction Enrichment, Data Enrichment, and Personal Financial Management.


  The FinGoal catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  FinGoal''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, sandbox, and 24 more developer resources.'
plans:
- name: Fingoal Plans Pricing
  plan_count: 0
  slug: fingoal-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Fingoal Rate Limits
  slug: fingoal-rate-limits
scopes:
- name: Fingoal Scopes
  scope_count: 3
  slug: fingoal-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 61.5
    developer_ergonomics: 42.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 55.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 69.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fingoal/refs/heads/main/screenshots/fingoal-2026-07-25T214520.png
security:
- kind: authentication
  name: Fingoal Authentication
  slug: fingoal-authentication
  summary_line: oauth2 · 2 schemes
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
- Financial-Services
- Fintech
- Transaction Enrichment
- Data Enrichment
- Personal Financial Management
- Banking
- Categorization
- Webhook
website: https://fingoal.com/
---
