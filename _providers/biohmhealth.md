---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: GraphQL endpoint providing schema for Biohmhealth's e‑commerce platform.
  name: GraphQL API
  slug: graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biohmhealth/refs/heads/main/llms/biohmhealth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biohmhealth-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biohmhealth/refs/heads/main/well-known/biohmhealth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biohmhealth-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biohmhealth/refs/heads/main/hosts/biohmhealth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biohmhealth-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biohmhealth/refs/heads/main/vendors/biohmhealth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biohmhealth-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biohmhealth.com/pages/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.biohmhealth.com/pages/help-center
- group: company
  title: ''
  type: Newsroom
  url: https://www.biohmhealth.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biohmhealth/refs/heads/main/security/biohmhealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biohmhealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biohmhealth.com
created: '2026-09-28'
description: BIOHM Health provides probiotic supplements, super greens powders, and colon cleanse products aimed at healing leaky gut and supporting a healthy microbiome. The company operates an e‑commerce storefront offering gut‑testing kits, wellness consultations, and a rewards program for customers seeking digestive health solutions.
image: https://cdn.shopify.com/s/files/1/1713/4291/files/logo-dark.png?height=628&pad_color=fff&v=1613725166&width=1200
layout: provider
modified: '2026-09-28'
name: Biohmhealth
nav: Providers
network: true
overview: 'Biohmhealth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Probiotics, Supplements, Gut Health, and E-Commerce.


  Biohmhealth''s developer surface includes support and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biohmhealth Domain Security
  slug: biohmhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biohmhealth
tags:
- Health
- Probiotics
- Supplements
- Gut Health
- E-Commerce
website: https://www.biohmhealth.com
---
