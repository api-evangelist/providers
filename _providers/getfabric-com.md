---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/getfabric-com/hosts/getfabric-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getfabric-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getfabric-com/vendors/getfabric-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getfabric-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getfabric.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.getfabric.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.getfabric.com/blog/is-warehouse-automation-really-killing-jobs
- group: auth
  href: https://artifacts.apis.io/getfabric-com/security/getfabric-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getfabric-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getfabric.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.getfabric.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Fabric provides a fast, profitable, all-in-one automated fulfillment solution. Their platform adapts to various use cases with unique features tailored to each application, enabling businesses to streamline order processing, inventory management, and shipping across multiple channels.
image: https://cdn.prod.website-files.com/66ebe77f6b0eb144deff3812/676163ed86cf10ab7f62a57c_1200%20(1).jpg
layout: provider
modified: '2026-10-23'
name: Fabric
nav: Providers
network: true
overview: 'Fabric is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fulfillment, Automation, Robotics, Grocery, and Health & Beauty.


  Fabric''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getfabric Com Domain Security
  slug: getfabric-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getfabric-com
tags:
- Fulfillment
- Automation
- Robotics
- Grocery
- Health & Beauty
- Micro Fulfillment
- Storage
- Q‑commerce
website: https://www.getfabric.com/
---
