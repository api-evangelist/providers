---
access_model:
  confidence: high
  label: Free · Institutional affiliation required for all but the harvesting endpoint
  onboarding: unknown
  pricing: free
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
  scored_at: '2026-09-03'
api_count: 7
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for the Vrije Universiteit Amsterdam Repository, served from the institution's own domain and administered by the VU University Library (adminEmail pure.ub@vu
  name: VU Research Portal OAI-PMH
  slug: research-portal-oai
- description: Vrije Universiteit Amsterdam operates its own SAML 2.0 identity provider on Microsoft ADFS and publishes signed, machine-readable federation metadata for it. entityID http://stsfed.login.vu.nl/adfs/se
  name: VU Amsterdam SAML 2.0 identity provider (SURFconext / eduGAIN)
  slug: identity-federation
- description: 'VU Amsterdam''s tenancy of the Elsevier Pure research information system, reachable at research.vu.nl/ws/api and API-key gated (GET /524/persons returns HTTP 401). The contract is Elsevier''s, not VU''s:'
  name: Elsevier Pure REST web service — VU Amsterdam deployment
  slug: pure-web-service-deployment
- description: 'VU Amsterdam''s research data management and publication platform, running at portal.yoda.vu.nl. Yoda is open-source iRODS-based software built by Utrecht University and, per its own DataCite registry '
  name: VU Yoda research data repository
  slug: yoda
- description: Vrije Universiteit Amsterdam publishes research datasets into DataverseNL, the shared national Dataverse service, under the collection dataverse.nl/dataverse/vuamsterdam. The REST API at dataverse.nl/
  name: VU Amsterdam collection on DataverseNL
  slug: dataverse-nl
- description: 'Instructure Canvas deployed for VU Amsterdam at canvas.vu.nl. The Canvas REST API is live and credential-gated — GET /api/v1/accounts returns HTTP 401 with a JSON body — and the sign-in page renders. '
  name: VU Amsterdam Canvas LMS API
  slug: canvas
- description: VU Amsterdam's class timetable at rooster.vu.nl, running Semestry MyTimetable (the vendor is named in an HTML comment in the served page). A JSON REST API is live behind authentication — /api/, /api/r
  name: VU Amsterdam timetable (MyTimetable)
  slug: timetable
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://vu.nl/en
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.vu.nl/
- group: other
  title: ''
  type: OpenData
  url: https://portal.yoda.vu.nl
- group: learn
  title: ''
  type: CourseCatalog
  url: https://studiegids.vu.nl/
- group: other
  title: ''
  type: IdentityFederation
  url: https://stsfed.login.vu.nl/FederationMetadata/2007-06/FederationMetadata.xml
- group: docs
  title: ''
  type: Documentation
  url: https://rdm.vu.nl/
- group: other
  title: ''
  type: AIPolicy
  url: https://vu.nl/en/education/more-about/teaching-and-ai
- group: build
  title: ''
  type: AITooling
  url: https://vu.nl/en/student/examinations/generative-ai-your-use-our-expectations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubvu
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vu.nl/en/about-vu/more-about/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vu.nl/en/about-vu/more-about/privacy-statement-vrije-universiteit-amsterdam
- group: operate
  title: ''
  type: Support
  url: https://vu.nl/en/about-vu/more-about/contact
- group: company
  title: ''
  type: Blog
  url: https://vu.nl/en/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/vrije-universiteit-amsterdam/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/VUamsterdam
- group: design
  title: ''
  type: Conformance
  url: conformance/vrije-universiteit-amsterdam-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vrije-universiteit-amsterdam-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vrije-universiteit-amsterdam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vrije-universiteit-amsterdam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vrije-universiteit-amsterdam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Two institution-operated machine-readable surfaces were reached and read in full — the OAI-PMH 2.0 endpoint at research.vu.nl/ws/oai (Identify, ListMetadataFormats, ListSets and a 108KB ListRecords harvest all returned 200) and the signed SAML 2.0 IdP metadata at stsfed.login.vu.nl (200, 116,822 bytes, also present in the SURFconext national feed). Beyond those two, every programmable surface under a vu.nl subdomain is a vendor product VU is a tenant of, and every one of them is credential-gated: the Elsevier Pure REST web service (research.vu.nl/ws/api/524/persons -> 401), Instructure Canvas (canvas.vu.nl/api/v1/accounts -> 401), Semestry MyTimetable (rooster.vu.nl/api/ -> 401) and VU Yoda''s WebDAV endpoint (data.yoda.vu.nl -> 401). The two Yoda public hosts and DataverseNL sit behind an Anubis bot challenge that returns HTTP 200 with a "checking your connection" body rather than content, and research.vu.nl HTML pages sit behind a Cloudflare challenge (403) even though its /ws/
    protocol endpoints are open. No developer portal, no llms.txt, no security.txt and no institution-authored API contract exists at any probed location. This profile is thin because the institution is a buyer, not a producer — not because the surface was unreachable.'
  evidence:
  - status: 200
    url: https://research.vu.nl/ws/oai?verb=Identify
  - status: 200
    url: https://research.vu.nl/ws/oai?verb=ListSets
  - status: 200
    url: https://stsfed.login.vu.nl/FederationMetadata/2007-06/FederationMetadata.xml
  - status: 200
    url: https://metadata.surfconext.nl/idps-metadata.xml
  - status: 401
    url: https://research.vu.nl/ws/api/524/persons
  - status: 401
    url: https://canvas.vu.nl/api/v1/accounts
  - status: 401
    url: https://rooster.vu.nl/api/
  - status: 401
    url: https://data.yoda.vu.nl/
  - status: 200
    url: https://portal.yoda.vu.nl/
  - status: 200
    url: https://publication.yoda.vu.nl/
  - status: 200
    url: https://dataverse.nl/api/info/version
  - status: 403
    url: https://research.vu.nl/en/organisations
  - status: 404
    url: https://vu.nl/llms.txt
  - status: 404
    url: https://vu.nl/.well-known/security.txt
  reason: tenant_only
  state: gated
created: '2026-06-03'
description: 'Vrije Universiteit Amsterdam (VU Amsterdam) is a public research university in the Netherlands, founded in 1880 and ranked #221 in the QS World University Rankings 2025. It operates no public developer program, no API portal, and no first-party API contract: every OpenAPI previously attributed to VU in this repository was Elsevier''s Pure API v5.34.3 (contact pure-support@elsevier.com), the same product contract at least nine other universities ship, and it has been removed. What VU genuinely operates and publishes machine-readably is two protocol surfaces on its own domain — a live OAI-PMH 2.0 repository interface at research.vu.nl/ws/oai serving OpenAIRE CERIF and Dublin Core, administered by the University Library, and a signed SAML 2.0 identity-provider metadata document at stsfed.login.vu.nl published into the SURFconext national federation and onward to eduGAIN. Everything else programmable under a vu.nl subdomain is a vendor product VU is the tenant of: the Elsevier
  Pure REST web service, VU Yoda (Utrecht University software maintained by SURF for VU), Instructure Canvas, and Semestry MyTimetable — all credential-gated. Research data is also published to the national DataverseNL service. The University Library GitHub organisation (ubvu) is the institution''s active open-source presence with 90 public repositories; the official VU GitHub organisation has none.'
finops:
- name: Vrije Universiteit Amsterdam Finops
  service_category: Education
  slug: vrije-universiteit-amsterdam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vrije-universiteit-amsterdam.png
layout: provider
modified: '2026-08-30'
name: Vrije Universiteit Amsterdam
nav: Providers
network: true
overview: 'Vrije Universiteit Amsterdam publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Netherlands, and Europe.


  Vrije Universiteit Amsterdam''s developer surface includes documentation, support, engineering blog, and 18 more developer resources.'
plans:
- name: Vrije Universiteit Amsterdam Plans Pricing
  plan_count: 2
  slug: vrije-universiteit-amsterdam-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Vrije Universiteit Amsterdam Rate Limits
  slug: vrije-universiteit-amsterdam-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 30.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/vrije-universiteit-amsterdam/refs/heads/main/screenshots/vrije-universiteit-amsterdam-2026-06-20T201145.png
security:
- kind: domain-security
  name: Vrije Universiteit Amsterdam Domain Security
  slug: vrije-universiteit-amsterdam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vrije-universiteit-amsterdam
tags:
- University
- Higher Education
- Education
- Netherlands
- Europe
- Research
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- Open Access
- Public Research University
website: https://vu.nl/en
---
