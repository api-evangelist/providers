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
api_count: 12
apis:
- description: 'Trinity''s own Shibboleth IdP, self-hosted on its own registrable domain: idp.tcd.ie resolves through idpha.tcd.ie to 134.226.14.232, inside Trinity''s 134.226.0.0/16 allocation. The metadata endpoint s'
  name: Trinity Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
- description: Trinity's Microsoft Entra ID tenant, d595be8d-b306-45f4-8064-9e5b82fbe52b, resolved from the tcd.ie domain hint. OpenID Connect discovery and SAML federation metadata both answer unauthenticated. Reco
  name: Trinity Microsoft Entra ID tenant (OIDC + SAML metadata)
  slug: entra-id-tenant
- description: TARA is Trinity's open-access institutional repository, a DSpace deployment on Trinity's own host (www.tara.tcd.ie) with its own DataCite repository registration, TCD.TARA. It exposes an OAI-PMH inter
  name: TARA OAI-PMH (Trinity's Access to Research Archive)
  slug: tara-oai
- description: The Library of Trinity College Dublin's Hyrax/Samvera digital asset repository, on Trinity's own host and built from Trinity's own open-source application (github.com/TCDLibrary/TCD-Hyrax-Web-App), se
  name: TCD Digital Collections (IIIF Presentation)
  slug: digital-collections-iiif
- description: Ireland's national legal-deposit digital repository, administered by the Library of Trinity College Dublin (OAI-PMH Identify reports adminEmail edepositadmin@tcd.ie) and registered under Trinity's Dat
  name: eDeposit Ireland — OAI-PMH and DSpace REST
  slug: edeposit-ireland
- description: An OpenSearch 1.1 description document served as application/xml from Trinity's own domain and explicitly authored by Trinity — the document's own Developer element reads "Trinity College Dublin, Digi
  name: Trinity College Dublin site OpenSearch description
  slug: opensearch
- description: Trinity is a DataCite consortium organization, symbol TCD, country IE, linked to https://ror.org/02tyrky19. It holds five prefixes (10.25546, 10.48495, 10.57864, 10.60557, 10.82163) and five registere
  name: DataCite consortium membership (provider TCD)
  slug: datacite-registrant
- description: Crossref member 49418, "Trinity College Dublin, the University of Dublin", holding prefix 10.69731. As of the 2026-09-01 probe the member record reports zero deposited DOIs — a live membership that is
  name: Crossref membership (member 49418)
  slug: crossref-member
- description: Trinity's Research Organization Registry identifier, https://ror.org/02tyrky19, the canonical machine-readable organizational identity used across DataCite, Crossref and OpenAIRE. The DataCite provide
  name: ROR organization record (02tyrky19)
  slug: ror-record
- description: Trinity Library's LibCal tenancy on Springshare's platform, tcd-ie.libcal.com. The public widget endpoint api_hours_today.php returns a machine-parseable per-branch hours fragment unauthenticated; the
  name: Library opening hours and room booking (Springshare LibCal)
  slug: libcal
- description: 'Trinity Library''s LibGuides tenancy at libguides.tcd.ie, the published documentation surface for TARA and for the Library''s generative-AI referencing guidance. The LibGuides API path returns 404 — no '
  name: Library subject and research guides (Springshare LibGuides)
  slug: libguides
- description: Trinity's own research information system at rss.tcd.ie, resolving through tcdlocalportalha.tcd.ie to 134.226.14.238 inside Trinity's own network. Sign-in redirects to Trinity's Entra ID tenant via SA
  name: Trinity Research Support System (RSS)
  slug: research-support-system
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.tcd.ie/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tcd.ie/library/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TCDLibrary
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TCDLibrary/TCD-Hyrax-Web-App
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TCDLibrary/TCD-Hyrax-Web-App/issues
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/trinity-college-dublin/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tcd.ie/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tcd.ie/disclaim/
- group: operate
  title: ''
  type: Support
  url: https://www.tcd.ie/itservices/our-services/it-service-desk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.tcd.ie/itservices/our-services/edugate---federated-access/
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.tcd.ie/library/riss/tara/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.tcd.ie/library/opub/catalogues.php
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.tcd.ie/courses/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.tchpc.tcd.ie/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.tcd.ie/academic-affairs/what-we-do/whats-new/generative-ai-statement/
- group: build
  title: ''
  type: AITooling
  url: https://www.tcd.ie/itservices/keeping-it-secure/artificial-intelligence-ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/trinity-college-dublin-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trinity-college-dublin-domain-standards.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trinity-college-dublin-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trinity-college-dublin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trinity-college-dublin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trinity-college-dublin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trinity-college-dublin-context.jsonld
coverage:
  detail: 'Trinity''s two institution-operated repository surfaces — TARA at www.tara.tcd.ie and Digital Collections at digitalcollections.tcd.ie — are both reachable in a browser and both refuse unattended clients. TARA returns a Cloudflare 403 interstitial on every path, including /oai/request and /server/oai/request. Digital Collections returns a soft-200 reCAPTCHA page from an F5 Distributed Cloud edge on every path, including /robots.txt and IIIF manifest URLs, so the 200 is not evidence of a readable surface. Neither is dead and neither is an authentication wall; both are bot mitigation. Everything reachable WAS read: the Shibboleth IdP metadata, the Entra ID OIDC and SAML metadata, the OpenSearch descriptor, the eDeposit Ireland OAI-PMH Identify/ListMetadataFormats/ListSets responses and the DSpace REST root, and the DataCite, Crossref and ROR registry records. Beyond that there is simply nothing to find: api.tcd.ie, data.tcd.ie and developer.tcd.ie do not resolve, and www.tcd.ie/llms.txt
    returns 404.'
  evidence:
  - status: 403
    url: https://www.tara.tcd.ie/oai/request?verb=Identify
  - status: 403
    url: https://www.tara.tcd.ie/server/oai/request?verb=Identify
  - status: 200
    url: https://digitalcollections.tcd.ie/
  - status: 200
    url: https://digitalcollections.tcd.ie/concern/works/kh04dp74f/manifest
  - status: 200
    url: https://idp.tcd.ie/idp/shibboleth
  - status: 200
    url: https://www.edepositireland.ie/server/oai/request?verb=Identify
  - status: 200
    url: https://www.tcd.ie/assets/xml/tcd-opensearch/tcd-opensearch.xml
  - status: 200
    url: https://api.datacite.org/providers/tcd
  - status: 404
    url: https://www.tcd.ie/llms.txt
  - status: 0
    url: https://api.tcd.ie/
  reason: bot_blocked
  state: gated
created: '2026-06-03'
description: 'Trinity College Dublin, the University of Dublin, founded in 1592, is Ireland''s oldest university and a legal deposit library for Ireland and the United Kingdom since 1801. Trinity operates no public developer portal, publishes no OpenAPI, issues no API keys and runs no documented open-API programme — and this profile says so rather than padding the gap. What Trinity does operate, and what is recorded here, is standards-based scholarly and identity infrastructure: a self-hosted Shibboleth Identity Provider on its own domain (idp.tcd.ie, scope tcd.ie) registered in HEAnet''s Edugate federation and exported to eduGAIN; a Microsoft Entra ID tenant with live OIDC discovery; an OpenSearch 1.1 description document authored by Trinity''s own Digital and Web team; DataCite consortium membership with five prefixes and 16,031 DOIs across five registered repositories; and Crossref membership. Its two flagship repositories — TARA (DSpace) and Digital Collections (Hyrax/Samvera, home of
  the Book of Kells) — sit on Trinity''s own hosts but are fronted by Cloudflare and F5 bot-mitigation that returns a challenge to every unattended client, so they are live but not machine-callable. eDeposit Ireland, the national legal-deposit repository Trinity Library administers, is the one repository that answers a harvester, and it does so as a tenant on Atmire''s Open Repository platform rather than as Trinity''s own engineering.'
finops:
- name: Trinity College Dublin Finops
  service_category: Education
  slug: trinity-college-dublin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trinity-college-dublin.png
jsonld:
- class_count: 20
  name: Trinity College Dublin Context
  property_count: 2
  slug: trinity-college-dublin-context
layout: provider
modified: '2026-09-01'
name: Trinity College Dublin
nav: Providers
network: true
overview: 'Trinity College Dublin publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Ireland, and Research Repository.


  The Trinity College Dublin catalog on APIs.io includes 1 JSON-LD context.


  Trinity College Dublin''s developer surface includes documentation, support, authentication, and 21 more developer resources.'
plans:
- name: Trinity College Dublin Plans Pricing
  plan_count: 2
  slug: trinity-college-dublin-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Trinity College Dublin Rate Limits
  slug: trinity-college-dublin-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 9.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 20.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/trinity-college-dublin/refs/heads/main/screenshots/trinity-college-dublin-2026-06-20T195720.png
security:
- kind: authentication
  name: Trinity College Dublin Authentication
  slug: trinity-college-dublin-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Trinity College Dublin Domain Security
  slug: trinity-college-dublin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trinity-college-dublin
tags:
- University
- Higher Education
- Education
- Ireland
- Research Repository
- Identity Federation
- Library
- Open Access
- Digital Collections
- IIIF
- OAI-PMH
- Shibboleth
- DataCite
- Legal Deposit
website: https://www.tcd.ie/
---
