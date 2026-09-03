---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: E2B Agentic Access
  operation_count: 17
  slug: e2b-agentic-access
  summary_line: 17 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The E2B Sandbox API creates and controls per-agent Linux microVMs that can run arbitrary code, install packages, read and write files, stream terminal output, and host headless browsers. Code Interpre
  name: E2B Sandbox API
  slug: sandbox-api
- baseURL: https://api.e2b.dev
  baseurl_source: declared
  description: The Sandboxes API from E2B — 12 operation(s) for sandboxes.
  name: E2B Sandboxes API
  slug: e2b-sandboxes-api
- baseURL: https://api.e2b.dev
  baseurl_source: declared
  description: The Templates API from E2B — 1 operation(s) for templates.
  name: E2B Templates API
  slug: e2b-templates-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: E2B Sandbox Sandboxes API
  slug: open-e2b-sandboxes-api
- collection_type: open
  name: E2B Sandbox Sandboxes Templates API
  slug: open-e2b-templates-api
- collection_type: open
  name: E2B Sandbox API
  slug: open-e2b
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/e2b-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/e2b-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/e2b-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/e2b-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://e2b.dev
- group: docs
  title: ''
  type: Documentation
  url: https://e2b.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://e2b.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/e2b-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://e2b.dev/pricing
- group: start
  title: ''
  type: Signup
  url: https://e2b.dev/auth/sign-up
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/U7KEcGErtQ
- group: company
  title: ''
  type: Twitter
  url: https://x.com/e2b_dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://e2b.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://e2b.dev/privacy
created: '2026-05-23'
description: E2B provides secure, isolated sandbox runtimes for AI-generated and agent-driven code, built on Firecracker microVMs that cold-start in under 200ms. The platform's Code Interpreter, AI Sandboxes, and Desktop Sandbox products let LLMs execute Python, JavaScript, Ruby, C++ and other languages with full filesystem, terminal, package management, and browser access for sessions up to 24 hours. Customers include AI labs, agent startups, data teams, and enterprises building code interpreters, deep-research agents, data analysis features, and computer-use agents. SDKs are available for Python and TypeScript and integrate with OpenAI, Anthropic, Mistral, Llama, LangChain, LlamaIndex, and the Vercel AI SDK. Pricing is freemium with Pro and Enterprise tiers and a startups program.
finops:
- name: E2B Finops
  service_category: API
  slug: e2b-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/e2b.png
layout: provider
modified: '2026-05-23'
name: E2B
nav: Providers
network: true
overview: 'E2B publishes 2 APIs on the [APIs.io](https://apis.io/) network: Sandboxes API and Templates API. Tagged areas include Code Interpreter, Sandboxes, Secure Execution, AI Agents, and Firecracker.


  E2B''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: E2B Plans Pricing
  plan_count: 1
  slug: e2b-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: E2B Rate Limits
  slug: e2b-rate-limits
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 50.4
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/e2b/refs/heads/main/screenshots/e2b-2026-06-20T180350.png
security:
- kind: authentication
  name: E2B Authentication
  slug: e2b-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: E2B Domain Security
  slug: e2b-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: E2B Vulnerability Disclosure
  slug: e2b-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: e2b
tags:
- Code Interpreter
- Sandboxes
- Secure Execution
- AI Agents
- Firecracker
- MicroVMs
- Code Execution
- Data Analysis
- Desktop Sandbox
- Computer Use
- Custom Templates
- Python
- TypeScript
website: https://e2b.dev
---
