---
access_model:
  confidence: high
  label: Free · Open harvesting endpoints, no signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: PHAIDRA is the University of Padua Library System's digital-collections repository, holding the institution's digitised images, documents, books and video. The data, the objects and the persistent ide
  name: PHAIDRA at Padua (deployment)
  slug: phaidra-unipd
- description: 'OAI-PMH 2.0 harvesting endpoint for IRIS UNIPD, the University of Padua''s institutional research catalogue of scientific production. Live and anonymous: verb=Identify returns HTTP 200 with repositoryN'
  name: IRIS UNIPD OAI-PMH
  slug: iris-unipd-oai
- description: 'OAI-PMH 2.0 harvesting endpoint for Research Data Unipd, the EPrints-based research-data archive of the University of Padua. Live and anonymous: verb=Identify returns HTTP 200 with repositoryName "Res'
  name: Research Data Unipd OAI-PMH
  slug: researchdata-unipd-oai
- description: OAI-PMH 2.0 harvesting endpoint for the University of Padua theses and dissertations archive. Live and anonymous at /oai/request (verb=Identify returns HTTP 200); the EPrints-style /cgi/oai2 path on t
  name: Padua Theses and Dissertations OAI-PMH
  slug: thesis-unipd-oai
- description: The University of Padua operates its own Shibboleth Identity Provider and publishes its SAML 2.0 metadata anonymously at https://shibidp.cca.unipd.it/idp/shibboleth — HTTP 200, application/xml, 17,853
  name: University of Padova Shibboleth Identity Provider (SAML metadata)
  slug: shibboleth-idp
artifact_total: 9
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/phaidra/phaidra-api/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.unipd.it/en
- group: build
  title: ''
  type: LibraryCatalog
  url: https://biblio.unipd.it/en
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.research.unipd.it/
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchdata.cab.unipd.it/
- group: other
  title: ''
  type: ResearchRepository
  url: https://thesis.unipd.it/
- group: other
  title: ''
  type: ResearchRepository
  url: https://phaidra.unipd.it/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.unipd.it/en/idem
- group: auth
  title: ''
  type: Authentication
  url: https://asit.unipd.it/single-sign-informazioni-tecniche-service-provider
- group: other
  title: ''
  type: AIPolicy
  url: https://www.unipd.it/en/policy-ateneo
- group: other
  title: ''
  type: AIPolicy
  url: https://wwwassets.unipd.it/sites/default/files/2026-04/LineeGuidaImpiegoAI_nella_ricerca_Unipd_ITA_rev20260414.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unipd.it/en/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://it.linkedin.com/school/university-of-padova/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-padua-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-padua-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-padua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-padua-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-padua-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Padua (Università degli Studi di Padova) is a public research university in Padua, Italy, founded in 1222. It operates no central developer portal and publishes no institution-authored API contract: an "API first" programme exists internally, routed through the IUNGO integration infrastructure and a GovWay API gateway, but the catalogue of REST web services it promises is not public and access runs through a helpdesk ticket. What Padua does operate, and what this profile records, is protocol infrastructure rather than product APIs — four live OAI-PMH 2.0 endpoints on its own hosts (the IRIS research catalogue, the Research Data Unipd data archive, the theses archive, and PHAIDRA), and a Shibboleth Identity Provider publishing SAML 2.0 metadata into the IDEM GARR federation and eduGAIN. The one documented REST API on a Padua host, PHAIDRA''s, is the contract of the PHAIDRA open-source repository platform developed at the University of Vienna, not Padua engineering;
  it is recorded here as a deployment and its specification is deliberately not held under this slug. An institutional Open Data portal was announced in December 2024 but has not launched — no open-data host resolves. There is no institutional GitHub organisation; github.com/unipd exists but holds zero public repositories.'
finops:
- name: University Of Padua Finops
  service_category: Education
  slug: university-of-padua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-padua.png
layout: provider
modified: '2026-08-30'
name: University of Padua
nav: Providers
network: true
overview: 'University of Padua publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Italy, and Europe.


  University of Padua''s developer surface includes authentication and 18 more developer resources.'
plans:
- name: University Of Padua Plans Pricing
  plan_count: 2
  slug: university-of-padua-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: University Of Padua Rate Limits
  slug: university-of-padua-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 4.4
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 29.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-padua/refs/heads/main/screenshots/university-of-padua-2026-06-20T200320.png
security:
- kind: domain-security
  name: University Of Padua Domain Security
  slug: university-of-padua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-padua
tags:
- University
- Higher Education
- Education
- Italy
- Europe
- Public Research University
- Research Repository
- Research Data
- Open Access
- OAI-PMH
- Identity Federation
- Digital Library
website: https://www.unipd.it/en
---
