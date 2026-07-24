---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 26
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/prompt-foo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prompt-foo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.promptfoo.dev
- group: start
  title: ''
  type: Portal
  url: https://www.promptfoo.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptfoo.dev/docs/intro/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.promptfoo.dev/docs/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptfoo.dev/docs/usage/command-line/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptfoo.dev/docs/red-team/quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptfoo.dev/docs/providers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptfoo.dev/docs/configuration/expected-outputs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.promptfoo.dev/docs/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promptfoo.dev/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.promptfoo.dev/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.promptfoo.app
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.promptfoo.dev
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
  type: Tools
  url: https://github.com/promptfoo/modelaudit
- group: build
  title: ''
  type: Tools
  url: https://github.com/promptfoo/mcp-agent-provider
- group: build
  title: ''
  type: Tools
  url: https://github.com/promptfoo/evil-mcp-server
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/promptfoo/example-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/promptfoo/demo-app
- group: build
  title: ''
  type: Library
  url: https://github.com/promptfoo/js-rouge
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/promptfoo
- group: build
  title: ''
  type: Package
  url: https://pypi.org/project/promptfoo/
- group: build
  title: ''
  type: Package
  url: https://formulae.brew.sh/formula/promptfoo
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/promptfoo/promptfoo/tree/main/helm/chart/promptfoo
- group: commercial
  title: ''
  type: License
  url: https://github.com/promptfoo/promptfoo/blob/main/LICENSE
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/promptfoo
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/promptfoo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/promptfoo
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/promptfoo/promptfoo/releases
created: '2026-05-25'
description: Promptfoo is an open-source CLI and TypeScript/Node.js library for evaluating, red-teaming, and security-testing LLM applications, agents, and RAG pipelines. It runs deterministic prompt evals with model-graded and rule-based assertions, generates dynamic adversarial attack probes across 50+ vulnerability categories (prompt injection, jailbreaks, RAG poisoning, PII leakage, harmful content, business rule violations), and integrates with CI/CD via a GitHub Action and a `code-scans` command for pull-request review. Promptfoo supports dozens of LLM providers — OpenAI, Anthropic Claude, Google Gemini, AWS Bedrock/SageMaker, Azure OpenAI, Mistral, Cohere, Groq, DeepSeek, Together, Fireworks, OpenRouter, LiteLLM, Vercel and Cloudflare AI gateways — plus local runtimes (Ollama, LocalAI, llama.cpp, vLLM, llamafile, Docker Model Runner) and custom HTTP/WebSocket/Python/JavaScript/Go/Ruby/Shell providers. It also ships an MCP server (`promptfoo mcp`), a Model Audit scanner (`scan-model`)
  for malicious ML artifacts, and a hosted Enterprise tier with team sharing, continuous monitoring, SSO, and a centralized compliance dashboard aligned to OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS, and the EU AI Act. The project is MIT-licensed, has 21k+ GitHub stars, and is now part of OpenAI while remaining open source.
features:
- Open-source CLI and Node.js/TypeScript library for LLM evaluation and red teaming
- '`promptfoo eval` — run deterministic prompt/model evals with caching, concurrency, and live reload'
- '`promptfoo redteam` — generate and run dynamic adversarial probes across 50+ vulnerability categories'
- '`promptfoo view` — local browser UI for browsing eval and red-team results'
- '`promptfoo share` — publish a shareable URL for an eval or model audit'
- '`promptfoo generate` — synthesize datasets, red-team tests, and assertions'
- '`promptfoo optimize` — improve prompts against a target provider'
- '`promptfoo scan-model` — security-scan ML model files (ModelAudit)'
- '`promptfoo code-scans` — scan code changes for LLM security vulnerabilities in IDEs and CI/CD'
- '`promptfoo mcp` — expose promptfoo tools as a Model Context Protocol server'
- '`promptfoo retry`, `list`, `export`, `import`, `validate`, `debug`, `cache`, `auth`'
- 'Assertions: rule-based (equals, contains, regex, javascript, python, cost, latency) and model-graded (llm-rubric, classifier, factuality, answer-relevance, similarity)'
- Red-team plugins covering prompt injection, jailbreaks, PII leakage, harmful content, bias, business-rule violations, RAG poisoning, and agent/tool abuse
- Attack strategies including multi-turn (Crescendo), GOAT (Meta), and iterative jailbreak techniques
- 'Framework alignment: OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS, EU AI Act'
- '50+ providers: OpenAI, Anthropic, Google Gemini, AWS Bedrock, SageMaker, Azure OpenAI, Mistral, Cohere, Groq, DeepSeek, Together, Fireworks, Perplexity, OpenRouter, LiteLLM, Vercel AI Gateway, Cloudflare AI Gateway'
- 'Local runtimes: Ollama, LocalAI, llama.cpp, vLLM, Docker Model Runner, llamafile'
- Custom providers via HTTP, WebSocket, Python, JavaScript, Go, Ruby, and Shell
- GitHub Action (`promptfoo/promptfoo-action`) for PR-level eval gating
- Self-hostable via Helm chart and on-premise enterprise deployment
- 'Hosted Enterprise tier: team sharing, continuous monitoring, centralized compliance dashboard, SSO, granular permissions, managed cloud, SLA-backed support'
- SOC 2 and ISO 27001 certified; trust center at trust.promptfoo.dev
- Distributed on npm (`promptfoo`), PyPI (`promptfoo`), and Homebrew (`brew install promptfoo`)
- MIT-licensed; 21k+ GitHub stars; now part of OpenAI
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prompt-foo.png
layout: provider
modified: '2026-05-25'
name: Promptfoo
nav: Providers
network: true
overview: 'Promptfoo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include LLM Evaluation, LLM Red Teaming, LLM Security, AI Security, and Prompt Engineering.


  Promptfoo''s developer surface includes developer portal, documentation, getting-started guide, pricing, engineering blog, tooling, code examples, and 27 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 22.6
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Prompt Foo Domain Security
  slug: prompt-foo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Prompt Foo Trust Center
  slug: prompt-foo-trust-center
  summary_line: SOC 2, ISO 27001
slug: prompt-foo
tags:
- LLM Evaluation
- LLM Red Teaming
- LLM Security
- AI Security
- Prompt Engineering
- Vulnerability Scanning
- Adversarial Testing
- Jailbreak Testing
- Prompt Injection
- RAG
- Agents
- MCP
- Model Audit
- OWASP LLM Top 10
- NIST AI RMF
- MITRE ATLAS
- EU AI Act
- CI/CD
- Open Source
- TypeScript
website: https://www.promptfoo.dev
---
