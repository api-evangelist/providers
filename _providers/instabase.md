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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Instabase Agentic Access
  operation_count: 27
  slug: instabase-agentic-access
  summary_line: 27 operations · 16 acting
api_count: 1
apis:
- baseURL: https://aihub.instabase.com/api
  baseurl_source: declared
  description: The Audit API from Instabase — 1 operation(s) for audit.
  name: Instabase Audit API
  slug: instabase-audit-api
- baseURL: https://aihub.instabase.com/api
  baseurl_source: declared
  description: The Batches API from Instabase — 8 operation(s) for batches.
  name: Instabase Batches API
  slug: instabase-batches-api
- baseURL: https://aihub.instabase.com/api
  baseurl_source: declared
  description: The Files API from Instabase — 1 operation(s) for files.
  name: Instabase Files API
  slug: instabase-files-api
- baseURL: https://aihub.instabase.com/api
  baseurl_source: declared
  description: The Jobs API from Instabase — 1 operation(s) for jobs.
  name: Instabase Jobs API
  slug: instabase-jobs-api
- baseURL: https://aihub.instabase.com/api
  baseurl_source: declared
  description: The Runs API from Instabase — 4 operation(s) for runs.
  name: Instabase Runs API
  slug: instabase-runs-api
- baseURL: https://aihub.instabase.com/api
  baseurl_source: declared
  description: The Secrets API from Instabase — 1 operation(s) for secrets.
  name: Instabase Secrets API
  slug: instabase-secrets-api
artifact_total: 20
asyncapis:
- description: ''
  name: Instabase Webhooks
  slug: instabase-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AI Hub Audit API
  slug: open-instabase-audit-api
- collection_type: open
  name: AI Hub Audit Batches API
  slug: open-instabase-batches-api
- collection_type: open
  name: AI Hub Audit Files API
  slug: open-instabase-files-api
- collection_type: open
  name: AI Hub Audit Jobs API
  slug: open-instabase-jobs-api
- collection_type: open
  name: AI Hub Audit Runs API
  slug: open-instabase-runs-api
- collection_type: open
  name: AI Hub Audit Secrets API
  slug: open-instabase-secrets-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/instabase-aihub-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.instabase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.instabase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instabase.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.instabase.com/api-sdk/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.instabase.com/overview/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.instabase.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.instabase.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instabase
- group: start
  title: ''
  type: SignUp
  url: https://aihub.instabase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instabase.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.instabase.com/
- group: build
  title: ''
  type: SDKs
  url: packages/instabase-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/instabase-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instabase-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instabase-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instabase-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/instabase-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instabase-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.instabase.com/policies/upgrades.md
- group: design
  title: ''
  type: Conformance
  url: conformance/instabase-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.instabase.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instabase-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/instabase-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instabase-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instabase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instabase-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/instabase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.instabase.com/
created: '2026-07-17'
description: Instabase is an agentic automation platform that transforms complex, document-heavy workflows using AI. Its AI Hub product uses large language models and packet-aware AI agents to extract, classify, validate, and reason over unstructured document packets (PDFs, images, spreadsheets, emails, scans, and more), turning them into structured, verifiable intelligence. AI Hub exposes a REST API and Python SDK for creating file batches, running automation apps and production deployments, reading and writing workspace files, and managing secrets, with industry solutions for financial services, insurance, healthcare, and the public sector. Instabase is venture-backed (a16z, Greylock, Index Ventures).
image: https://cdn.prod.website-files.com/6883b569dca0edf626a1fce5/68cdbf2b866f068b4585e5ea_Open%20graph.png
layout: provider
mcp_servers:
- description: 'Official Instabase AI Hub documentation MCP server. The AI Hub docs site advertises an MCP endpoint for AI client integration (Claude Code, Cursor, etc.) that exposes the documentation corpus. Probed '
  name: Instabase MCP Server
  slug: instabase-mcp-server
modified: '2026-07-19'
name: Instabase
nav: Providers
network: true
overview: 'Instabase publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Batches API, Files API, and 3 more. Tagged areas include Company, Intelligent Document Processing, Document AI, Artificial Intelligence, and Machine-Learning.


  The Instabase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Instabase''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 23 more developer resources.'
random_paper: 9
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 64.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: dora
    - jurisdiction: EU
      standard: eu-ai-act
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 48.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instabase/refs/heads/main/screenshots/instabase-2026-07-25T222558.png
security:
- kind: authentication
  name: Instabase Authentication
  slug: instabase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instabase Domain Security
  slug: instabase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Instabase Vulnerability Disclosure
  slug: instabase-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Instabase Trust Center
  slug: instabase-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: instabase
tags:
- Company
- Intelligent Document Processing
- Document AI
- Artificial Intelligence
- Machine-Learning
- Automation
- Data Extraction
- LLM
- Financial-Services
- Insurance
website: https://www.instabase.com/
---
