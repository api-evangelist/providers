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
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/foodics-com/authentication/foodics-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/foodics-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/foodics-com/llms/foodics-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/foodics-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/foodics-com/well-known/foodics-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/foodics-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/foodics-com/hosts/foodics-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foodics-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/foodics-com/vendors/foodics-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/foodics-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/foodics-com/packages/foodics-com-packages.yml
  title: ''
  type: SDKs
  url: packages/foodics-com-packages.yml
- group: build
  href: https://artifacts.apis.io/foodics-com/packages/foodics-com-packages.yml
  title: ''
  type: Packages
  url: packages/foodics-com-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.foodics.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://console.foodics.com/signup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.foodics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.foodics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foodics
- group: auth
  href: https://artifacts.apis.io/foodics-com/security/foodics-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foodics-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foodics.com
coverage:
  checked: '2026-10-25'
  detail: Developer portal at https://developers.foodics.com returns HTML likely rendered by JavaScript with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://developers.foodics.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Alwans, operating under the brand Foodics, provides a comprehensive cloud‑based restaurant management platform that streamlines point‑of‑sale, inventory, staff scheduling, and analytics for food‑service businesses. Founded in 2014 and backed by prominent investors, the company serves thousands of restaurants across the Middle East and beyond, offering integrations with payment gateways, delivery services, and third‑party apps. Their API enables developers to build custom extensions, retrieve sales data, manage menus, and automate operational workflows, fostering a vibrant ecosystem of partners and developers.
image: https://www.foodics.com/wp-content/uploads/2023/11/POS-AdRoll.webp
layout: provider
modified: '2026-10-25'
name: Alwans
nav: Providers
network: true
overview: 'Alwans is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, SaaS, API, and Cloud.


  Alwans'' developer surface includes authentication, support, signup flow, documentation, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Foodics Com Authentication
  slug: foodics-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Foodics Com Domain Security
  slug: foodics-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: foodics-com
tags:
- Company
- Restaurant
- SaaS
- API
- Cloud
website: https://foodics.com
---
