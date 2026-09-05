---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Runtime Authorization (PDP permit/deny, policy resolution, user access token, cache invalidation), Management (policy/asset/application/mapper/identity CRUD, orchestration, SaaS vendors), and Administ
  name: PlainID Authorization Platform API
  slug: plainid-authorization-platform-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.plainid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.plainid.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plainid.io/v1-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.plainid.io/apidocs/authorization-apis.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.plainid.io/docs/getting-started-2.md
- group: company
  title: ''
  type: Blog
  url: https://www.plainid.com/resources/?category=blog
- group: operate
  title: ''
  type: Support
  url: https://plainid.atlassian.net/servicedesk/customer/portals
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plainid.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plainid.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plainid.com/terms-of-use/
- group: auth
  title: ''
  type: Authentication
  url: authentication/plainid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plainid-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plainid-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plainid-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plainid-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/plainid-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plainid-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plainid-llms.txt
created: '2026-07-17'
description: 'PlainID is an enterprise authorization company whose Policy-Based Access Control (PBAC) platform, "The Authorization Platform," controls what identities (human and AI agent) can access, do, and expose across data, APIs, applications, and AI systems. The platform centralizes policy authoring and externalizes runtime access decisions through a Policy Decision Point (PDP), Policy Information Points (PIP), and Policy Authorization Agents. PlainID exposes three public REST API families: Runtime Authorization APIs (permit/deny decisions, policy resolution, user access tokens, PDP cache invalidation), Management APIs (policy, asset-template, application, mapper, and identity-template CRUD plus orchestration and SaaS-vendor management), and Administration APIs (audit events, API client credentials, platform reports). PlainID is backed by Insight Partners.'
image: https://logo.clearbit.com/plainid.com
layout: provider
modified: '2026-07-20'
name: PlainID
nav: Providers
network: true
overview: 'PlainID publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Authorization, Access Control, and PBAC.


  PlainID''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 29.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plainid/refs/heads/main/screenshots/plainid-2026-09-02T151354.png
security:
- kind: authentication
  name: Plainid Authentication
  slug: plainid-authentication
  summary_line: apiKey/oauth2/http · 3 schemes
- kind: domain-security
  name: Plainid Domain Security
  slug: plainid-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: plainid
tags:
- Company
- Cybersecurity
- Authorization
- Access Control
- PBAC
- Identity
- Policy Management
- API Security
website: https://www.plainid.com/
---
