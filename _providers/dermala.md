---
agent_readiness:
  band: agent-aware
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
  score: 7.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GraphQL API discovered at https://www.dermala.com/api/graphql. Endpoint appears to be a Shopify-hosted GraphQL service; ownership could not be verified.
  name: Dermala GraphQL API
  slug: dermala-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dermala/llms/dermala-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dermala-llms.txt
- group: agent
  href: https://artifacts.apis.io/dermala/well-known/dermala-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dermala-well-known.yml
- group: other
  href: https://artifacts.apis.io/dermala/hosts/dermala-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dermala-hosts.yml
- group: other
  href: https://artifacts.apis.io/dermala/vendors/dermala-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dermala-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dermala.com/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dermala.com/pages/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.dermala.com/account/login
- group: auth
  href: https://artifacts.apis.io/dermala/security/dermala-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dermala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dermala.com/
coverage:
  checked: '2026-10-23'
  detail: GraphQL endpoint is reachable but ownership could not be verified and no OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://www.dermala.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Dermala provides personalized microbiome-based solutions for acne and skin health. Their platform offers a skin quiz to personalize supplement kits, a range of probiotic skincare products, and a SkinGPT AI tool for skin condition insights. The company operates an e‑commerce site with detailed product pages, clinical study information, and a blog about skin health.
layout: provider
modified: '2026-10-22'
name: Dermala
nav: Providers
network: true
overview: Dermala is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Skincare, Microbiome, and E-Commerce.
random_paper: 6
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dermala Domain Security
  slug: dermala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dermala
tags:
- Company
- Health
- Skincare
- Microbiome
- E-Commerce
website: https://www.dermala.com/
---
