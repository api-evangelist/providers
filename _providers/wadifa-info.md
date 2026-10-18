---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wadifa Info Agentic Access
  operation_count: 5
  slug: wadifa-info-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- baseURL: https://www.wadifa-info.com
  baseurl_source: spec
  description: The Agenda API from Wadifa Info — 1 operation(s) for agenda.
  name: Wadifa Info Agenda API
  slug: wadifa-info-agenda-api
- baseURL: https://www.wadifa-info.com
  baseurl_source: spec
  description: The Concours API from Wadifa Info — 1 operation(s) for concours.
  name: Wadifa Info Concours API
  slug: wadifa-info-concours-api
- baseURL: https://www.wadifa-info.com
  baseurl_source: spec
  description: The Jours Feries API from Wadifa Info — 1 operation(s) for jours feries.
  name: Wadifa Info Jours Feries API
  slug: wadifa-info-jours-feries-api
- baseURL: https://www.wadifa-info.com
  baseurl_source: spec
  description: The Salaires API from Wadifa Info — 1 operation(s) for salaires.
  name: Wadifa Info Salaires API
  slug: wadifa-info-salaires-api
- baseURL: https://www.wadifa-info.com
  baseurl_source: spec
  description: The Vacances Scolaires API from Wadifa Info — 1 operation(s) for vacances scolaires.
  name: Wadifa Info Vacances Scolaires API
  slug: wadifa-info-vacances-scolaires-api
artifact_total: 13
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/agentic-access/wadifa-info-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wadifa-info-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/rate-limits/wadifa-info-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wadifa-info-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/plans/wadifa-info-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wadifa-info-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/rules/wadifa-info-rules.yml
  title: ''
  type: Spectral
  url: rules/wadifa-info-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/json-ld/wadifa-info-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wadifa-info-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/vocabulary/wadifa-info-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wadifa-info-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/data-model/wadifa-info-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wadifa-info-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/conventions/wadifa-info-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wadifa-info-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/conformance/wadifa-info-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wadifa-info-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/llms/wadifa-info-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wadifa-info-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/hosts/wadifa-info-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wadifa-info-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/vendors/wadifa-info-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wadifa-info-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.whatsapp.com/send?text=API+gratuite+des+concours+de+la+fonction+publique+au+Maroc%0ahttps%3a%2f%2fwww.wadifa-info.com%2fdeveloppeurs%3futm_source%3dshare%26utm_medium%3dwhatsapp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/security/wadifa-info-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wadifa-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wadifa-info.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wadifa-info.com/developpeurs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wadifa-info.com/index/PrivacyPolicy
- group: company
  title: ''
  type: Newsroom
  url: https://www.wadifa-info.com/sitemap/news
- group: other
  title: ''
  type: RSS
  url: https://www.wadifa-info.com/rss
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wadifa-info.com/developpeurs
created: '2026-10-09'
description: Wadifa Info is a Moroccan public-sector jobs portal (concours de la fonction publique) based in Rabat, publishing a free, keyless, read-only JSON API of open civil-service recruitment competitions, indicative net salaries by grade, public holidays and school holidays, plus iCalendar agendas, RSS and CSV datasets under CC BY 4.0.
image: https://www.wadifa-info.com/index/GenerateHomeCard?lang=ar&d=20261009
json_schemas:
- name: ConcoursList
  property_count: 4
  slug: wadifa-info-concours-list
- name: SalaryList
  property_count: 4
  slug: wadifa-info-salary-list
jsonld:
- class_count: 5
  name: Wadifa Info Context
  property_count: 18
  slug: wadifa-info-context
layout: provider
modified: '2026-10-09'
name: Wadifa Info
nav: Providers
network: true
overview: 'Wadifa Info publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agenda API, Concours API, Jours Feries API, and 2 more. Tagged areas include Company, Job, Public Sector, Morocco, and Open Data.


  The Wadifa Info catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wadifa Info''s developer surface includes documentation, pricing, and 18 more developer resources.'
plans:
- name: Wadifa Info Plans Pricing
  plan_count: 1
  slug: wadifa-info-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Wadifa Info Rate Limits
  slug: wadifa-info-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Wadifa Info API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: wadifa-info-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 73.8
    catalog_earned_first_party: 16.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 54.6
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
    - mena
    - north-africa
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/wadifa-info/refs/heads/main/screenshots/wadifa-info-2026-10-11T133230.png
security:
- kind: domain-security
  name: Wadifa Info Domain Security
  slug: wadifa-info-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wadifa-info
tags:
- Company
- Job
- Public Sector
- Morocco
- Open Data
- Salaries
- Government
website: https://www.wadifa-info.com/
---
