---
access_model:
  confidence: high
  label: Free · no onboarding path · REST surfaces closed to the public
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probed
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
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: OAI-PMH 2.0 metadata-harvesting endpoint for BORIS Portal, the University of Bern's institutional repository and current research information system. Runs on a Bern-operated host under the university'
  name: BORIS Portal OAI-PMH Endpoint
  slug: boris-oai
- description: BORIS Portal runs DSpace with the DSpace-CRIS extension and, by design, exposes a HAL/JSON REST API at /server/api covering communities, collections, items, bitstreams and CRIS research entities. It i
  name: BORIS Portal DSpace REST API (public access suspended)
  slug: boris-rest
- description: 'OAI-PMH 2.0 endpoint for Bern Open Publishing, the University Library''s diamond open-access journal platform, self-hosted on bop.unibe.ch on Open Journal Systems 3.4.0.6. Verified live 2026-09-01: rep'
  name: Bern Open Publishing (BOP Serials) OAI-PMH Endpoint
  slug: bop-oai
- description: 'The Open Journal Systems REST API v1 on the University Library''s Bern Open Publishing platform. Present and responding, but closed: an anonymous GET of /index.php/index/api/v1/contexts returns HTTP 40'
  name: Bern Open Publishing OJS REST API (token required)
  slug: bop-rest
- description: The University Library of Bern runs an Upptime uptime monitor over the 15 public applications it operates, publishing a live status site plus per-service JSON endpoints (uptime.json, response-time.jso
  name: University Library Public Services Status API
  slug: ub-services-status
- description: A IIIF server operated by the University Library of Bern at iiif.ub.unibe.ch, serving images for its digitized collections (Collection Ryhiner, DigiBern, Berner Ortsgeschichten and others) and monitor
  name: University Library IIIF Image Server
  slug: ub-iiif
- description: The University of Bern operates its own SAML 2.0 / Shibboleth Identity Provider, published as machine-readable metadata in the SWITCHaai federation aggregate (the Swiss national research-and-education
  name: SWITCHaai Identity Federation — University of Bern IdP
  slug: switchaai-idp
- description: 'The University of Bern is a DataCite direct member, registering DOIs for its research outputs. Verified 2026-09-01 at https://api.datacite.org/providers/unibe (200): symbol UNIBE, memberType direct_me'
  name: DataCite Membership — University of Bern (UNIBE)
  slug: datacite-member
- description: The University of Bern's Research Organization Registry identifier, https://ror.org/02k7v4d05, verified live 2026-09-01. Domain unibe.ch, established 1834, located in Bern, Switzerland; cross-referenc
  name: ROR Registry Record — University of Bern
  slug: ror-record
- description: Library discovery for the University of Bern runs on swisscovery, the Swiss Library Service Platform's shared Ex Libris Alma / Primo VE installation. Bern has an institution-specific tenant view at ht
  name: swisscovery — University Library of Bern tenant view
  slug: swisscovery-tenant
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.unibe.ch/index_eng.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.ub.unibe.ch/services/digital_scholarship/apis/index_eng.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.ub.unibe.ch/services/open_science/boris_portal/index_eng.html
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ubbern.swisscovery.slsp.ch
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.unibe.ch/studies/student_starter_kit/tools/cts/index_eng.html
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.aai.switch.ch/metadata.switchaai.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc-unibe-ch.github.io/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.unibe.ch/universitaet/organisation/leitung_und_zentralbereich/vizerektorat_lehre/startseite_vizerektorat_lehre/faq_zur_verwendung_von_ki_gestuetzten_hilfsmitteln_in_der_lehre__vizerektorat_lehre_universitaet_bern/index_ger.html
- group: build
  title: ''
  type: AITooling
  url: https://www.ub.unibe.ch/service/ki_im_wissenschaftlichen_arbeiten/index_ger.html
- group: operate
  title: ''
  type: Status
  url: https://ub-unibe-ch.github.io/ub-public-services-status/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/id-unibe-ch
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ub-unibe-ch
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hpc-unibe-ch
- group: operate
  title: ''
  type: Support
  url: https://www.ub.unibe.ch/about_us/contacts/index_eng.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unibe.ch/legal_notice/index_eng.html
- group: company
  title: ''
  type: Blog
  url: https://www.unibe.ch/news/index_eng.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bern/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-bern-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-bern-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bern-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bern-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bern-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bern-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-09-01'
  detail: 'Bern''s open surfaces are harvesting protocols and registry memberships; every REST surface it operates is closed to anonymous callers. BORIS Portal (boris-portal.unibe.ch) serves a soft-200 "Temporary Access Restriction" HTML page to the entire public — root and /server/api alike — stating that access "is currently granted exclusively to" the University of Bern network, the Inselspital network and university VPN connections, and boristheses.unibe.ch serves the same page. Only /server/oai/request is exempted, and it returns real OAI-PMH XML. The Bern Open Publishing OJS REST API answers api.403.unauthorized without a token. There is no developer portal, no OpenAPI, and no llms.txt anywhere on a unibe.ch host. This is a correct thin profile, not a failed crawl: the surfaces were reached, read, and are genuinely closed.'
  evidence:
  - status: 200
    url: https://boris-portal.unibe.ch/server/oai/request?verb=Identify
  - status: 200
    url: https://boris-portal.unibe.ch/server/api
  - status: 200
    url: https://boris-portal.unibe.ch/
  - status: 200
    url: https://bop.unibe.ch/index.php/index/oai?verb=Identify
  - status: 403
    url: https://bop.unibe.ch/index.php/index/api/v1/contexts
  - status: 404
    url: https://www.unibe.ch/llms.txt
  - status: 500
    url: https://www.unibe.ch/sitemap.xml
  - status: 200
    url: https://www.unibe.ch/.well-known/security.txt
  - status: 0
    url: https://opendata.iwi.unibe.ch/
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'The University of Bern (Universität Bern), founded in 1834, is a comprehensive public research university in the Swiss capital with around 16,000 students across eight faculties. It is a federation of buyers rather than an API producer: it operates no developer portal, publishes no OpenAPI, AsyncAPI, JSON Schema, apis.json, llms.txt or agent card on any host it controls, and offers no self-service API onboarding of any kind. What it does operate is protocol- and identity-shaped. Two OAI-PMH 2.0 harvesting endpoints run on its own hosts — BORIS Portal, the institutional repository and CRIS on DSpace, and BOP Serials, the Bern Open Publishing OJS platform — and both answered verb=Identify live. The University Library publishes an Upptime status page whose per-service JSON is the only genuinely open, machine-readable HTTP API in this profile. The university runs its own Shibboleth Identity Provider inside the SWITCHaai federation (entityID https://aai-idp.unibe.ch/idp/shibboleth,
  scope unibe.ch, 52 service providers), and it is a direct DataCite member (symbol UNIBE) with five registered repositories. Everything transactional is closed: BORIS Portal''s DSpace REST API is not merely authenticated but deliberately suspended for the public — the whole host answers every anonymous request with a "Temporary Access Restriction" page citing automated-traffic volume and allowing only the University of Bern network, the Inselspital network and university VPN — and the OJS REST API returns api.403.unauthorized. Library discovery runs on a vendor platform under a Bern-specific tenant view (swisscovery / Ex Libris Primo VE), and the course system KSL sits behind SWITCH AAI. The library''s much-linked "APIs" page is a curated guide to OTHER organizations'' APIs (OpenAlex, Crossref, Scopus, Elsevier, IEEE), not to anything Bern operates.'
finops:
- name: University Of Bern Finops
  service_category: Education
  slug: university-of-bern-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bern.png
jsonld:
- class_count: 13
  name: University Of Bern Context
  property_count: 5
  slug: university-of-bern-context
layout: provider
modified: '2026-09-01'
name: University of Bern
nav: Providers
network: true
overview: 'University of Bern publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Switzerland, and Public Research University.


  The University of Bern catalog on APIs.io includes 1 JSON-LD context.


  University of Bern''s developer surface includes documentation, status page, GitHub presence, support, engineering blog, and 19 more developer resources.'
plans:
- name: University Of Bern Plans Pricing
  plan_count: 2
  slug: university-of-bern-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of Bern Rate Limits
  slug: university-of-bern-rate-limits
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 10.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 20.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bern/refs/heads/main/screenshots/university-of-bern-2026-06-20T200135.png
security:
- kind: domain-security
  name: University Of Bern Domain Security
  slug: university-of-bern-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Bern Vulnerability Disclosure
  slug: university-of-bern-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-bern
tags:
- University
- Higher Education
- Education
- Switzerland
- Public Research University
- Research
- Open Science
- Open Access
- Institutional Repository
- Library
- OAI-PMH
- Identity Federation
- Shibboleth
- Research Computing
- Scholarly Publishing
website: https://www.unibe.ch/index_eng.html
---
