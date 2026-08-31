---
access_model:
  confidence: high
  label: Self-serve signup with a 30-day trial
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - https://www.opensanctions.org/api/
  - https://www.opensanctions.org/docs/api/authentication/
  - https://www.opensanctions.org/docs/api/faq/
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Opensanctions Agentic Access
  operation_count: 12
  slug: opensanctions-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- description: REST API for screening people, companies, vessels and other entities against sanctions, watchlist and PEP data. Query-by-example matching returns scored candidates with per-feature explanations; free-
  name: OpenSanctions Screening API
  slug: opensanctions-screening-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opensanctions-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opensanctions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opensanctions.org/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.opensanctions.org/articles/rss/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.opensanctions.org/docs/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.opensanctions.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.opensanctions.org/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.opensanctions.org/docs/api/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://www.opensanctions.org/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://discuss.opensanctions.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opensanctions
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/opensanctions/api-examples
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opensanctions.org/api/
- group: start
  title: ''
  type: SignUp
  url: https://www.opensanctions.org/api/
- group: start
  title: ''
  type: Login
  url: https://www.opensanctions.org/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opensanctions.org/docs/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opensanctions.org/docs/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.opensanctions.org/docs/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opensanctions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/opensanctions-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opensanctions.org/docs/security/
- group: design
  title: ''
  type: Conformance
  url: conformance/opensanctions-conformance.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opensanctions.org/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.opensanctions.org/docs/data/changes/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opensanctions-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opensanctions-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opensanctions-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opensanctions-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opensanctions-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opensanctions-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/opensanctions-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/opensanctions-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/opensanctions-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/opensanctions-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opensanctions-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opensanctions-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opensanctions-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/opensanctions-data-model.yml
created: '2026-05-28'
description: OpenSanctions is an open database of international sanctions, watchlists, criminal designations and politically exposed persons (PEPs), published as a screening API, bulk data downloads and MIT-licensed open-source software from Berlin. It consolidates hundreds of primary government sources — OFAC, the EU consolidated list, UN Security Council, UK FCDO, procurement debarment registers, regulatory enforcements and national PEP registers — into a single de-duplicated entity graph expressed in the FollowTheMoney ontology it stewards. The hosted Screening API at api.opensanctions.org offers query-by-example entity matching with scored, per-feature explanations, free-text search, entity fetch with relationship traversal, statement-level provenance for every asserted value, and an OpenRefine reconciliation manifest. It is used for customer due diligence, transaction monitoring, supply-chain and vessel screening, KYB, and investigative journalism. The dataset is free for non-commercial
  use under CC BY-NC 4.0; commercial use is licensed, and the API is metered at EUR 0.10 per query.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opensanctions.png
layout: provider
mcp_servers:
- description: ''
  name: OpenSanctions MCP Server
  slug: opensanctions-mcp-server
modified: '2026-08-27'
name: OpenSanctions
nav: Providers
network: true
overview: 'OpenSanctions publishes 1 API on the [APIs.io](https://apis.io/) network: Screening API. Tagged areas include Sanctions Screening, Anti-Money Laundering, Politically Exposed Persons, Compliance, and Financial Crime.


  OpenSanctions'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Opensanctions Plans Pricing
  plan_count: 4
  slug: opensanctions-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Opensanctions Rate Limits
  slug: opensanctions-rate-limits
score:
  band: exemplar
  composite: 74.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 85.7
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 74.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/screenshots/opensanctions-2026-06-20T191029.png
security:
- kind: authentication
  name: Opensanctions Authentication
  slug: opensanctions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opensanctions Domain Security
  slug: opensanctions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opensanctions Vulnerability Disclosure
  slug: opensanctions-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Opensanctions Trust Center
  slug: opensanctions-trust-center
  summary_line: ISO/IEC 27001:2022
slug: opensanctions
tags:
- Sanctions Screening
- Anti-Money Laundering
- Politically Exposed Persons
- Compliance
- Financial Crime
- Know Your Customer
- Entity Resolution
- Open Data
- Risk Data
- Due Diligence
- Public APIs
- agent-native
website: https://www.opensanctions.org/
---
