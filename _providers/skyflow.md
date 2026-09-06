---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Insert, retrieve, tokenize/detokenize, query, and manage records and files in a Skyflow data privacy vault. Authenticated with a JWT bearer token or API key (RFC 6750). Base URLs are per-vault under t
  name: Skyflow Data API
  slug: skyflow-data-api
- description: Create and manage vaults, workspaces, service accounts, roles, policies, and other account resources. Authenticated with a JWT bearer token.
  name: Skyflow Management API
  slug: skyflow-management-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/skyflow-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/skyflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.skyflow.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skyflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.skyflow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skyflow.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skyflow.com/api/data
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skyflow.com/get-started/
- group: build
  title: ''
  type: SDKs
  url: packages/skyflow-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/skyflow-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skyflowapi
- group: company
  title: ''
  type: Blog
  url: https://www.skyflow.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.skyflow.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.skyflow.com/try-skyflow
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skyflow.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skyflow.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/skyflow
- group: operate
  title: ''
  type: StatusPage
  url: https://status.skyflow.com
- group: auth
  title: ''
  type: Compliance
  url: https://docs.skyflow.com/docs/fundamentals/compliance-certifications
- group: auth
  title: ''
  type: Authentication
  url: authentication/skyflow-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skyflow-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skyflow-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skyflow-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skyflow-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/skyflow-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skyflow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skyflow-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skyflow-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skyflow-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/skyflow-components.yml
created: '2026-07-17'
description: Skyflow is a data privacy vault platform that lets companies isolate, protect, and govern sensitive customer data (PII, PCI, PHI) and secrets in a zero-trust vault, then use it safely through tokenization, encryption, polymorphic de-identification, and fine-grained data governance. Developers integrate via the REST Data API and Management API plus first-party SDKs for Python, Node.js, Go, Java, JavaScript, React, React Native, Android, and iOS, and client-side Skyflow Elements for securely collecting and revealing data. Skyflow also ships an MCP Data Protection layer for agentic AI. Backed by Insight Partners and Seedcamp.
image: https://avatars.githubusercontent.com/u/72233674?v=4
layout: provider
mcp_servers:
- description: Skyflow's documentation MCP server for AI clients (Claude Code, Cursor, etc.). Exposes Skyflow's docs and API reference over the Model Context Protocol so agents can retrieve accurate build guidance.
  name: Skyflow MCP Server
  slug: skyflow-mcp-server
modified: '2026-07-21'
name: Skyflow
nav: Providers
network: true
overview: 'Skyflow publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Privacy, PII, Tokenization, and Data Security.


  Skyflow''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 24 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skyflow/refs/heads/main/screenshots/skyflow-2026-08-17T081918.png
security:
- kind: authentication
  name: Skyflow Authentication
  slug: skyflow-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Skyflow Domain Security
  slug: skyflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Skyflow Vulnerability Disclosure
  slug: skyflow-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Skyflow Trust Center
  slug: skyflow-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: skyflow
tags:
- Company
- Data Privacy
- PII
- Tokenization
- Data Security
- Vault
- Compliance
- PCI
- Encryption
- Data Governance
website: https://www.skyflow.com/
---
