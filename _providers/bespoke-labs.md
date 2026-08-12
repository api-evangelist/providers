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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bespoke Labs Agentic Access
  operation_count: 1
  slug: bespoke-labs-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Minicheck API from Bespoke Labs — 1 operation(s) for minicheck.
  name: Bespoke Labs Minicheck API
  slug: bespoke-labs-minicheck-api
artifact_total: 5
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bespoke-labs-minicheck-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bespoke-labs-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bespoke-labs-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bespoke-labs-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/bespoke-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bespoke-labs-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bespoke-labs-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bespoke-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bespoke-labs-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bespoke-labs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bespoke-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bespoke-labs-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bespoke-labs-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bespoke-labs-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bespokelabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bespokelabs.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bespokelabs.ai/models/bespoke-minicheck/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bespokelabs.ai/bespoke-curator/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://console.bespokelabs.ai
- group: operate
  title: ''
  type: Support
  url: https://bespokelabs.ai/contact
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/KqpXvpzVBS
- group: company
  title: ''
  type: Blog
  url: https://bespokelabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bespokelabsai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bespokelabs.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bespokelabs.ai/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://bespokelabs.ai
created: '2026-07-17'
description: Bespoke Labs is an applied AI research lab building environment infrastructure, data curation, and evaluation tooling for AI agents and post-training. Its open-source Bespoke Curator library generates high-quality synthetic data at scale for model finetuning and structured extraction, and its Bespoke MiniCheck ("Argus") API offers a lightweight grounded-factuality / hallucination-detection service that scores whether a claim is supported by a given context. The lab is also known for OpenThoughts reasoning datasets, Terminal-Bench, the GEPA prompt optimizer, MiniChart, and OpenThinker. Backed by 8VC, Mayfield, and Wing Venture Capital.
image: https://framerusercontent.com/images/3uXQTaKpkGh6gD7qAWsAwPMhk.png
layout: provider
mcp_servers:
- description: ''
  name: bespoke-labs-mcp.yml
  slug: bespoke-labs-mcpyml
modified: '2026-07-18'
name: Bespoke Labs
nav: Providers
network: true
overview: 'Bespoke Labs publishes 1 API on the [APIs.io](https://apis.io/) network: Minicheck API. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM, and Synthetic Data.


  Bespoke Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 20 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 41.3
  delta: -1.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 49.3
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bespoke-labs/refs/heads/main/screenshots/bespoke-labs-2026-07-25T202750.png
security:
- kind: authentication
  name: Bespoke Labs Authentication
  slug: bespoke-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bespoke Labs Domain Security
  slug: bespoke-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bespoke-labs
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM
- Synthetic Data
- Data Curation
- Fact Checking
- Hallucination Detection
- AI Agents
- Evaluation
website: https://bespokelabs.ai
---
