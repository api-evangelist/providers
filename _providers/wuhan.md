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
api_count: 8
apis:
- description: WHU's federated login, published as a SAML 2.0 EntityDescriptor at https://idp.whu.edu.cn/idp/shibboleth (HTTP 200, application/xml, 14,864 bytes). Declares HTTP-Redirect, HTTP-POST and POST-SimpleSig
  name: Wuhan University Shibboleth Identity Provider (SAML 2.0)
  slug: shibboleth-idp
- description: The campus authentication server at cas.whu.edu.cn/authserver, which every institutional application redirects into, running the Wisedu CAS distribution. It publishes an OpenID Connect discovery docum
  name: Wuhan University Campus Single Sign-On (CAS / OpenID Connect / SAML)
  slug: cas-sso
- description: 'One of the International GNSS Service''s Global Data Centers, operated by Wuhan University''s GNSS Research Center. The archive is anonymously listable over FTP at ftp://igs.gnsswhu.cn/pub/ and carries '
  name: IGS Data Center at Wuhan University (GNSS archive)
  slug: igs-data-center
- description: Wuhan University is a registered identity provider in CARSI, China's national research-and-education identity federation, operated from Peking University and a production eduGAIN member since 2019-06-
  name: CARSI membership (CERNET Authentication and Resource Sharing Infrastructure)
  slug: carsi
- description: Wuhan University is registered in ROR as https://ror.org/033vjfk17 (active, established 1893), cross-walked to GRID grid.49470.3e, ISNI 0000 0001 2331 6153, Wikidata Q1108197 and three Crossref Open F
  name: ROR registry entry (Research Organization Registry)
  slug: ror
- description: The library's online public access catalog at opac.lib.whu.edu.cn, running Ex Libris Aleph — the root document is Aleph's own session bootstrap ("Aleph main menu", redirecting to /F?RN=) on 202.114.65
  name: Wuhan University Library catalog (Ex Libris Aleph tenant)
  slug: opac
- description: The institutional teaching-administration and course-registration system. jwgl.whu.edu.cn is live and redirects unauthenticated callers to https://cas.whu.edu.cn/authserver/login?service=https%3A%2F%2
  name: Wuhan University academic affairs / registrar system (SSO-gated)
  slug: jwgl
- description: WHU's own journal publishing platform at ch.whu.edu.cn (115.156.123.29, WHR-CERNET), hosting 武汉大学学报·信息科学版 / Geomatics and Information Science of Wuhan University. Live and institution-operated, but it
  name: Geomatics and Information Science of Wuhan University (journal platform)
  slug: journal-platform
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wuhan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.whu.edu.cn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WHUIR
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/wuhan-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/WHU_1893
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.whu.edu.cn/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opac.lib.whu.edu.cn/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://jwgl.whu.edu.cn/
- group: other
  title: ''
  type: OpenData
  url: ftp://igs.gnsswhu.cn/pub/
- group: auth
  title: ''
  type: Authentication
  url: authentication/wuhan-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/wuhan-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wuhan-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wuhan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wuhan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wuhan-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Wuhan University publishes no public API, no developer portal and no contract of any kind, and that is the honest result rather than a wall we hit. api., data., open., developer., dspace., repository. and library. under whu.edu.cn return no DNS answer; /.well-known/apis.json, /.well-known/security.txt, /llms.txt, /robots.txt and /sitemap.xml are 404 on both www.whu.edu.cn and en.whu.edu.cn; and no OpenAPI, AsyncAPI, GraphQL SDL or Postman collection was located anywhere, so none has been saved and none has been derived.

    Four institution-operated surfaces WERE confirmed live, all on CERNET address space allocated to the Wuhan region or attributed by a standards body, and all are recorded above: the Shibboleth SAML 2.0 identity provider at idp.whu.edu.cn, registered in CARSI since 2024-12-10; the campus CAS/OIDC/SAML single-sign-on server at cas.whu.edu.cn, whose OpenID Connect discovery document is the only conforming machine-readable contract WHU serves the public; the IGS Global Data Center at ftp://igs.gnsswhu.cn/pub/, which the International GNSS Service''s own data-access page attributes to Wuhan University; and the journal platform at ch.whu.edu.cn. None of the four publishes an API specification. The IdP''s self-published metadata is Shibboleth''s shipped template, expired in 2019, and namespace-ill-formed (undeclared md: prefix at lines 131-133, so namespace-aware parsers fail with "unbound prefix") — the service conforms, the document describing it does not.

    Library discovery is an Ex Libris Aleph tenancy and is recorded as a tenant relationship, not as a WHU contract. The registrar system jwgl.whu.edu.cn is real and institution-operated but sits behind campus SSO. One host, ir.whu.edu.cn, returns 403 from an openresty edge on every path and every user-agent tried, so it is unreadable from outside China and is deliberately NOT characterized here — a 403 with no body is not evidence of an institutional repository.

    Language was not the barrier: the Chinese-language estate was searched alongside the English one, and the only English-only gap found is the reverse — the CAS protocol errors are emitted in Chinese only.'
  evidence:
  - status: 200
    url: https://en.whu.edu.cn/
  - status: 200
    url: https://www.whu.edu.cn/
  - status: 404
    url: https://en.whu.edu.cn/.well-known/apis.json
  - status: 404
    url: https://en.whu.edu.cn/llms.txt
  - status: 404
    url: https://www.whu.edu.cn/sitemap.xml
  - status: 200
    url: https://idp.whu.edu.cn/idp/shibboleth
  - status: 400
    url: https://idp.whu.edu.cn/idp/profile/SAML2/Redirect/SSO
  - status: 200
    url: https://cas.whu.edu.cn/authserver/oidc/.well-known/openid-configuration
  - status: 200
    url: https://cas.whu.edu.cn/authserver/idp/metadata
  - status: 200
    url: https://cas.whu.edu.cn/authserver/serviceValidate
  - status: 200
    url: https://www.carsi.edu.cn/IdPlist.html
  - status: 200
    url: https://igs.org/data-access/
  - status: 226
    url: ftp://igs.gnsswhu.cn/pub/
  - status: 200
    url: https://opac.lib.whu.edu.cn/
  - status: 200
    url: https://jwgl.whu.edu.cn/
  - status: 200
    url: https://ch.whu.edu.cn/oai?verb=Identify
  - status: 403
    url: https://ir.whu.edu.cn/
  - status: 200
    url: https://api.datacite.org/clients?query=Wuhan%20University
  - status: 200
    url: https://api.ror.org/v2/organizations/033vjfk17
  reason: no_public_api
  state: none
created: '2026-06-03'
description: 'Wuhan University (武汉大学, WHU), founded in 1893 in Wuhan, Hubei, is a comprehensive public research university under China''s Ministry of Education, a Double First-Class and former Project 985 institution, and is strongest in surveying, remote sensing, geoinformatics and GNSS. It operates no public developer portal, no open data portal and no documented public API: api., data., open. and developer. under whu.edu.cn do not resolve, /.well-known/apis.json, llms.txt, security.txt, robots.txt and sitemap.xml all return 404 on both the Chinese and English sites, and no OpenAPI, AsyncAPI or GraphQL contract exists anywhere in this profile. What it does operate, on its own CERNET address space, is an identity estate and a bulk research-data archive. Wuhan University runs a Shibboleth SAML 2.0 identity provider registered in CARSI, China''s national research-and-education federation and a production eduGAIN member, and a campus CAS single-sign-on server that publishes a live OpenID Connect
  discovery document — the only conforming, self-describing, machine-readable contract WHU serves to the anonymous public, and it is the SSO product''s shape rather than WHU engineering. It also operates one of the IGS Global Data Centers: the International GNSS Service''s own data-access page names Wuhan University and links ftp://igs.gnsswhu.cn/, an anonymously listable archive of GPS, BDS, MGEX, high-rate and IERS products. Library discovery is an Ex Libris Aleph tenancy on a WHU host, and the registrar system is behind campus SSO. The institution''s only evidenced education-regime conformance is SAML and Shibboleth; it is not a DataCite or Crossref depositing member, and no institution-operated OAI-PMH endpoint was found.'
finops:
- name: Wuhan Finops
  service_category: Education
  slug: wuhan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wuhan.png
jsonld:
- class_count: 11
  name: Wuhan Context
  property_count: 1
  slug: wuhan-context
layout: provider
modified: '2026-09-01'
name: Wuhan University
nav: Providers
network: true
overview: 'Wuhan University publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The Wuhan University catalog on APIs.io includes 1 JSON-LD context.


  Wuhan University''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Wuhan Plans Pricing
  plan_count: 2
  slug: wuhan-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Wuhan Rate Limits
  slug: wuhan-rate-limits
scopes:
- name: Wuhan Scopes
  scope_count: 0
  slug: wuhan-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 27.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wuhan/refs/heads/main/screenshots/wuhan-2026-06-20T201647.png
security:
- kind: authentication
  name: Wuhan Authentication
  slug: wuhan-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Wuhan Domain Security
  slug: wuhan-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wuhan
tags:
- Education
- Higher Education
- University
- Research
- China
- Identity Federation
- Single Sign-On
- Research Data
- GNSS
- Library
- Open-Source
website: https://en.whu.edu.cn
---
