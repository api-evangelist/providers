---
access_model:
  confidence: high
  label: Free · Institutional affiliation or federation membership required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - identity-federation
  - plans
  trial: false
  try_now: false
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Sorbonne University's federated login, published as a signed SAML 2.0 EntityDescriptor at https://auth.id.sorbonne-universite.fr/saml/metadata (HTTP 200, application/xml, 11,704 bytes). Declares HTTP-
  name: Sorbonne University Identity Provider (SAML 2.0)
  slug: identity-provider
- description: Sorbonne University's open archive of scholarly publications, harvestable over OAI-PMH 2.0 at the Sorbonne-scoped base URL https://api.archives-ouvertes.fr/oai/sorbonne-universite/, which returns a va
  name: HAL Sorbonne Universite Open Archive — OAI-PMH (Sorbonne scope)
  slug: hal-oai
- description: The HAL Solr search API scoped to Sorbonne University's collection at https://api.archives-ouvertes.fr/search/SORBONNE-UNIVERSITE/, which returns 326,851 records (HTTP 200, application/json) with face
  name: HAL Search API — SORBONNE-UNIVERSITE collection
  slug: hal-search
- description: Sorbonne University's research-data collection on the French national Recherche Data Gouv repository, addressable through the Dataverse Native REST API at https://entrepot.recherche.data.gouv.fr/api/d
  name: Recherche Data Gouv Dataverse — sorbonne-univ collection
  slug: dataverse
- description: Library discovery for Sorbonne University's letters, sciences and medicine libraries, running on Ex Libris Primo over the Alma library services platform, at the institution-specific view https://sorbo
  name: Sorbonne University Libraries — Ex Libris Primo discovery
  slug: library-discovery
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.sorbonne-universite.fr/en
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/sorbonne-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sorbonne-conformance.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://hal.sorbonne-universite.fr/
- group: other
  title: ''
  type: ResearchData
  url: https://entrepot.recherche.data.gouv.fr/dataverse/sorbonne-univ
- group: build
  title: ''
  type: LibraryCatalog
  url: https://sorbonne-universite.primo.exlibrisgroup.com/discovery/search?vid=33BSU_INST:33BSU
- group: other
  title: ''
  type: ResearchComputing
  url: https://sacado.sorbonne-universite.fr/
- group: other
  title: ''
  type: AIPolicy
  url: https://sante.sorbonne-universite.fr/actualites/recommandations-dutilisation-de-lintelligence-artificielle-generative-dans-le-cadre-de
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sorbonne-universite.fr/en/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sorbonne-universite.fr/en/data-protection-policy
- group: operate
  title: ''
  type: Support
  url: https://www.sorbonne-universite.fr/en/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.sorbonne-universite.fr/en/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.sorbonne-universite.fr/rss.xml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sorbonne-universite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/sorbonne-universite/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sorbonne-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sorbonne-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sorbonne-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sorbonne-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Sorbonne University (Sorbonne Universite) is a public research university in Paris, France, formed in 2018 from the merger of Paris-Sorbonne and Pierre et Marie Curie universities, serving roughly 53,000 students across faculties of Arts & Humanities, Health Sciences, and Science & Engineering. It operates no central developer portal, no open-data portal, and no institution-operated REST API, and this profile says so rather than padding the gap. What it does operate, and self-publish, is a complete machine-readable SAML 2.0 identity federation contract. The identity provider at auth.id.sorbonne-universite.fr serves a signed EntityDescriptor at a dereferenceable entityID, is registered in the RENATER federation with the REFEDS Research & Scholarship entity category and a SIRTFI assurance certification, and reaches the world through eduGAIN. Operator was settled by IP ownership rather than hostname: it CNAMEs to llng.sorbonne-universite.fr and resolves into FR-UPMC-NET, the university''s
  own RIPE allocation at 4 Place Jussieu, behind an organization-validated GEANT TCS certificate issued to O=SORBONNE UNIVERSITE, running self-hosted LemonLDAP::NG. Three further RENATER service providers — including the 4EU+ virtual campus platform and a federated-wifi portal — sit on the university''s own production estate. SAML is therefore Sorbonne''s only institution-operated education-regime conformance, and Shibboleth is deliberately not claimed: the stack is LemonLDAP::NG and SimpleSAMLphp, not Shibboleth. Everything else that looks like a Sorbonne API is a national or commercial platform on which the university holds an account, and is recorded here as a tenant relationship rather than as a Sorbonne contract: the HAL open archive and its OAI-PMH and Solr search endpoints are CCSD''s (CNRS), the sorbonne-univ research-data collection runs on Recherche Data Gouv''s Dataverse with DOIs minted under Recherche Data Gouv''s DataCite account, and library discovery is Ex Libris Primo/Alma.
  The GitHub organization exists and holds no public repositories. The university''s own HAL portal host serves an Anubis proof-of-work bot challenge, so the one institutional research surface on a Sorbonne domain is closed to agents.'
finops:
- name: Sorbonne Finops
  service_category: Education
  slug: sorbonne-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sorbonne.png
jsonld:
- class_count: 11
  name: Sorbonne Context
  property_count: 12
  slug: sorbonne-context
layout: provider
modified: '2026-08-30'
name: Sorbonne University
nav: Providers
network: true
overview: 'Sorbonne University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, France, and Identity Federation.


  The Sorbonne University catalog on APIs.io includes 1 JSON-LD context.


  Sorbonne University''s developer surface includes support, engineering blog, GitHub presence, and 17 more developer resources.'
plans:
- name: Sorbonne Plans Pricing
  plan_count: 2
  slug: sorbonne-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Sorbonne Rate Limits
  slug: sorbonne-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 70.0
    catalog_earned_first_party: 0.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 18.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sorbonne/refs/heads/main/screenshots/sorbonne-2026-06-20T194214.png
security:
- kind: domain-security
  name: Sorbonne Domain Security
  slug: sorbonne-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sorbonne
tags:
- Education
- Higher Education
- University
- France
- Identity Federation
- Research Repository
- Research Data
- Library
- Open Access
- Open Science
website: https://www.sorbonne-universite.fr/en
---
