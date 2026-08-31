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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A single GraphQL endpoint for the Filed platform. Create clients and ingest source documents into a binder, trigger tax prep and tax advisor runs and poll them to completion, read leadsheets and revie
  name: Filed API
  slug: filed-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.filed.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apps.filed.com/
- group: company
  title: ''
  type: Blog
  url: https://www.filed.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.filed.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.filed.com/early-access
- group: start
  title: ''
  type: Login
  url: https://web.apps.filed.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.filed.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.filed.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.filed.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/filed-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/filed-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/filed-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/filed-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/filed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/filed-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/filed-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.apps.filed.com/mcp
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/filed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/filed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/filed-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/filed-domain-security.yml
created: '2026-07-17'
description: Filed is an AI tax platform for accounting firms and tax professionals. It reads source documents (W-2s, 1099s, K-1s, brokerage statements, prior-year returns), compares them line by line against the draft return to catch errors and find optimizations, performs actual data entry into professional tax software (Drake, ProConnect, UltraTax, CCH Axcess, Lacerte, ProSeries), and evaluates 120+ tax strategies to produce client-ready tax plans with citations. Firms keep the tax software they already use; Filed sits inside the existing workflow via three products — Filed Reviewer, Filed Prep, and Filed Tax Planner. Filed exposes a GraphQL API (router.apps.filed.com/graphql), a remote MCP server, and an embeddable binder UI. Backed by Northzone, Day One Ventures, and Neo.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/filed.png
layout: provider
mcp_servers:
- description: Remote MCP server (OAuth via Dynamic Client Registration, no API key) exposing docs, run_batch_queries, run_batch_mutations, and get_file_upload_info. Built but not yet live in production. Detail in m
  name: Filed MCP Server
  slug: filed-mcp-server
modified: '2026-07-19'
name: Filed
nav: Providers
network: true
overview: 'Filed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, Accounting, Artificial Intelligence, and Document Processing.


  Filed''s developer surface includes engineering blog, pricing, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 33.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/filed/refs/heads/main/screenshots/filed-2026-07-25T214447.png
security:
- kind: authentication
  name: Filed Authentication
  slug: filed-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Filed Domain Security
  slug: filed-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Filed Vulnerability Disclosure
  slug: filed-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Filed Trust Center
  slug: filed-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, SOC 3
slug: filed
tags:
- Company
- Tax
- Accounting
- Artificial Intelligence
- Document Processing
- GraphQL
- Compliance
- Enterprise
website: https://www.filed.com
---
