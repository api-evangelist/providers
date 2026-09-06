---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oncoc4-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oncoc4-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oncoc4-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oncoc4-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oncoc4-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oncoc4-llms.txt
- group: company
  title: ''
  type: Website
  url: https://oncoc4.com/en/
- group: company
  title: ''
  type: About
  url: https://oncoc4.com/en/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://oncoc4.com/en/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oncoc4.com/en/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://oncoc4.com/en/careers/
- group: company
  title: ''
  type: News
  url: https://oncoc4.com/en/news-resources/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oncoc4
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/oncoc4_stock/
coverage:
  checked: '2026-08-04'
  detail: OncoC4 is a late clinical-stage biopharmaceutical company whose product is a drug, not software — the entire oncoc4.com site is an Umbraco-hosted corporate brochure (about, pipeline, clinical trials, publications, careers) with no developer section, and the only machine-readable documents it serves are Umbraco's default OIDC/OAuth member-login discovery files.
  evidence:
  - status: 404
    url: https://oncoc4.com/openapi.json
  - status: 404
    url: https://oncoc4.com/api-docs
  - status: 404
    url: https://oncoc4.com/graphql
  - status: 404
    url: https://oncoc4.com/.well-known/agent-card.json
  - status: 200
    url: https://oncoc4.com/.well-known/openid-configuration
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: OncoC4, Inc. is a privately held, late clinical-stage biopharmaceutical company headquartered in Rockville, Maryland, founded in 2020, with subsidiaries in Nanjing, Guangzhou and Beijing, China, and Brisbane, Australia. The company discovers and develops novel biologics for the treatment of cancer, working across immune checkpoints including CTLA-4, CD24, PD-1/VEGF and the Siglec family, with monoclonal antibodies, bispecific antibodies, antibody-drug conjugates and CAR T-cell therapies. Its lead clinical candidate is gotistobart (BNT316/ONC-392), a next-generation anti-CTLA-4 antibody co-developed and commercialized with BioNTech under a strategic collaboration announced in March 2023. OncoC4 publishes no developer program, public API, SDK or developer documentation; its corporate website runs on the Umbraco CMS, which serves a default OpenID Connect / OAuth 2.0 discovery document and JWKS for CMS member authentication.
image: https://oncoc4.com/media/tlofbavh/logo.svg
layout: provider
modified: '2026-08-04'
name: OncoC4
nav: Providers
network: true
overview: 'OncoC4 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Biopharmaceutical, Life Sciences, and Oncology.


  OncoC4''s developer surface includes authentication, product news, and 12 more developer resources.'
random_paper: 15
scopes:
- name: Oncoc4 Scopes
  scope_count: 0
  slug: oncoc4-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oncoc4/refs/heads/main/screenshots/oncoc4-2026-08-07T190225.png
security:
- kind: authentication
  name: Oncoc4 Authentication
  slug: oncoc4-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Oncoc4 Domain Security
  slug: oncoc4-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oncoc4
tags:
- Company
- Biotechnology
- Biopharmaceutical
- Life Sciences
- Oncology
- Immunotherapy
- Clinical Trials
- Healthcare
- Pharmaceuticals
website: https://oncoc4.com/en/
---
