---
access_model:
  confidence: high
  label: Free tier, self-serve paid plans from $20/month
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - https://www.enigma.com/pricing
  - plans/enigma-plans-pricing.yml
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: GraphQL API for querying Enigma business data — brands, operating locations, legal entities, card transactions, and industries — with text, lookup, natural-language prompt, and async segmentation sear
  name: Enigma GraphQL Data API
  slug: enigma-graphql-data-api
- description: REST API for business identity verification and compliance — identify and verify packages with TIN/EIN verification, OFAC watchlist screening, and SSN verification add-on tasks. A /v2/kyb-legacy/ endp
  name: Enigma KYB REST API
  slug: enigma-kyb-rest-api
- description: 'REST API for sanctions and watchlist screening of customers and transactions. Weighted-attribute ENTITY screening and unstructured TEXT screening, plus LLM-enhanced variants that add live web search; '
  name: Enigma Screening API
  slug: enigma-screening-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/enigma-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.enigma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.enigma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.enigma.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.enigma.com/reference/graphql_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.enigma.com/guides/graphql/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enigma-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.enigma.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.enigma.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.enigma.com/company/support
- group: start
  title: ''
  type: SignUp
  url: https://console.enigma.com/
- group: start
  title: ''
  type: Login
  url: https://console.enigma.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enigma.com/company/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enigma.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enigma.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.enigma.com/legal/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/enigma-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enigma-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enigma-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/enigma-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/enigma-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enigma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.enigma.com/legal/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enigma-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enigma-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enigma-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enigma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enigma-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/enigma-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/enigma-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/enigma-graphql-surface.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/enigma-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/enigma-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enigma-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/enigma-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/enigma-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/enigma-robots.txt
created: '2026-07-17'
description: Enigma provides business identity infrastructure for the United States, built on entity-resolution technology that links brands, DBAs, operating locations, legal entities, and ownership into unified business records. Its Identity Graph aggregates hundreds of public and third-party sources plus 750M+ anonymized cards and 30B+ annual transactions, powering KYB and onboarding, sanctions and negative-news screening, payment risk and underwriting, and go-to-market data. Developers access this through a GraphQL Data API, a KYB v2 REST API, a sanctions Screening REST API, and a remote MCP server exposing sixteen published tools under OAuth 2.1. Enigma also publishes its own Agent Skills as a Claude Code plugin, an llms.txt, and hard plan-tiered rate limits.
image: https://www.enigma.com/favicon.ico
layout: provider
mcp_servers:
- description: 'Remote MCP server for U.S. business intelligence: entity resolution, KYB verification, sanctions and negative-news screening, card-transaction analytics, and public-records search. Returns structured '
  name: Enigma MCP Server
  slug: enigma-mcp-server
modified: '2026-08-14'
name: Enigma
nav: Providers
network: true
overview: 'Enigma publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Data, Identity Resolution, KYB, and Compliance.


  Enigma''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 31 more developer resources.'
plans:
- name: Enigma Plans Pricing
  plan_count: 4
  slug: enigma-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Enigma Rate Limits
  slug: enigma-rate-limits
scopes:
- name: Enigma Scopes
  scope_count: 1
  slug: enigma-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 49.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enigma/refs/heads/main/screenshots/enigma-2026-07-25T213358.png
security:
- kind: authentication
  name: Enigma Authentication
  slug: enigma-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Enigma Domain Security
  slug: enigma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enigma Vulnerability Disclosure
  slug: enigma-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Enigma Trust Center
  slug: enigma-trust-center
  summary_line: SOC 2
slug: enigma
tags:
- Company
- Business Data
- Identity Resolution
- KYB
- Compliance
- Fraud
- GraphQL
- Data Enrichment
- Financial-Services
- MCP
- Sanctions Screening
- Agent Skills
website: https://www.enigma.com/
---
