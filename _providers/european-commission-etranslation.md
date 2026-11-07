---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Use the European Commission’s free, secure AI-based translation and language tools to translate, generate and improve content in multiple languages.
  name: eTranslation API
  slug: etranslation-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/european-commission-etranslation/well-known/european-commission-etranslation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/european-commission-etranslation-well-known.yml
- group: other
  href: https://artifacts.apis.io/european-commission-etranslation/hosts/european-commission-etranslation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/european-commission-etranslation-hosts.yml
- group: other
  href: https://artifacts.apis.io/european-commission-etranslation/vendors/european-commission-etranslation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/european-commission-etranslation-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commission.europa.eu/legal-notice_en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commission.europa.eu/privacy-policy-websites-managed-european-commission_en
- group: auth
  href: https://artifacts.apis.io/european-commission-etranslation/security/european-commission-etranslation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/european-commission-etranslation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://commission.europa.eu/resources-partners/etranslation_en
- group: docs
  title: ''
  type: Documentation
  url: https://translation.ec.europa.eu/tools-and-resources/ai-translation-and-language-tools_en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://translation.ec.europa.eu/
- group: start
  title: ''
  type: GettingStarted
  url: https://translation.ec.europa.eu/tools-and-resources/ai-translation-and-language-tools_en
- group: operate
  title: ''
  type: Support
  url: https://translation.ec.europa.eu/index_en
coverage:
  checked: '2026-10-27'
  detail: Documentation is provided as HTML pages without a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://translation.ec.europa.eu/tools-and-resources/ai-translation-and-language-tools_en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: European Commission eTranslation provides AI-powered language translation and related tools as part of the European Commission’s multilingualism initiatives. It offers free, secure translation, summarisation, and content generation services across all 24 EU official languages, targeting public sector users, language professionals, and educators. The service builds on decades of EU translation expertise and aims to enhance accessibility and communication within the European Union.
image: https://translation.ec.europa.eu/sites/default/files/styles/ewcms_metatag_image/public/2025-10/16.png?h=2d3fd349&itok=FOFVerF6
layout: provider
modified: '2026-10-27'
name: European Commission eTranslation
nav: Providers
network: true
overview: 'European Commission eTranslation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Translation, Artificial Intelligence, and Multilingual.


  European Commission eTranslation''s developer surface includes documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/european-commission-etranslation/european-commission-etranslation-2026-11-03T131639.png
security:
- kind: domain-security
  name: European Commission Etranslation Domain Security
  slug: european-commission-etranslation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: european-commission-etranslation
tags:
- Company
- Government
- Translation
- Artificial Intelligence
- Multilingual
website: https://commission.europa.eu/resources-partners/etranslation_en
---
