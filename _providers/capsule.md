---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Capsule Agentic Access
  operation_count: 32
  slug: capsule-agentic-access
  summary_line: 32 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.capsulecrm.com/api/v2
  baseurl_source: declared
  description: The Opportunities API from Capsule — 7 operation(s) for opportunities.
  name: Capsule Opportunities API
  slug: capsule-opportunities-api
- baseURL: https://api.capsulecrm.com/api/v2
  baseurl_source: declared
  description: The Parties API from Capsule — 5 operation(s) for parties.
  name: Capsule Parties API
  slug: capsule-parties-api
- baseURL: https://api.capsulecrm.com/api/v2
  baseurl_source: declared
  description: The Projects API from Capsule — 5 operation(s) for projects.
  name: Capsule Projects API
  slug: capsule-projects-api
- baseURL: https://api.capsulecrm.com/api/v2
  baseurl_source: declared
  description: The Tasks API from Capsule — 2 operation(s) for tasks.
  name: Capsule Tasks API
  slug: capsule-tasks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Capsule Rest Hooks Webhooks
  slug: capsule-rest-hooks-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Capsule CRM REST Opportunities API
  slug: open-capsule-opportunities-api
- collection_type: open
  name: Capsule CRM REST Opportunities Parties API
  slug: open-capsule-parties-api
- collection_type: open
  name: Capsule CRM REST Opportunities Projects API
  slug: open-capsule-projects-api
- collection_type: open
  name: Capsule CRM REST Opportunities Tasks API
  slug: open-capsule-tasks-api
- collection_type: open
  name: Capsule CRM REST API
  slug: open-capsule
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capsule-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capsule-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capsule-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capsulecrm
- group: company
  title: ''
  type: Website
  url: https://capsulecrm.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.capsulecrm.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://capsulecrm.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://capsulecrm.com/support
- group: company
  title: ''
  type: Blog
  url: https://capsulecrm.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capsulecrm.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capsulecrm.com/terms/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/capsule-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://api.capsulecrm.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/capsule-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/capsule-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/capsule-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capsule-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/capsule-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/capsule-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://capsulecrm.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/capsule-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/capsule-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/capsule-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/capsule-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/capsule-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.capsulecrm.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/capsule-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/capsule-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/capsule-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/capsule-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/capsule-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/capsule-rest-hooks-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.capsulecrm.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.capsulecrm.com/v2/operations/Party
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.capsulecrm.com/v2/overview/authentication
- group: start
  title: ''
  type: SignUp
  url: https://capsulecrm.com/signup/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zestia
- group: operate
  title: ''
  type: HelpCenter
  url: https://capsulecrm.com/help/
created: '2025-01-01'
description: Capsule is a CRM and project-management platform for small and mid-sized businesses that unifies contacts, sales pipelines, tasks, cases, and projects. The Capsule REST API exposes parties (contacts and companies), opportunities, projects, tasks, cases, entries, tracks, and settings such as tags, pipelines, milestones, stages, and custom fields, with REST Hooks webhooks for event-driven integration.
finops:
- name: Capsule Finops
  service_category: API
  slug: capsule-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capsule.png
layout: provider
mcp_servers:
- description: 'First-party Model Context Protocol server for Capsule CRM, published by Zestia Ltd (the company that operates Capsule - the capsulecrm.com CAA record names caa-iodef@zestia.com, and the repository is '
  name: Capsule MCP Server
  slug: capsule-mcp-server
modified: '2026-09-05'
name: Capsule
nav: Providers
network: true
overview: 'Capsule publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Opportunities API, Parties API, Projects API, and 1 more. Tagged areas include Contact Management, CRM, Custom Fields, Opportunities, and Pipelines.


  The Capsule catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Capsule''s developer surface includes authentication, documentation, pricing, support, engineering blog, changelog, API reference, and 32 more developer resources.'
plans:
- name: Capsule Plans Pricing
  plan_count: 5
  slug: capsule-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Capsule Rate Limits
  slug: capsule-rate-limits
scopes:
- name: Capsule Scopes
  scope_count: 0
  slug: capsule-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 33.1
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 0.0
    contract_quality: 58.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 73.7
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/capsule/refs/heads/main/screenshots/capsule-2026-06-20T173941.png
security:
- kind: authentication
  name: Capsule Authentication
  slug: capsule-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Capsule Domain Security
  slug: capsule-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Capsule Vulnerability Disclosure
  slug: capsule-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Capsule Trust Center
  slug: capsule-trust-center
  summary_line: ISO 27001, PCI-DSS, SOC (report)
slug: capsule
tags:
- Contact Management
- CRM
- Custom Fields
- Opportunities
- Pipelines
- Project Management
- REST
- Sales
- Task
- Webhook
website: https://capsulecrm.com
---
