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
  scored_at: '2026-09-01'
api_count: 8
apis:
- description: 'ENS de Lyon self-hosts its Shibboleth Identity Provider on its own registrable domain. The entityID is https://idp.ens-lyon.fr/idp/shibboleth, the asserted scope is ens-lyon.fr, the technical contact '
  name: ENS de Lyon Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
- description: ENS de Lyon's Identity Provider as registered by RENATER, France's national research and education network, in the Fédération Éducation-Recherche and exported to eduGAIN. The per-entity MDQ endpoint r
  name: RENATER Fédération Éducation-Recherche entity (ENS de Lyon IdP)
  slug: renater-fer-entity
- description: 'The Entra ID tenant behind ens-lyon.fr accounts, resolved from the domain hint: c30cf67d-aee4-44f6-8f1b-12f4935b7d2c, region scope EU. OIDC discovery and SAML federation metadata both answer unauthent'
  name: ENS de Lyon Microsoft Entra ID tenant (OIDC + SAML metadata)
  slug: entra-id-tenant
- description: Apereo CAS service running on ENS de Lyon's own host cas.ens-lyon.fr (140.77.51.3). The CAS 3.0 validation endpoint /cas/p3/serviceValidate answers unauthenticated with a well-formed cas:serviceRespon
  name: ENS de Lyon CAS single sign-on (Apereo CAS 3.0 protocol)
  slug: cas-sso
- description: OAI-PMH 2.0 harvesting endpoint scoped to ENS de Lyon's named collection on HAL, the French national open archive operated by CCSD (CNRS). The Identify response names the repository as HAL, the reposi
  name: HAL OAI-PMH — ens-lyon collection
  slug: hal-oai-pmh
- description: HAL's Solr-backed search API scoped to the ENS de Lyon collection. A probe of /search/ens-lyon/?q=*:*&wt=json returned numFound 106,836 on 2026-09-01, which is the size of ENS de Lyon's deposited scho
  name: HAL Search API — ens-lyon collection
  slug: hal-search
- description: ENS de Lyon's record in the Research Organization Registry, https://ror.org/04zmssz18, typed education and funder, carrying ISNI 0000 0001 2175 9188, GRID grid.15140.31, Wikidata Q10159 and Crossref F
  name: ROR registry record (04zmssz18)
  slug: ror-record
- description: 'ENS de Lyon is registered in the Crossref Open Funder Registry as https://doi.org/10.13039/501100018692, name "École Normale Supérieure de Lyon", location France. This is a funder registration, not a '
  name: Crossref Funder Registry entry (501100018692)
  slug: crossref-funder
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.ens-lyon.fr/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ens-lyon.fr/acces/mentions-legales
- group: operate
  title: ''
  type: Support
  url: https://www.ens-lyon.fr/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://fr.linkedin.com/school/ens-lyon/
- group: other
  title: ''
  type: IdentityFederation
  url: https://services.renater.fr/federation/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ens-lyon.hal.science
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.ens-lyon.fr/PSMN/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ens-lyon-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ens-lyon-domain-standards.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ens-lyon-domain-security.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ens-lyon-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/ens-lyon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ens-lyon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ens-lyon-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'ENS de Lyon publishes no institution-operated public API and no developer portal. A DNS sweep of the obvious candidates under ens-lyon.fr (api, apis, data, opendata, developer, courses, cours, sis, webservices, graphql, hpc, mesocentre, moodle, bibliotheque, catalogue) resolved only ldap, intranet, cas and idp — three of which are internal or authentication-only. www.ens-lyon.fr returns 404 for llms.txt, sitemap.xml, .well-known/security.txt and .well-known/openid-configuration, and serves a 77KB soft-404 body, so status codes were read rather than page presence. Everything reachable WAS read: the Shibboleth IdP metadata (application/xml, 12,129 bytes), the RENATER Fédération Éducation-Recherche MDQ entity for that entityID in both the fer and edugain namespaces, the RENATER IdP aggregate (344 entities, ENS de Lyon present), the Entra ID OIDC discovery document and its SAML federation metadata, the CAS 3.0 serviceValidate response, the HAL OAI-PMH Identify response for the ens-lyon
    set, the HAL Solr search endpoint scoped to the ens-lyon collection (106,836 records), and the ROR and Crossref Funder Registry records. Two surfaces are live but not machine-callable: the HAL institutional portal ens-lyon.hal.science and books.openedition.org both return a 200 carrying an Anubis bot-mitigation challenge rather than content. The github.com/ENS-Lyon organisation that the June 2026 profile pointed at has zero public repositories, no name, no URL and no verified domain, so it cannot be attributed to the institution and the pointer has been removed. No public AI policy or AI-tooling statement was found on the French or English surface. The profile is thin because the institution is thin, not because we could not read it.'
  evidence:
  - status: 200
    url: https://idp.ens-lyon.fr/idp/shibboleth
  - status: 200
    url: https://mdq.federation.renater.fr/fer/entities/https%3A%2F%2Fidp.ens-lyon.fr%2Fidp%2Fshibboleth
  - status: 200
    url: https://mdq.federation.renater.fr/edugain/entities/https%3A%2F%2Fidp.ens-lyon.fr%2Fidp%2Fshibboleth
  - status: 200
    url: https://metadata.federation.renater.fr/renater/main/main-idps-renater-metadata.xml
  - status: 200
    url: https://login.microsoftonline.com/ens-lyon.fr/v2.0/.well-known/openid-configuration
  - status: 200
    url: https://cas.ens-lyon.fr/cas/p3/serviceValidate
  - status: 200
    url: https://api.archives-ouvertes.fr/oai/ens-lyon?verb=Identify
  - status: 200
    url: https://api.archives-ouvertes.fr/search/ens-lyon/?q=*:*&rows=0&wt=json
  - status: 200
    url: https://ens-lyon.hal.science/
  - status: 200
    url: https://api.ror.org/v2/organizations/04zmssz18
  - status: 200
    url: https://api.crossref.org/funders/501100018692
  - status: 200
    url: https://api.datacite.org/clients?query=ens-lyon
  - status: 404
    url: https://www.ens-lyon.fr/llms.txt
  - status: 404
    url: https://www.ens-lyon.fr/.well-known/security.txt
  - status: 0
    url: https://api.ens-lyon.fr/
  - status: 0
    url: https://data.ens-lyon.fr/
  reason: no_public_api
  state: gated
created: '2026-06-03'
description: 'École Normale Supérieure de Lyon (ENS de Lyon) is a French public grande école and research university, one of the four Écoles normales supérieures, ranked #187 in the QS World University Rankings 2025. It operates no public developer portal, publishes no OpenAPI, issues no API keys and runs no documented open-API programme — api.ens-lyon.fr, data.ens-lyon.fr and developer.ens-lyon.fr do not resolve — and this profile says so rather than padding the gap. What ENS de Lyon does operate, and what is recorded here, is standards-based identity and scholarly infrastructure. It self-hosts a Shibboleth Identity Provider on its own domain (idp.ens-lyon.fr, scope ens-lyon.fr, on the school''s own 140.77.0.0/16 allocation), registered by RENATER in the Fédération Éducation-Recherche, carrying the REFEDS Research & Scholarship entity category and exported to eduGAIN; it runs an Apereo CAS single sign-on service at cas.ens-lyon.fr that answers the CAS 3.0 protocol; and it holds a Microsoft
  Entra ID tenant with live OIDC discovery. Its research output is machine-readable only as the ens-lyon collection on HAL, the national open archive operated by CCSD/CNRS — 106,836 records, harvestable over OAI-PMH and Solr search at api.archives-ouvertes.fr. That data is ENS de Lyon''s; the platform, the contract and the admin contact (contact@archives-ouvertes.fr) are HAL''s, so those surfaces are recorded as tenancies and HAL''s generic reference and SWORD APIs are deliberately not claimed here. The school is registered in ROR and in the Crossref Funder Registry; it holds no DataCite membership and no Crossref depositor membership of its own.'
finops:
- name: Ens Lyon Finops
  service_category: Education
  slug: ens-lyon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ens-lyon.png
jsonld:
- class_count: 15
  name: Ens Lyon Context
  property_count: 6
  slug: ens-lyon-context
layout: provider
modified: '2026-09-01'
name: École Normale Supérieure de Lyon
nav: Providers
network: true
overview: 'École Normale Supérieure de Lyon publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, France, and Grande École.


  The École Normale Supérieure de Lyon catalog on APIs.io includes 1 JSON-LD context.


  École Normale Supérieure de Lyon''s developer surface includes support, authentication, and 13 more developer resources.'
plans:
- name: Ens Lyon Plans Pricing
  plan_count: 2
  slug: ens-lyon-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Ens Lyon Rate Limits
  slug: ens-lyon-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ens-lyon/refs/heads/main/screenshots/ens-lyon-2026-06-20T180729.png
security:
- kind: authentication
  name: Ens Lyon Authentication
  slug: ens-lyon-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ens Lyon Domain Security
  slug: ens-lyon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ens-lyon
tags:
- University
- Higher Education
- Education
- France
- Grande École
- Identity Federation
- Shibboleth
- SAML
- Research Repository
- Open Access
- OAI-PMH
- Research Computing
website: https://www.ens-lyon.fr/
---
