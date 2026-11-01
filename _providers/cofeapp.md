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
api_count: 1
apis:
- description: API for the COFE platform offering agentic commerce and procurement capabilities.
  name: COFE Platform API
  slug: cofe-platform-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/cofeapp/conformance/cofeapp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cofeapp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cofeapp/llms/cofeapp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cofeapp-llms.txt
- group: other
  href: https://artifacts.apis.io/cofeapp/hosts/cofeapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cofeapp-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.cofeapp.com/company/team
- group: company
  title: ''
  type: Blog
  url: https://www.cofeapp.com/resources/blog
- group: auth
  href: https://artifacts.apis.io/cofeapp/security/cofeapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cofeapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cofeapp.com
- group: company
  title: ''
  type: About
  url: https://www.cofeapp.com/company/about
- group: company
  title: ''
  type: News
  url: https://www.cofeapp.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cofeapp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cofeapp.com/terms-and-conditions-users
- group: auth
  href: https://artifacts.apis.io/cofeapp/security/cofeapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cofeapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cofeapp.com
- group: company
  title: ''
  type: About
  url: https://www.cofeapp.com/company/about
- group: company
  title: ''
  type: News
  url: https://www.cofeapp.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cofeapp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cofeapp.com/terms-and-conditions-users
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cofeapp.com
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cofeapp, operating under the brand COFE Technologies, provides an agentic platform combining Agentic Commerce and Agentic Procurement engines. The platform powers a super‑app used by millions, offering e‑commerce, ordering, payments, loyalty, data intelligence, and enterprise automation solutions across the MENA region. It serves both consumer and enterprise customers, enabling businesses to run their operations with AI‑driven agents and a unified data model.
image: https://www.cofeapp.com/og.jpg
layout: provider
modified: '2026-10-09'
name: Cofeapp
nav: Providers
network: true
overview: 'Cofeapp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Platform, Artificial Intelligence, Commerce, and Procurement.


  Cofeapp''s developer surface includes engineering blog, product news, and 15 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 60.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
  previous_composite: 13.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cofeapp Domain Security
  slug: cofeapp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cofeapp
tags:
- Company
- Platform
- Artificial Intelligence
- Commerce
- Procurement
- MENA
website: https://www.cofeapp.com
---
