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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Viewpoints Ai Agentic Access
  operation_count: 7
  slug: viewpoints-ai-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: Create studies and retrieve results
  name: Viewpoints AI Studies API
  slug: viewpoints-ai-studies-api
- description: Upload stimuli files for use in studies
  name: Viewpoints AI Study File Uploads API
  slug: viewpoints-ai-study-file-uploads-api
- description: Manage recurring study schedules
  name: Viewpoints AI Study Schedules API
  slug: viewpoints-ai-study-schedules-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Viewpoints Study Studies API
  slug: open-viewpoints-ai-studies-api
- collection_type: open
  name: Viewpoints Study Studies Study File Uploads API
  slug: open-viewpoints-ai-study-file-uploads-api
- collection_type: open
  name: Viewpoints Study Studies Study Schedules API
  slug: open-viewpoints-ai-study-schedules-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.viewpoints.ai
- group: docs
  title: ''
  type: Documentation
  url: https://api.viewpoints.ai
- group: docs
  title: ''
  type: APIReference
  url: https://api.viewpoints.ai
- group: start
  title: ''
  type: Login
  url: https://app.viewpoints.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viewpoints.ai/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viewpoints.ai/privacy.html
- group: auth
  title: ''
  type: Compliance
  url: https://viewpoints.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viewpoints-ai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/viewpoints-ai-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/viewpoints-ai-agentic-access.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/viewpoints-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/viewpoints-ai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/viewpoints-ai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/viewpoints-ai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/viewpoints-ai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/viewpoints-ai-study-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/viewpoints-ai-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viewpoints-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viewpoints.ai
created: '2026-07-17'
description: Viewpoints AI (viewpoints.ai) is a Stanford-founded research platform that runs AI jury simulations for litigation teams and AI audience panels for market researchers. Companies upload case materials or creative/marketing stimuli and a representative panel of simulated personas reads them, deliberates, and returns verdict or response distributions, the themes driving them, and per-participant reasoning — same-day, with a claimed 88% match to real studies (Stanford-validated). The Viewpoints Study API lets developers programmatically create studies, upload stimuli, poll asynchronous creation jobs, retrieve full participant results, and schedule recurring runs. SOC 2 Type II. Backed by Forerunner Ventures.
image: https://viewpoints.ai/og-image-2.png
layout: provider
mcp_servers:
- description: ''
  name: Viewpoints AI MCP Server
  slug: viewpoints-ai-mcp-server
modified: '2026-07-21'
name: Viewpoints AI
nav: Providers
network: true
overview: 'Viewpoints AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Studies API, Study File Uploads API, and Study Schedules API. Tagged areas include Company, Artificial Intelligence, Market Research, Synthetic Personas, and Consumer Insights.


  Viewpoints AI''s developer surface includes documentation, API reference, authentication, and 17 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Viewpoints Ai Authentication
  slug: viewpoints-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Viewpoints Ai Domain Security
  slug: viewpoints-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: viewpoints-ai
tags:
- Company
- Artificial Intelligence
- Market Research
- Synthetic Personas
- Consumer Insights
- Litigation
- Jury Simulation
- Research
website: https://viewpoints.ai
---
