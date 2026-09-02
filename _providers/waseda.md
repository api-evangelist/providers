---
access_model:
  confidence: high
  label: Free and anonymous for IIIF and repository harvesting; campus systems are credentialed
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
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
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: Waseda University operates its own IIIF server for the Kotenseki Sogo Database (古典籍総合データベース) of classical Japanese books and the Waseda Cultural Resources Database (文化資源データベース). It serves IIIF Present
  name: Waseda IIIF Presentation API (Cultural Resources)
  slug: iiif-presentation
- description: The image-tile half of the same Waseda-operated IIIF deployment. info.json declares protocol http://iiif.io/api/image at Image API 2.0 compliance level 1, 256x256 tiles with scale factors to 512, five
  name: Waseda IIIF Image API
  slug: iiif-image
- description: Waseda operates its own Shibboleth SAML 2.0 identity provider. The metadata document is served anonymously as application/xml and declares entityID https://iaidp.ia.waseda.jp/idp/shibboleth, shibmd:Sc
  name: Waseda Identity Provider (Shibboleth SAML 2.0)
  slug: shibboleth-idp
- description: Waseda's identity provider is registered in GakuNin (学術認証フェデレーション), the Japanese academic identity federation operated by the National Institute of Informatics, and reaches eduGAIN through it. The ent
  name: GakuNin Academic Access Federation membership
  slug: gakunin-federation
- description: Waseda Moodle runs on Waseda's own host and is a live LTI 1.3 learning-tools-interoperability platform. It publishes a JWKS keyset anonymously (one RSA/RS256 key, kid ea841dc4e7af7463cc4c), an OIDC th
  name: Waseda Moodle — LTI 1.3 / LTI Advantage platform
  slug: moodle-lti
- description: The Moodle Web Services REST endpoint is deployed on Waseda's own host and answers an anonymous call with Moodle's structured invalidtoken fault. Access requires a per-user token issued by a Waseda Mo
  name: Waseda Moodle Web Services (REST)
  slug: moodle-webservices
- description: OAI-PMH 2.0 metadata harvesting for the Waseda University Repository. The collection, the administrative contact (repository@list.waseda.jp) and the identity are Waseda's; the host and the WEKO3 softw
  name: Waseda University Repository (OAI-PMH)
  slug: repository-oai
- description: Waseda University Library's discovery service, WINE, is an Ex Libris Primo VE tenancy under institution code 81SOKEI_WUNI. The discovery UI is live and is Waseda's service, but it is Ex Libris's engin
  name: WINE Library Discovery (Ex Libris Primo tenancy)
  slug: wine-primo
- description: Waseda University is registered in the Research Organization Registry as https://ror.org/00ntfnx83 — established 1882, types education and funder, with external identifiers GRID grid.5290.e, ISNI 0000
  name: ROR registration (Research Organization Registry)
  slug: ror-registration
- description: Waseda University holds Crossref Open Funder Registry ID 501100004423, located in Japan, with 1,458 works attributed and two descendant funder identifiers (501100006539, 501100018983). Waseda is in th
  name: Crossref Open Funder Registry membership
  slug: crossref-funder
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.waseda.jp/top/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.waseda.jp/top/en/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/wasedauniversity/
- group: operate
  title: ''
  type: Support
  url: https://support.waseda.jp/it/s/
- group: other
  title: ''
  type: IdentityFederation
  url: https://iaidp.ia.waseda.jp/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://waseda.repo.nii.ac.jp/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://waseda.primo.exlibrisgroup.com/discovery/search?vid=81SOKEI_WUNI:WINE
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.wsl.waseda.jp/syllabus/JAA101.php
- group: other
  title: ''
  type: OpenData
  url: https://archive.waseda.jp/archive/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.waseda.jp/top/news/89507?lng=en
- group: docs
  title: ''
  type: Documentation
  url: https://www.wul.waseda.ac.jp/kotenseki/ga_IIIF/about_iiif.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.waseda.jp/library/user/using-images/
- group: auth
  title: ''
  type: Authentication
  url: authentication/waseda-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/waseda-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/waseda-examples.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waseda-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/waseda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/waseda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/waseda-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Waseda University is a large private research university in Shinjuku, Tokyo, founded in 1882 and one of Japan''s two best-known private institutions. It operates no developer portal, publishes no OpenAPI, and has no official GitHub organization — but it is not the empty profile that description usually implies, because three genuinely institution-operated machine-readable surfaces sit under its own domains and answer anonymous calls. Waseda runs its own IIIF server at iiif.archive.waseda.jp, serving IIIF Presentation 2.1 manifests and IIIF Image API 2.0 level-1 endpoints for the Kotenseki Sogo Database of classical Japanese books and the Waseda Cultural Resources Database — a real, callable cultural-heritage API on Waseda''s engineering. It runs its own Shibboleth SAML 2.0 identity provider at iaidp.ia.waseda.jp, whose entityID is registered in the GakuNin federation operated by NII and propagated onward to eduGAIN. And Waseda Moodle at wsdmoodle.waseda.jp is a live LTI 1.3
  / LTI Advantage platform publishing a JWKS keyset, an OAuth 2.0 client-credentials token endpoint and an LTI services endpoint, alongside a token-gated Moodle Web Services REST endpoint. Its other apparent APIs are not its own: the Waseda University Repository''s OAI-PMH 2.0 endpoint is real and its content is Waseda''s, but it runs on NII''s JAIRO Cloud, and the WINE library discovery service is an Ex Libris Primo tenancy whose Primo and Alma SRU interfaces are not enabled for public use. Waseda is registered in ROR (00ntfnx83) and holds Crossref Open Funder Registry ID 501100004423, but is not a Crossref depositing member and holds no DataCite account.'
finops:
- name: Waseda Finops
  service_category: Education
  slug: waseda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waseda.png
jsonld:
- class_count: 23
  name: Waseda Context
  property_count: 1
  slug: waseda-context
layout: provider
modified: '2026-09-01'
name: Waseda University
nav: Providers
network: true
overview: 'Waseda University publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Japan, and Asia.


  The Waseda University catalog on APIs.io includes 1 JSON-LD context.


  Waseda University''s developer surface includes support, documentation, authentication, code examples, and 16 more developer resources.'
plans:
- name: Waseda Plans Pricing
  plan_count: 2
  slug: waseda-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Waseda Rate Limits
  slug: waseda-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 9.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 20.5
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/waseda/refs/heads/main/screenshots/waseda-2026-06-20T201241.png
security:
- kind: authentication
  name: Waseda Authentication
  slug: waseda-authentication
  summary_line: saml2/oauth2/apiKey/none · 0 schemes
- kind: domain-security
  name: Waseda Domain Security
  slug: waseda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: waseda
tags:
- University
- Higher Education
- Education
- Japan
- Asia
- Private Research University
- Research
- Library
- Open Access
- Cultural Heritage
- Digital Archives
- IIIF
- Identity Federation
- Learning Management
- Research Repository
website: https://www.waseda.jp/top/en/
---
