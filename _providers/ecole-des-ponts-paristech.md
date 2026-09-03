---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: The one machine-readable contract École des Ponts ParisTech operates on its own infrastructure. A live SAML 2.0 EntityDescriptor served as application/xml from idp.enpc.fr, declaring SingleSignOnServi
  name: ENPC SAML 2.0 Identity Provider Metadata
  slug: saml-idp
- description: 'ENPC''s institutional open-access repository is the ENPC collection inside HAL, the French national open archive operated by CCSD/CNRS, with an ENPC-branded portal at enpc.hal.science. 43,955 records, '
  name: HAL — ENPC Open-Access Collection (tenant)
  slug: hal-enpc
- description: ENPC's research-data repository is the collection with alias "ecoledesponts" (id 148870, dataverseType ORGANIZATIONS_INSTITUTIONS, created 2022-09-13) inside Recherche Data Gouv, the French national D
  name: Recherche Data Gouv — ENPC Dataverse Collection (tenant)
  slug: recherche-data-gouv
- description: ENPC's heritage digital library, holding more than 15,000 digitised documents from the school's collections, serves IIIF Presentation API 2.0 manifests and Gallica image delivery under the hostname he
  name: L'Héritage des Ponts et Chaussées — IIIF Presentation API (tenant)
  slug: heritage-iiif
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://ecoledesponts.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://ecoledesponts.fr/en/documentation/open-science
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.enpc.fr/saml/metadata
- group: other
  title: ''
  type: ResearchRepository
  url: https://enpc.hal.science/
- group: other
  title: ''
  type: ResearchData
  url: https://entrepot.recherche.data.gouv.fr/dataverse/ecoledesponts
- group: build
  title: ''
  type: LibraryCatalog
  url: https://bibliotheque.enpc.fr/exl-php/accueil
- group: build
  title: ''
  type: Library
  url: https://ecoledesponts.fr/bibliotheque
- group: build
  title: ''
  type: DigitalLibrary
  url: https://heritage.ecoledesponts.fr/enpc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EcoleDesPontsParisTech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecoledesponts.fr/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecoledesponts.fr/en/data-processing-and-privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://ecoledesponts.fr/declaration-accessibilite
- group: company
  title: ''
  type: Blog
  url: https://ecoledesponts.fr/actualites-evenements
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ecole-nationale-des-ponts-et-chaussees/
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/ecoledesponts.bsky.social
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/EcoledesPonts
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/ecoledesponts/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ecole-des-ponts-paristech-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ecole-des-ponts-paristech-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecole-des-ponts-paristech-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ecole-des-ponts-paristech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ecole-des-ponts-paristech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ecole-des-ponts-paristech-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'ENPC publishes no public API, no developer portal and no OpenAPI. Probed and found absent: api.enpc.fr, api.ecoledesponts.fr, data.enpc.fr, data.ecoledesponts.fr (all DNS-unresolvable), /llms.txt and /.well-known/security.txt on the main site (404). One institution-operated machine-readable contract exists and is recorded — the SAML 2.0 IdP metadata at idp.enpc.fr. Every other programmable surface belongs to a national or vendor platform on which ENPC is a tenant: HAL (CCSD), Recherche Data Gouv (Dataverse), and Gallica Marque Blanche (BnF), the last of which runs under an ENPC hostname that resolves into BnF address space. The previous profile recorded the generic national HAL endpoints at api.archives-ouvertes.fr as ENPC''s own APIs; they are shared national infrastructure used by every French institution and have been re-labelled as a single tenant relationship. Two soft-200 traps were found and are NOT recorded as surfaces: the heritage SRU route returns the HTML search page
    for every request including operation=explain, and idp.enpc.fr answers every unknown path, including /.well-known/openid-configuration, with the LemonLDAP::NG portal shell. The HAL portal enpc.hal.science answers 200 with an Anubis bot challenge — live, not dead. A dead pointer was removed: the previous Library pointer lib.enpc.fr now redirects off-domain to an unrelated research demo at aikon-demo.huma-num.fr, and the previous Twitter pointer 404s with no X account linked from the ENPC homepage.'
  evidence:
  - status: 200
    url: https://ecoledesponts.fr/
  - note: DNS does not resolve
    status: 0
    url: https://api.ecoledesponts.fr/
  - note: DNS does not resolve
    status: 0
    url: https://api.enpc.fr/
  - note: DNS does not resolve
    status: 0
    url: https://data.ecoledesponts.fr/
  - status: 404
    url: https://ecoledesponts.fr/llms.txt
  - status: 404
    url: https://ecoledesponts.fr/.well-known/security.txt
  - note: institution-operated SAML 2.0 EntityDescriptor, 18751 bytes
    status: 200
    url: https://idp.enpc.fr/saml/metadata
  - note: soft-200 — returns the LemonLDAP::NG portal HTML, not an OIDC document
    status: 200
    url: https://idp.enpc.fr/.well-known/openid-configuration
  - note: Anubis bot challenge body — live but bot-blocked
    status: 200
    url: https://enpc.hal.science/
  - note: soft-200 — 45KB HTML search page, not an SRU response
    status: 200
    url: https://heritage.ecoledesponts.fr/services/engine/search/sru?operation=explain&version=1.2
  - note: redirects off-domain to aikon-demo.huma-num.fr — dead as an ENPC pointer, removed
    status: 200
    url: https://lib.enpc.fr/
  - note: dead pointer, removed
    status: 404
    url: https://twitter.com/EcoledesPonts
  reason: no_public_api
  state: none
created: '2026-06-03'
description: 'École des Ponts ParisTech (École nationale des ponts et chaussées, ENPC) is a public French grande école of engineering founded in 1747, based in Champs-sur-Marne and a founding member of ParisTech. Its programmable footprint is small and must be read honestly: ENPC operates no public API programme, no developer portal and no API key issuance — api.enpc.fr and api.ecoledesponts.fr do not resolve, and there is no developer section anywhere in the 1,910-URL sitemap of ecoledesponts.fr. The single machine-readable contract ENPC genuinely operates itself is its SAML 2.0 Identity Provider metadata at idp.enpc.fr, whose entityID is registered in the RENATER Fédération Éducation-Recherche and therefore reachable through eduGAIN. Everything else that looks like an ENPC API is a tenant relationship on someone else''s platform: the open-access repository is the ENPC collection inside the national HAL platform operated by CCSD; the research-data repository is the ecoledesponts collection
  inside the national Recherche Data Gouv Dataverse; and the heritage digital library, though served under heritage.ecoledesponts.fr, is a Gallica Marque Blanche deployment hosted on BnF infrastructure with BnF ARKs and BnF attribution. Those are real institutional facts and are recorded as tenant surfaces — the data is ENPC''s, the contract is not.'
finops:
- name: Ecole Des Ponts Paristech Finops
  service_category: Education
  slug: ecole-des-ponts-paristech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecole-des-ponts-paristech.png
jsonld:
- class_count: 22
  name: Ecole Des Ponts Paristech Context
  property_count: 3
  slug: ecole-des-ponts-paristech-context
layout: provider
modified: '2026-08-30'
name: École des Ponts ParisTech
nav: Providers
network: true
overview: 'École des Ponts ParisTech publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Technical University, and Grande École.


  The École des Ponts ParisTech catalog on APIs.io includes 1 JSON-LD context.


  École des Ponts ParisTech''s developer surface includes documentation, engineering blog, YouTube channel, authentication, and 20 more developer resources.'
plans:
- name: Ecole Des Ponts Paristech Plans Pricing
  plan_count: 2
  slug: ecole-des-ponts-paristech-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Ecole Des Ponts Paristech Rate Limits
  slug: ecole-des-ponts-paristech-rate-limits
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 20.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 33.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecole-des-ponts-paristech/refs/heads/main/screenshots/ecole-des-ponts-paristech-2026-06-20T180431.png
security:
- kind: authentication
  name: Ecole Des Ponts Paristech Authentication
  slug: ecole-des-ponts-paristech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ecole Des Ponts Paristech Domain Security
  slug: ecole-des-ponts-paristech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecole-des-ponts-paristech
tags:
- University
- Higher Education
- Education
- Technical University
- Grande École
- Engineering
- France
- Research
- Open Access
- Research Data
- Identity Federation
- Digital Library
- OAI-PMH
- IIIF
- SAML
website: https://ecoledesponts.fr/
---
