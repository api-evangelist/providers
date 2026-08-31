---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans/blue-prism-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Blue Prism API is the REST contract for Blue Prism Enterprise. It exposes work queues and work queue items, sessions and session logs, schedules, scheduled tasks and schedule logs, calendars and h
  name: Blue Prism API
  slug: blue-prism
- description: Also called the Timeline API. Lets third-party clients upload data to Process Intelligence projects, drive program modules without the UI, and retrieve processed results such as timeline statistics an
  name: Process Intelligence API
  slug: process-intelligence
artifact_total: 11
asyncapis:
- description: ''
  name: Blue Prism Webhooks
  slug: blue-prism-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.blueprism.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.blueprism.com/en-us/home.htm
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.blueprism.com/bp-7-5/en-us/bp-api/api-spec-home.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.blueprism.com/bp-7-5/en-us/Guides/bp-api/api-introduction.htm
- group: operate
  title: ''
  type: Support
  url: https://www.blueprism.com/contact/
- group: operate
  title: ''
  type: Community
  url: https://community.blueprism.com/
- group: company
  title: ''
  type: Blog
  url: https://www.blueprism.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blue-prism
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blue-prism-limited
- group: start
  title: ''
  type: Login
  url: https://portal.blueprism.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blueprism.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueprism.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blueprism.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.blueprism.com/bp-7-5/en-us/release-notes/rn-home.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/blue-prism-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blue-prism-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blue-prism-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/blue-prism-security.txt
- group: auth
  title: ''
  type: Security
  url: security/blue-prism-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blue-prism-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/blue-prism-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/blue-prism-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blue-prism-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blue-prism-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blue-prism-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blue-prism-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blue-prism-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blue-prism-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blue-prism-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blue-prism-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/blue-prism-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/blue-prism-enterprise-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/blue-prism-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/blue-prism-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/blue-prism-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blue-prism-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blue-prism-finops.yml
created: '2026-03-27'
description: SS&C Blue Prism is an enterprise intelligent-automation vendor whose platform combines robotic process automation, business process management and agentic AI. Its products — Blue Prism Enterprise, Blue Prism Cloud, WorkHQ, Chorus, AI Gateway, Decipher IDP and Process Intelligence — coordinate people, AI agents, digital workers and APIs across regulated, mission-critical workflows. Blue Prism Enterprise publishes a REST contract, the Blue Prism API, covering work queues, sessions, schedules, calendars, processes, runtime resources, licensing and webhook subscriptions. The company was acquired by SS&C Technologies in 2022.
finops:
- name: Blue Prism Finops
  service_category: API
  slug: blue-prism-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blue-prism.png
layout: provider
modified: '2026-08-29'
name: Blue Prism
nav: Providers
network: true
overview: 'Blue Prism publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Automation, RPA, Intelligent Automation, Business Process Management, and Process Orchestration.


  The Blue Prism catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Blue Prism''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 31 more developer resources.'
plans:
- name: Blue Prism Plans Pricing
  plan_count: 0
  slug: blue-prism-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Blue Prism Rate Limits
  slug: blue-prism-rate-limits
scopes:
- name: Blue Prism Scopes
  scope_count: 2
  slug: blue-prism-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 58.1
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 49.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blue-prism/refs/heads/main/screenshots/blue-prism-2026-06-20T173529.png
security:
- kind: authentication
  name: Blue Prism Authentication
  slug: blue-prism-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Blue Prism Domain Security
  slug: blue-prism-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blue Prism Vulnerability Disclosure
  slug: blue-prism-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Blue Prism Trust Center
  slug: blue-prism-trust-center
  summary_line: ISO/IEC 27001, Cyber Essentials
slug: blue-prism
tags:
- AI Automation
- RPA
- Intelligent Automation
- Business Process Management
- Process Orchestration
- Agentic AI
- Workflow-Automation
- Enterprise Software
website: https://www.blueprism.com
---
