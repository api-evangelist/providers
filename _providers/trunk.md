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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Trunk Agentic Access
  operation_count: 16
  slug: trunk-agentic-access
  summary_line: 16 operations · 15 acting
api_count: 1
apis:
- description: CI test-result ingestion surface. The trunk-analytics-cli (and the trunk-io/analytics-uploader GitHub Action) uploads JUnit XML, Bazel BEP, and XCResult test reports to Trunk for flaky-test detection,
  name: Trunk Test Uploads (Analytics CLI)
  slug: test-uploads-api
- description: Svix-powered outbound webhooks for subscribing to Flaky Tests events (test_case.status_changed, test_case.monitor_status_changed, test_case.investigation_completed) and Merge Queue events (pull_reques
  name: Trunk Webhooks
  slug: webhooks-api
- description: Meta-linter and static analysis manager exposed through the trunk CLI and a local daemon (no public REST API). Commands include trunk init, trunk check, and trunk check --all; it hermetically installs
  name: Trunk Code Quality CLI
  slug: code-quality-cli
- description: Query Flaky Tests state and link tickets.
  name: Trunk Flaky Tests API
  slug: trunk-flaky-tests-api
- description: Control the Trunk Merge Queue.
  name: Trunk Merge Queue API
  slug: trunk-merge-queue-api
artifact_total: 18
asyncapis:
- description: ''
  name: Trunk Webhooks
  slug: trunk-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trunk Flaky Tests API
  slug: open-trunk-flaky-tests-api
- collection_type: open
  name: Trunk API
  slug: open-trunk-io
- collection_type: open
  name: Trunk Flaky Tests Merge Queue API
  slug: open-trunk-merge-queue-api
common:
- group: company
  title: ''
  type: Website
  url: https://trunk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trunk.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trunk-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trunkhq
- group: company
  title: ''
  type: Blog
  url: https://trunk.io/feed.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trunk.io/legal/terms
- group: auth
  title: ''
  type: Authentication
  url: authentication/trunk-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trunk-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trunk-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trunk-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trunk-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trunk-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trunk-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trunk-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/trunk-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trunk-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/trunk-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trunk-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trunk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trunk.io/security
- group: commercial
  title: ''
  type: Plans
  url: plans/trunk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trunk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trunk-finops.yml
created: '2026-07-17'
description: Trunk builds developer experience and CI reliability tooling. Its platform spans Code Quality (a meta-linter and static analysis manager driven by the trunk CLI), a flake-aware parallel Merge Queue, and Flaky Tests detection / CI Analytics. Test results are uploaded from CI via the Trunk Analytics CLI / GitHub Action, and an HTTP REST API at api.trunk.io exposes Flaky Tests and Merge Queue control plus Svix-powered outbound webhooks. Trunk is a portfolio company of a16z.
finops:
- name: Trunk Finops
  service_category: Developer Tools
  slug: trunk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trunk.png
layout: provider
mcp_servers:
- description: ''
  name: Trunk MCP Server
  slug: trunk-mcp-server
modified: '2026-08-08'
name: Trunk
nav: Providers
network: true
overview: 'Trunk publishes 2 APIs on the [APIs.io](https://apis.io/) network: Flaky Tests API and Merge Queue API. Tagged areas include Developer Tools, CI/CD, Code Quality, Flaky Tests, and Merge Queue.


  The Trunk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trunk''s developer surface includes documentation, engineering blog, authentication, CLI, and 20 more developer resources.'
plans:
- name: Trunk Plans Pricing
  plan_count: 3
  slug: trunk-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Trunk Rate Limits
  slug: trunk-rate-limits
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 63.6
    developer_ergonomics: 51.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trunk/refs/heads/main/screenshots/trunk-2026-06-20T195810.png
security:
- kind: authentication
  name: Trunk Authentication
  slug: trunk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trunk Domain Security
  slug: trunk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trunk Vulnerability Disclosure
  slug: trunk-vulnerability-disclosure
  summary_line: disclosure policy published
slug: trunk
tags:
- Developer Tools
- CI/CD
- Code Quality
- Flaky Tests
- Merge Queue
- Test Analytics
- Static Analysis
- Webhook
website: https://trunk.io/
---
