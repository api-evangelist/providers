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
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: Sungkyunkwan University's institutional identity provider, publishing machine-readable SAML 2.0 metadata through the KAFE (Korea Access Federation) aggregate and interfederated internationally through
  name: SKKU SAML 2.0 Identity Provider (KAFE / eduGAIN metadata)
  slug: identity-federation
- description: 'SKKU''s research information system and public researcher/output profiles, running on Elsevier Pure at pure.skku.edu. This is a genuine institutional fact and one of the very few programmable research '
  name: SKKU Research Portal (Elsevier Pure) — TENANT
  slug: pure-research-portal
- description: 'SKKU''s electronic theses and dissertations repository, running on dCollection, the national academic-information distribution platform operated for Korean universities. The collection and its records '
  name: SKKU dCollection Thesis Repository (KERIS) — TENANT
  slug: dcollection-repository
- description: Two Sungkyunkwan University units are Crossref members in their own right and register DOIs under their own prefixes — member 9930, Sungkyunkwan University School of Medicine, prefix 10.23838; and mem
  name: SKKU Crossref Membership (DOI registration)
  slug: crossref-membership
- description: Sungkyunkwan University is registered in the Research Organization Registry as https://ror.org/04q78tk20, with registrable domain skku.edu, established 1398, located in Suwon, Gyeonggi-do, KR, and cro
  name: SKKU ROR Registration (organization identifier)
  slug: ror-registration
- description: Kingo Portal is SKKU's single sign-on environment, the front door to the university's own online services — Google Workspace, GLS, iCampus (icampus.skku.edu, a Laravel learning system on SKKU's domain
  name: Kingo Portal (campus SSO and gated student systems)
  slug: kingo-portal
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.skku.edu/eng/
- group: docs
  title: ''
  type: Documentation
  url: https://www.skku.edu/eng/CampusLife/ITServices/KingoPortal1_1.do
- group: operate
  title: ''
  type: Support
  url: https://www.skku.edu/eng/CampusLife/ITServices/ITCallCenter.do
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skku.edu/skku/etc/private.do
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skku.edu/skku/etc/netizen.do
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/%EC%84%B1%EA%B7%A0%EA%B4%80%EB%8C%80%ED%95%99%EA%B5%90/
- group: other
  title: ''
  type: IdentityFederation
  url: https://technical.edugain.org/api.php?action=show_entity&entityid=https%3A%2F%2Fkafe.skku.edu%2Fidp%2Fsimplesamlphp
- group: other
  title: ''
  type: ResearchRepository
  url: https://pure.skku.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.skku.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://sugang.skku.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://chatgpt.skku.edu/chatgpt/index.do
- group: build
  title: ''
  type: AITooling
  url: https://ctl.skku.edu/ctl/index.do
- group: build
  title: ''
  type: Examples
  url: examples/skku-idp-saml-entity-descriptor-example.xml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skku-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skku-conformance.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/skku-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skku-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/skku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Re-profiled 2026-09-01 under the university pipeline, with the operator axis settled before anything was saved. Sungkyunkwan University publishes no public, documented developer API and no open-data portal, and that absence was established by negative probe rather than assumed: api.skku.edu, developer.skku.edu, data.skku.edu, open.skku.edu, research.skku.edu, repository.skku.edu, dspace.skku.edu, scholarworks.skku.edu, hpc.skku.edu and status.skku.edu all fail to resolve, and www.skku.edu returns 404 for llms.txt, .well-known/security.txt and .well-known/openid-configuration. Every consumable system SKKU runs is behind enrolment authentication — Kingo Portal SSO, iCampus, sugang.skku.edu course registration, the library discovery layer — which is why the state is `gated` rather than `none`: real surfaces exist, and none of them is reachable without credentials. The two exceptions were probed and are recorded: the SAML 2.0 identity provider metadata for kafe.skku.edu, which is
    public and machine-readable through the eduGAIN aggregate, and the OAI-PMH 2.0 provider at pure.skku.edu, which is public and unauthenticated but is an Elsevier Pure tenancy and is credited as such, not as SKKU engineering. The Pure Web Service itself (pure.skku.edu/ws/api) returns 401 and its documentation canonicalises to api.elsevierpure.com, so even the tenant has no publicly reachable programmable interface there. Deliberate exclusions, each with a reason: github.com/GDG-SKKU is a Google Developer Group student chapter publishing student project code, not SKKU''s engineering, so the previous profile''s institutional GitHub pointer has been removed rather than re-credited; github.com/skku exists but holds zero repositories and carries no name, description or website, so it is not evidence of an institutional presence; skku.dcollection.net is a KERIS dCollection tenancy whose robots.txt disallows all crawling and whose /oai, /srv/oai and /oai/request paths return the site''s HTML
    shell with HTTP 200 rather than an OAI-PMH response, so it is recorded as a relationship and explicitly not as a harvesting surface; no ORCID institutional membership was found, and the 7,574 public ORCID records naming SKKU as an affiliation are a fact about researchers, not a membership. Language was a real factor and was worked around rather than reported as a barrier: the AI guidance site, the privacy policy, the netizen ethics code and course registration exist only on the Korean surface and were probed there. No specification was saved for any surface in this repository, because SKKU operates no contract of its own and every contract that touches it belongs to a vendor.'
  evidence:
  - note: SAML 2.0 md:EntityDescriptor for entityID https://kafe.skku.edu/idp/simplesamlphp, 9,390 bytes. registrationAuthority http://kafe.kreonet.net (KAFE), registered 2022-09-26, shibmd:Scope skku.edu, REFEDS R&S supported, Sirtfi asserted. INSTITUTION-OPERATED.
    status: 200
    url: https://technical.edugain.org/api.php?action=show_entity&entityid=https%3A%2F%2Fkafe.skku.edu%2Fidp%2Fsimplesamlphp
  - note: IdP host live on SKKU's own domain. /idp/simplesamlphp and /simplesaml/saml2/idp/metadata.php return a Korean WAF interstitial (404); metadata is distributed via the federation aggregate.
    status: 200
    url: https://kafe.skku.edu/
  - note: LIVE, not dead. SimpleSAMLphp answers "No SAML request provided — You accessed the Single Sign On Service interface, but did not provide a SAML Authentication Request", with a session tracking number. The advertised SSO endpoint is real and functioning.
    status: 400
    url: https://kafe.skku.edu/simplesaml/saml2/idp/SSOService.php
  - note: TENANT. Conformant OAI-PMH 2.0 Identify — repositoryName "Pure OAI Repository", adminEmail purehosted@elsevier.com, earliestDatestamp 2025-04-30T16:00:15Z.
    status: 200
    url: https://pure.skku.edu/ws/oai?verb=Identify
  - note: 'Six prefixes: oai_dc, qdc, mods, mods_swepub, xmetadiss, nl_didl. OpenAIRE CERIF 1.2 profile declared.'
    status: 200
    url: https://pure.skku.edu/ws/oai?verb=ListMetadataFormats
  - note: '"Request not authorized. Please provide a valid API key for access." Elsevier Pure Web Service, gated.'
    status: 401
    url: https://pure.skku.edu/ws/api/524/
  - note: TENANT confirmed by DNS — pure.skku.edu CNAME skku.elsevierpure.com -> apac.prod.elsevierpure.com. Vanity domain on Elsevier infrastructure.
    status: 200
    url: https://pure.skku.edu/
  - note: Two SKKU member records — 9930 School of Medicine (prefix 10.23838) and 6576 Institute of Legal Studies (prefix 10.17008). REGISTRY membership.
    status: 200
    url: https://api.crossref.org/members?query=sungkyunkwan
  - note: ROR https://ror.org/04q78tk20, domain skku.edu, established 1398, GRID grid.264381.a, ISNI 0000 0001 2181 989X, Wikidata Q41085. REGISTRY registration.
    status: 200
    url: https://api.ror.org/organizations?query=Sungkyunkwan
  - note: Negative probe. meta.total 0 — no DataCite provider. /clients also returns 0.
    status: 200
    url: https://api.datacite.org/providers?query=sungkyunkwan
  - note: 'TENANT. KERIS dCollection thesis repository. robots.txt is "User-agent: * / Disallow: /", and /srv/oai, /oai/request?verb=Identify and /dcollection/oai all return the HTML shell, not OAI-PMH.'
    status: 200
    url: https://skku.dcollection.net/
  - note: Institution-hosted learning system, a Laravel application. /api/v1/courses returns 419 Page Expired (CSRF); /api/v1/accounts/self, /api/graphql and /mod/lti/certs.php return the app 404.
    status: 200
    url: https://icampus.skku.edu/
  - note: Course registration (수강신청), Korean-only, session-gated. No machine-readable course catalog.
    status: 200
    url: https://sugang.skku.edu/
  - note: Library discovery layer, single-page app. /api returns 404; no SRU, OpenSearch or catalog API found.
    status: 200
    url: https://lib.skku.edu/
  - note: SKKU AI 종합안내 홈페이지 — institution-operated AI guidance portal carrying usage guidelines, academic-integrity cases and the Ministry of Education university AI ethics guideline.
    status: 200
    url: https://chatgpt.skku.edu/chatgpt/index.do
  - note: 개인정보 처리방침 — privacy policy, Korean surface only (/eng/etc/private.do returns 404).
    status: 200
    url: https://www.skku.edu/skku/etc/private.do
  - note: sitemapindex advertised from https://www.skku.edu/robots.txt (200).
    status: 200
    url: http://www.skku.edu/sitemap_index.xml
  - note: Negative probe. No API gateway; host does not resolve.
    status: 0
    url: https://api.skku.edu/
  - note: Negative probe. No developer portal; host does not resolve.
    status: 0
    url: https://developer.skku.edu/
  - note: Negative probe. No open-data portal; host does not resolve. open.skku.edu also fails.
    status: 0
    url: https://data.skku.edu/
  - note: Negative probe. No status page; host does not resolve.
    status: 0
    url: https://status.skku.edu/
  - note: Negative probe. No agent-directed content policy.
    status: 404
    url: https://www.skku.edu/llms.txt
  - note: Negative probe. No RFC 9116 security contact.
    status: 404
    url: https://www.skku.edu/.well-known/security.txt
  - note: Negative probe. No OIDC discovery; federated identity here is SAML 2.0, not OIDC.
    status: 404
    url: https://www.skku.edu/.well-known/openid-configuration
  - note: Negative finding. The org exists but has 0 public repositories and no name, description, website or location. Not evidence of an institutional GitHub presence; not credited.
    status: 200
    url: https://api.github.com/orgs/skku
  - note: Pointer repaired. The previous profile pointed at /company/sungkyunkwan-university, which returns 404 to every non-browser client — calibration confirmed LinkedIn returns 404 on that path shape for a deliberately fabricated slug too, so it reads as dead. The canonical school page is the Korean-name school URL (성균관대학교, 45,242 followers); 999 is LinkedIn's bot challenge and grades live.
    status: 999
    url: https://www.linkedin.com/school/%EC%84%B1%EA%B7%A0%EA%B4%80%EB%8C%80%ED%95%99%EA%B5%90/
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Sungkyunkwan University (SKKU) is a private research university in Seoul and Suwon, South Korea, founded in 1398 and operated since 1996 under the Samsung Foundation of Education. Like almost every university it is a federation of buyers rather than an API producer, and this profile is deliberate about which of that federation''s surfaces are actually SKKU''s engineering. SKKU operates no central developer portal and no API gateway — api.skku.edu, developer.skku.edu, data.skku.edu and status.skku.edu do not resolve — and publishes no OpenAPI for anything. What it does operate, and what almost no university catalog records, is a SAML 2.0 identity provider at kafe.skku.edu registered in eduGAIN through KAFE, the Korea Access Federation: entityID https://kafe.skku.edu/idp/simplesamlphp, scope skku.edu, supporting the REFEDS Research and Scholarship entity category and asserting the REFEDS Sirtfi assurance profile. That machine-readable metadata document is the strongest programmable
  surface SKKU runs. Its research information portal at pure.skku.edu looks institutional and is not: it CNAMEs to skku.elsevierpure.com and its OAI-PMH provider self-identifies as "Pure OAI Repository" with adminEmail purehosted@elsevier.com, so the live, conformant OAI-PMH 2.0 endpoint there is recorded as an Elsevier Pure TENANCY — SKKU''s data on Elsevier''s contract — and no Pure specification is saved in this repository. The thesis repository at skku.dcollection.net is likewise a KERIS dCollection tenancy whose robots.txt disallows all crawling and whose OAI paths return an HTML shell. Two SKKU units are Crossref members in their own right (School of Medicine, prefix 10.23838; Institute of Legal Studies, prefix 10.17008) and the institution is registered in ROR as 04q78tk20; no DataCite provider or client exists. Everything else — Kingo Portal SSO, iCampus, course registration at sugang.skku.edu, the library discovery layer — is enrolment-gated with no public API, no developer registration
  and no published rate limits.'
finops:
- name: Skku Finops
  service_category: Education
  slug: skku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skku.png
jsonld:
- class_count: 7
  name: Skku Context
  property_count: 3
  slug: skku-context
layout: provider
modified: '2026-09-01'
name: Sungkyunkwan University
nav: Providers
network: true
overview: 'Sungkyunkwan University publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and South Korea.


  The Sungkyunkwan University catalog on APIs.io includes 1 JSON-LD context.


  Sungkyunkwan University''s developer surface includes documentation, support, code examples, authentication, and 17 more developer resources.'
plans:
- name: Skku Plans Pricing
  plan_count: 2
  slug: skku-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Skku Rate Limits
  slug: skku-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 20.5
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 36.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skku/refs/heads/main/screenshots/skku-2026-06-20T194017.png
security:
- kind: authentication
  name: Skku Authentication
  slug: skku-authentication
  summary_line: saml2 · 1 scheme
- kind: domain-security
  name: Skku Domain Security
  slug: skku-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skku
tags:
- University
- Higher Education
- Education
- Research
- South Korea
- Seoul
- Identity Federation
- SAML
- eduGAIN
- Research Repository
- OAI-PMH
- Open Access
website: https://www.skku.edu/eng/
---
