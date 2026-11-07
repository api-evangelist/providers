---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/browsingbee-com/plans/browsingbee-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/browsingbee-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/browsingbee-com/llms/browsingbee-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/browsingbee-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/browsingbee-com/well-known/browsingbee-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/browsingbee-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/browsingbee-com/hosts/browsingbee-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/browsingbee-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/browsingbee-com/vendors/browsingbee-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/browsingbee-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.browsingbee.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.browsingbee.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.browsingbee.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.browsingbee.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.browsingbee.com/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theindianappguy
- group: company
  title: ''
  type: Blog
  url: https://www.browsingbee.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.browsingbee.com/blog/quickstart-your-first-skill
- group: auth
  href: https://artifacts.apis.io/browsingbee-com/security/browsingbee-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/browsingbee-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://browsingbee.com/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable spec was found on the provider's hosts.
  evidence:
  - status: error
    url: https://api.browsingbee.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BrowsingBee provides a remote browser connector that lets Claude and ChatGPT browse the internet, search web pages, read PDFs, and extract data. Users can access any page without installing software, with a free tier of 300 pages per month. The service aims to enhance AI assistants by giving them real-time web access, supporting both Claude and ChatGPT platforms.
image: https://www.browsingbee.com/api/og?title=BrowsingBee%20%E2%80%93%20Let%20Claude%20browse%20the%20internet%20for%20you&description=Open%20any%20page%2C%20search%20the%20web%2C%20read%20PDFs%20and%20pull%20data%20from%20claude.ai%20on%20any%20device.%20A%20remote%20browser%20connector%20for%20Claude%20and%20ChatGPT.%20Nothing%20to%20install%2C%20free%20for%20300%20pages%20a%20month.
layout: provider
modified: '2026-11-03'
name: BrowsingBee
nav: Providers
network: true
overview: 'BrowsingBee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Browser, Connector, Claude, and ChatGPT.


  BrowsingBee''s developer surface includes support, pricing, engineering blog, getting-started guide, and 11 more developer resources.'
plans:
- name: Browsingbee Com Plans Pricing
  plan_count: 2
  slug: browsingbee-com-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 2.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Browsingbee Com Domain Security
  slug: browsingbee-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: browsingbee-com
tags:
- Artificial Intelligence
- Browser
- Connector
- Claude
- ChatGPT
website: https://browsingbee.com/
---
