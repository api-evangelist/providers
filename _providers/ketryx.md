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
    error_semantics: documented
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
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ketryx Agentic Access
  operation_count: 2
  slug: ketryx-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Upload build artifacts, test results, and SBOM files.
  name: Ketryx Artifacts API
  slug: ketryx-artifacts-api
- description: Report builds and their status to Ketryx.
  name: Ketryx Builds API
  slug: ketryx-builds-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ketryx Build Artifacts API
  slug: open-ketryx-artifacts-api
- collection_type: open
  name: Ketryx Build Artifacts Builds API
  slug: open-ketryx-builds-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ketryx-build-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ketryx-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ketryx.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ketryx.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ketryx.com/api/build-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ketryx
- group: company
  title: ''
  type: Blog
  url: https://www.ketryx.com/learn/blog
- group: operate
  title: ''
  type: Support
  url: https://ketryx.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ketryx.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.ketryx.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ketryx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ketryx.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ketryx.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ketryx.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ketryx.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ketryx-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ketryx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ketryx-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ketryx-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ketryx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ketryx-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ketryx-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ketryx-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Ketryx is an AI-native application lifecycle management (ALM) and compliance platform for regulated medical-device and life-sciences software teams. It integrates with developer tools such as Jira and GitHub to automate the documentation, traceability, and quality-management work required by FDA, EU MDR, ISO 13485, ISO 14971, and IEC 62304, keeping teams continuously audit-ready. Capabilities include automated Design and Development File generation, requirement-risk-code-test traceability, agentic AI for repetitive compliance tasks, ISO 14971 risk management, software bill-of-materials (SBOM) and vulnerability tracking, QMS enforcement, and change-impact assessment. Ketryx exposes a public Build API that lets CI/CD pipelines report builds, JUnit / Cucumber test results, build artifacts, and CycloneDX / SPDX SBOM documents into a project, via a first-party GitHub Action and Python utility. The company is backed by Lightspeed Venture Partners.
image: https://www.ketryx.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Ketryx MCP Server
  slug: ketryx-mcp-server
modified: '2026-07-19'
name: Ketryx
nav: Providers
network: true
overview: 'Ketryx publishes 2 APIs on the [APIs.io](https://apis.io/) network: Artifacts API and Builds API. Tagged areas include Company, Medical Devices, Life Sciences, Compliance, and Regulatory.


  Ketryx''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ketryx/refs/heads/main/screenshots/ketryx-2026-07-25T223638.png
security:
- kind: authentication
  name: Ketryx Authentication
  slug: ketryx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ketryx Domain Security
  slug: ketryx-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Ketryx Trust Center
  slug: ketryx-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO/IEC 27001:2022, ISO 13485:2016, ISO 14971:2019, IEC 62304:2006, HIPAA BAA, FDA 21 CFR Part 11
slug: ketryx
tags:
- Company
- Medical Devices
- Life Sciences
- Compliance
- Regulatory
- Application Lifecycle Management
- Quality Management
- SBOM
- DevOps
- Healthcare
- Governance
- CI/CD
website: https://docs.ketryx.com
---
