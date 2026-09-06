---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.getaleph.com/
- group: company
  title: ''
  type: Blog
  url: https://www.getaleph.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getaleph
- group: operate
  title: ''
  type: Support
  url: https://www.getaleph.com/platform/customer-success
- group: start
  title: ''
  type: SignUp
  url: https://www.getaleph.com/trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getaleph.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getaleph.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aleph-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aleph-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/aleph-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getaleph.com/platform/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aleph-domain-security.yml
created: '2026-07-17'
description: Aleph is an AI-native financial planning & analysis (FP&A) platform for finance teams that want live data, spreadsheet-native workflows, automated reporting, and AI-assisted analysis in one system. It consolidates data from ERP, HRIS, CRM, billing, and databases through 200+ no-code connectors, offers bi-directional Excel and Google Sheets add-ins, web dashboards, and an AI layer (Aleph Intelligence, Aleph Agent, AI Variance Analysis, AI Mappings). Aleph also ships an Aleph Agent MCP integration that brings governed financial data to Claude, ChatGPT, Cursor, and other MCP-compatible tools. Backed by Bain Capital Ventures; SOC 1 Type II and SOC 2 Type II certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aleph.png
layout: provider
mcp_servers:
- description: Official Aleph Agent MCP integration that brings an FP&A team's trusted, governed financial data to MCP-compatible AI clients. Connects Aleph's consolidated data from ERP, CRM, HRIS and 200+ integrati
  name: Aleph Agent MCP
  slug: aleph-agent-mcp
modified: '2026-07-17'
name: Aleph
nav: Providers
network: true
overview: 'Aleph is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, FP&A, Finance, and Financial Planning.


  Aleph''s developer surface includes engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aleph/refs/heads/main/screenshots/aleph-2026-07-25T195555.png
security:
- kind: domain-security
  name: Aleph Domain Security
  slug: aleph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aleph
tags:
- Company
- Ai Apps
- FP&A
- Finance
- Financial Planning
- Analytics
- Spreadsheets
- MCP
website: https://www.getaleph.com/
---
