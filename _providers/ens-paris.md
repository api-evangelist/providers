---
access_model:
  confidence: high
  label: Free · No registration for public reads; federated identity otherwise
  onboarding: open
  pricing: free
  public: true
  source:
  - probed
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: ENS-PSL runs its own Shibboleth identity provider under its own registrable domain. The SAML 2.0 entity descriptor is served at https://federation.ens.psl.eu/idp/shibboleth (HTTP 200, application/xml)
  name: ENS-PSL Identity Provider (SAML 2.0 / Shibboleth)
  slug: identity-federation
- description: 'The catalogue of the ten ENS-PSL libraries, hosted at catalogue.bib.ens.psl.eu under the institution''s own domain and integrated by BibLibre. Two machine-readable interfaces answer publicly. The Koha '
  name: ENS-PSL Library Catalogue (Koha REST + OAI-PMH)
  slug: library-catalog
- description: ENS research output is deposited into the ENS-PARIS collection of HAL, the French national open archive operated by CCSD (CNRS). The collection is real and substantial — HAL's ENS-scoped Search API re
  name: HAL-ENS Open Archive — ENS-PARIS collection
  slug: hal-ens
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.ens.psl.eu/en
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ecole-normale-superieure/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ens.psl.eu/mentions-legales
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ens.psl.eu/en/rss.xml
- group: other
  title: ''
  type: IdentityFederation
  url: https://federation.ens.psl.eu/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalogue.bib.ens.psl.eu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://hal-ens.archives-ouvertes.fr/
- group: design
  title: ''
  type: Conformance
  url: conformance/ens-paris-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ens-paris-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ens-paris-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ens-paris-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ens-paris-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ens-paris-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/ens-paris-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld-context
  url: json-ld/ens-paris-context.jsonld
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
created: '2026-06-03'
description: 'École normale supérieure - PSL (ENS, rue d''Ulm) is a French grande école and constituent institution of Université PSL, running 15 departments, 35 research laboratories and a ten-library network in the Quartier latin of Paris. ENS publishes no developer portal, no OpenAPI description and no API key programme, and this profile does not pretend otherwise. What it does operate, verified live on 2026-08-30, is two machine-readable surfaces on its own domain: a SAML 2.0 / Shibboleth identity provider at federation.ens.psl.eu, registered in the RENATER Fédération Éducation-Recherche with scopes ens.fr and ens.psl.eu; and the ENS-PSL library catalogue at catalogue.bib.ens.psl.eu, a Koha deployment exposing an unauthenticated REST API and an OAI-PMH 2.0 provider whose Identify names the repository "bibliothèques de l''ENS-PSL". Alongside those, ENS holds one tenant relationship worth recording — the ENS-PARIS collection inside the national HAL open archive, operated by CCSD/CNRS,
  harvestable as the OAI-PMH set collection:ENS-PARIS and queryable through HAL''s ENS-scoped Search API. An earlier version of this profile credited ENS with the French Ministry of Higher Education''s Opendatasoft Explore API; that contract is Opendatasoft''s, deployed by the ministry, and it and everything derived from it were removed on 2026-08-30.'
finops:
- name: Ens Paris Finops
  service_category: Education
  slug: ens-paris-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ens-paris.png
jsonld:
- class_count: 7
  name: Ens Paris Context
  property_count: 4
  slug: ens-paris-context
layout: provider
modified: '2026-08-30'
name: École Normale Supérieure de Paris
nav: Providers
network: true
overview: 'École Normale Supérieure de Paris publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, France, and Université PSL.


  The École Normale Supérieure de Paris catalog on APIs.io includes 1 JSON-LD context.


  École Normale Supérieure de Paris'' developer surface includes authentication and 16 more developer resources.'
plans:
- name: Ens Paris Plans Pricing
  plan_count: 2
  slug: ens-paris-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Ens Paris Rate Limits
  slug: ens-paris-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 23.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ens-paris/refs/heads/main/screenshots/ens-paris-2026-06-20T180723.png
security:
- kind: authentication
  name: Ens Paris Authentication
  slug: ens-paris-authentication
  summary_line: saml/basic/none · 4 schemes
- kind: domain-security
  name: Ens Paris Domain Security
  slug: ens-paris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ens-paris
tags:
- University
- Higher Education
- Education
- France
- Université PSL
- Research
- Identity Federation
- Library
- Open Access
- OAI-PMH
website: https://www.ens.psl.eu/en
---
