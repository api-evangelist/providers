---
access_model:
  confidence: medium
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: start
  title: ''
  type: Login
  url: https://app.autoady.io/sign-in
- group: commercial
  href: https://artifacts.apis.io/autoady-io/plans/autoady-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autoady-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/autoady-io/vocabulary/autoady-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autoady-io-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/autoady-io/cli/autoady-io-cli.yml
  title: ''
  type: CLI
  url: cli/autoady-io-cli.yml
- group: auth
  href: https://artifacts.apis.io/autoady-io/authentication/autoady-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autoady-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/autoady-io/conformance/autoady-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autoady-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autoady-io/llms/autoady-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoady-io-llms.txt
- group: other
  href: https://artifacts.apis.io/autoady-io/a2a/autoady-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/autoady-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/autoady-io/well-known/autoady-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoady-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/autoady-io/hosts/autoady-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoady-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoady-io/vendors/autoady-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoady-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autoady.io/terms
- group: operate
  title: ''
  type: Support
  url: https://help.autoady.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autoady.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.autoady.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.autoady.io/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.autoady.io/developers/overview
- group: company
  title: ''
  type: Blog
  url: https://www.autoady.io/blog
- group: docs
  title: ''
  type: APIReference
  url: https://help.autoady.io/developers/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.autoady.io/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://help.autoady.io/
- group: auth
  href: https://artifacts.apis.io/autoady-io/security/autoady-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoady-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoady.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://help.autoady.io/mcp
  - status: 403
    url: https://api.autoady.io/mcp
  - status: 403
    url: https://autoady.io/mcp
  - status: 403
    url: https://app.autoady.io/mcp
  - status: 403
    url: https://status.autoady.io/mcp
  - status: 200
    url: https://autoady.io/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: AutoAdy provides an AI‑powered media‑buying workspace that unifies Meta and Google Ads intelligence, creative generation, website analytics and reporting. It helps marketers reduce guesswork, increase revenue, and automate ad creative workflows across platforms.
image: https://www.autoady.io/opengraph-image?0901906fc03570ed
layout: provider
modified: '2026-11-02'
name: AutoAdy
nav: Providers
network: true
overview: 'AutoAdy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Media Buying, and Marketing.


  AutoAdy''s developer surface includes CLI, authentication, support, pricing, engineering blog, API reference, getting-started guide, and 16 more developer resources.'
plans:
- name: Autoady Io Plans Pricing
  plan_count: 6
  slug: autoady-io-plans-pricing
random_paper: 12
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.3
    catalog_earned_first_party: 12.0
    catalog_gap: 74.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 60.5
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 41.7
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 34.5
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Autoady Io Authentication
  slug: autoady-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Autoady Io Domain Security
  slug: autoady-io-domain-security
  summary_line: TLSv1.3
slug: autoady-io
tags:
- Company
- Artificial Intelligence
- Advertising
- Media Buying
- Marketing
website: https://autoady.io/
---
