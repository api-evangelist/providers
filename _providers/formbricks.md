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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Formbricks Agentic Access
  operation_count: 26
  slug: formbricks-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 1
apis:
- baseURL: https://app.formbricks.com/api
  baseurl_source: declared
  description: Define code and no-code actions that trigger in-product surveys.
  name: Formbricks Action Classes API
  slug: formbricks-action-classes-api
- baseURL: https://app.formbricks.com/api
  baseurl_source: declared
  description: Public unauthenticated Client API used by survey front-ends.
  name: Formbricks Client API
  slug: formbricks-client-api
- baseURL: https://app.formbricks.com/api
  baseurl_source: declared
  description: Manage contacts and contact attribute keys.
  name: Formbricks Contacts API
  slug: formbricks-contacts-api
- baseURL: https://app.formbricks.com/api
  baseurl_source: declared
  description: Account and environment information for an API key.
  name: Formbricks Me API
  slug: formbricks-me-api
- baseURL: https://app.formbricks.com/api
  baseurl_source: declared
  description: Create, query, and manage survey responses.
  name: Formbricks Responses API
  slug: formbricks-responses-api
- baseURL: https://app.formbricks.com/api
  baseurl_source: declared
  description: Create and manage surveys.
  name: Formbricks Surveys API
  slug: formbricks-surveys-api
- baseURL: https://app.formbricks.com/api
  baseurl_source: declared
  description: Real-time HTTP notifications for response events.
  name: Formbricks Webhooks API
  slug: formbricks-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Formbricks Action Classes API
  slug: open-formbricks-action-classes-api
- collection_type: open
  name: Formbricks Action Classes Client API
  slug: open-formbricks-client-api
- collection_type: open
  name: Formbricks Action Classes Contacts API
  slug: open-formbricks-contacts-api
- collection_type: open
  name: Formbricks Action Classes Me API
  slug: open-formbricks-me-api
- collection_type: open
  name: Formbricks Action Classes Responses API
  slug: open-formbricks-responses-api
- collection_type: open
  name: Formbricks Action Classes Surveys API
  slug: open-formbricks-surveys-api
- collection_type: open
  name: Formbricks Action Classes Webhooks API
  slug: open-formbricks-webhooks-api
- collection_type: open
  name: Formbricks API
  slug: open-formbricks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formbricks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formbricks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formbricks-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/formbricks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formbricks
- group: company
  title: ''
  type: Website
  url: https://www.formbricks.com
- group: docs
  title: ''
  type: Documentation
  url: https://formbricks.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/formbricks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formbricks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/formbricks-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://formbricks.com/blog
created: '2026-06-20'
description: Formbricks is an open-source experience management and survey platform (a privacy-first Typeform / Qualtrics alternative). Its REST API lets you create and manage surveys, collect and query responses, manage contacts and their attributes, and wire up webhooks, with a Public Client API (no auth) for survey delivery and a Management API authenticated with an x-api-key header.
finops:
- name: Formbricks Finops
  service_category: Analytics and Experience Management
  slug: formbricks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formbricks.png
layout: provider
modified: '2026-06-20'
name: Formbricks
nav: Providers
network: true
overview: 'Formbricks publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Action Classes API, Client API, Contacts API, and 4 more. Tagged areas include Surveys, Experience Management, Feedback, Forms, and Open-Source.


  Formbricks'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Formbricks Plans Pricing
  plan_count: 5
  slug: formbricks-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Formbricks Rate Limits
  slug: formbricks-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formbricks/refs/heads/main/screenshots/formbricks-2026-06-20T181436.png
security:
- kind: authentication
  name: Formbricks Authentication
  slug: formbricks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Formbricks Domain Security
  slug: formbricks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: formbricks
tags:
- Surveys
- Experience Management
- Feedback
- Forms
- Open-Source
website: https://www.formbricks.com
---
