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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Nebulock Agentic Access
  operation_count: 55
  slug: nebulock-agentic-access
  summary_line: 55 operations · 33 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Actors, users, and hosts — the identity/asset correlation graph.
  name: Nebulock Entities API
  slug: nebulock-entities-api
- description: Retrieve and manage security findings and their comments.
  name: Nebulock Findings API
  slug: nebulock-findings-api
- description: Threat hunts, hunt suggestions, and hunt reports.
  name: Nebulock Hunts API
  slug: nebulock-hunts-api
- description: Create, validate, and run detection rules (Sigma / scheduled SQL).
  name: Nebulock Rules API
  slug: nebulock-rules-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a hunt, add a follow-up directive, then generate and fetch its report.
  name: Run a Nebulock hunt and generate a report
  slug: nebulock-run-hunt-and-report
- description: Validate rule content, create it inactive, then activate it.
  name: Validate and deploy a Nebulock detection rule
  slug: nebulock-validate-and-deploy-rule
artifact_total: 11
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nebulock.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nebulock.io/reference/getting-started-with-the-nebulock-findings-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nebulock.io/docs/access
- group: company
  title: ''
  type: Blog
  url: https://nebulock.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://nebulock.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nebulock
- group: operate
  title: ''
  type: Support
  url: https://docs.nebulock.io/docs/help
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.nebulock.io/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/nebulock-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nebulock-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nebulock-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nebulock-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nebulock-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nebulock-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/nebulock-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nebulock-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nebulock-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nebulock-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nebulock-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nebulock-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nebulock-run-hunt-and-report.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nebulock-validate-and-deploy-rule.yml
- group: company
  title: ''
  type: Website
  url: https://nebulock.io/
created: '2026-07-17'
description: Nebulock is an agentic, contextual security-analytics platform built for hunt-first security operations. A swarm of AI agents continuously hunts across cloud, SaaS, network, endpoint, and identity telemetry, maintaining a behavioral Context Graph to surface endpoint- and identity-based threats, close detection coverage gaps, and catch human and agentic insider threats before they escalate into incidents. The platform runs hypothesis-driven investigations, writes and deploys detection rules (Sigma and scheduled SQL), retrohunts historical data, simulates attacks, and maps coverage against MITRE ATT&CK. Nebulock exposes a customer-facing public API for Findings, Entities (actors/users/hosts correlation), Hunts, hunt suggestions and reports, and detection Rules, authenticated with per-organization API keys. The company raised a $25M Series A and is backed by Bain Capital Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nebulock.png
layout: provider
mcp_servers:
- description: ''
  name: nebulock-mcp.yml
  slug: nebulock-mcpyml
modified: '2026-07-20'
name: Nebulock
nav: Providers
network: true
overview: 'Nebulock publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Findings API, Hunts API, and 1 more. Tagged areas include Company, Security, Threat Hunting, Threat Detection, and Security Operations.


  Nebulock''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 35.5
  delta: -2.2
  facets:
    commercial_clarity: 7.9
    contract_quality: 56.8
    developer_ergonomics: 47.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nebulock Authentication
  slug: nebulock-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nebulock Domain Security
  slug: nebulock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nebulock
tags:
- Company
- Security
- Threat Hunting
- Threat Detection
- Security Operations
- Detection Engineering
- AI Agents
- SIEM
website: https://nebulock.io/
---
