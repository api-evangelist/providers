---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-02'
api_count: 6
apis:
- description: The Promptfoo CLI is the primary entry point for running prompt and model evaluations from the command line or CI. It is installable via npm, Homebrew, pip, or npx and reads a YAML configuration to fa
  name: Promptfoo CLI
  slug: promptfoo-cli
- description: The Promptfoo Node.js package exposes the same evaluation engine programmatically so developers can embed evaluations, assertions, and dataset runs directly into JavaScript and TypeScript applications
  name: Promptfoo Node.js Library
  slug: promptfoo-library
- description: Promptfoo Red Team generates adversarial test cases against LLM applications targeting prompt injection, jailbreaks, PII leakage, bias, and other OWASP LLM Top 10 categories. Runs from the CLI and pro
  name: Promptfoo Red Team
  slug: promptfoo-red-team
- description: Promptfoo Enterprise is the commercial SaaS at promptfoo.app providing centralized evaluation history, shared red team findings, remediation reports, role-based access control, SSO, and team-wide gove
  name: Promptfoo Enterprise
  slug: promptfoo-enterprise
- description: MCP Proxy is Promptfoo's security gateway for Model Context Protocol traffic, inspecting tool calls and responses flowing between agents and MCP servers to enforce policies and surface adversarial act
  name: Promptfoo MCP Proxy
  slug: promptfoo-mcp-proxy
- description: Promptfoo Code Scanning analyzes source code in IDEs and CI pipelines to find LLM-related vulnerabilities including unsafe prompt construction, missing guardrails, and risky tool usage in agent code.
  name: Promptfoo Code Scanning
  slug: promptfoo-code-scanning
artifact_total: 33
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/promptfoo/promptfoo/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/promptfoo/promptfoo/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/promptfoo/promptfoo/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/promptfoo/promptfoo/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: TrustCenter
  url: security/promptfoo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/promptfoo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.promptfoo.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptfoo.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.promptfoo.dev/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.promptfoo.dev/docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.promptfoo.dev/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promptfoo.dev/pricing/
- group: start
  title: ''
  type: Login
  url: https://promptfoo.app/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/promptfoo/promptfoo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/promptfoo/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/promptfoo
- group: operate
  title: ''
  type: Contact
  url: https://www.promptfoo.dev/contact/
- group: commercial
  title: ''
  type: License
  url: https://github.com/promptfoo/promptfoo/blob/main/LICENSE
- group: start
  title: ''
  type: Portal
  url: https://www.promptfoo.dev
- group: operate
  title: ''
  type: StatusPage
  url: https://status.promptfoo.app
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/promptfoo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/promptfoo/promptfoo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/promptfoo/promptfoo-python
- group: build
  title: ''
  type: Tools
  url: https://github.com/promptfoo/promptfoo-action
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/promptfoo/example-app
- group: build
  title: ''
  type: Library
  url: https://github.com/promptfoo/js-rouge
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/promptfoo
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/promptfoo/promptfoo/tree/main/helm/chart/promptfoo
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/promptfoo
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/promptfoo
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/promptfoo/promptfoo/releases
created: '2026-05-23'
description: Promptfoo is an open-source LLM evaluation and red-teaming framework distributed as a TypeScript CLI and Node.js library under the MIT license. Developers use it to evaluate prompts, models, and RAG pipelines side by side, run automated red team attacks against LLM applications, scan code for LLM vulnerabilities in IDE and CI, and proxy Model Context Protocol traffic. Promptfoo also operates a commercial Enterprise platform at promptfoo.app for teams that need centralized governance, remediation reports, and shared evaluation history.
features:
- description: Compare prompts and models across providers with assertion-based scoring.
  name: Side-by-Side Evaluation
- description: Automated adversarial test generation across prompt injection, jailbreaks, PII, bias, and more.
  name: Red Teaming
- description: Evaluate retrieval-augmented generation pipelines for accuracy, faithfulness, and groundedness.
  name: RAG Evaluation
- description: Run evaluations on every pull request with exit-code-driven gating.
  name: CI/CD Integration
- description: Inspect evaluation runs and diffs in a local browser UI without sending data to a third party.
  name: Local Web Viewer
- description: Inspect and govern Model Context Protocol traffic between agents and tool servers.
  name: MCP Proxy
- description: Static analysis of LLM application code in IDEs and CI to surface risky patterns.
  name: Code Scanning
- description: Open source CLI and library run locally with no telemetry to Promptfoo required.
  name: Self-Hosting
finops:
- name: Promptfoo Finops
  service_category: API
  slug: promptfoo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/promptfoo.png
integrations:
- description: Native provider for OpenAI Chat Completions, Assistants, and Responses APIs.
  name: OpenAI
- description: Native provider for Anthropic Claude models.
  name: Anthropic
- description: Provider for Azure-hosted OpenAI deployments.
  name: Azure OpenAI
- description: Provider for Anthropic, Meta, Mistral, and other models on Bedrock.
  name: AWS Bedrock
- description: Provider for Gemini and other models on Vertex.
  name: Google Vertex AI
- description: Provider for locally hosted open source models via Ollama.
  name: Ollama
- description: Evaluate LangChain chains and agents through custom providers.
  name: LangChain
- description: Run promptfoo evaluations in CI on every pull request.
  name: GitHub Actions
- description: MCP Proxy and MCP provider support for agentic workflows.
  name: Model Context Protocol
layout: provider
modified: '2026-08-08'
name: Promptfoo
nav: Providers
network: true
overview: 'Promptfoo publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include LLM Evaluation, Red Teaming, AI Security, Guardrails, and Open-Source.


  Promptfoo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, developer portal, tooling, and 24 more developer resources.'
plans:
- name: Promptfoo Plans Pricing
  plan_count: 1
  slug: promptfoo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Promptfoo Rate Limits
  slug: promptfoo-rate-limits
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 52.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 100.0
  previous_composite: 42.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/promptfoo/refs/heads/main/screenshots/promptfoo-2026-06-20T192156.png
security:
- kind: domain-security
  name: Promptfoo Domain Security
  slug: promptfoo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Promptfoo Trust Center
  slug: promptfoo-trust-center
  summary_line: SOC 2, ISO 27001
slug: promptfoo
tags:
- LLM Evaluation
- Red Teaming
- AI Security
- Guardrails
- Open-Source
- CLI
- Developer Tools
use_cases:
- description: Compare prompt variants against datasets to choose the best-performing version.
  name: Prompt Iteration
- description: Benchmark candidate models across providers before committing to one in production.
  name: Model Selection
- description: Evaluate chunking, retrieval, and generation choices in RAG systems.
  name: RAG Quality Assurance
- description: Probe pre-production LLM applications for adversarial failure modes.
  name: AI Red Teaming
- description: Wire evaluations and red team scans into CI so regressions block deploys.
  name: Continuous LLM Testing
website: https://www.promptfoo.dev/
---
