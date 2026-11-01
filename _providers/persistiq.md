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
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Persistiq Agentic Access
  operation_count: 44
  slug: persistiq-agentic-access
  summary_line: 44 operations · 19 acting
api_count: 2
apis:
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: Outreach campaigns
  name: PersistIQ Campaigns API
  slug: persistiq-campaigns-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: Suppressed domains
  name: PersistIQ Do Not Contact Domains API
  slug: persistiq-do-not-contact-domains-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: Activity events
  name: PersistIQ Events API
  slug: persistiq-events-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: Lead field definitions
  name: PersistIQ Lead Fields API
  slug: persistiq-lead-fields-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: Lead status definitions
  name: PersistIQ Lead Statuses API
  slug: persistiq-lead-statuses-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: Leads (prospects)
  name: PersistIQ Leads API
  slug: persistiq-leads-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: Company users
  name: PersistIQ Users API
  slug: persistiq-users-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: The Campaign Leads API from PersistIQ — 2 operation(s) for campaign leads.
  name: PersistIQ Campaign Leads API
  slug: persistiq-campaign-leads-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: The DNC Domains API from PersistIQ — 1 operation(s) for dnc domains.
  name: PersistIQ DNC Domains API
  slug: persistiq-dnc-domains-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: The Replies API from PersistIQ — 1 operation(s) for replies.
  name: PersistIQ Replies API
  slug: persistiq-replies-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: The Tags API from PersistIQ — 1 operation(s) for tags.
  name: PersistIQ Tags API
  slug: persistiq-tags-api
- baseURL: https://api.persistiq.com
  baseurl_source: declared
  description: The Webhook Plugin API from PersistIQ — 1 operation(s) for webhook plugin.
  name: PersistIQ Webhook Plugin API
  slug: persistiq-webhook-plugin-api
artifact_total: 30
asyncapis:
- description: ''
  name: Persistiq Webhooks
  slug: persistiq-webhooks
collections:
- collection_type: open
  name: PersistIQ Campaigns API
  slug: open-persistiq-campaigns-api
- collection_type: open
  name: PersistIQ Campaigns Do Not Contact Domains API
  slug: open-persistiq-do-not-contact-domains-api
- collection_type: open
  name: PersistIQ Campaigns Events API
  slug: open-persistiq-events-api
- collection_type: open
  name: PersistIQ Campaigns Lead Fields API
  slug: open-persistiq-lead-fields-api
- collection_type: open
  name: PersistIQ Campaigns Lead Statuses API
  slug: open-persistiq-lead-statuses-api
- collection_type: open
  name: PersistIQ Campaigns Leads API
  slug: open-persistiq-leads-api
- collection_type: open
  name: PersistIQ Campaigns Users API
  slug: open-persistiq-users-api
common:
- group: other
  href: https://artifacts.apis.io/persistiq/capabilities/persistiq-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/persistiq-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/persistiq/skills/persistiq-handle-campaign-replies.md
  title: ''
  type: AgentSkill
  url: skills/persistiq-handle-campaign-replies.md
- group: docs
  href: https://artifacts.apis.io/persistiq/openapi/_original/persistiq-api-v1-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/persistiq-api-v1-openapi.json
- group: other
  href: https://artifacts.apis.io/persistiq/overlays/persistiq-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/persistiq-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/persistiq/overlays/persistiq-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/persistiq-api-v1-overlay.yaml
- group: design
  href: https://artifacts.apis.io/persistiq/asyncapi/persistiq-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/persistiq-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/persistiq/plans/persistiq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/persistiq-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/persistiq/changelog/persistiq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/persistiq-changelog.yml
- group: agent
  href: https://artifacts.apis.io/persistiq/agentic-access/persistiq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/persistiq-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PersistIQ
- group: auth
  href: https://artifacts.apis.io/persistiq/security/persistiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/persistiq-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/persistiq/authentication/persistiq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/persistiq-authentication.yml
- group: design
  href: https://artifacts.apis.io/persistiq/conventions/persistiq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/persistiq-conventions.yml
- group: design
  href: https://artifacts.apis.io/persistiq/errors/persistiq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/persistiq-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/persistiq/rate-limits/persistiq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/persistiq-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/persistiq/lifecycle/persistiq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/persistiq-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/persistiq/conformance/persistiq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/persistiq-conformance.yml
- group: design
  href: https://artifacts.apis.io/persistiq/data-model/persistiq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/persistiq-data-model.yml
- group: agent
  href: https://artifacts.apis.io/persistiq/mcp/persistiq-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/persistiq-mcp.yml
- group: build
  href: https://artifacts.apis.io/persistiq/packages/persistiq-packages.yml
  title: ''
  type: Packages
  url: packages/persistiq-packages.yml
- group: agent
  href: https://artifacts.apis.io/persistiq/llms/persistiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/persistiq-llms.txt
- group: agent
  href: https://artifacts.apis.io/persistiq/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.persistiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.persistiq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.persistiq.com/
- group: start
  title: ''
  type: GettingStarted
  url: http://help.persistiq.com/en/articles/466972-getting-started-guide
- group: operate
  title: ''
  type: Support
  url: http://help.persistiq.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.persistiq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.persistiq.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://persistiq.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://persistiq.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.persistiq.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.persistiq.com/privacy/
- group: company
  title: ''
  type: Website
  url: https://persistiq.com
created: '2026-07-17'
description: PersistIQ is a sales engagement platform for small teams to find new customers, start conversations, and personalize sales outreach at scale from one place. It combines prospect research (Chrome extension), multi-channel outreach (email, calls, tasks), campaign management with A/B testing, performance analytics, and CRM integrations. PersistIQ exposes a REST API (v1) for users, leads (prospects), lead statuses and fields, tags, campaigns (including duplication and inbox replies), activity events, Do Not Contact domains, and a webhook plugin carrying five events. It is specified by PersistIQ's own OpenAPI 3.0.1 document, served from the API host at /api-docs/v1/swagger.json. Authentication is a single company-wide API key sent in the x-api-key header, with page-number pagination and a documented 100 request/minute per-key rate limit.
finops:
- has_sources: true
  method: derived
  name: Persistiq Finops
  primary_unit: ''
  service_category: ''
  slug: persistiq-finops
  template: true
image: https://persistiq.com/favicon.ico
layout: provider
modified: '2026-09-16'
name: PersistIQ
nav: Providers
network: true
overview: 'PersistIQ publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Campaigns API, Do Not Contact Domains API, Events API, and 9 more. Tagged areas include Company, Sales Engagement, Sales, Outbound, and Email Outreach.


  The PersistIQ catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PersistIQ''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
plans:
- name: Persistiq Plans Pricing
  plan_count: 0
  slug: persistiq-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Persistiq Rate Limits
  slug: persistiq-rate-limits
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 54.2
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 50.0
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/persistiq/persistiq-2026-08-17T081210.png
security:
- kind: authentication
  name: Persistiq Authentication
  slug: persistiq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Persistiq Domain Security
  slug: persistiq-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 4
skills:
- name: Handle campaign replies and wire up webhooks
  slug: persistiq-handle-campaign-replies
- name: Import leads and enroll them in a campaign
  slug: persistiq-import-and-enroll-leads
- name: Manage Do Not Contact suppression
  slug: persistiq-manage-suppression
- name: Sync lead activity and update statuses
  slug: persistiq-sync-lead-activity
slug: persistiq
tags:
- Company
- Sales Engagement
- Sales
- Outbound
- Email Outreach
- CRM
- Lead Management
- Marketing
- Webhook
- SEP
website: https://persistiq.com
---
