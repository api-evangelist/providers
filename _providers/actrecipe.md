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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/actrecipe/hosts/actrecipe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actrecipe-hosts.yml
- group: other
  href: https://artifacts.apis.io/actrecipe/vendors/actrecipe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actrecipe-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actrecipe.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.actrecipe.com/news/gree/
- group: start
  title: ''
  type: Login
  url: https://app.actrecipe.com/login
- group: auth
  href: https://artifacts.apis.io/actrecipe/security/actrecipe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actrecipe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actrecipe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.actrecipe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.actrecipe.com/features/
- group: operate
  title: ''
  type: Support
  url: https://support.actrecipe.com/
- group: company
  title: ''
  type: Blog
  url: https://www.actrecipe.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/actrecipe
created: '2026-10-19'
description: ActRecipe is a Japanese iPaaS platform that enables businesses to automate workflows by connecting SaaS applications through customizable "recipes". It offers features such as SaaS integration, task reminders, bank API connections, and back‑office process automation. The service provides a visual interface for building integrations, supports multiple languages, and includes pricing plans for various company sizes. ActRecipe aims to simplify complex system integrations for IT teams and non‑technical users alike, helping to streamline operations and improve efficiency across departments.
image: https://www.actrecipe.com/wp-content/uploads/2023/04/ipaas-actrecipe-2023-spring.jpg
layout: provider
modified: '2026-10-19'
name: ActRecipe
nav: Providers
network: true
overview: 'ActRecipe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, iPaaS, Automation, SaaS Integration, and Japanese.


  ActRecipe''s developer surface includes documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Actrecipe Domain Security
  slug: actrecipe-domain-security
  summary_line: TLSv1.2 · DMARC
slug: actrecipe
tags:
- Company
- iPaaS
- Automation
- SaaS Integration
- Japanese
website: https://actrecipe.com/
---
