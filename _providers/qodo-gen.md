---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Qodo Gen Agentic Access
  operation_count: 8
  slug: qodo-gen-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 1
apis:
- baseURL: https://qodo-merge.st.qodo.ai/api/v1
  baseurl_source: declared
  description: Terminal agent runner; serve agents as HTTP APIs or MCP services.
  name: Qodo Qodo Command API
  slug: qodo-gen-qodo-command-api
- baseURL: https://qodo-merge.st.qodo.ai/api/v1
  baseurl_source: declared
  description: AI coding assistant IDE plugin - generation, chat, and test generation.
  name: Qodo Qodo Gen API
  slug: qodo-gen-qodo-gen-api
- baseURL: https://qodo-merge.st.qodo.ai/api/v1
  baseurl_source: declared
  description: Agentic pull request review Git app (built on open-source PR-Agent).
  name: Qodo Qodo Merge API
  slug: qodo-gen-qodo-merge-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qodo Platform (Modeled Capability Surfaces) Qodo Command API
  slug: open-qodo-gen-qodo-command-api
- collection_type: open
  name: Qodo Platform (Modeled Capability Surfaces) Qodo Command Qodo Gen API
  slug: open-qodo-gen-qodo-gen-api
- collection_type: open
  name: Qodo Platform (Modeled Capability Surfaces) Qodo Command Qodo Merge API
  slug: open-qodo-gen-qodo-merge-api
- collection_type: open
  name: Qodo Platform (Modeled Capability Surfaces)
  slug: open-qodo-gen
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/qodo-ai/pr-agent/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/qodo-ai/pr-agent/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/The-PR-Agent/pr-agent/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/The-PR-Agent/pr-agent/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/The-PR-Agent/pr-agent/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/qodo-ai/pr-agent/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qodo-gen-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qodo-gen-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qodo-gen-domain-security.yml
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
  url: plans/qodo-gen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qodo-gen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qodo-gen-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.qodo.ai/blog/
created: '2026-07-11'
description: Qodo (formerly CodiumAI) is an AI code quality and integrity platform for the whole software development lifecycle. Its products include Qodo Gen (an AI coding assistant IDE plugin for code generation, chat, and test generation), Qodo Merge (an agentic pull request review app for GitHub, GitLab, Bitbucket, and Azure DevOps, built on the open-source PR-Agent project), Qodo Command / Qodo Gen CLI (a terminal agent runner installed via npm that can serve agents as HTTP APIs or MCP services), Qodo Cover (test coverage automation), and Qodo Aware (codebase context). Qodo's public surfaces are primarily an IDE plugin, a Git application driven by webhooks and PR comment commands, and a CLI - the hosted platform REST surface is gated. The open-source PR-Agent engine (MIT) that powers Qodo Merge is self-hostable as a CLI, GitHub Action, or webhook server.
finops:
- name: Qodo Gen Finops
  service_category: AI and Developer Tools
  slug: qodo-gen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qodo-gen.png
layout: provider
modified: '2026-07-11'
name: Qodo
nav: Providers
network: true
overview: 'Qodo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Qodo Command API, Qodo Gen API, and Qodo Merge API. Tagged areas include AI Coding Assistant, Code Review, Test Generation, Developer Tools, and LLM.


  Qodo''s developer surface includes authentication, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Qodo Gen Plans Pricing
  plan_count: 4
  slug: qodo-gen-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Qodo Gen Rate Limits
  slug: qodo-gen-rate-limits
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 60.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qodo-gen/refs/heads/main/screenshots/qodo-gen-2026-09-02T152526.png
security:
- kind: authentication
  name: Qodo Gen Authentication
  slug: qodo-gen-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Qodo Gen Domain Security
  slug: qodo-gen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qodo-gen
tags:
- AI Coding Assistant
- Code Review
- Test Generation
- Developer Tools
- LLM
- Artificial Intelligence
- Pull Request Review
- Code Quality
- Agents
- Open-Source
website: https://www.qodo.ai
---
