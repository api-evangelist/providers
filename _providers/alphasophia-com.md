---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agent_card: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API provides access to healthcare commercial intelligence data as described on the pricing page.
  name: Alpha Sophia API
  slug: alpha-sophia-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/alphasophia-com/plans/alphasophia-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alphasophia-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/alphasophia-com/authentication/alphasophia-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alphasophia-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/alphasophia-com/llms/alphasophia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphasophia-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alphasophia-com/well-known/alphasophia-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphasophia-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alphasophia-com/hosts/alphasophia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphasophia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphasophia-com/vendors/alphasophia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphasophia-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alphasophia.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alphasophia.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alphasophia.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.alphasophia.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alphasophia
- group: auth
  href: https://artifacts.apis.io/alphasophia-com/security/alphasophia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphasophia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphasophia.com/
coverage:
  checked: '2026-11-01'
  detail: Pricing page loads content via JavaScript, no machine‑readable spec is available.
  evidence:
  - status: 200
    url: https://www.alphasophia.com/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Alpha Sophia provides a comprehensive healthcare commercial intelligence platform, offering detailed data on providers, organizations, and market insights across pharma, biotech, medtech, and related sectors. Their API enables searchable access to extensive provider profiles, procedure volumes, licensing information, and more, supporting sales, marketing, research, and investment decision-making.
image: https://www.alphasophia.com/opengraph.jpg
layout: provider
modified: '2026-11-01'
name: Alpha Sophia
nav: Providers
network: true
overview: 'Alpha Sophia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Data, Commercial Intelligence, and Platform.


  Alpha Sophia''s developer surface includes authentication, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Alphasophia Com Plans Pricing
  plan_count: 2
  slug: alphasophia-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 20.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alphasophia Com Authentication
  slug: alphasophia-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alphasophia Com Domain Security
  slug: alphasophia-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alphasophia-com
tags:
- Healthcare
- Data
- Commercial Intelligence
- Platform
website: https://alphasophia.com/
---
