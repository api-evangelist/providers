---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/wealthengine/llms/wealthengine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wealthengine-llms.txt
- group: agent
  href: https://artifacts.apis.io/wealthengine/well-known/wealthengine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wealthengine-well-known.yml
- group: other
  href: https://artifacts.apis.io/wealthengine/hosts/wealthengine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wealthengine-hosts.yml
- group: other
  href: https://artifacts.apis.io/wealthengine/vendors/wealthengine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wealthengine-vendors.yml
- group: build
  href: https://artifacts.apis.io/wealthengine/packages/wealthengine-packages.yml
  title: ''
  type: SDKs
  url: packages/wealthengine-packages.yml
- group: build
  href: https://artifacts.apis.io/wealthengine/packages/wealthengine-packages.yml
  title: ''
  type: Packages
  url: packages/wealthengine-packages.yml
- group: auth
  href: https://artifacts.apis.io/wealthengine/security/wealthengine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wealthengine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wealthengine.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wealthengine.com/developer-api
- group: docs
  title: ''
  type: Documentation
  url: https://wealthengine.com/developer-api
- group: docs
  title: ''
  type: APIReference
  url: https://wealthengine.com/developer-api
- group: start
  title: ''
  type: GettingStarted
  url: https://wealthengine.com/developer-api
- group: operate
  title: ''
  type: Support
  url: https://wealthengine.com/contact
- group: company
  title: ''
  type: Blog
  url: https://wealthengine.com/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altrata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altrata.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://wealthengine.com/request-a-demo
coverage:
  checked: '2026-10-27'
  detail: The developer portal provides only HTML documentation without a machine‑readable OpenAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://wealthengine.com/developer-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Wealth Engine provides a data platform that aggregates and analyzes wealth-related information to help organizations identify, understand, and engage high‑net‑worth individuals and households. Leveraging machine learning on billions of data points, the service offers real‑time net‑worth estimates, income, asset holdings, philanthropic capacity, and other wealth attributes. This enables nonprofits, financial services, and marketers to target prospects more effectively, personalize outreach, and improve fundraising or sales strategies.
layout: provider
modified: '2026-10-27'
name: Wealth Engine
nav: Providers
network: true
overview: 'Wealth Engine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Wealth, Analytics, and Marketing.


  Wealth Engine''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wealthengine Domain Security
  slug: wealthengine-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wealthengine
tags:
- Company
- Data
- Wealth
- Analytics
- Marketing
- Nonprofit
website: https://wealthengine.com/
---
