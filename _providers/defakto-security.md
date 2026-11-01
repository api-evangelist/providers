---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The Defakto control-plane API. A gRPC service surface of sixteen versioned services covering trust domains, clusters, realms, workloads, access policy, service accounts and sessions, agent and provide
  name: Defakto Management API
  slug: defakto-security-management-api
- description: The pre-rebrand SPIRL control-plane endpoint, still documented and still serving the legacy app.spirl.com console and the spirlctl CLI alongside the current api.defakto.security host. Same gRPC servic
  name: SPIRL Management API (legacy)
  slug: defakto-security-legacy-management-api
artifact_total: 13
asyncapis:
- description: ''
  name: Defakto Security Audit Events
  slug: defakto-security-audit-events
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.defakto.security/feed/
- group: auth
  href: https://artifacts.apis.io/defakto-security/security/defakto-security-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/defakto-security-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/defakto-security/security/defakto-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defakto-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.defakto.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://d.defakto.security/
- group: docs
  title: ''
  type: Documentation
  url: https://d.defakto.security/
- group: docs
  title: ''
  type: APIReference
  url: https://d.defakto.security/cli/spirlctl/overview.md
- group: start
  title: ''
  type: GettingStarted
  url: https://d.defakto.security/mint/quick-start.md
- group: company
  title: ''
  type: Blog
  url: https://www.defakto.security/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/defakto-security
- group: operate
  title: ''
  type: Support
  url: https://www.defakto.security/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.defakto.security/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.defakto.security/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.defakto.security/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.defakto.security/security/
- group: agent
  href: https://artifacts.apis.io/defakto-security/llms/defakto-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defakto-security-llms.txt
- group: build
  href: https://artifacts.apis.io/defakto-security/packages/defakto-security-packages.yml
  title: ''
  type: Packages
  url: packages/defakto-security-packages.yml
- group: build
  href: https://artifacts.apis.io/defakto-security/packages/defakto-security-packages.yml
  title: ''
  type: SDKs
  url: packages/defakto-security-packages.yml
- group: build
  href: https://artifacts.apis.io/defakto-security/cli/defakto-security-cli.yml
  title: ''
  type: CLI
  url: cli/defakto-security-cli.yml
- group: auth
  href: https://artifacts.apis.io/defakto-security/authentication/defakto-security-authentication.yml
  title: ''
  type: Authentication
  url: authentication/defakto-security-authentication.yml
- group: design
  href: https://artifacts.apis.io/defakto-security/conventions/defakto-security-conventions.yml
  title: ''
  type: Conventions
  url: conventions/defakto-security-conventions.yml
- group: design
  href: https://artifacts.apis.io/defakto-security/conformance/defakto-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/defakto-security-conformance.yml
- group: design
  href: https://artifacts.apis.io/defakto-security/errors/defakto-security-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/defakto-security-problem-types.yml
- group: design
  href: https://artifacts.apis.io/defakto-security/lifecycle/defakto-security-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/defakto-security-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/defakto-security/lifecycle/defakto-security-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/defakto-security-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/defakto-security/changelog/defakto-security-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/defakto-security-changelog.yml
- group: design
  href: https://artifacts.apis.io/defakto-security/data-model/defakto-security-data-model.yml
  title: ''
  type: DataModel
  url: data-model/defakto-security-data-model.yml
- group: start
  href: https://artifacts.apis.io/defakto-security/sandbox/defakto-security-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/defakto-security-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/defakto-security/plans/defakto-security-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/defakto-security-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/defakto-security/rate-limits/defakto-security-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/defakto-security-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/defakto-security/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'Defakto (formerly SPIRL) is a non-human identity (NHI) security company that issues short-lived, cryptographically attested identities to workloads, services, CI/CD pipelines and AI agents in place of static secrets, API keys and long-lived service accounts. The platform is built on SPIFFE and ships two products: Mint, which runs Trust Domain Servers and Agents that mint X.509-SVIDs, JWT-SVIDs and proof-of-possession WIT-SVIDs for Kubernetes, Linux, Docker and serverless workloads under a dozen attestation methods; and Ledger, which discovers, risk-scores and eradicates static secrets across AWS, Azure, GCP, Kubernetes, Anthropic, OpenAI, Bedrock AgentCore and Gemini. The control plane is driven by a gRPC management API and the spirlctl CLI, with a Go SDK, an OpenTofu/Terraform provider, workload identity federation into AWS/Azure/GCP, and OCSF 1.8.0 audit logging.'
finops:
- has_sources: true
  method: derived
  name: Defakto Security Finops
  primary_unit: ''
  service_category: ''
  slug: defakto-security-finops
  template: true
image: https://www.defakto.security/wp-content/uploads/2025/09/defakto-logo.svg
layout: provider
modified: '2026-10-06'
name: Defakto Security
nav: Providers
network: true
overview: 'Defakto Security is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Identity, Non-Human Identity, Workload Identity, and SPIFFE.


  The Defakto Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Defakto Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 24 more developer resources.'
plans:
- name: Defakto Security Plans Pricing
  plan_count: 0
  slug: defakto-security-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Defakto Security Rate Limits
  slug: defakto-security-rate-limits
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 80.4
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 48.9
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/defakto-security/defakto-security-2026-08-17T080850.png
security:
- kind: authentication
  name: Defakto Security Authentication
  slug: defakto-security-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Defakto Security Domain Security
  slug: defakto-security-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Defakto Security Vulnerability Disclosure
  slug: defakto-security-vulnerability-disclosure
  summary_line: Hackerone · contact published
skill_count: 4
skills:
- name: defakto-audit-credential-issuance
  slug: defakto-security-audit-credential-issuance
- name: defakto-onboard-trust-domain
  slug: defakto-security-onboard-trust-domain
- name: defakto-rotate-signing-keys
  slug: defakto-security-rotate-signing-keys
- name: defakto-secretless-cicd
  slug: defakto-security-secretless-cicd
slug: defakto-security
tags:
- Security
- Identity
- Non-Human Identity
- Workload Identity
- SPIFFE
- Authentication
- Zero Trust
- Secrets Management
- Kubernetes
- CI/CD
- Cloud Security
- gRPC
- Machine Identity
- AI Agents
- Developer Tools
- Identity Federation
website: https://www.defakto.security/
---
