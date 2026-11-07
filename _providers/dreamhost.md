---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/dreamhost/well-known/dreamhost-dreamhost-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dreamhost-dreamhost-security.txt
- group: commercial
  href: https://artifacts.apis.io/dreamhost/plans/dreamhost-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dreamhost-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dreamhost/llms/dreamhost-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreamhost-llms.txt
- group: auth
  href: https://artifacts.apis.io/dreamhost/well-known/dreamhost-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dreamhost-www-security.txt
- group: auth
  href: https://artifacts.apis.io/dreamhost/well-known/dreamhost-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dreamhost-security.txt
- group: agent
  href: https://artifacts.apis.io/dreamhost/well-known/dreamhost-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dreamhost-well-known.yml
- group: other
  href: https://artifacts.apis.io/dreamhost/hosts/dreamhost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamhost-hosts.yml
- group: other
  href: https://artifacts.apis.io/dreamhost/vendors/dreamhost-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreamhost-vendors.yml
- group: build
  href: https://artifacts.apis.io/dreamhost/packages/dreamhost-packages.yml
  title: ''
  type: SDKs
  url: packages/dreamhost-packages.yml
- group: build
  href: https://artifacts.apis.io/dreamhost/packages/dreamhost-packages.yml
  title: ''
  type: Packages
  url: packages/dreamhost-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dreamhost.com/legal/terms-of-service/
- group: start
  title: ''
  type: SignUp
  url: https://www.dreamhost.com/news/announcements/register-a-online-domain-for-0-99/
- group: auth
  title: ''
  type: Security
  url: https://www.dreamhost.com/features/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamhost.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dreamhost.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.dreamhost.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.dreamhost.com/pro-services/management/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dreamhost.com/get-started/
- group: company
  title: ''
  type: Blog
  url: https://www.dreamhost.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.dreamhost.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dreamhost
- group: auth
  href: https://artifacts.apis.io/dreamhost/security/dreamhost-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dreamhost-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dreamhost/security/dreamhost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamhost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamhost.com/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.dreamhost.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: DreamHost DreamObjects provides cloud hosting services, including web hosting, domain registration, managed WordPress hosting, business email, and cloud storage. It offers a 100% uptime guarantee, 24/7 support, and a range of developer-friendly tools and APIs for managing resources and automating workflows.
image: https://www.dreamhost.com/images/ogImages/dreamhost-og-image.jpg
layout: provider
modified: '2026-10-27'
name: DreamHost DreamObjects
nav: Providers
network: true
overview: 'DreamHost DreamObjects is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hosting, Cloud, and Domains.


  DreamHost DreamObjects'' developer surface includes signup flow, pricing, getting-started guide, engineering blog, documentation, and 19 more developer resources.'
plans:
- name: Dreamhost Plans Pricing
  plan_count: 3
  slug: dreamhost-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dreamhost/dreamhost-2026-11-03T131033.png
security:
- kind: domain-security
  name: Dreamhost Domain Security
  slug: dreamhost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dreamhost Vulnerability Disclosure
  slug: dreamhost-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dreamhost
tags:
- Company
- Hosting
- Cloud
- Domains
website: https://dreamhost.com/
---
