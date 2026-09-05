---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Dotloop Agentic Access
  operation_count: 43
  slug: dotloop-agentic-access
  summary_line: 43 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: The authenticated dotloop account.
  name: dotloop Account API
  slug: dotloop-account-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Read-only loop activity feed.
  name: dotloop Activities API
  slug: dotloop-activities-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: The authenticated user's contacts (address book).
  name: dotloop Contacts API
  slug: dotloop-contacts-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Documents within a loop folder.
  name: dotloop Documents API
  slug: dotloop-documents-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Folders that organize documents within a loop.
  name: dotloop Folders API
  slug: dotloop-folders-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Structured detail fields of a loop.
  name: dotloop Loop Details API
  slug: dotloop-loop-details-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Single-call loop creation facade.
  name: dotloop Loop It API
  slug: dotloop-loop-it-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Reusable transaction blueprints under a profile.
  name: dotloop Loop Templates API
  slug: dotloop-loop-templates-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Loops (real estate transactions).
  name: dotloop Loops API
  slug: dotloop-loops-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Parties to a loop.
  name: dotloop Participants API
  slug: dotloop-participants-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Individual, team, and brokerage profiles that scope loops.
  name: dotloop Profiles API
  slug: dotloop-profiles-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Task lists and task items on a loop.
  name: dotloop Tasks API
  slug: dotloop-tasks-api
- baseURL: https://api-gateway.dotloop.com/public/v2
  baseurl_source: declared
  description: Webhook subscriptions and delivered events.
  name: dotloop Webhooks API
  slug: dotloop-webhooks-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: dotloop Public API v2 Account API
  slug: open-dotloop-account-api
- collection_type: open
  name: dotloop Public API v2 Account Activities API
  slug: open-dotloop-activities-api
- collection_type: open
  name: dotloop Public API v2 Account Contacts API
  slug: open-dotloop-contacts-api
- collection_type: open
  name: dotloop Public API v2 Account Documents API
  slug: open-dotloop-documents-api
- collection_type: open
  name: dotloop Public API v2 Account Folders API
  slug: open-dotloop-folders-api
- collection_type: open
  name: dotloop Public API v2 Account Loop Details API
  slug: open-dotloop-loop-details-api
- collection_type: open
  name: dotloop Public API v2 Account Loop It API
  slug: open-dotloop-loop-it-api
- collection_type: open
  name: dotloop Public API v2 Account Loop Templates API
  slug: open-dotloop-loop-templates-api
- collection_type: open
  name: dotloop Public API v2 Account Loops API
  slug: open-dotloop-loops-api
- collection_type: open
  name: dotloop Public API v2 Account Participants API
  slug: open-dotloop-participants-api
- collection_type: open
  name: dotloop Public API v2 Account Profiles API
  slug: open-dotloop-profiles-api
- collection_type: open
  name: dotloop Public API v2 Account Tasks API
  slug: open-dotloop-tasks-api
- collection_type: open
  name: dotloop Public API v2 Account Webhooks API
  slug: open-dotloop-webhooks-api
- collection_type: open
  name: dotloop Public API v2
  slug: open-dotloop
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dotloop-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dotloop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dotloop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dotloop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dotloop-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotloop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotloop
- group: company
  title: ''
  type: Website
  url: https://www.dotloop.com
- group: docs
  title: ''
  type: Documentation
  url: https://dotloop.github.io/public-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dotloop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dotloop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dotloop-finops.yml
created: '2026-07-04'
description: dotloop is a real estate transaction management platform (owned by Zillow Group) that lets agents, teams, and brokerages create and manage transactions - called "loops" - end to end, including documents, e-signatures, tasks, participants, and compliance workflows. The dotloop Public API v2 is a documented, OAuth2-secured JSON REST API at https://api-gateway.dotloop.com/public/v2 that exposes accounts, profiles, loops and loop details, folders, documents, participants, tasks, activities, contacts, loop templates, and webhook subscriptions, plus a Loop-It facade for one-call loop creation.
finops:
- name: Dotloop Finops
  service_category: Business Applications
  slug: dotloop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotloop.png
layout: provider
modified: '2026-07-04'
name: dotloop
nav: Providers
network: true
overview: 'dotloop publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Activities API, Contacts API, and 10 more. Tagged areas include Real-Estate, Transaction Management, Loops, Documents, and E-Signature.


  dotloop''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Dotloop Plans Pricing
  plan_count: 4
  slug: dotloop-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Dotloop Rate Limits
  slug: dotloop-rate-limits
scopes:
- name: Dotloop Scopes
  scope_count: 8
  slug: dotloop-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dotloop/refs/heads/main/screenshots/dotloop-2026-07-25T212314.png
security:
- kind: authentication
  name: Dotloop Authentication
  slug: dotloop-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Dotloop Domain Security
  slug: dotloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dotloop
tags:
- Real-Estate
- Transaction Management
- Loops
- Documents
- E-Signature
- Zillow Group
website: https://www.dotloop.com
---
