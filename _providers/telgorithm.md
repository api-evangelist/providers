---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Telgorithm Webhooks
  slug: telgorithm-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/telgorithm/rate-limits/telgorithm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/telgorithm-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/telgorithm/asyncapi/telgorithm-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/telgorithm-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/telgorithm/llms/telgorithm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/telgorithm-llms.txt
- group: other
  href: https://artifacts.apis.io/telgorithm/hosts/telgorithm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telgorithm-hosts.yml
- group: other
  href: https://artifacts.apis.io/telgorithm/vendors/telgorithm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/telgorithm-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.telgorithm.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telgorithm.com/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telgorithm.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.telgorithm.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telgorithm.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.telgorithm.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.telgorithm.com\\\
- group: docs
  title: ''
  type: APIReference
  url: https://api.telgorithm.com/docs/voice
- group: auth
  href: https://artifacts.apis.io/telgorithm/security/telgorithm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telgorithm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://telgorithm.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.telgorithm.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telgorithm.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.telgorithm.com/news
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.telgorithm.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.telgorithm.com/getting-started
coverage:
  checked: '2026-10-22'
  detail: Documentation pages are JavaScript-rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://api.telgorithm.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Telgorithm provides A2P 10DLC, RCS, SMS, MMS, Voice and smart queueing APIs for software platforms. Their patented Smart Queueing automates 10DLC campaign registration, offers 24‑hour approval, and no charge for inbound messages. Pricing starts at $0.005 per message. The platform supports high‑volume messaging, compliance, and detailed analytics for developers.
image: https://cdn.prod.website-files.com/66f41b46fd3a43f7076b0891/66f58e6c347824dcccf92a58_telgorithm-webflow.webflow.io_.avif
layout: provider
modified: '2026-10-21'
name: Telgorithm
nav: Providers
network: true
overview: 'Telgorithm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, A2P, SMS, and Voice.


  The Telgorithm catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Telgorithm''s developer surface includes signup flow, API reference, documentation, pricing, engineering blog, getting-started guide, and 14 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 4
  name: Telgorithm Rate Limits
  slug: telgorithm-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 22.6
    discoverability: 56.3
    operational_transparency: 47.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 10.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/telgorithm/telgorithm-2026-11-03T144429.png
security:
- kind: domain-security
  name: Telgorithm Domain Security
  slug: telgorithm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telgorithm
tags:
- Company
- Messaging
- A2P
- SMS
- Voice
website: https://telgorithm.com
---
