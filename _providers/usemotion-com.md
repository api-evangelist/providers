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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Get information on the owner of this API key.
  name: Motion API
  slug: motion-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/usemotion-com/well-known/usemotion-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/usemotion-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/usemotion-com/well-known/usemotion-com-google-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/usemotion-com-google-security.txt
- group: operate
  href: https://artifacts.apis.io/usemotion-com/rate-limits/usemotion-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/usemotion-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/usemotion-com/plans/usemotion-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usemotion-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usemotion.com/security
- group: auth
  href: https://artifacts.apis.io/usemotion-com/authentication/usemotion-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usemotion-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usemotion.com/
- group: design
  href: https://artifacts.apis.io/usemotion-com/lifecycle/usemotion-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usemotion-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/usemotion-com/llms/usemotion-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usemotion-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/usemotion-com/well-known/usemotion-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usemotion-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/usemotion-com/hosts/usemotion-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usemotion-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/usemotion-com/vendors/usemotion-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usemotion-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.usemotion.com/
- group: auth
  title: ''
  type: Security
  url: https://www.usemotion.com/security
- group: auth
  href: https://artifacts.apis.io/usemotion-com/security/usemotion-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/usemotion-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/usemotion-com/security/usemotion-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/usemotion-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/usemotion-com/security/usemotion-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usemotion-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usemotion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usemotion.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usemotion.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usemotion.com/cookbooks/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.usemotion.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usemotion.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usemotion.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usemotion.com/legal/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Docs provide endpoint details but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.usemotion.com/api-reference/users/me/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'Motion is the #1 Rated Productivity Platform for the AI Era, offering AI Projects, Tasks, Calendar, Meetings, Docs, Notes, Reports, and Workflows. It unifies project management, scheduling, and collaboration in an AI‑powered super‑app, integrating with services like Zapier, Zoom, Google Meet, and Slack. Users can start a free trial and cancel anytime, experiencing a modernized, automated workflow platform.'
image: https://www-cdn.usemotion.com/default-og-image-1764610536.png
layout: provider
modified: '2026-10-28'
name: Motion
nav: Providers
network: true
overview: 'Motion is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Artificial Intelligence, Project Management, Automation, and Collaboration.


  Motion''s developer surface includes authentication, support, documentation, API reference, getting-started guide, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Usemotion Com Plans Pricing
  plan_count: 4
  slug: usemotion-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Usemotion Com Rate Limits
  slug: usemotion-com-rate-limits
scopes:
- name: Usemotion Com Scopes
  scope_count: 0
  slug: usemotion-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/usemotion-com/usemotion-com-2026-11-03T145532.png
security:
- kind: authentication
  name: Usemotion Com Authentication
  slug: usemotion-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Usemotion Com Domain Security
  slug: usemotion-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Usemotion Com Vulnerability Disclosure
  slug: usemotion-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Usemotion Com Trust Center
  slug: usemotion-com-trust-center
  summary_line: SOC 2, HIPAA, GDPR, CSA STAR
slug: usemotion-com
tags:
- Productivity
- Artificial Intelligence
- Project Management
- Automation
- Collaboration
website: https://www.usemotion.com/
---
