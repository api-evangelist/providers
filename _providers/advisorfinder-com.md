---
access_model:
  confidence: medium
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/advisorfinder-com/plans/advisorfinder-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/advisorfinder-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/advisorfinder-com/changelog/advisorfinder-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/advisorfinder-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/advisorfinder-com/llms/advisorfinder-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/advisorfinder-com-llms.txt
- group: other
  href: https://artifacts.apis.io/advisorfinder-com/hosts/advisorfinder-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/advisorfinder-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/advisorfinder-com/vendors/advisorfinder-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/advisorfinder-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://advisorfinder.com/app/signin
- group: other
  title: ''
  type: Leadership
  url: https://advisorfinder.com/team/jason-friedman
- group: operate
  title: ''
  type: ChangeLog
  url: https://advisorfinder.com/release-notes
- group: auth
  href: https://artifacts.apis.io/advisorfinder-com/security/advisorfinder-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/advisorfinder-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advisorfinder.com/
- group: company
  title: ''
  type: Blog
  url: https://advisorfinder.com/resources-for-clients/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://advisorfinder.com/for-financial-advisors/pricing-plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advisorfinder.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advisorfinder.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://advisorfinder.com/help-support
- group: start
  title: ''
  type: GettingStarted
  url: https://advisorfinder.com/app/assessment
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found after probing standard locations on advisorfinder.com and api.advisorfinder.com.
  evidence:
  - status: 404
    url: https://advisorfinder.com/openapi.json
  - status: 404
    url: https://advisorfinder.com/openapi.yaml
  - status: 0
    url: https://api.advisorfinder.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AdvisorFinder is a free platform that helps individuals, families, and business owners find and connect with qualified financial advisors. Founded in June 2022 and publicly launched in January 2023, the service offers a marketplace and a free assessment to match users with advisors. Profiles include license and registration information from SEC and FINRA, with links to BrokerCheck and IAPD. The mission is to make financial advice accessible with no hidden fees or premium tiers.
image: https://cdn.prod.website-files.com/627ea2baa1713902cd0ee593/6517de18d6409bc054878909_og-june%202023.webp
layout: provider
modified: '2026-10-31'
name: AdvisorFinder
nav: Providers
network: true
overview: 'AdvisorFinder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Advisor, Fintech, Marketplace, and Free.


  AdvisorFinder''s developer surface includes changelog, engineering blog, pricing, support, getting-started guide, and 11 more developer resources.'
plans:
- name: Advisorfinder Com Plans Pricing
  plan_count: 3
  slug: advisorfinder-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Advisorfinder Com Rate Limits
  slug: advisorfinder-com-rate-limits
scopes:
- name: Advisorfinder Com Scopes
  scope_count: 0
  slug: advisorfinder-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 49.1
    operational_transparency: 7.9
  previous_composite: 27.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Advisorfinder Com Authentication
  slug: advisorfinder-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Advisorfinder Com Domain Security
  slug: advisorfinder-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advisorfinder-com
tags:
- Finance
- Advisor
- Fintech
- Marketplace
- Free
website: https://advisorfinder.com/
---
