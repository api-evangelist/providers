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
  href: https://artifacts.apis.io/traivefinance-com/hosts/traivefinance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/traivefinance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/traivefinance-com/vendors/traivefinance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/traivefinance-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/traivefinance-com/security/traivefinance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/traivefinance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://traive.com.br/
- group: other
  title: ''
  type: Image
  url: https://traive.com.br/wp-content/uploads/2025/05/Traive-a-ponte-entre-o-campo-e-o-credito.png
- group: company
  title: ''
  type: Blog
  url: https://traive.com.br/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://traive.com.br/termos-e-condicoes-de-uso/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://traive.com.br/politica-de-privacidade/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://traive.com.br/codigo-de-conduta-do-fornecedor-cliente/
- group: commercial
  title: ''
  type: Pricing
  url: https://traive.com.br/solucoes/mercado-agricola/
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec endpoint returned 403, indicating authentication is required and no public spec is available.
  evidence:
  - status: 403
    url: https://api.traivefinance.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Traive is a technology company that connects agribusiness with the financial market using AI and data intelligence. It transforms agricultural credit into liquid financial assets, offering products and services that simplify access to credit and investment opportunities for producers, cooperatives, distributors, and investors. The platform leverages advanced technology, data, and expertise to create a powerful link between the agricultural sector and financial investors, aiming to improve credit availability and market efficiency.
image: https://traive.com.br/wp-content/uploads/2025/05/Traive-a-ponte-entre-o-campo-e-o-credito.png
layout: provider
modified: '2026-10-29'
name: Traive
nav: Providers
network: true
overview: 'Traive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Agritech, AI, and Data.


  Traive''s developer surface includes engineering blog, pricing, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Traivefinance Com Domain Security
  slug: traivefinance-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: traivefinance-com
tags:
- Company
- FinTech
- Agritech
- AI
- Data
- Credit
website: https://traive.com.br/
---
