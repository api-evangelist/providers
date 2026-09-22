---
access_model:
  confidence: medium
  label: Free to start, price not published
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://v2.gigacatalyst.com/agent.md
  - https://v2.gigacatalyst.com/signup
  - https://gigacatalyst.com/pricing
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.5
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: The one public, unauthenticated operation Gigacatalyst publishes on its own behalf. A coding agent reads the project's API surface, builds a JSON description of it (organization, integrations, tools w
  name: Gigacatalyst Self-Serve Registration API
  slug: gigacatalyst-self-serve-registration-api
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/security/gigacatalyst-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gigacatalyst-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/security/gigacatalyst-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gigacatalyst-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gigacatalyst.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gigacatalyst
- group: docs
  title: ''
  type: Documentation
  url: https://gigacatalyst.com/self-serve-agent.md
- group: docs
  title: ''
  type: APIReference
  url: https://v2.gigacatalyst.com/agent.md
- group: start
  title: ''
  type: GettingStarted
  url: https://gigacatalyst.com/self
- group: company
  title: ''
  type: Blog
  url: https://gigacatalyst.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://v2.gigacatalyst.com/signup
- group: start
  title: ''
  type: Login
  url: https://v2.gigacatalyst.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gigacatalyst.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gigacatalyst.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://gigacatalyst.com/trust/vulnerability-disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/security/gigacatalyst-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gigacatalyst-vulnerability-disclosure.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/packages/gigacatalyst-packages.yml
  title: ''
  type: Packages
  url: packages/gigacatalyst-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/packages/gigacatalyst-packages.yml
  title: ''
  type: SDKs
  url: packages/gigacatalyst-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/cli/gigacatalyst-cli.yml
  title: ''
  type: CLI
  url: cli/gigacatalyst-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/components/gigacatalyst-components.yml
  title: ''
  type: Components
  url: components/gigacatalyst-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/llms/gigacatalyst-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gigacatalyst-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/conventions/gigacatalyst-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gigacatalyst-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/data-model/gigacatalyst-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gigacatalyst-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/errors/gigacatalyst-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gigacatalyst-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/authentication/gigacatalyst-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gigacatalyst-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/conformance/gigacatalyst-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gigacatalyst-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/lifecycle/gigacatalyst-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gigacatalyst-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/plans/gigacatalyst-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gigacatalyst-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/rate-limits/gigacatalyst-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gigacatalyst-rate-limits.yml
created: '2026-07-17'
description: Gigacatalyst (Giga Next Inc.) is a Y Combinator-backed enterprise AI platform that embeds an API-connected app builder directly into B2B SaaS products, so that customers, solutions engineers, and customer-success teams can describe a dashboard, report, or workflow in natural language and have it generated against the host product's own APIs, design language, permissions, and roles. Generated apps run inside the customer's environment using the signed-in user's session credentials, with granular write control and a choice of a Managed deployment (routed through the Gigacatalyst proxy for caching, rate limiting, and analytics, with AWS Bedrock zero-retention AI) or a Direct deployment where nothing routes through Gigacatalyst and the customer brings their own AI key. Gigacatalyst is primarily an API consumer rather than an API producer, but it does publish one public, unauthenticated, agent-facing operation - the self-serve registration endpoint documented at v2.gigacatalyst.com/agent.md
  - plus an official npm SDK and CLI, an embeddable React chat component, and an open-source browser extension.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gigacatalyst.png
layout: provider
modified: '2026-08-14'
name: Gigacatalyst
nav: Providers
network: true
overview: 'Gigacatalyst publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Software-as-a-Service, Sales Enablement, and Solutions Engineering.


  Gigacatalyst''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, CLI, authentication, and 21 more developer resources.'
plans:
- name: Gigacatalyst Plans Pricing
  plan_count: 0
  slug: gigacatalyst-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Gigacatalyst Rate Limits
  slug: gigacatalyst-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    operational_transparency: 13.2
  previous_composite: 28.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/gigacatalyst/refs/heads/main/screenshots/gigacatalyst-2026-07-25T215805.png
security:
- kind: authentication
  name: Gigacatalyst Authentication
  slug: gigacatalyst-authentication
  summary_line: none/session · 2 schemes
- kind: domain-security
  name: Gigacatalyst Domain Security
  slug: gigacatalyst-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Gigacatalyst Vulnerability Disclosure
  slug: gigacatalyst-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gigacatalyst Trust Center
  slug: gigacatalyst-trust-center
  summary_line: trust center published
slug: gigacatalyst
tags:
- Company
- Artificial Intelligence
- Software-as-a-Service
- Sales Enablement
- Solutions Engineering
- Customer Success
- Automation
- No-Code
- Agents
- Embedded Analytics
- Low-Code
- Developer Tools
- Y Combinator
website: https://gigacatalyst.com
---
