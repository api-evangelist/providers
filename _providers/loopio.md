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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: An asynchronous endpoint
  name: Loopio Asynchronous API
  slug: loopio-asynchronous-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: The CRM API from Loopio — 2 operation(s) for crm.
  name: Loopio CRM API
  slug: loopio-crm-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Create and manage Custom Project Fields
  name: Loopio Custom Project Fields API
  slug: loopio-custom-project-fields-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Get information about Customer instances
  name: Loopio Customers API
  slug: loopio-customers-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Manage Loopio files
  name: Loopio Files API
  slug: loopio-files-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Create and manage Library Entries
  name: Loopio Library Entries API
  slug: loopio-library-entries-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Reusable Library/Project-wide variables
  name: Loopio Merge Variables API
  slug: loopio-merge-variables-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Get Information about Project Templates
  name: Loopio Project Templates API
  slug: loopio-project-templates-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Create and manage Projects
  name: Loopio Projects API
  slug: loopio-projects-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: The Roles API from Loopio — 2 operation(s) for roles.
  name: Loopio Roles API
  slug: loopio-roles-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: View accessible stacks or Library structure
  name: Loopio Stacks API
  slug: loopio-stacks-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Create and manage Tags
  name: Loopio Tags API
  slug: loopio-tags-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Get Information about Teams
  name: Loopio Teams API
  slug: loopio-teams-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Create and manage Users
  name: Loopio Users API
  slug: loopio-users-api
- baseURL: https://api.loopio.com/data/v2
  baseurl_source: declared
  description: Create & Manage webhook subscriptions
  name: Loopio Webhooks API
  slug: loopio-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Loopio Events Webhooks
  slug: loopio-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loopio-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/loopio-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loopio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://loopio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.loopio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.loopio.com/docs/loopio-api/c56ffe1fdae3e-getting-started-with-the-loopio-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.loopio.com/docs/loopio-api/68a341c676710-loopio
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.loopio.com/docs/loopio-api/c56ffe1fdae3e-getting-started-with-the-loopio-api
- group: operate
  title: ''
  type: Support
  url: https://support.loopio.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://loopio.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://loopio.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loopio.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loopio.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.loopiostatus.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loopio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loopio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/loopio-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loopio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loopio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loopio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loopio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loopio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://loopio.com/legal/compliance-statement/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/loopio-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loopio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loopio-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/loopio-openapi-overlay.yaml
created: '2026-08-25'
description: Loopio is a Toronto-based response management platform used by teams to answer RFPs, RFIs, DDQs, and security questionnaires from a governed, reusable content Library. It publishes a public REST API — the Loopio Public API v2 at https://api.loopio.com/data/v2 — documented on a Stoplight developer portal at developer.loopio.com, with a 96-operation OpenAPI 3.0.1 contract covering Library Entries, Projects, Project Entries, Sections and subSections, Custom Project Fields, Merge Variables, Compliance Sets, Project Templates, Stacks, Tags, Teams, Users, Roles, Files, CRM opportunity links, asynchronous task status, and webhook subscriptions. Authentication is OAuth 2.0 client credentials against https://api.loopio.com/oauth2/access_token with 22 in-spec scopes, and the authorization server publishes RFC 8414 and RFC 9728 discovery documents that advertise a wider 51-scope surface including SCIM user/group provisioning and MCP tool/prompt/resource scopes.
image: https://cdn.loopio.com/cache/8.328.b01/resources/images/favicon.png
layout: provider
modified: '2026-08-25'
name: Loopio
nav: Providers
network: true
overview: 'Loopio publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Asynchronous API, CRM API, Custom Project Fields API, and 12 more. Tagged areas include Company, RFP, Proposals, Response Management, and Content Library.


  The Loopio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loopio''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Loopio Plans Pricing
  plan_count: 0
  slug: loopio-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Loopio Rate Limits
  slug: loopio-rate-limits
scopes:
- name: Loopio Scopes
  scope_count: 52
  slug: loopio-scopes
  summary_line: 52 scopes
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 61.6
    developer_ergonomics: 18.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 34.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loopio/refs/heads/main/screenshots/loopio-2026-09-02T150315.png
security:
- kind: authentication
  name: Loopio Authentication
  slug: loopio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Loopio Domain Security
  slug: loopio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loopio
tags:
- Company
- RFP
- Proposals
- Response Management
- Content Library
- Sales Enablement
- Questionnaires
- Compliance
- Collaboration
- Documents
- Webhook
- Software-as-a-Service
website: https://loopio.com/
---
