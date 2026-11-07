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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bidit provides a suite of ecommerce tools suite as described on the website.
  name: Bidit API
  slug: bidit-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bidit-com-au/hosts/bidit-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidit-com-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidit-com-au/vendors/bidit-com-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidit-com-au-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://bidit.com.au/resources/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidit.com.au/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.bidit.com.au/
- group: auth
  href: https://artifacts.apis.io/bidit-com-au/security/bidit-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidit-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidit.com.au/
coverage:
  checked: '2026-11-02'
  detail: No machine‑readable API contract was found on the provider’s site or discovered hosts.
  evidence:
  - status: 200
    url: https://bidit.com.au/
  - status: 200
    url: https://blog.bidit.com.au/
  - status: 401
    url: https://dashboard.bidit.com.au/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bidit provides a suite of ecommerce tools that embed directly into online stores, enabling merchants to capture purchase offers from shoppers in real time. The platform offers features such as Bidit Classic, Cart, Onsite Abandonment, Retargeting, Plus, Analytics, and Instore, helping businesses close more sales and improve conversion rates across fashion, footwear, jewellery, gifting, furniture, automotive, and other industries.
layout: provider
modified: '2026-11-02'
name: Bidit
nav: Providers
network: true
overview: 'Bidit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Sales, Retail, Marketing, and Technology.


  Bidit''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidit Com Au Domain Security
  slug: bidit-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bidit-com-au
tags:
- E-Commerce
- Sales
- Retail
- Marketing
- Technology
- Company
website: https://bidit.com.au/
---
