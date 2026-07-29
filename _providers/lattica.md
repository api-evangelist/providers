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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The LatticaAI platform API for deploying and operating encrypted workloads. An RPC-style HTTPS surface rooted at https://api.lattica.ai/api/, authenticated with a Bearer token, covering account and fi
  name: Lattica Platform API
  slug: platform
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lattica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lattica.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lattica.ai/documentation.html
- group: docs
  title: ''
  type: Documentation
  url: https://platformdocs.lattica.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://platformdocs.lattica.ai/how-to-guides/client-installation.md
- group: start
  title: ''
  type: SignUp
  url: https://console.lattica.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.lattica.ai/contact.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lattica-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://platformdocs.lattica.ai/conceptual-guide/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lattica.ai/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lattica.ai/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://www.lattica.ai/news.html
- group: other
  title: ''
  type: WhitePaper
  url: https://www.lattica.ai/assets/docs/lattica-fhe-technical-whitepaper.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lattica/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/latticaai
- group: build
  title: ''
  type: Packages
  url: packages/lattica-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lattica-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lattica-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lattica-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lattica-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lattica-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lattica-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lattica-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lattica-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lattica-data-model.yml
created: '2026-07-17'
description: LatticaAI is an Israeli privacy-technology company building Fully Homomorphic Encryption (FHE) as a service, letting AI inference and database queries run on encrypted data at cloud scale with zero plaintext exposure. Lattica builds the full stack — the cryptography, a compiler that turns models into homomorphic-ready pipelines, and a GPU-accelerated FHE runtime called the Encrypted Execution Layer. Service providers deploy models and vector databases as workloads; end users query them through a Query Client that encrypts input on-device and decrypts results locally, so the server only ever sees ciphertext. HEAL (Homomorphic Encryption Abstraction Layer) bridges the FHE software stack to acceleration hardware.
image: https://www.lattica.ai/assets/logo/White%20logo%20-%20no%20background.svg
layout: provider
mcp_servers:
- description: ''
  name: lattica-mcp.yml
  slug: lattica-mcpyml
modified: '2026-07-19'
name: Lattica
nav: Providers
network: true
overview: 'Lattica publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privacy, Fully Homomorphic Encryption, Encryption, and Confidential Computing.


  Lattica''s developer surface includes documentation, getting-started guide, signup flow, support, pricing, engineering blog, authentication, and 18 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 30.7
  delta: -0.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 31.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lattica/refs/heads/main/screenshots/lattica-2026-07-25T224607.png
security:
- kind: authentication
  name: Lattica Authentication
  slug: lattica-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Lattica Domain Security
  slug: lattica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lattica
tags:
- Company
- Privacy
- Fully Homomorphic Encryption
- Encryption
- Confidential Computing
- Artificial Intelligence
- Machine Learning
- Inference
- Vector Search
- Security
website: https://www.lattica.ai/
---
