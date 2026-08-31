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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: The Findings API from Pixee — 2 operation(s) for findings.
  name: Pixee Findings API
  slug: pixee-ai-findings-api
- description: The Fixes API from Pixee — 2 operation(s) for fixes.
  name: Pixee Fixes API
  slug: pixee-ai-fixes-api
- description: The Repositories API from Pixee — 2 operation(s) for repositories.
  name: Pixee Repositories API
  slug: pixee-ai-repositories-api
- description: The Scans API from Pixee — 1 operation(s) for scans.
  name: Pixee Scans API
  slug: pixee-ai-scans-api
- description: The Webhooks API from Pixee — 2 operation(s) for webhooks.
  name: Pixee Webhooks API
  slug: pixee-ai-webhooks-api
artifact_total: 26
asyncapis:
- description: Pixee webhooks deliver real-time HTTP POST notifications when remediation events occur. This AsyncAPI document is a faithful reconstruction of the event types and payload schemas documented at https:/
  name: Pixee Webhooks
  slug: pixee-ai-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pixee REST Findings API
  slug: open-pixee-ai-findings-api
- collection_type: open
  name: Pixee REST Findings Fixes API
  slug: open-pixee-ai-fixes-api
- collection_type: open
  name: Pixee REST Findings Repositories API
  slug: open-pixee-ai-repositories-api
- collection_type: open
  name: Pixee REST Findings Scans API
  slug: open-pixee-ai-scans-api
- collection_type: open
  name: Pixee REST Findings Webhooks API
  slug: open-pixee-ai-webhooks-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pixee-ai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pixee-ai-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.pixee.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pixee.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pixee.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pixee.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pixee.ai/getting-started/first-fix
- group: company
  title: ''
  type: Blog
  url: https://www.pixee.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pixee.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.pixee.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixee
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pixee.ai/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pixee.ai/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pixee-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/pixee-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pixee-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pixee-ai-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pixee-ai-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pixee-ai-well-known.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pixee-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixee-ai-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: security/pixee-ai-trust-center.yml
created: '2026-07-17'
description: Pixee is an agentic security engineering (AppSec) platform — "your automated product security engineer." It ingests findings from SAST, SCA, and IaC scanners as SARIF, runs a three-tier triage engine that classifies each vulnerability with auditable, timestamped evidence, and delivers remediations as native pull requests across GitHub, GitLab, Azure DevOps, and Bitbucket using deterministic codemods plus quality-evaluated AI fixes. Pixee exposes a HAL-based REST API (organization-scoped bearer tokens), documented webhooks, a first-party CLI with bundled agent skills, and the open-source Codemodder framework (Java and Python). It is backed by Wing Venture Capital.
image: https://cdn.prod.website-files.com/696822cb241ff5e67581075b/69b1a742e6436bad27408920_pixee%20agentic%20appsec%20image.png
layout: provider
mcp_servers:
- description: ''
  name: Pixee (candidate MCP server)
  slug: pixee-candidate-mcp-server
modified: '2026-07-20'
name: Pixee
nav: Providers
network: true
overview: 'Pixee publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Findings API, Fixes API, Repositories API, and 2 more. Tagged areas include Company, Security, Application Security, AppSec, and Vulnerability Remediation.


  The Pixee catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pixee''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 16 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 61.2
    developer_ergonomics: 73.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 51.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixee-ai/refs/heads/main/screenshots/pixee-ai-2026-08-17T081243.png
security:
- kind: authentication
  name: Pixee Ai Authentication
  slug: pixee-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pixee Ai Domain Security
  slug: pixee-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pixee Ai Trust Center
  slug: pixee-ai-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
skill_count: 10
skills:
- name: pixee-analysis
  slug: pixee-analysis
- name: pixee-api
  slug: pixee-api
- name: pixee-auth
  slug: pixee-auth
- name: pixee-finding
  slug: pixee-finding
- name: pixee-integration
  slug: pixee-integration
- name: pixee-preferences
  slug: pixee-preferences
- name: pixee-repo
  slug: pixee-repo
- name: pixee-scan
  slug: pixee-scan
- name: pixee-shared
  slug: pixee-shared
- name: pixee-workflow
  slug: pixee-workflow
slug: pixee-ai
tags:
- Company
- Security
- Application Security
- AppSec
- Vulnerability Remediation
- Static Analysis
- SARIF
- Code Security
- Artificial Intelligence
- Developer Tools
website: https://www.pixee.ai/
---
