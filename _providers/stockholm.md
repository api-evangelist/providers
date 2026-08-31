---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - rate-limits
  trial: false
  try_now: true
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
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: Stockholm University operates its own Shibboleth Identity Provider and publishes its SAML 2.0 entity metadata anonymously on its registrable domain. The document declares entityID https://idp.it.su.se
  name: Stockholm University Shibboleth Identity Provider (SAML2 Metadata)
  slug: identity-federation
- description: Stockholm University's publication records are harvestable over OAI-PMH 2.0 from its DiVA instance at su.diva-portal.org, with an institution-scoped set (all-su) and eight metadata formats (oai_dc, oa
  name: DiVA Institutional Repository (OAI-PMH)
  slug: diva-oai
- description: su.figshare.com is Stockholm University's research data repository, running on Figshare. The data, the DOIs and the institutional group are SU's; the contract behind it is Figshare's generic api.figsh
  name: Stockholm University Research Data Repository (Figshare tenancy)
  slug: figshare-repository
- description: www.su.se runs SiteVision, whose REST framework is reachable at /rest-api/ and answers with structured JSON. No public RestApp is exposed there (a request to /rest-api/search returns {"success":false,
  name: Stockholm University Education Archive Sitemap (SiteVision REST)
  slug: education-archive-sitemap
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.su.se/english/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.su.se/english/about-the-university/university-facts/about-this-website-and-processing-of-personal-data
- group: operate
  title: ''
  type: Support
  url: https://www.su.se/english/about-the-university/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stockholmuniversity
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/stockholmuniversity/shib-keygen-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/stockholm-university/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.it.su.se/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://bolin.su.se/data/
- group: other
  title: ''
  type: ResearchRepository
  url: https://su.diva-portal.org/
- group: other
  title: ''
  type: ResearchRepository
  url: https://su.figshare.com/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.su.se/utbildning/utbildningskatalog
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.su.se/english/library/
- group: design
  title: ''
  type: Conformance
  url: conformance/stockholm-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stockholm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stockholm-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stockholm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stockholm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stockholm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-08-30'
  detail: 'Stockholm University publishes no public, documented API of its own, and this profile now says so. The operator axis is the entire finding. Everything the June 2026 pass credited to SU — eleven per-tag OpenAPIs titled "Figshare altmetric ... API", all with servers[0] https://api.figshare.com/v2 and info.contact "Figshare Support" — was one vendor contract that twelve other institutions in this cohort also ship. Those 48 files (10 refined specs, the pristine Figshare source in openapi/_original, the refine report, 3 JSON Schemas, 2 JSON Structures, 2 examples, a JSON-LD context, 2 rulesets, a vocabulary, scopes, an authentication summary, an agentic-access card, a capability map and 21 collection files) have been removed file by file with git rm. Two tenant relationships were kept rather than deleted, because they are real institutional facts: the DiVA OAI-PMH endpoint (operated by the DiVA consortium at Uppsala University Library) and su.figshare.com. Two institution-operated
    surfaces were found by live probe and are new to this profile: the Shibboleth SAML2 IdP metadata at idp.it.su.se, registered in SWAMID and therefore eduGAIN, and the SiteVision /rest-api/sitemap education archive index on www.su.se. A third institution-operated asset, the Bolin Centre Database on bolin.su.se, mints DataCite DOIs under prefix 10.17043 (DataCite repository snd.bolin, active since 2014) but publishes no REST API, so it is recorded as a ResearchRepository pointer and as DataCite conformance rather than as an API. Four education-regime domain standards are evidenced in conformance/: shibboleth, saml, oai-pmh and datacite. Eight more (scim, lti, oneroster, ed-fi, caliper, qti, orcid, crossref) were probed and not found. Absences confirmed by negative probe rather than assumed: no developer portal, no API gateway, no open data portal, no llms.txt, no sitemap at the conventional path, no first-party security contact (su.se/.well-known/security.txt exists but names soc@sitevision.se,
    the CMS vendor''s SOC, not the university''s).'
  evidence:
  - note: INSTITUTION. application/xml, 5,263 bytes. SAML2 IdP metadata, entityID https://idp.it.su.se/idp/shibboleth, shibmd:Scope su.se.
    status: 200
    url: https://idp.it.su.se/idp/shibboleth
  - note: SWAMID IdP aggregate contains exactly one su.se entity — SU's IdP. Aggregate is SUNET's.
    status: 200
    url: https://mds.swamid.se/md/swamid-idp.xml
  - note: INSTITUTION. Serves a valid <sitemapindex> body (315 bytes, text/xml) despite the 404 status code, naming sitemap1, sitemap2 and educationArchiveSitemap. Advertised in robots.txt.
    status: 404
    url: https://www.su.se/rest-api/sitemap
  - note: 3,921,519 bytes of text/xml — every course syllabus in the planarkiv, with course codes.
    status: 200
    url: https://www.su.se/rest-api/sitemap/educationArchiveSitemap
  - note: 'SiteVision REST framework is live and answers JSON, but exposes no public RestApp: {"success":false,"type":"invalidParameter","message":"No RestApp found for /rest-api/search"}.'
    status: 400
    url: https://www.su.se/rest-api/search
  - note: INSTITUTION. Bolin Centre Database, SU-operated research data repository. No REST API.
    status: 200
    url: https://bolin.su.se/data/
  - note: DataCite repository "Bolin Centre Database", year 2014, url https://bolin.su.se/data/.
    status: 200
    url: https://api.datacite.org/clients/snd.bolin
  - note: TENANT. OAI-PMH 2.0, repositoryName "DiVA - Academic Archive On-line", adminEmail diva-support@ub.uu.se, repositoryIdentifier DiVA.org.
    status: 200
    url: https://su.diva-portal.org/dice/oai?verb=Identify
  - note: TENANT. Empty body, bot challenge. Figshare deployment; contract is api.figshare.com/v2.
    status: 202
    url: https://su.figshare.com/
  - note: Negative probe. No API gateway; host does not resolve.
    status: 0
    url: https://api.su.se/
  - note: Negative probe. No developer portal; host does not resolve.
    status: 0
    url: https://developer.su.se/
  - note: Negative probe. No open data portal; host does not resolve.
    status: 0
    url: https://data.su.se/
  - note: Negative probe. No API path on the institutional website.
    status: 404
    url: https://www.su.se/api/
  - note: Negative probe. No agent-directed content policy.
    status: 404
    url: https://www.su.se/llms.txt
  - note: Negative probe. Sitemap lives at /rest-api/sitemap instead, per robots.txt.
    status: 404
    url: https://www.su.se/sitemap.xml
  - note: 'Present but not the institution''s own contact — Contact: mailto:soc@sitevision.se, the SiteVision CMS vendor''s security operations centre. Expires 2026-09-30.'
    status: 200
    url: https://www.su.se/.well-known/security.txt
  reason: no_public_api
  state: none
created: '2026-06-03'
description: 'Stockholm University (Stockholms universitet) is a public research university in Sweden and one of the country''s largest, with roughly 33,000 students across four faculties. It operates no public developer portal, no API gateway and no first-party documented API: api.su.se, data.su.se and developer.su.se do not resolve, and www.su.se/api returns 404. What the institution genuinely runs and serves anonymously is narrow — a Shibboleth SAML2 identity provider at idp.it.su.se whose entity metadata is published by the university and registered in the SWAMID federation (and so in eduGAIN), the Bolin Centre Database research data repository on bolin.su.se minting its own DataCite DOIs under prefix 10.17043 since 2014, and a SiteVision REST sitemap on www.su.se that indexes every course syllabus in the education archive. Its two harvestable research surfaces are both tenancies rather than SU engineering: the DiVA OAI-PMH endpoint at su.diva-portal.org is operated by the DiVA consortium
  at Uppsala University Library, and su.figshare.com is a Figshare deployment. This profile previously credited Stockholm University with eleven APIs that were all one Figshare contract at api.figshare.com/v2; those contracts and everything derived from them have been removed and the two repository relationships recorded as tenant surfaces instead.'
finops:
- name: Stockholm Finops
  service_category: Education
  slug: stockholm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stockholm.png
layout: provider
modified: '2026-08-30'
name: Stockholm University
nav: Providers
network: true
overview: 'Stockholm University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Research Data.


  Stockholm University''s developer surface includes support and 18 more developer resources.'
plans:
- name: Stockholm Plans Pricing
  plan_count: 2
  slug: stockholm-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Stockholm Rate Limits
  slug: stockholm-rate-limits
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -15.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 10.5
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/stockholm/refs/heads/main/screenshots/stockholm-2026-06-20T194559.png
security:
- kind: domain-security
  name: Stockholm Domain Security
  slug: stockholm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stockholm Vulnerability Disclosure
  slug: stockholm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stockholm
tags:
- Education
- Higher Education
- University
- Research
- Research Data
- Open Access
- Repository
- Identity Federation
- Course Catalog
- Sweden
- Europe
website: https://www.su.se/english/
---
