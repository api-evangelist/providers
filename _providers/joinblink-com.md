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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 4
  name: Joinblink Com Agentic Access
  operation_count: 51
  slug: joinblink-com-agentic-access
  summary_line: 51 operations · 30 acting · 4 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.joinblink.com/api/platform
  baseurl_source: declared
  description: Grant and revoke access to a chat. Access is permission to be in a chat, distinct from membership of it.
  name: Blink Access API
  slug: joinblink-com-access-api
- baseURL: https://api.joinblink.com/api/platform
  baseurl_source: declared
  description: Create, read, update and delete chats.
  name: Blink Chats API
  slug: joinblink-com-chats-api
- baseURL: https://api.joinblink.com/v2
  baseurl_source: declared
  description: The Feed API from Blink — 6 operation(s) for feed.
  name: Blink Feed API
  slug: joinblink-com-feed-api
- baseURL: https://api.joinblink.com/v2
  baseurl_source: declared
  description: The Forms API from Blink — 2 operation(s) for forms.
  name: Blink Forms API
  slug: joinblink-com-forms-api
- baseURL: https://api.joinblink.com/scim
  baseurl_source: declared
  description: The Group API from Blink — 2 operation(s) for group.
  name: Blink Group API
  slug: joinblink-com-group-api
- baseURL: https://api.joinblink.com/v2
  baseurl_source: declared
  description: The Linked Account API from Blink — 1 operation(s) for linked account.
  name: Blink Linked Account API
  slug: joinblink-com-linked-account-api
- baseURL: https://api.joinblink.com/v2
  baseurl_source: declared
  description: The Linked Accounts API from Blink — 1 operation(s) for linked accounts.
  name: Blink Linked Accounts API
  slug: joinblink-com-linked-accounts-api
- baseURL: https://api.joinblink.com/api/platform
  baseurl_source: declared
  description: Manage the users and apps that are in a chat — joining, leaving, removing and roles.
  name: Blink Members API
  slug: joinblink-com-members-api
- baseURL: https://api.joinblink.com/api/platform
  baseurl_source: declared
  description: Send, read, edit and delete messages within a chat.
  name: Blink Messages API
  slug: joinblink-com-messages-api
- baseURL: https://api.joinblink.com/v2
  baseurl_source: declared
  description: The User API from Blink — 6 operation(s) for user.
  name: Blink User API
  slug: joinblink-com-user-api
- baseURL: https://api.joinblink.com/scim
  baseurl_source: declared
  description: The Service Provider Config API from Blink — 1 operation(s) for service provider config.
  name: Blink Service Provider Config API
  slug: joinblink-com-service-provider-config-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/joinblink-com/agentic-access/joinblink-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/joinblink-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/joinblink-com/rate-limits/joinblink-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/joinblink-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/joinblink-com/plans/joinblink-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/joinblink-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/joinblink-com/rules/joinblink-com-rules.yml
  title: ''
  type: Spectral
  url: rules/joinblink-com-rules.yml
- group: design
  href: https://artifacts.apis.io/joinblink-com/json-ld/joinblink-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/joinblink-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/joinblink-com/vocabulary/joinblink-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/joinblink-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/joinblink-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/joinblink-com/data-model/joinblink-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/joinblink-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/joinblink-com/authentication/joinblink-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/joinblink-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/joinblink-com/errors/joinblink-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/joinblink-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/joinblink-com/conformance/joinblink-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/joinblink-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/joinblink-com/llms/joinblink-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/joinblink-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/joinblink-com/well-known/joinblink-com-helpdesk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/joinblink-com-helpdesk-security.txt
- group: auth
  href: https://artifacts.apis.io/joinblink-com/well-known/joinblink-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/joinblink-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/joinblink-com/well-known/joinblink-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/joinblink-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/joinblink-com/hosts/joinblink-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinblink-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinblink-com/vendors/joinblink-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinblink-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinblink.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.joinblink.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinblink.com/
- group: auth
  title: ''
  type: Security
  url: https://www.joinblink.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinblink.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joinblink.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.joinblink.com/press
- group: start
  title: ''
  type: Login
  url: https://app.joinblink.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://developer.joinblink.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.joinblink.com/docs/creating-an-integration
- group: docs
  title: ''
  type: Documentation
  url: https://developer.joinblink.com/
- group: auth
  href: https://artifacts.apis.io/joinblink-com/security/joinblink-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinblink-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joinblink.com/
created: '2026-10-28'
description: 'Blink is an employee communication app for frontline workers — the 200,000+ people in retail, hospitality, healthcare, logistics, and aviation who don''t sit at a desk, don''t have a company email, and aren''t issued a company device. Blink is a digital front door: consumer‑grade, real‑time, two‑way communication that actually reaches your people, plus everything they need to get work done in one tap, from day one to day 1,000. Across 350+ customers implemented since 2019, Blink achieves 87% adoption against an 80% target, 97%+ CSAT, and 99% year‑on‑year retention.'
image: https://cdn.prod.website-files.com/673646818ea715450da97028/67f426b35db49131f6dfa79f_blink-preview%20(1).png
jsonld:
- class_count: 66
  name: Joinblink Com Context
  property_count: 93
  slug: joinblink-com-context
layout: provider
modified: '2026-10-28'
name: Blink
nav: Providers
network: true
overview: 'Blink publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Chats API, Feed API, and 8 more. Tagged areas include Company, Employee Experience, MobileFirst, Frontline Workers, and Communications.


  The Blink catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Blink''s developer surface includes authentication, support, pricing, API reference, getting-started guide, documentation, and 24 more developer resources.'
plans:
- name: Joinblink Com Plans Pricing
  plan_count: 3
  slug: joinblink-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Joinblink Com Rate Limits
  slug: joinblink-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Blink API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: joinblink-com-rules
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 76.8
    catalog_earned_first_party: 20.0
    catalog_gap: 38.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 67.2
    developer_ergonomics: 30.4
    discoverability: 79.5
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/joinblink-com/joinblink-com-2026-11-03T134215.png
security:
- kind: authentication
  name: Joinblink Com Authentication
  slug: joinblink-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Joinblink Com Domain Security
  slug: joinblink-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: joinblink-com-create-and-get-user
  slug: joinblink-com-create-and-get-user
- name: joinblink-com-join-and-list-members
  slug: joinblink-com-join-and-list-members
- name: joinblink-com-manage-access
  slug: joinblink-com-manage-access
- name: joinblink-com-manage-chat
  slug: joinblink-com-manage-chat
- name: joinblink-com-send-and-list-messages
  slug: joinblink-com-send-and-list-messages
slug: joinblink-com
tags:
- Company
- Employee Experience
- MobileFirst
- Frontline Workers
- Communications
website: https://www.joinblink.com/
---
