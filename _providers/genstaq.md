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
  href: https://artifacts.apis.io/genstaq/hosts/genstaq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/genstaq-hosts.yml
- group: other
  href: https://artifacts.apis.io/genstaq/vendors/genstaq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/genstaq-vendors.yml
- group: auth
  href: https://artifacts.apis.io/genstaq/security/genstaq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/genstaq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://genstaq.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://genstaq.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://genstaq.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://genstaq.ai/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://genstaq.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://genstaq.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://genstaq.ai/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://genstaq.ai/
  reason: no-developer-program
  state: none
created: '2026-10-17'
description: GenStaq.ai provides modular, production‑ready GenAI infrastructure for enterprises. Recently acquired by RevRag.ai, the platform offers customizable AI systems, robust security, and scalable services for the BFSI sector. The company focuses on making GenAI infra modular, enterprise‑grade, and easy to integrate across products.
layout: provider
modified: '2026-10-17'
name: GenStaq.ai
nav: Providers
network: true
overview: 'GenStaq.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Infrastructure, Enterprise, and Generative AI.


  GenStaq.ai''s developer surface includes documentation, API reference, getting-started guide, pricing, and 6 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Genstaq Domain Security
  slug: genstaq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: genstaq
tags:
- Company
- Artificial Intelligence
- Infrastructure
- Enterprise
- Generative AI
website: https://genstaq.ai/
---
