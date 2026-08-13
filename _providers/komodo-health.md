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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Marmot Development Kit is Komodo Health's developer surface — a Python SDK and `komodo` CLI published to PyPI that handle OAuth 2.0 authentication, account selection, service-principal credentials
  name: Komodo Health Marmot Development Kit
  slug: komodo-health-marmot-development-kit
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/komodo-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/komodo-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.komodohealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.komodohealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.komodohealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.komodohealth.com/reference/sdk/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.komodohealth.com/guides-tutorials/guides/1-quickstart/
- group: company
  title: ''
  type: Blog
  url: https://www.komodohealth.com/perspectives/
- group: operate
  title: ''
  type: Support
  url: https://komodohealthsupport.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/komodohealth
- group: start
  title: ''
  type: SignUp
  url: https://www.komodohealth.com/get-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.komodohealth.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.komodohealth.com/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.komodohealth.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.komodohealth.com/reference/changelog/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.komodohealth.com/
- group: build
  title: ''
  type: Packages
  url: packages/komodo-health-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/komodo-health-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/komodo-health-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/komodo-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/komodo-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/komodo-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/komodo-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/komodo-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/komodo-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/komodo-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/komodo-health-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Komodo Health is a healthcare technology company that combines a de-identified real-world data foundation — the Healthcare Map, over one trillion linked records covering 330M+ patients and refreshed daily — with a validated healthcare AI layer called Marmot, serving life sciences, payers, providers, financial services and consultancies. Its developer surface is the Marmot Development Kit: a first-party Python SDK and `komodo` CLI distributed on PyPI that authenticate with OAuth 2.0 (device flow for users, service-principal client credentials for machines) and broker access to a dedicated, per-account Komodo-managed Snowflake warehouse. The same package ships a first-party Model Context Protocol server that lets AI assistants explore warehouse schemas and drive the Komodo App Builder, plus a beta Cohort API for interactive patient-cohort exploration over ICD-10, CPT/HCPCS and NDC codes.'
image: https://www.komodohealth.com/wp-content/uploads/2026/04/Default-New.png
layout: provider
mcp_servers:
- description: ''
  name: komodo-health-mcp.yml
  slug: komodo-health-mcpyml
modified: '2026-07-19'
name: Komodo Health
nav: Providers
network: true
overview: 'Komodo Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Data, Life Sciences, and Real-World Data.


  Komodo Health''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 21 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 75.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 38.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/komodo-health/refs/heads/main/screenshots/komodo-health-2026-07-25T224138.png
security:
- kind: authentication
  name: Komodo Health Authentication
  slug: komodo-health-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Komodo Health Domain Security
  slug: komodo-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Komodo Health Trust Center
  slug: komodo-health-trust-center
  summary_line: SOC 2 Type II, SOC 2 Type I, GDPR, CCPA, CISA Secure by Design Pledge, EcoVadis, CMS Qualified Entity (QE) Program
slug: komodo-health
tags:
- Company
- Healthcare
- Health Data
- Life Sciences
- Real-World Data
- Healthcare Analytics
- Artificial Intelligence
- Data
- Snowflake
- MCP
website: https://www.komodohealth.com/
---
