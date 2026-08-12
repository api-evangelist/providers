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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Eigenpal Agentic Access
  operation_count: 60
  slug: eigenpal-agentic-access
  summary_line: 60 operations · 27 acting
api_count: 6
apis:
- description: Inspect runnable workflow and agent automations, their versions, triggers, and source sync state.
  name: Eigenpal Automations API
  slug: eigenpal-automations-api
- description: Manage datasets, examples, evaluators, experiment batches, evaluator scores, and run promotion workflows.
  name: Eigenpal Evaluation API
  slug: eigenpal-evaluation-api
- description: Upload reusable files for later run or dataset use.
  name: Eigenpal Files API
  slug: eigenpal-files-api
- description: Authenticate and inspect the current API context.
  name: Eigenpal Metadata API
  slug: eigenpal-metadata-api
- description: Record human review verdicts, manage corrected outputs, and monitor review health.
  name: Eigenpal Reviews API
  slug: eigenpal-reviews-api
- description: Start, monitor, retry, review, and debug automation runs, including artifacts.
  name: Eigenpal Runs API
  slug: eigenpal-runs-api
artifact_total: 11
asyncapis:
- description: ''
  name: Eigenpal Webhooks
  slug: eigenpal-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eigenpal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eigenpal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eigenpal-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.eigenpal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eigenpal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.eigenpal.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.eigenpal.com/guides/first-workflow
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eigenpal
- group: company
  title: ''
  type: Website
  url: https://www.eigenpal.com/
- group: other
  title: ''
  type: X
  url: https://x.com/eigenpal
- group: build
  title: ''
  type: Packages
  url: packages/eigenpal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eigenpal-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/eigenpal-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eigenpal-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/eigenpal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eigenpal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eigenpal-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eigenpal.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eigenpal-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.eigenpal.com/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/eigenpal-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eigenpal-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/eigenpal-openapi-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/eigenpal-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eigenpal-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eigenpal-llms.txt
created: '2026-07-17'
description: EigenPal is an AI document-automation platform that replaces manual document reading and data entry for enterprises. Teams build directed graphs of typed steps (workflows) or Git-backed agents that parse, extract, classify, transform, and route data from messy scans, handwritten forms, invoices, KYC documents, claims, shipping forms, contracts, and receipts. Workflows are authored as plain files, evaluated against datasets with automated scoring before going live, and deployed on-prem or in the cloud. A public REST API, TypeScript and Python SDKs, and a CLI let developers start and monitor runs, manage files and datasets, collect human reviews, run evaluation experiments, and receive signed run-lifecycle webhooks.
image: https://www.eigenpal.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: eigenpal-mcp.yml
  slug: eigenpal-mcpyml
modified: '2026-07-19'
name: Eigenpal
nav: Providers
network: true
overview: 'Eigenpal publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Automations API, Evaluation API, Files API, and 3 more. Tagged areas include Company, Document Processing, Artificial Intelligence, Workflow Automation, and Machine Learning.


  The Eigenpal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Eigenpal''s developer surface includes authentication, documentation, API reference, getting-started guide, CLI, changelog, and 21 more developer resources.'
random_paper: 25
score:
  band: developing
  composite: 45.8
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 71.8
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eigenpal/refs/heads/main/screenshots/eigenpal-2026-07-25T213002.png
security:
- kind: authentication
  name: Eigenpal Authentication
  slug: eigenpal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eigenpal Domain Security
  slug: eigenpal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eigenpal
tags:
- Company
- Document Processing
- Artificial Intelligence
- Workflow Automation
- Machine Learning
- Data Extraction
- OCR
- Developer Tools
- Enterprise
website: https://www.eigenpal.com/
---
