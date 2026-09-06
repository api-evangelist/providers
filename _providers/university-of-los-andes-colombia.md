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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://revistas.uniandes.edu.co/index.php/index/oai
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata harvesting interface for the Revistas Uniandes scholarly journal portal — the only Universidad de los Andes surface found that serves an anonymous automated client real data. Veri
  name: Revistas Uniandes - OAI-PMH
  slug: revistas-oai
- description: The Open Journal Systems v1 REST API on the university's own journal host. Present and answering — /index.php/{journal}/api/v1/* returns a structured JSON 403 ({"error":"api.403.unauthorized"}) rather
  name: Revistas Uniandes - OJS REST API
  slug: revistas-rest
- description: Agora is the university's community and news site, running on its own host and serving a publicly readable WordPress REST API discovery document at /wp-json/ (HTTP 200, ~326KB of JSON naming every reg
  name: Agora Uniandes - WordPress REST API
  slug: agora-wp-rest
- description: OAI-PMH metadata harvesting interface for "Seneca", the DSpace 7 institutional repository that collects the university's open-access scholarly output. The host is the university's own. Re-probed 2026-
  name: Repositorio Institucional Seneca - OAI-PMH
  slug: repositorio-oai
- description: DSpace 7 REST API for the "Seneca" repository, under the /server/api path of the deployment. Confirmed to be DSpace 7 by the Angular entity URLs its DOIs resolve to. Re-probed 2026-09-01 under a brows
  name: Repositorio Institucional Seneca - DSpace REST API
  slug: repositorio-rest
- description: An undocumented API host on the university's own registrable domain. It resolves through Cloudflare and answers HTTP 403 with the Cloudflare WAF "Attention Required!" page on every path attempted — /,
  name: api.uniandes.edu.co
  slug: api-gateway
- description: The university's own SAML 2.0 and OpenID Connect identity provider, hosted as Microsoft Entra ID tenant fabd047c-ff48-492a-8bbb-8f98b9fb9cca. A federation is shared by definition, but the IdP behind i
  name: Universidad de los Andes Identity Provider (Microsoft Entra ID)
  slug: entra-identity-federation
- description: The university's digital heritage and rare-materials collection, on an institution-specific subdomain that CNAMEs to cdm22043.contentdm.oclc.org — an OCLC CONTENTdm tenancy, site 22043. The tenancy is
  name: Patrimonio Documental y Bibliografico - CONTENTdm
  slug: patrimonio-contentdm
- description: 'The university''s learning management system, "Bloque Neon", on an institution-specific subdomain that CNAMEs to uniandes.brightspace.com — a D2L Brightspace tenancy. Unauthenticated requests redirect '
  name: Bloque Neon - D2L Brightspace LMS
  slug: bloqueneon-brightspace
- description: DOI registration membership at Crossref. Member 11812, primary-name "Universidad de los Andes", location "Bogota, Colombia", with eight prefixes — 10.7440, 10.13043, 10.53010, 10.29263, 10.16924, 10.1
  name: Crossref Member 11812 - Universidad de los Andes
  slug: crossref-member
- description: DOI registration membership at DataCite. Consortium organization UDLAC, displayName "Universidad de los Andes - Colombia", operating two repository clients. IGJZ.MNJGJS — "Repositorios Digitales Unian
  name: DataCite Consortium Organization UDLAC - Universidad de los Andes Colombia
  slug: datacite-member
- description: Research Organization Registry record for the institution. ROR ID 02mhbdp94, established 1948, declared domain uniandes.edu.co, with cross-registry identifiers Funder Registry 501100006070, GRID grid.
  name: ROR 02mhbdp94 - Universidad de los Andes
  slug: ror-record
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.uniandes.edu.co/
- group: company
  title: ''
  type: LinkedIn
  url: https://co.linkedin.com/school/universidad-de-los-andes/
- group: company
  title: ''
  type: Blog
  url: https://agora.uniandes.edu.co/
- group: company
  title: ''
  type: BlogRSS
  url: https://agora.uniandes.edu.co/feed/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://biblioteca.uniandes.edu.co/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositorio.uniandes.edu.co/
- group: other
  title: ''
  type: ResearchRepository
  url: https://revistas.uniandes.edu.co/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.microsoftonline.com/uniandes.edu.co/v2.0/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-los-andes-colombia-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-los-andes-colombia-conformance.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-los-andes-colombia-revistas-oai-pmh-openapi.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-los-andes-colombia-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-los-andes-colombia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-los-andes-colombia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-los-andes-colombia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Universidad de los Andes operates no public developer portal, no API key programme and no OpenAPI of its own, and this profile does not pad that absence. Real probing found one anonymously readable institution-operated surface — the Revistas Uniandes OAI-PMH 2.0 endpoint, live across all six verbs — plus a WordPress REST discovery document on the Agora news host. Everything else the institution runs on its own domain is closed to automated clients rather than absent: the DSpace 7 "Seneca" repository returns a bot-detection challenge and 403 on both its OAI and REST paths even under a browser User-Agent, api.uniandes.edu.co answers with a Cloudflare WAF block on every path tried, and the OJS REST API returns a structured 403 needing an editor-issued token. Coverage is therefore gated by bot mitigation on the institution''s own infrastructure, not by the institution publishing nothing. Two further notes on the state of the estate at review time: the main website www.uniandes.edu.co
    and every path under it redirect to mantenimiento.uniandes.edu.co, a branded maintenance page, on three consecutive attempts — the Website pointer is retained because it is the canonical institutional domain serving the institution''s own page, but the site itself was not serving content; and the news feed previously harvested from www.uniandes.edu.co/es/noticias is dead for the same reason, which is why the Blog pointer has been moved to agora.uniandes.edu.co, whose RSS feed is live. Beyond the institution''s own hosts the footprint is relationships: an Entra ID tenant that is the university''s own SAML/OIDC identity provider, Crossref and DataCite DOI registrations, a ROR record, an OCLC CONTENTdm tenancy and a D2L Brightspace tenancy. Those are recorded with x-operator federation, registry and tenant; none of those vendors'' or registries'' contracts are saved under this institution. No searched-and-not-found surface has been invented: DNS for idp/shibboleth/sso/auth/datos/datosabiertos/developer/hpc/cris/scienti
    under uniandes.edu.co is NXDOMAIN, cursos and horario return 404, adfs and exacore resolve but filter TCP 80/443 from the public internet, and the github.com/uniandes organization has zero public repositories.'
  evidence:
  - status: 200
    url: https://revistas.uniandes.edu.co/index.php/index/oai?verb=Identify
  - status: 200
    url: https://revistas.uniandes.edu.co/index.php/index/oai?verb=ListRecords&metadataPrefix=oai_dc
  - status: 200
    url: https://revistas.uniandes.edu.co/index.php/index/oai?verb=ListSets
  - status: 403
    url: https://revistas.uniandes.edu.co/index.php/index/api/v1/contexts
  - status: 200
    url: https://agora.uniandes.edu.co/wp-json/
  - status: 200
    url: https://agora.uniandes.edu.co/feed/
  - status: 403
    url: https://repositorio.uniandes.edu.co/oai/request?verb=Identify
  - status: 403
    url: https://repositorio.uniandes.edu.co/server/api
  - status: 403
    url: https://api.uniandes.edu.co/
  - status: 403
    url: https://api.uniandes.edu.co/openapi.json
  - status: 200
    url: https://www.uniandes.edu.co/
  - status: 200
    url: https://login.microsoftonline.com/fabd047c-ff48-492a-8bbb-8f98b9fb9cca/federationmetadata/2007-06/federationmetadata.xml
  - status: 200
    url: https://login.microsoftonline.com/uniandes.edu.co/v2.0/.well-known/openid-configuration
  - status: 200
    url: https://patrimoniodocumental.uniandes.edu.co/oai/oai.php?verb=Identify
  - status: 200
    url: https://patrimoniodocumental.uniandes.edu.co/digital/api/collections
  - status: 200
    url: https://bloqueneon.uniandes.edu.co/
  - status: 200
    url: https://api.crossref.org/members/11812
  - status: 200
    url: https://api.datacite.org/providers/udlac
  - status: 200
    url: https://api.ror.org/organizations?query=Universidad%20de%20los%20Andes%20Colombia
  - status: 200
    url: https://biblioteca.uniandes.edu.co/
  - status: 404
    url: https://cursos.uniandes.edu.co/
  - status: 200
    url: https://api.github.com/orgs/uniandes
  reason: bot_blocked
  state: gated
created: '2026-06-03'
description: 'Universidad de los Andes (Uniandes) is a private research university in Bogota, Colombia, founded in 1948 and ranked #179 in the QS World University Rankings 2025. Like most universities it is a federation of buyers rather than a producer of APIs: it publishes no developer portal, no API key programme, no OpenAPI of its own and no public API documentation of any kind. What it does operate, on its own registrable domain, is one genuinely public machine-readable surface — an OAI-PMH 2.0 metadata harvesting endpoint for the Revistas Uniandes journal portal, which answers anonymous automated clients across all six protocol verbs and serves the university''s own journals. Its second institutional repository, the DSpace 7 deployment "Seneca", sits behind a bot-detection challenge that returns 403 to automated clients; an undocumented host at api.uniandes.edu.co exists but is closed by a Cloudflare WAF on every path. Beyond that, the university''s programmable footprint is relationships
  rather than engineering: a Microsoft Entra ID tenant that is its own SAML 2.0 and OpenID Connect identity provider, DOI registrations at both Crossref and DataCite, a ROR record, an OCLC CONTENTdm heritage collection and a D2L Brightspace LMS. Those are real institutional facts and are catalogued here as such, each carrying an x-operator that says who actually runs the thing — none of the vendors'' contracts are attributed to Uniandes.'
finops:
- name: University Of Los Andes Colombia Finops
  service_category: Education
  slug: university-of-los-andes-colombia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-los-andes-colombia.png
jsonld:
- class_count: 12
  name: University Of Los Andes Colombia Context
  property_count: 7
  slug: university-of-los-andes-colombia-context
layout: provider
modified: '2026-09-01'
name: University of Los Andes Colombia
nav: Providers
network: true
overview: 'University of Los Andes Colombia publishes 1 API on the [APIs.io](https://apis.io/) network: Revistas Uniandes - OAI-PMH. Tagged areas include University, Higher Education, Education, Colombia, and Latin America.


  The University of Los Andes Colombia catalog on APIs.io includes 1 JSON-LD context.


  University of Los Andes Colombia''s developer surface includes engineering blog, authentication, and 14 more developer resources.'
plans:
- name: University Of Los Andes Colombia Plans Pricing
  plan_count: 2
  slug: university-of-los-andes-colombia-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of Los Andes Colombia Rate Limits
  slug: university-of-los-andes-colombia-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 57.9
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 36.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-los-andes-colombia/refs/heads/main/screenshots/university-of-los-andes-colombia-2026-06-20T200202.png
security:
- kind: authentication
  name: University Of Los Andes Colombia Authentication
  slug: university-of-los-andes-colombia-authentication
  summary_line: openIdConnect/saml2/none · 3 schemes
- kind: domain-security
  name: University Of Los Andes Colombia Domain Security
  slug: university-of-los-andes-colombia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-los-andes-colombia
tags:
- University
- Higher Education
- Education
- Colombia
- Latin America
- Private Research University
- Open Access
- Institutional Repository
- Research Data
- Scholarly Publishing
- OAI-PMH
- Identity Federation
- Library
- Research
website: https://www.uniandes.edu.co/
---
