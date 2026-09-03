---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.7
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The PLaMo API is Preferred Networks' cloud service for its domestically developed PLaMo large language models. Its interface is compatible with the OpenAI API, so existing OpenAI/LangChain client code
  name: PLaMo API
  slug: plamo-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/preferred-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.preferred.jp/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plamo.preferredai.jp/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plamo.preferredai.jp/en/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.plamo.preferredai.jp/en/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.plamo.preferredai.jp/en/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.plamo.preferredai.jp/hc/ja
- group: company
  title: ''
  type: Blog
  url: https://tech.preferred.jp/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pfnet
- group: commercial
  title: ''
  type: Pricing
  url: https://plamo.preferredai.jp/api
- group: start
  title: ''
  type: SignUp
  url: https://plamo.preferredai.jp/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plamo.preferredai.jp/info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.preferred.jp/en/policy/
- group: build
  title: ''
  type: Examples
  url: https://github.com/pfnet-research/plamo-examples
- group: commercial
  title: ''
  type: Plans
  url: plans/preferred-networks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/preferred-networks-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/preferred-networks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/preferred-networks-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/preferred-networks-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/preferred-networks-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/preferred-networks-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/preferred-networks-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/preferred-networks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/preferred-networks-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/preferred-networks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/preferred-networks-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/preferred-networks-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/preferred-networks-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/preferred-networks-llms.txt
created: '2026-08-26'
description: Preferred Networks, Inc. (PFN) is a Tokyo-based AI company founded in March 2014 that vertically integrates the AI value chain from its own MN-Core AI processors and supercomputing infrastructure through to generative-AI foundation models, solutions and products. PFN develops PLaMo, a Japanese large language model built fully from scratch, and offers it commercially through the cloud-hosted PLaMo API — an OpenAI-compatible chat-completions, tokenize and models service at api.platform.preferredai.jp — alongside on-premises, Amazon Bedrock Marketplace, Snowflake and edge (PLaMo Lite) deployment options. PFN also maintains widely used open-source machine-learning software including Optuna, Chainer, PFRL, pytorch-pfn-extras and the PLaMo Translate CLI, which doubles as a locally hosted MCP server.
image: https://www.preferred.jp/images/ogp.png
layout: provider
mcp_servers:
- description: Preferred Networks ships one real MCP server, and it is not for the PLaMo API. The first-party plamo-translate CLI starts an MCP server as part of its `server` command, exposing the local plamo-2-tran
  name: Preferred Networks MCP surface
  slug: preferred-networks-mcp-surface
modified: '2026-08-26'
name: Preferred Networks
nav: Providers
network: true
overview: 'Preferred Networks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Large Language Models, and Generative AI.


  Preferred Networks'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Preferred Networks Plans Pricing
  plan_count: 4
  slug: preferred-networks-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 7
  name: Preferred Networks Rate Limits
  slug: preferred-networks-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 39.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/preferred-networks/refs/heads/main/screenshots/preferred-networks-2026-09-02T151924.png
security:
- kind: authentication
  name: Preferred Networks Authentication
  slug: preferred-networks-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Preferred Networks Domain Security
  slug: preferred-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Preferred Networks Trust Center
  slug: preferred-networks-trust-center
  summary_line: ISO/IEC 27001
slug: preferred-networks
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Large Language Models
- Generative AI
- LLM Inference
- Foundation Models
- Japan
- Semiconductors
- Supercomputing
- Translation
- MCP
website: https://www.preferred.jp/en/
---
