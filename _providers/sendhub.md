---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Sendhub Agentic Access
  operation_count: 28
  slug: sendhub-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.sendhub.com
  baseurl_source: declared
  description: Log in via Username & Password and "Sign In As User"
  name: SendHub Authentication API
  slug: sendhub-authentication-api
- baseURL: https://api.sendhub.com
  baseurl_source: declared
  description: Create and manage contacts.
  name: SendHub Contact API
  slug: sendhub-contact-api
- baseURL: https://api.sendhub.com
  baseurl_source: declared
  description: Create and manage groups.
  name: SendHub Group API
  slug: sendhub-group-api
- baseURL: https://api.sendhub.com
  baseurl_source: declared
  description: Send and manage messages.
  name: SendHub Message API
  slug: sendhub-message-api
- baseURL: https://api.sendhub.com
  baseurl_source: declared
  description: View and manage your account and lines
  name: SendHub Profile API
  slug: sendhub-profile-api
- baseURL: https://api.sendhub.com
  baseurl_source: declared
  description: View and manage inbox threads.
  name: SendHub Thread API
  slug: sendhub-thread-api
artifact_total: 23
asyncapis:
- description: ''
  name: Sendhub Webhooks
  slug: sendhub-webhooks
collections:
- collection_type: open
  name: SendHub Authentication API
  slug: open-sendhub-authentication-api
- collection_type: open
  name: SendHub Authentication Contact API
  slug: open-sendhub-contact-api
- collection_type: open
  name: SendHub Authentication Group API
  slug: open-sendhub-group-api
- collection_type: open
  name: SendHub Authentication Message API
  slug: open-sendhub-message-api
- collection_type: open
  name: SendHub Authentication Profile API
  slug: open-sendhub-profile-api
- collection_type: open
  name: SendHub Authentication Thread API
  slug: open-sendhub-thread-api
common:
- group: other
  href: https://artifacts.apis.io/sendhub/capabilities/sendhub-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sendhub-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://sendhub.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sendhub.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.sendhub.com/SendHub-API-v1-Documentation.html
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.sendhub.com/SendHub-API-v1-Documentation.html
- group: commercial
  title: ''
  type: Pricing
  url: https://sendhub.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://sendhub.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://support.sendhub.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.sendhub.com/signup/
- group: start
  title: ''
  type: Login
  url: https://app.sendhub.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendhub.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendhub.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendhub
- group: auth
  href: https://artifacts.apis.io/sendhub/authentication/sendhub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendhub-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sendhub/security/sendhub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendhub-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/sendhub/agentic-access/sendhub-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendhub-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/sendhub/packages/sendhub-packages.yml
  title: ''
  type: Packages
  url: packages/sendhub-packages.yml
- group: build
  href: https://artifacts.apis.io/sendhub/packages/sendhub-packages.yml
  title: ''
  type: SDKs
  url: packages/sendhub-packages.yml
- group: agent
  href: https://artifacts.apis.io/sendhub/mcp/sendhub-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sendhub-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sendhub/llms/sendhub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendhub-llms.txt
- group: design
  href: https://artifacts.apis.io/sendhub/errors/sendhub-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendhub-error-codes.yml
- group: design
  href: https://artifacts.apis.io/sendhub/conventions/sendhub-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sendhub-conventions.yml
- group: design
  href: https://artifacts.apis.io/sendhub/data-model/sendhub-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sendhub-data-model.yml
- group: design
  href: https://artifacts.apis.io/sendhub/lifecycle/sendhub-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sendhub-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sendhub/conformance/sendhub-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendhub-conformance.yml
- group: other
  href: https://artifacts.apis.io/sendhub/overlays/sendhub-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendhub-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/sendhub/asyncapi/sendhub-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sendhub-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/sendhub/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/sendhub/plans/sendhub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendhub-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sendhub/rate-limits/sendhub-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sendhub-rate-limits.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sendhub.com/developer/
created: '2026-07-17'
description: SendHub is a business text messaging platform for SMS/MMS marketing campaigns, two-way texting, appointment reminders, bulk messaging, SMS surveys, group messaging, and VoIP calling, used by more than 10,000 businesses. It exposes a REST-like v1 API at api.sendhub.com for programmatically managing contacts, groups, messages, inbox threads, account settings, and enterprise users, authenticated with a line username and API key (query params) or HTTP Basic. Published plans run Lite $19/mo to Basic $100/mo plus a quoted Custom tier, and every tier lists API access, though the developer page still says API access is custom-plan only. SendHub also supports 100+ integrations via direct connectors and Zapier plus inbound-SMS webhooks, and is a New Era Technology company. Surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline.
finops:
- has_sources: true
  method: derived
  name: Sendhub Finops
  primary_unit: subscription
  service_category: ''
  slug: sendhub-finops
  template: false
image: https://www.sendhub.com/wp-content/uploads/2019/01/faviconsendhub-150x150.png
layout: provider
modified: '2026-08-13'
name: SendHub
nav: Providers
network: true
overview: 'SendHub publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Contact API, Group API, and 3 more. Tagged areas include Company, SMS, Messaging, Text Messaging, and Communications.


  The SendHub catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SendHub''s developer surface includes documentation, API reference, pricing, engineering blog, support, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Sendhub Plans Pricing
  plan_count: 9
  slug: sendhub-plans-pricing
- name: Sendhub Price Estimates
  plan_count: 0
  slug: sendhub-price-estimates
random_paper: 1
rate_limits:
- limit_count: 0
  name: Sendhub Rate Limits
  slug: sendhub-rate-limits
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 57.6
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 26.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sendhub/sendhub-2026-08-17T081802.png
security:
- kind: authentication
  name: Sendhub Authentication
  slug: sendhub-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Sendhub Domain Security
  slug: sendhub-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Manage contacts and groups
  slug: sendhub-manage-contacts-groups
- name: Read the two-way texting inbox
  slug: sendhub-read-inbox
- name: Send an SMS to contacts or groups
  slug: sendhub-send-message
slug: sendhub
tags:
- Company
- SMS
- Messaging
- Text Messaging
- Communications
- Marketing
- Webhook
- VoIP
website: https://sendhub.com
---
