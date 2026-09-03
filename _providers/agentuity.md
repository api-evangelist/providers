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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Direct HTTP access to Agentuity platform services — projects, deployments, API keys, OAuth applications, storage (key-value, vector, object, Postgres), message queues, durable streams, sandboxes, sche
  name: Agentuity Platform REST API
  slug: agentuity-platform-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Agentuity Webhooks
  slug: agentuity-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.agentuity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.agentuity.com
- group: docs
  title: ''
  type: Documentation
  url: https://agentuity.dev
- group: docs
  title: ''
  type: APIReference
  url: https://agentuity.dev/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://agentuity.dev/get-started
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/UPRUw4cn65
- group: company
  title: ''
  type: Blog
  url: https://agentuity.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentuity
- group: commercial
  title: ''
  type: Pricing
  url: https://agentuity.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.agentuity.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.agentuity.com
- group: start
  title: ''
  type: Console
  url: https://app.agentuity.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentuity.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentuity.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentuity-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/agentuity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agentuity-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/agentuity-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentuity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentuity-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agentuity-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentuity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentuity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agentuity.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentuity-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentuity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://agentuity.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/agentuity-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agentuity-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/agentuity-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agentuity-webhooks.yml
created: '2026-07-17'
description: Agentuity is a full-stack cloud platform for building, deploying, and operating AI agents and the framework apps around them. Developers keep their existing framework (Next.js, Hono, React Router, SvelteKit, Nuxt, Astro, Vite React, TanStack Start) and attach Agentuity service clients for key-value, vector, object, and Postgres storage, durable streams, queues, webhooks, email, and cron schedules, plus sandboxes (isolated Linux containers), an AI Gateway that routes to OpenAI/Anthropic/Groq/Google, and OpenTelemetry observability. The agentuity CLI scaffolds projects, runs local development with environment wiring, and deploys to managed cloud, private cloud, on-prem, multi-cloud, or edge via the Gravity Network. A documented REST API, first-party JavaScript/TypeScript, Python, and Go SDKs, published Agent Skills, and Claude Code / OpenCode plugins round out the developer surface.
image: https://agentuity.com/og-image.png
layout: provider
modified: '2026-07-17'
name: Agentuity
nav: Providers
network: true
overview: 'Agentuity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agents, Artificial Intelligence, Cloud, and Serverless.


  The Agentuity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agentuity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 48.2
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentuity/refs/heads/main/screenshots/agentuity-2026-07-25T195301.png
security:
- kind: authentication
  name: Agentuity Authentication
  slug: agentuity-authentication
  summary_line: http/apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Agentuity Domain Security
  slug: agentuity-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agentuity Vulnerability Disclosure
  slug: agentuity-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Agentuity Trust Center
  slug: agentuity-trust-center
  summary_line: SOC 2, HIPAA, GDPR, FIPS 140
slug: agentuity
tags:
- Company
- Agents
- Artificial Intelligence
- Cloud
- Serverless
- Platform
- Developer Tools
- LLM
- Infrastructure
- Deployment
- AI Gateway
website: https://www.agentuity.com/
---
