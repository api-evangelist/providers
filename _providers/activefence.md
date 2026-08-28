---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Activefence Agentic Access
  operation_count: 18
  slug: activefence-agentic-access
  summary_line: 18 operations · 16 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Provides APIs to manage API key(s), including adding new keys, listing existing keys, and deleting keys.
  name: ActiveFence api keys API
  slug: activefence-api-keys-api
- description: Collection API Represents grouped entities. A collection is comprised of multiple items grouped together in a playlist, album, folder, group or channel on your platform. For example, a playlist of vid
  name: ActiveFence Collection API
  slug: activefence-collection-api
- description: Content APIs Represents WHAT content was created on your platform, such as a post, comment, review, message, article or data. For example, a web page containing a video, a customer review of a product
  name: ActiveFence Content API
  slug: activefence-content-api
- description: The Flags API enables you to send details about the flag made on an item on your platform to the Alice T&S platform.
  name: ActiveFence Flags API
  slug: activefence-flags-api
- description: Users API Represents WHO created content on your platform. These are the end users that have uploaded content to your platform, meaning the people who are the creators or publishers of the content. Fo
  name: ActiveFence Users API
  slug: activefence-users-api
- description: WonderBuild provides red teaming and security assessment tools for AI applications. APIs for running comprehensive security assessments on gen-AI applications.
  name: ActiveFence Wonder Build API
  slug: activefence-wonderbuild-api
- description: 'WonderFence provides real-time guardrails for AI-generated content. APIs for evaluating and moderating AI-generated content and interactions to protect against harmful outputs and prompt attacks. ## A'
  name: ActiveFence Wonder Fence API
  slug: activefence-wonderfence-api
artifact_total: 20
asyncapis:
- description: ''
  name: Activefence Webhooks
  slug: activefence-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alice API Documentation api keys API
  slug: open-activefence-api-keys-api
- collection_type: open
  name: Alice API Documentation Collection API
  slug: open-activefence-collection-api
- collection_type: open
  name: Alice API Documentation Content API
  slug: open-activefence-content-api
- collection_type: open
  name: Alice API Documentation Flags API
  slug: open-activefence-flags-api
- collection_type: open
  name: Alice API Documentation Users API
  slug: open-activefence-users-api
- collection_type: open
  name: Alice API Documentation Wonder Build API
  slug: open-activefence-wonderbuild-api
- collection_type: open
  name: Alice API Documentation Wonder Fence API
  slug: open-activefence-wonderfence-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/activefence-mcp.yml
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
mcp_servers:
- description: ''
  name: ActiveFence MCP Server
  slug: activefence-mcp-server
modified: '2026-08-06'
name: ActiveFence
nav: Providers
network: true
overview: 'ActiveFence publishes 7 APIs on the [APIs.io](https://apis.io/) network, including api keys API, Collection API, Content API, and 4 more. Tagged areas include AI Safety, AI Security, Trust and Safety, Content Moderation, and Guardrails.


  The ActiveFence catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ActiveFence''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 23 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 51.6
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 67.0
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/activefence/refs/heads/main/screenshots/activefence-2026-08-07T160856.png
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
- AI Safety
- AI Security
- Trust and Safety
- Content Moderation
- Guardrails
- Red Teaming
- LLM Security
- Prompt Injection
- AI Governance
- Risk Scoring
- User Generated Content
- Child Safety
website: https://alice.io/
---
