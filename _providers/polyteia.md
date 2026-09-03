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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Polyteia Agentic Access
  operation_count: 1
  slug: polyteia-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://app.polyteia.com/api
  baseurl_source: declared
  description: The Organization API from Polyteia — 1 operation(s) for organization.
  name: Polyteia Organization API
  slug: polyteia-organization-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Polyteia Platform Dataset API
  slug: open-polyteia-dataset-api
- collection_type: open
  name: Polyteia Platform Dataset Organization API
  slug: open-polyteia-organization-api
- collection_type: open
  name: Polyteia Platform Dataset Solution API
  slug: open-polyteia-solution-api
- collection_type: open
  name: Polyteia Platform Dataset Workspace API
  slug: open-polyteia-workspace-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.polyteia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.polyteia.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.polyteia.com/api-docs/en/readme.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.polyteia.com/readme/erste-schritte.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/polyteia-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.polyteia.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.polyteia.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polyteia.com/imprint
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polyteia.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.polyteia.com/services/customer-support
- group: company
  title: ''
  type: Blog
  url: https://www.polyteia.com/about/news
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/polyteia-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/polyteia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polyteia-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/polyteia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/polyteia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/polyteia-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polyteia-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/polyteia-platform-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/polyteia-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.polyteia.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/polyteia-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/polyteia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.polyteia.com/resources/data-security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polyteia-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polyteia-agentic-access.yml
created: '2026-07-17'
description: Polyteia is a Berlin-based govtech company offering a data platform for the German and European public sector. It lets public administrations connect existing systems, harmonize fragmented data, and use it in AI-supported workflows for forms, case processing, statistical evaluation, and reporting. The platform ships pre-built Solutions for common public-sector use cases (social-service planning, budget controlling, crisis response, kindergarten demand forecasting) plus a no-code/low-code Studio. It serves 80+ government entities in Germany, including the states of Schleswig-Holstein and Saarland. The platform is fully driveable through an RPC-style API (command/query over a single POST endpoint) authenticated with Personal Access Keys, backed by a Trust Center and GDPR/BSI/C5 compliance. Founded by Faruk Tuncer, Taisia Antonova, and Lukas Rambold; backed by HV Capital and DvH Ventures.
image: https://cdn.prod.website-files.com/64f07393c02984e046baf5f8/6833060d76c3b033ca002dff_Social%20Sharing.png
layout: provider
mcp_servers:
- description: ''
  name: Polyteia MCP Server
  slug: polyteia-mcp-server
modified: '2026-07-20'
name: Polyteia
nav: Providers
network: true
overview: 'Polyteia publishes 1 API on the [APIs.io](https://apis.io/) network: Organization API. Tagged areas include Company, Ai Enterprise Software, GovTech, Public Sector, and Data Platform.


  Polyteia''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, pricing, support, and 20 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polyteia/refs/heads/main/screenshots/polyteia-2026-08-17T081321.png
security:
- kind: authentication
  name: Polyteia Authentication
  slug: polyteia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Polyteia Domain Security
  slug: polyteia-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Polyteia Vulnerability Disclosure
  slug: polyteia-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Polyteia Trust Center
  slug: polyteia-trust-center
  summary_line: GDPR, BSI IT-Grundschutz, BSI C5, ISO 27001 (in progress)
slug: polyteia
tags:
- Company
- Ai Enterprise Software
- GovTech
- Public Sector
- Data Platform
- Government
- Data Analytics
- Germany
- Business Intelligence
- No-Code
website: https://docs.polyteia.com/
---
