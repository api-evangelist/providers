---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - '{''url'': ''https://safetyculture.com'', ''status'': 301, ''note'': ''declared website redirects to https://mitti.com/ — a different registrable domain (safetyculture.com -> mitti.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: REST API for the SafetyCulture platform — inspections, templates, assets, actions, issues, users, groups, schedules, training, credentials, and webhooks. Bearer-token auth over HTTPS.
  name: SafetyCulture API
  slug: safetyculture-api
artifact_total: 7
asyncapis:
- description: ''
  name: Safetyculture Webhooks
  slug: safetyculture-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://safetyculture.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.safetyculture.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.safetyculture.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.safetyculture.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.safetyculture.com/reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://safetyculture.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://safetyculture.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.safetyculture.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://safetyculture.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://safetyculture.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://safetyculture.com/partner-program/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SafetyCulture
- group: operate
  title: ''
  type: StatusPage
  url: https://status.safetyculture.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/authentication/safetyculture-authentication.yml
  title: ''
  type: Authentication
  url: authentication/safetyculture-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/llms/safetyculture-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/safetyculture-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/well-known/safetyculture-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/safetyculture-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/well-known/safetyculture-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/safetyculture-security.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/rate-limits/safetyculture-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/safetyculture-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/asyncapi/safetyculture-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/safetyculture-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/conventions/safetyculture-conventions.yml
  title: ''
  type: Conventions
  url: conventions/safetyculture-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/lifecycle/safetyculture-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/safetyculture-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/conformance/safetyculture-conformance.yml
  title: ''
  type: Conformance
  url: conformance/safetyculture-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://safetyculture.com/security
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/packages/safetyculture-packages.yml
  title: ''
  type: Packages
  url: packages/safetyculture-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/packages/safetyculture-packages.yml
  title: ''
  type: SDKs
  url: packages/safetyculture-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/cli/safetyculture-cli.yml
  title: ''
  type: CLI
  url: cli/safetyculture-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/mcp/safetyculture-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/safetyculture-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/security/safetyculture-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/safetyculture-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/security/safetyculture-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/safetyculture-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://safetyculture.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/security/safetyculture-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/safetyculture-trust-center.yml
created: '2026-07-17'
description: SafetyCulture (formerly iAuditor) is a workplace operations and safety platform used by frontline teams to run inspections, capture and track issues, assign corrective actions, manage assets and sites, deliver training, and provision users. Its public REST API at https://api.safetyculture.io exposes more than 380 documented operations across inspections, templates, assets, actions, issues, users, groups, schedules, training, credentials, and webhooks, secured with bearer API tokens (service-user and personal). Near real-time webhooks stream a rich catalog of inspection, action, incident, media, and training events, and SCIM 2.0 supports user provisioning via Microsoft Entra ID and Okta.
image: https://safetyculture.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: SafetyCulture
nav: Providers
network: true
overview: 'SafetyCulture publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Safety, Inspection, and Workplace Operations.


  The SafetyCulture catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SafetyCulture''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 25 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 6
  name: Safetyculture Rate Limits
  slug: safetyculture-rate-limits
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.7
    discoverability: 75.9
    operational_transparency: 68.4
  previous_composite: 50.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/safetyculture/refs/heads/main/screenshots/safetyculture-2026-08-17T081708.png
security:
- kind: authentication
  name: Safetyculture Authentication
  slug: safetyculture-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Safetyculture Domain Security
  slug: safetyculture-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Safetyculture Vulnerability Disclosure
  slug: safetyculture-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Safetyculture Trust Center
  slug: safetyculture-trust-center
  summary_line: SOC 2, ISO 27001
slug: safetyculture
tags:
- Company
- Business Applications
- Safety
- Inspection
- Workplace Operations
- EHS
- Compliance
- Training
- Field Service
- Webhook
website: https://safetyculture.com
---
