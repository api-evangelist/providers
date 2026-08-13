---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: New York Public Library Whats On The Menu Agentic Access
  operation_count: 9
  slug: new-york-public-library-whats-on-the-menu-agentic-access
  summary_line: 9 operations
api_count: 2
apis:
- description: Dish records appearing across menus.
  name: New York Public Library What's On The Menu Dishes API
  slug: new-york-public-library-whats-on-the-menu-dishes-api
- description: Historical menu records and pages.
  name: New York Public Library What's On The Menu Menus API
  slug: new-york-public-library-whats-on-the-menu-menus-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/new-york-public-library-whats-on-the-menu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/new-york-public-library-whats-on-the-menu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/new-york-public-library-whats-on-the-menu-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NYPL
- group: company
  title: ''
  type: Website
  url: https://www.nypl.org/research/support/whats-on-the-menu
- group: docs
  title: ''
  type: Documentation
  url: http://nypl.github.io/menus-api/
- group: other
  title: ''
  type: DataDictionary
  url: http://curatingmenus.org/data_dictionary/
created: '2024-11-14'
description: The New York Public Library's What's On The Menu project is a crowdsourced digital collection of over 17,000 historical restaurant menus from the New York City area dating back to the 1850s, with more than 1.3 million transcribed dishes. The dataset is modeled as four related entities (Menu, MenuPage, MenuItem, Dish) and distributed as bulk CSV downloads. A companion HTTP API formerly provided programmatic access to menus, pages, and dishes; the live site and api.menus.nypl.org were retired in January 2025, but the crowdsourced dataset remains available as a gzip archive on Amazon S3 alongside a data dictionary.
examples:
- key_count: 9
  name: New York Public Library Whats On The Menu Dish Example
  slug: new-york-public-library-whats-on-the-menu-dish-example
- key_count: 20
  name: New York Public Library Whats On The Menu Menu Example
  slug: new-york-public-library-whats-on-the-menu-menu-example
- key_count: 9
  name: New York Public Library Whats On The Menu Menu Item Example
  slug: new-york-public-library-whats-on-the-menu-menu-item-example
- key_count: 7
  name: New York Public Library Whats On The Menu Menu Page Example
  slug: new-york-public-library-whats-on-the-menu-menu-page-example
finops:
- name: New York Public Library Whats On The Menu Finops
  service_category: API
  slug: new-york-public-library-whats-on-the-menu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/new-york-public-library-whats-on-the-menu.png
json_schemas:
- name: Dish
  property_count: 9
  slug: new-york-public-library-whats-on-the-menu-dish
- name: MenuItem
  property_count: 9
  slug: new-york-public-library-whats-on-the-menu-menu-item
- name: MenuPage
  property_count: 7
  slug: new-york-public-library-whats-on-the-menu-menu-page
- name: Menu
  property_count: 20
  slug: new-york-public-library-whats-on-the-menu-menu
json_structures:
- name: New York Public Library Whats On The Menu Dataset Structure
  property_count: 4
  slug: new-york-public-library-whats-on-the-menu-dataset-structure
jsonld:
- class_count: 26
  name: New York Public Library Whats On The Menu Context
  property_count: 21
  slug: new-york-public-library-whats-on-the-menu-context
layout: provider
modified: '2026-06-03'
name: New York Public Library What's On The Menu
nav: Providers
network: true
overview: 'New York Public Library What''s On The Menu publishes 2 APIs on the [APIs.io](https://apis.io/) network: Dishes API and Menus API. Tagged areas include Libraries, Menus, Restaurants, History, and Open Data.


  The New York Public Library What''s On The Menu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  New York Public Library What''s On The Menu''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: New York Public Library Whats On The Menu Plans Pricing
  plan_count: 3
  slug: new-york-public-library-whats-on-the-menu-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: New York Public Library Whats On The Menu Rate Limits
  slug: new-york-public-library-whats-on-the-menu-rate-limits
rules:
- name: New York Public Library What's On The Menu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: new-york-public-library-whats-on-the-menu-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 68.7
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/new-york-public-library-whats-on-the-menu/refs/heads/main/screenshots/new-york-public-library-whats-on-the-menu-2026-06-20T190231.png
security:
- kind: authentication
  name: New York Public Library Whats On The Menu Authentication
  slug: new-york-public-library-whats-on-the-menu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: New York Public Library Whats On The Menu Domain Security
  slug: new-york-public-library-whats-on-the-menu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: new-york-public-library-whats-on-the-menu
tags:
- Libraries
- Menus
- Restaurants
- History
- Open Data
- Food
- Datasets
- Cultural Heritage
website: https://www.nypl.org/research/support/whats-on-the-menu
---
