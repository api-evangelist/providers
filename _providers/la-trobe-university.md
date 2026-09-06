---
access_model:
  confidence: high
  label: Not publicly available
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
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
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: 'La Trobe''s own API gateway, an Azure API Management instance published at api.latrobe.edu.au (CNAME ltu-api-prod-apim.developer.azure-api.net). It is not a public developer product: every path returns'
  name: La Trobe API Gateway (Gated)
  slug: api-gateway
- description: OPAL is La Trobe's open-access research repository — its publications, theses, datasets and DOIs — deployed as an institutional tenancy on Figshare. opal.latrobe.edu.au is a CNAME to figshare.com, and
  name: OPAL (Open @ La Trobe) Research Repository
  slug: opal-figshare-repository
- description: La Trobe's SAML 2.0 identity provider in the Australian Access Federation, and through AAF in eduGAIN. The entity is La Trobe's — entityID https://aaf.latrobe.edu.au/idp/shibboleth, shibmd:Scope latro
  name: La Trobe Shibboleth Identity Provider (AAF)
  slug: aaf-shibboleth-idp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.latrobe.edu.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/la-trobe-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/latrobe
- group: other
  title: ''
  type: ResearchRepository
  url: https://opal.latrobe.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://handbook.latrobe.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://latrobe.primo.exlibrisgroup.com/discovery/search?vid=61LATROBE_INST:LATROBE
- group: other
  title: ''
  type: IdentityFederation
  url: https://aaf.latrobe.edu.au/idp/shibboleth
- group: design
  title: ''
  type: Conformance
  url: conformance/la-trobe-university-conformance.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/la-trobe-university-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/la-trobe-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/la-trobe-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/la-trobe-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/la-trobe-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-08-30'
  detail: 'La Trobe University publishes no institution-authored API contract. The one API host on its own registrable domain, api.latrobe.edu.au, is an Azure API Management developer portal whose every path — /apis, /developer, /.well-known/openid-configuration — redirects to /signin, so the catalogue behind it is not externally observable. developer.latrobe.edu.au and data.latrobe.edu.au do not resolve. There is no CKAN or Socrata open-data portal and no institution-hosted OAI-PMH responder (opal.latrobe.edu.au/oai answers HTTP 202 with an empty body). The remaining machine-readable surfaces are tenancies — Figshare, CourseLoop, Ex Libris and an AAF-managed Shibboleth IdP — and are recorded as such, with x-operator on each entry, rather than credited to La Trobe as its own engineering. A secondary condition worth noting for future runs: every www/library/policy page on latrobe.edu.au sits behind a Cloudflare managed challenge and answers 403 to any non-browser client, including /robots.txt,
    /llms.txt and /.well-known/security.txt, so no institutional policy or terms pointer could be verified and none is claimed here.'
  evidence:
  - status: 200
    url: https://api.latrobe.edu.au/
  - status: 200
    url: https://api.latrobe.edu.au/apis
  - status: 0
    url: https://developer.latrobe.edu.au/
  - status: 0
    url: https://data.latrobe.edu.au/
  - status: 202
    url: https://opal.latrobe.edu.au/oai?verb=Identify
  - status: 200
    url: https://aaf.latrobe.edu.au/idp/shibboleth
  - status: 200
    url: https://handbook.latrobe.edu.au/
  - status: 403
    url: https://cf-api-ap-southeast-2.prod.courseloop.com/publisher/search-all?siteId=ltu-prod-pres
  - status: 403
    url: https://www.latrobe.edu.au/
  - status: 403
    url: https://www.latrobe.edu.au/llms.txt
  - status: 403
    url: https://www.latrobe.edu.au/.well-known/security.txt
  reason: no_public_api
  state: gated
created: '2026-06-03'
description: 'La Trobe University is a public research university headquartered in Bundoora, Melbourne, Victoria, Australia, founded in 1964 and ranked #217 in the QS World University Rankings 2025. La Trobe operates no public, self-service API product and publishes no OpenAPI, AsyncAPI or GraphQL description of its own. Its single institution-operated API host, api.latrobe.edu.au, is an Azure API Management developer portal (CNAME ltu-api-prod-apim.developer.azure-api.net) that redirects every unauthenticated path to /signin, with no public catalogue, documentation or sign-up. Everything else that looks programmable under the La Trobe name is a vendor platform running under an institutional tenancy: the open-access repository OPAL (opal.latrobe.edu.au, CNAME figshare.com) and its alias researchdata.latrobe.edu.au are Figshare; the course handbook (handbook.latrobe.edu.au) is CourseLoop, whose backend at cf-api-ap-southeast-2.prod.courseloop.com refuses unauthenticated calls; library discovery
  and resource management are Ex Libris Primo and Alma; the Shibboleth identity provider at aaf.latrobe.edu.au is operated by the Australian Access Federation under La Trobe''s own domain, entityID and scope. What La Trobe genuinely holds in its own name is registry identity — a DataCite membership with the DOI prefix 10.26181 over 47,824 DOIs, Crossref member 11371, ROR 01rxfrp27, and the AAF/eduGAIN SAML entity that federates its staff and students. That is the honest footprint: institutional identity and stewardship, not institutional engineering.'
finops:
- name: La Trobe University Finops
  service_category: Education
  slug: la-trobe-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/la-trobe-university.png
jsonld:
- class_count: 15
  name: La Trobe University Context
  property_count: 6
  slug: la-trobe-university-context
layout: provider
modified: '2026-08-30'
name: La Trobe University
nav: Providers
network: true
overview: 'La Trobe University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Australia, and Victoria.


  The La Trobe University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: La Trobe University Plans Pricing
  plan_count: 2
  slug: la-trobe-university-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: La Trobe University Rate Limits
  slug: la-trobe-university-rate-limits
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 19.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/la-trobe-university/refs/heads/main/screenshots/la-trobe-university-2026-06-20T184236.png
security:
- kind: domain-security
  name: La Trobe University Domain Security
  slug: la-trobe-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: la-trobe-university
tags:
- Education
- Higher Education
- University
- Australia
- Victoria
- Research
- Research Repository
- Course Catalog
- Identity Federation
- Library
- Open Access
website: https://www.latrobe.edu.au/
---
