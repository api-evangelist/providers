---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stockly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stockly.ai/
- group: operate
  title: ''
  type: Support
  url: https://stockly.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@admin_31497
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stockly
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stockly.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stockly.ai/legal
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stockly-llms.txt
created: '2026-07-17'
description: Stockly (Stockly SAS, headquartered in Vitry-sur-Seine, France) operates a global inventory network for e-commerce, positioning itself as "the first global inventory for Retail." It connects online retailers that are missing stock (Demanders) with brands and official retailers that hold surplus inventory (Suppliers), detecting out-of-stock variants and filling the gaps in real time so that e-shops never run out of stock. Stockly integrates directly with a retailer's e-commerce infrastructure via API, a CMS, or a marketplace, and is building toward a stock exchange for e-commerce inventory in compliance with brands' distribution policies. The company reports 300+ partnered retailers across Europe and 100M+ available items, and is backed by Techstars. Stockly is primarily a partner-onboarded platform rather than a broad self-serve public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stockly.png
layout: provider
modified: '2026-07-21'
name: Stockly
nav: Providers
network: true
overview: 'Stockly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Inventory, and Stock Management.


  Stockly''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stockly/refs/heads/main/screenshots/stockly-2026-09-02T160913.png
security:
- kind: domain-security
  name: Stockly Domain Security
  slug: stockly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stockly
tags:
- Company
- E-Commerce
- Retail
- Inventory
- Stock Management
- Fulfillment
- Marketplace
- Supply Chain
website: https://stockly.ai/
---
