---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Ortto Agentic Access
  operation_count: 11
  slug: ortto-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Create, update, retrieve, and manage accounts (organizations).
  name: Ortto Accounts API
  slug: ortto-accounts-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Send custom activity events and manage activity definitions.
  name: Ortto Activities API
  slug: ortto-activities-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Retrieve campaigns, reports, and assets.
  name: Ortto Campaigns API
  slug: ortto-campaigns-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Create, update, retrieve, and manage people (contacts).
  name: Ortto People API
  slug: ortto-people-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Retrieve account tags.
  name: Ortto Tags API
  slug: ortto-tags-api
- baseURL: https://api.ap3api.com/v1
  baseurl_source: declared
  description: Send transactional email and SMS.
  name: Ortto Transactional API
  slug: ortto-transactional-api
artifact_total: 24
asyncapis:
- description: ''
  name: Ortto Webhooks
  slug: ortto-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: CapabilityMap
  url: capabilities/ortto-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ortto-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ortto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ortto-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/ortto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ortto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ortto-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ortto.com/blog
- group: build
  title: ''
  type: Packages
  url: packages/ortto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ortto-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ortto-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ortto-security.txt
- group: auth
  title: ''
  type: Security
  url: security/ortto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ortto-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/ortto-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ortto-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ortto-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ortto-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ortto-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ortto-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ortto-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ortto-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ortto-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ortto-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ortto-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
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
  title: ''
  type: PostmanCollection
  url: collections/ortto.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/ortto.opencollection.json
created: '2026-06-25'
description: Ortto (formerly Autopilot) is a marketing automation, customer data platform (CDP), and analytics product. Its REST API at https://api.ap3api.com/v1 lets applications create and update people/contacts and accounts, send custom activity events, manage tags, retrieve campaign reports, and send transactional email and SMS, all authenticated with a custom API key via the X-Api-Key header, with EU and AU service endpoints for accounts in those data-residency regions. Ortto also runs a first-party hosted MCP server, released in version 1.27 (December 2025), giving agents a read-heavy surface over campaigns, contacts, audiences, reports, schema and knowledge-base content. Ortto publishes no machine-readable OpenAPI; the specifications here are scaffolded from its help-center API reference. Ortto announced in April 2026 that it is joining Canva.
finops:
- name: Ortto Finops
  service_category: Marketing and Customer Engagement
  slug: ortto-finops
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
overview: 'Ortto publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Campaigns API, and 3 more. Tagged areas include Marketing Automation, CDP, Customer Data Platform, Analytics, and Email.


  The Ortto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ortto''s developer surface includes authentication, documentation, engineering blog, changelog, getting-started guide, support, signup flow, and 37 more developer resources.'
plans:
- name: Ortto Plans Pricing
  plan_count: 5
  slug: ortto-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 14
  name: Ortto Rate Limits
  slug: ortto-rate-limits
score:
  band: exemplar
  composite: 71.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 61.4
    developer_ergonomics: 67.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 89.5
  previous_composite: 71.2
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
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ortto/refs/heads/main/screenshots/ortto-2026-08-07T190955.png
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
