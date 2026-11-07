---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ortto Agentic Access
  operation_count: 11
  slug: ortto-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Create, update, retrieve, and manage accounts (organizations).
  name: Ortto Accounts API
  phrasing_intents:
  - id: mergeAccounts
    intent: Create or update company accounts
    question: How do I add or update organizations (accounts) in Ortto from my CRM?
  phrasing_ops: 1
  slug: ortto-accounts-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Send custom activity events and manage activity definitions.
  name: Ortto Activities API
  phrasing_intents:
  - id: createActivities
    intent: Record custom activity events for people
    question: How do I send custom events like 'signed up for webinar' into Ortto?
  phrasing_ops: 1
  slug: ortto-activities-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Retrieve campaigns, reports, and assets.
  name: Ortto Campaigns API
  phrasing_intents:
  - id: getCampaignCalendar
    intent: List campaigns scheduled in a time period
    question: Which journeys and campaigns are running on my marketing calendar this month?
  - id: getCampaignReport
    intent: Get performance report for a campaign or asset
    question: How did my email campaign perform in Ortto?
  phrasing_ops: 2
  slug: ortto-campaigns-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Create, update, retrieve, and manage people (contacts).
  name: Ortto People API
  phrasing_intents:
  - id: mergePeople
    intent: Create or update contacts
    question: How do I sync contacts from my app into Ortto without creating duplicates?
  - id: getPeople
    intent: Search contacts with a filter
    question: How can I find all contacts matching a condition, like a certain city or tag?
  - id: getPeopleByIds
    intent: Look up contacts by their contact IDs
    question: I already have Ortto contact IDs; how do I fetch those exact people?
  - id: deletePeople
    intent: Delete contacts
    question: How do I permanently remove contacts from my Ortto account?
  phrasing_ops: 4
  slug: ortto-people-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Retrieve account tags.
  name: Ortto Tags API
  phrasing_intents:
  - id: getTags
    intent: List tags on the account
    question: What tags exist in my Ortto account?
  phrasing_ops: 1
  slug: ortto-tags-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Send transactional email and SMS.
  name: Ortto Transactional API
  phrasing_intents:
  - id: sendTransactionalEmail
    intent: Send a transactional email
    question: How do I send a password reset or receipt email through Ortto?
  - id: sendTransactionalSms
    intent: Send a transactional SMS
    question: How do I text a one-time code or order update to a customer via Ortto?
  phrasing_ops: 2
  slug: ortto-transactional-api
artifact_total: 28
asyncapis:
- description: ''
  name: Ortto Webhooks
  slug: ortto-webhooks
collections:
- collection_type: open
  name: Ortto Accounts API
  slug: open-ortto-accounts-api
- collection_type: open
  name: Ortto Accounts Activities API
  slug: open-ortto-activities-api
- collection_type: open
  name: Ortto Accounts Campaigns API
  slug: open-ortto-campaigns-api
- collection_type: open
  name: Ortto Accounts People API
  slug: open-ortto-people-api
- collection_type: open
  name: Ortto Accounts Tags API
  slug: open-ortto-tags-api
- collection_type: open
  name: Ortto Accounts Transactional API
  slug: open-ortto-transactional-api
- collection_type: open
  name: Ortto API
  slug: open-ortto
common:
- group: other
  href: https://artifacts.apis.io/ortto/capabilities/ortto-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ortto-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ortto/agentic-access/ortto-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ortto-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ortto/security/ortto-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ortto-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ortto/security/ortto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ortto-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ortto/authentication/ortto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ortto-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autopilot3
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ortto
- group: company
  title: ''
  type: Website
  url: https://ortto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ortto.com/developers/
- group: commercial
  href: https://artifacts.apis.io/ortto/plans/ortto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ortto-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ortto/rate-limits/ortto-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ortto-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ortto/finops/ortto-finops.yml
  title: ''
  type: FinOps
  url: finops/ortto-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ortto.com/blog
- group: build
  href: https://artifacts.apis.io/ortto/packages/ortto-packages.yml
  title: ''
  type: Packages
  url: packages/ortto-packages.yml
- group: build
  href: https://artifacts.apis.io/ortto/packages/ortto-packages.yml
  title: ''
  type: SDKs
  url: packages/ortto-packages.yml
- group: agent
  href: https://artifacts.apis.io/ortto/well-known/ortto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ortto-well-known.yml
- group: auth
  href: https://artifacts.apis.io/ortto/well-known/ortto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ortto-security.txt
- group: auth
  href: https://artifacts.apis.io/ortto/security/ortto-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ortto-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ortto/security/ortto-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ortto-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ortto/security/ortto-trust-center.yml
  title: ''
  type: Compliance
  url: security/ortto-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/ortto/mcp/ortto-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ortto-mcp.yml
- group: build
  href: https://artifacts.apis.io/ortto/mcp/ortto-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ortto-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ortto/llms/ortto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ortto-llms.txt
- group: design
  href: https://artifacts.apis.io/ortto/conformance/ortto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ortto-conformance.yml
- group: design
  href: https://artifacts.apis.io/ortto/errors/ortto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ortto-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ortto/conventions/ortto-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ortto-conventions.yml
- group: design
  href: https://artifacts.apis.io/ortto/lifecycle/ortto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ortto-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ortto/data-model/ortto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ortto-data-model.yml
- group: design
  href: https://artifacts.apis.io/ortto/components/ortto-components.yml
  title: ''
  type: Components
  url: components/ortto-components.yml
- group: design
  href: https://artifacts.apis.io/ortto/asyncapi/ortto-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ortto-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/ortto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/ortto/changelog/ortto-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ortto-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://roadmap.ortto.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://www.orttostatus.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.ortto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ortto.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ortto.com/a-222-ortto-developer-documentation
- group: operate
  title: ''
  type: Support
  url: https://help.ortto.com/
- group: start
  title: ''
  type: SignUp
  url: https://ortto.com/trial/
- group: start
  title: ''
  type: Login
  url: https://ortto.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ortto.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ortto.com/privacy/
- group: build
  href: https://artifacts.apis.io/ortto/collections/ortto.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/ortto.postman_collection.json
- group: build
  href: https://artifacts.apis.io/ortto/collections/ortto.opencollection.json
  title: ''
  type: OpenCollection
  url: collections/ortto.opencollection.json
created: '2026-06-25'
description: Ortto (formerly Autopilot) is a marketing automation, customer data platform (CDP), and analytics product. Its REST API at https://api.ap3api.com/v1 lets applications create and update people/contacts and accounts, send custom activity events, manage tags, retrieve campaign reports, and send transactional email and SMS, all authenticated with a custom API key via the X-Api-Key header, with EU and AU service endpoints for accounts in those data-residency regions. Ortto also runs a first-party hosted MCP server, released in version 1.27 (December 2025), giving agents a read-heavy surface over campaigns, contacts, audiences, reports, schema and knowledge-base content. Ortto publishes no machine-readable OpenAPI; the specifications here are scaffolded from its help-center API reference. Ortto announced in April 2026 that it is joining Canva.
finops:
- has_sources: true
  method: derived
  name: Ortto Finops
  primary_unit: ''
  service_category: ''
  slug: ortto-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ortto.png
layout: provider
mcp_servers:
- description: Ortto ships a first-party hosted MCP server, announced in the 1.27 release (19 December 2025) and documented in its own help-center category (help.ortto.com/c-332-ortto-mcp). It is a remote HTTP MCP e
  name: Ortto MCP
  slug: ortto-mcp
modified: '2026-08-13'
name: Ortto
nav: Providers
network: true
overview: 'Ortto publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Campaigns API, and 3 more. Tagged areas include Marketing Automation, CDP, Customer Data Platform, Analytics, and Email.


  The Ortto catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ortto''s developer surface includes authentication, documentation, engineering blog, changelog, getting-started guide, support, signup flow, and 37 more developer resources.'
plans:
- name: Ortto Plans Pricing
  plan_count: 5
  slug: ortto-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 14
  name: Ortto Rate Limits
  slug: ortto-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Ortto API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: ortto-rules
score:
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 56.1
    developer_ergonomics: 67.3
    discoverability: 75.0
    operational_transparency: 89.5
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ortto/ortto-2026-08-07T190955.png
security:
- kind: authentication
  name: Ortto Authentication
  slug: ortto-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ortto Domain Security
  slug: ortto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ortto Vulnerability Disclosure
  slug: ortto-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ortto Trust Center
  slug: ortto-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CCPA, EU-US Data Privacy Framework
skill_count: 4
skills:
- name: Pull campaign reporting
  slug: ortto-pull-campaign-reporting
- name: Send a transactional email or SMS
  slug: ortto-send-transactional-message
- name: Sync contacts into Ortto
  slug: ortto-sync-contacts
- name: Track a custom activity event
  slug: ortto-track-custom-activity
slug: ortto
tags:
- Marketing Automation
- CDP
- Customer Data Platform
- Analytics
- Email
- SMS
- Transactional Email
- Webhook
- MCP
- Push Notifications
website: https://ortto.com/
---
