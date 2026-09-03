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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Runautomat Agentic Access
  operation_count: 1
  slug: runautomat-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://studio.runautomat.com
  baseurl_source: declared
  description: The extract API from Runautomat — 1 operation(s) for extract.
  name: Runautomat extract API
  slug: runautomat-extract-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: extract API
  slug: open-runautomat-extract-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/runautomat-extract-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://runautomat.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runautomat.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runautomat.com/guides/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runautomat.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runautomat.com/guides/getting-started/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/runautomat-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.runautomat.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.runautomat.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://studio.runautomat.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://runautomat.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runautomat.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.runautomat.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runautomat.com/
- group: auth
  title: ''
  type: Compliance
  url: https://runautomat.com/enterprise
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runautomat-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/runautomat-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/runautomat-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/runautomat-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/runautomat-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/runautomat-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/runautomat-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runautomat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runautomat-domain-security.yml
created: '2026-07-17'
description: Runautomat (dba Automat) builds AI agents that operate computers the way people do, replacing legacy RPA tools like UiPath, Automation Anywhere, and Blue Prism with self-healing managed automations. Founded in 2022 by ex-Google engineers Lucas Ochoa and Gautam Bose and backed by Felicis, Khosla Ventures, Initialized Capital, and Y Combinator. The platform spans UI-based AI agents (Computer Use RPA), AI document extraction (IDP), API-based automations (iPaaS), and a managed forward-deployed-engineer service. Its public developer surface is the Automat Document Extraction API, a single synchronous /api/extract operation that turns PDFs and images into structured JSON matching a configured extractor, authenticated with an organization API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runautomat.png
layout: provider
modified: '2026-07-21'
name: Runautomat
nav: Providers
network: true
overview: 'Runautomat publishes 1 API on the [APIs.io](https://apis.io/) network: extract API. Tagged areas include Company, Automation, Robotic Process Automation, Document Processing, and Artificial Intelligence.


  Runautomat''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 18 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runautomat/refs/heads/main/screenshots/runautomat-2026-08-17T081652.png
security:
- kind: authentication
  name: Runautomat Authentication
  slug: runautomat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runautomat Domain Security
  slug: runautomat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: runautomat
tags:
- Company
- Automation
- Robotic Process Automation
- Document Processing
- Artificial Intelligence
- Machine-Learning
- Data Extraction
- iPaaS
- Agents
website: https://runautomat.com
---
