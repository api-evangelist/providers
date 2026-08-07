---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Activefence Agentic Access
  operation_count: 18
  slug: activefence-agentic-access
  summary_line: 18 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Single REST API covering both Alice product families. ActiveFamily endpoints accept text, image, video and audio items — plus users, collections and user flags — and return per-violation risk scores b
  name: Alice API (formerly ActiveFence)
  slug: alice-api-formerly-activefence
artifact_total: 5
asyncapis:
- description: ''
  name: Activefence Webhooks
  slug: activefence-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/activefence-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://alice.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.activefence.com/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.activefence.com/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.activefence.com/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.activefence.com/index.html#section/Authentication
- group: operate
  title: ''
  type: Support
  url: https://alice.io/contact-us
- group: company
  title: ''
  type: Blog
  url: https://alice.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ActiveFence
- group: start
  title: ''
  type: Login
  url: https://app.alice.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alice.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alice.io/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/activefence-demo-team
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/activefence-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/activefence-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/activefence-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/activefence-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/activefence-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/activefence-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/activefence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/activefence-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/activefence-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/activefence-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activefence-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/activefence-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/activefence-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/activefence-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/activefence-alice-api-overlay.yaml
created: '2026-08-06'
description: 'ActiveFence — now operating as Alice — is an AI security, safety and trust & safety company headquartered in New York and Tel Aviv. It sells two product families through one REST API at api.alice.io: ActiveFamily (ActiveScore automated detection plus the ActiveOS moderation workbench) for user-generated-content trust and safety across text, image, video and audio in 120+ languages and 20+ abuse areas; and WonderSuite for generative-AI protection — WonderBuild (pre-deployment red teaming and adversarial assessment of models, apps and agents), WonderFence (real-time runtime guardrails that evaluate prompts and responses for prompt injection, jailbreaks, PII leakage and policy violations) and WonderCheck (ongoing post-launch evaluation and drift detection). The API offers synchronous endpoints for low-latency moderation and asynchronous endpoints that acknowledge receipt and post results back to a customer-configured callback URL, plus configurable action webhooks fired from the
  ActiveOS moderation view or an automated workflow. Authentication is a single af-api-key header issued from the platform console; the default rate limit is 50 requests per second. First-party SDKs ship for Python (wonderfence-sdk) and TypeScript (@alice-io/wonderfence-ts-sdk), with a Parlant integration and the open-source Caterpillar agent-skill security scanner. Alice is SOC 2 and ISO 27001 certified.'
image: https://cdn.prod.website-files.com/69005ca0f0832195cbc1370c/6966208e49b12596bab0f42e_Group%201707480796.png
layout: provider
modified: '2026-08-06'
name: ActiveFence
nav: Providers
network: true
overview: 'ActiveFence publishes 1 API on the [APIs.io](https://apis.io/) network: Alice API (formerly ActiveFence). Tagged areas include ai-safety, ai-security, trust-and-safety, content-moderation, and guardrails.


  The ActiveFence catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ActiveFence''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 22 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 54.6
  facets:
    commercial_clarity: 42.1
    contract_quality: 76.3
    developer_ergonomics: 71.2
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Activefence Authentication
  slug: activefence-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Activefence Domain Security
  slug: activefence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: activefence
tags:
- ai-safety
- ai-security
- trust-and-safety
- content-moderation
- guardrails
- red-teaming
- llm-security
- prompt-injection
- ai-governance
- risk-scoring
- user-generated-content
- child-safety
website: https://alice.io/
---
