---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/enfusion/llms/enfusion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/enfusion-llms.txt
- group: other
  href: https://artifacts.apis.io/enfusion/hosts/enfusion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enfusion-hosts.yml
- group: other
  href: https://artifacts.apis.io/enfusion/vendors/enfusion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enfusion-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cwan.com/company/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://cwan.com/company/leadership/
- group: auth
  href: https://artifacts.apis.io/enfusion/security/enfusion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enfusion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enfusion.com/
- group: company
  title: ''
  type: Blog
  url: https://cwan.com/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://cwan.com/support/enfusion/
- group: operate
  title: ''
  type: HelpCenter
  url: https://zendesk.enfusionsystems.com/hc/
- group: start
  title: ''
  type: Login
  url: https://webapp.enfusionsystems.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cwan.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cwan.com/enfusion-platform-terms-and-conditions/
coverage:
  checked: '2026-10-20'
  detail: Enfusion (now a Clearwater Analytics product at cwan.com) publishes no developer portal or spec; its knowledge base at zendesk.enfusionsystems.com returns 403, its MCP endpoint 401, and the platform sits behind the webapp.enfusionsystems.com client login.
  evidence:
  - status: 403
    url: https://zendesk.enfusionsystems.com/hc/
  - status: 401
    url: https://zendesk.enfusionsystems.com/mcp
  - status: 200
    url: https://cwan.com/products/enfusion/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Enfusion is a cloud-native, front-to-back investment management platform for hedge funds and asset managers, unifying portfolio management (PMS), order and execution management (OEMS), pre- and post-trade compliance, a unified IBOR/ABOR accounting book of record, and analytics on a single SaaS database. It serves over 1,000 clients across 30 countries, offers direct connectivity to 300+ liquidity sources via FIX, and maintains a 4M+ instrument security master. Enfusion was acquired by Clearwater Analytics (CWAN) in 2025; the enfusion.com domain now redirects to cwan.com, where Enfusion is offered as a product line. There is no public developer portal or open API specification: the platform API and knowledge base are gated behind the client web application and Zendesk help center. This profile was surfaced as an ICONIQ Capital portfolio lead and enriched from public marketing, support, and legal surfaces.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enfusion.png
layout: provider
modified: '2026-07-19'
name: Enfusion
nav: Providers
network: true
overview: 'Enfusion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investment Management, Hedge Funds, and Asset Management.


  Enfusion''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/enfusion/enfusion-2026-07-25T213344.png
security:
- kind: domain-security
  name: Enfusion Domain Security
  slug: enfusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enfusion
tags:
- Company
- Fintech
- Investment Management
- Hedge Funds
- Asset Management
- Portfolio Management
- OMS
- Trading
- Compliance
- Software-as-a-Service
website: https://www.enfusion.com/
---
