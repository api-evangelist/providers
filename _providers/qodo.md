---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://www.qodo.ai
  baseurl_source: spec
  description: AI pull-request reviewer. Available as the Apache-2.0 open-source PR-Agent (CLI, GitHub Action, Docker, self-hosted webhook server) and as the hosted Qodo Merge Git app. It is invoked through Git prov
  name: Qodo Merge (PR-Agent)
  slug: qodo-merge-pr-agent
- description: AI pair-programmer delivered as JetBrains and VS Code IDE plugins for context-aware code generation, test generation, and documentation. It is an editor extension and does not expose a public HTTP API
  name: Qodo Gen
  slug: qodo-gen
- description: Terminal runtime for building, running, and managing AI agents across the SDLC, installed via npm (@qodo/command). Agents can be exposed locally as HTTP services (--webhook), as a web UI (--ui), or as
  name: Qodo Command/CLI
  slug: qodo-command-cli
- baseURL: https://www.qodo.ai
  baseurl_source: spec
  description: The hosted Qodo platform that backs Qodo Merge, Qodo Gen, and Qodo Command. As of this writing Qodo does not publish a documented, general-purpose public HTTP REST API with stable endpoints; access is
  name: Qodo Hosted API
  slug: qodo-hosted-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qodo
  slug: open-qodo
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/qodo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qodo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qodo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qodo-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qodoai
- group: company
  title: ''
  type: Website
  url: https://www.qodo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qodo.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/qodo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qodo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qodo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.qodo.ai/feed/
created: '2026-06-21'
description: Qodo (formerly CodiumAI) is an AI code-integrity platform for automated code review, test generation, and code quality across the SDLC. Its developer surface is delivered primarily as a hosted Git app and open-source PR-Agent (Qodo Merge), IDE plugins (Qodo Gen), and a terminal agent runtime (Qodo Command/CLI) rather than a broad public HTTP API.
finops:
- name: Qodo Finops
  service_category: Developer Tools
  slug: qodo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qodo.png
layout: provider
modified: '2026-06-21'
name: Qodo
nav: Providers
network: true
overview: 'Qodo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Merge (PR-Agent) and Hosted API. Tagged areas include Artificial Intelligence, Code Review, Code Integrity, Developer Tools, and Pull Requests.


  Qodo''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Qodo Plans Pricing
  plan_count: 4
  slug: qodo-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Qodo Rate Limits
  slug: qodo-rate-limits
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 30.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qodo/refs/heads/main/screenshots/qodo-2026-09-02T152526.png
security:
- kind: domain-security
  name: Qodo Domain Security
  slug: qodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qodo Vulnerability Disclosure
  slug: qodo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Qodo Trust Center
  slug: qodo-trust-center
  summary_line: SOC 2
slug: qodo
tags:
- Artificial Intelligence
- Code Review
- Code Integrity
- Developer Tools
- Pull Requests
website: https://www.qodo.ai
---
