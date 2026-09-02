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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Civic Agentic Access
  operation_count: 7
  slug: civic-agentic-access
  summary_line: 7 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Civic Hub is a Model Context Protocol gateway that provides AI agents with secure, audited access to 80+ external tools and services through a single Streamable HTTP endpoint. Authentication uses 30-d
  name: Civic Hub MCP API
  slug: civic-hub-mcp-api
- description: Civic Auth provides OAuth 2.0 and PKCE-based authentication for web and mobile applications with support for email, Google, and Web3 wallet sign-in. Includes embedded wallet provisioning on Solana and
  name: Civic Auth API
  slug: civic-auth-api
- description: Issue and manage Civic Passes
  name: Civic pass API
  slug: civic-pass-api
- description: Get user PII and approve / reject receipt of PII
  name: Civic piirequest API
  slug: civic-piirequest-api
artifact_total: 24
collections:
- collection_type: postman
  name: Civic Customer pass API
  slug: postman-civic-pass-api
- collection_type: postman
  name: Civic Customer pass piirequest API
  slug: postman-civic-piirequest-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Civic Customer pass API
  slug: open-civic-pass-api
- collection_type: open
  name: Civic Customer pass piirequest API
  slug: open-civic-piirequest-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/civicteam/typescript-sdk/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/civic/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/civic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/civic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/civic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/civic-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.civic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.civic.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.civic.com/civic/quickstart
- group: start
  title: ''
  type: Portal
  url: https://app.civic.com
- group: start
  title: ''
  type: Signup
  url: https://app.civic.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.civic.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/civic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/civic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/civic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.civic.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.civic.com/civic/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/civicteam
- group: auth
  title: ''
  type: Security
  url: https://docs.civic.com/civic/reference/security
- group: operate
  title: ''
  type: Contact
  url: mailto:bd@civic.com
created: '2026-06-14'
description: Civic is a digital identity and security platform offering authentication, identity verification, and AI agent security infrastructure. Core products include Civic Hub (a Model Context Protocol gateway with guardrails, audit logging, secret management, and instant revocation for AI agents connecting to tools), Civic Auth (OAuth 2.0 / PKCE authentication for web and mobile apps with email, Google, and Web3 wallet sign-in plus embedded wallets on Solana and EVM chains), and Civic Labs (open-source agent infrastructure components). Originally known as a Web3 identity and KYC verification platform issuing Civic Passes (non-transferable on-chain tokens representing verified user attributes), Civic has evolved into a broader agent security layer. The Hub MCP gateway exposes a single Streamable HTTP endpoint backed by 80+ pre-built MCP server integrations and is compatible with 23+ AI agent frameworks.
examples:
- key_count: 4
  name: Civic Pass Get
  slug: civic-pass-get
- key_count: 4
  name: Civic Pass Issue
  slug: civic-pass-issue
- key_count: 4
  name: Civic Pass List
  slug: civic-pass-list
- key_count: 4
  name: Civic Pass Update
  slug: civic-pass-update
- key_count: 4
  name: Civic Pii Get
  slug: civic-pii-get
finops:
- name: Civic Finops
  service_category: Security and Identity
  slug: civic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/civic.png
json_schemas:
- name: Civic Pass Customer API Schemas
  property_count: 0
  slug: civic-pass-customer-api
jsonld:
- class_count: 2
  name: Civic Pass Context
  property_count: 25
  slug: civic-pass-context
layout: provider
modified: '2026-06-14'
name: Civic
nav: Providers
network: true
overview: 'Civic publishes 2 APIs on the [APIs.io](https://apis.io/) network: pass API and piirequest API. Tagged areas include AI Agents, Authentication, Digital Identity, Identity Verification, and KYC.


  The Civic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Civic''s developer surface includes authentication, documentation, getting-started guide, developer portal, signup flow, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Civic Plans Pricing
  plan_count: 3
  slug: civic-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Civic Rate Limits
  slug: civic-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Civic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: civic-jsonschema-spectral-rules
scopes:
- name: Civic Scopes
  scope_count: 2
  slug: civic-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 66.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 50.0
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/civic/refs/heads/main/screenshots/civic-2026-06-20T174430.png
security:
- kind: authentication
  name: Civic Authentication
  slug: civic-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Civic Domain Security
  slug: civic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: civic
tags:
- AI Agents
- Authentication
- Digital Identity
- Identity Verification
- KYC
- MCP
- Security
- Solana
- Web3
- Wallets
website: https://www.civic.com/
---
