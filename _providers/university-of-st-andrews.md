---
access_model:
  confidence: high
  label: Free and open · no registration on the OAI-PMH or federation metadata endpoints
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: 'OAI-PMH 2.0 endpoint for the DSpace-based St Andrews Research Repository, the University''s open-access repository of theses, articles and other research outputs. Verified live on 2026-09-01: verb=Iden'
  name: St Andrews Research Repository OAI-PMH
  slug: repository-oai
- description: The University's own SAML 2.0 / Shibboleth Identity Provider, entityID https://idp.st-andrews.ac.uk/shibboleth, registered in the UK Access Management Federation as entity uk000278 since 2008-01-16 an
  name: University of St Andrews Shibboleth Identity Provider
  slug: identity-federation
- description: research-portal.st-andrews.ac.uk is the University's research information system and public research portal, running on Elsevier Pure - the host CNAMEs to standrews.elsevierpure.com. The research reco
  name: St Andrews Research Portal (Elsevier Pure tenancy)
  slug: research-portal
- description: 'The University publishes IT service status at status.st-andrews.ac.uk, which carries a read-only JSON API at /api/v1 with /status, /components and /notices. Verified live on 2026-09-01: /api/v1/status'
  name: University of St Andrews Service Status API (SorryApp tenancy)
  slug: status-api
- description: The University of St Andrews is a registered DataCite provider - id nahy, symbol NAHY, memberType consortium_organization, country GB, rorId https://ror.org/02wn5qz54, created 2020-09-01 - minting DOI
  name: DataCite Membership (provider NAHY)
  slug: datacite-membership
- description: 'The University of St Andrews Library is Crossref member 6332, holding 688 DOIs (151 current, 537 backfile) as of a probe on 2026-09-01 against https://api.crossref.org/members?query=st+andrews (200). '
  name: Crossref Membership (member 6332)
  slug: crossref-membership
- description: The University of St Andrews is registered in the Research Organization Registry as https://ror.org/02wn5qz54, status active, types education and funder, established 1410, domain st-andrews.ac.uk, loc
  name: ROR Registration (02wn5qz54)
  slug: ror-registration
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.st-andrews.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research-repository.st-andrews.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research-portal.st-andrews.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.st-andrews.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: http://metadata.ukfederation.org.uk/ukfederation-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://github.com/StAResComp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StAResComp
- group: learn
  title: ''
  type: CourseCatalog
  url: https://timetables.st-andrews.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.st-andrews.ac.uk/policy/information-governance-and-management-information-security/use-of-generative-ai---llm.pdf
- group: other
  title: ''
  type: AIPolicy
  url: https://www.st-andrews.ac.uk/policy/academic-policies-assessment-examination-and-award-good-academic-practice/generative-ai-faqs-students-guidance.pdf
- group: operate
  title: ''
  type: Status
  url: https://status.st-andrews.ac.uk/
- group: company
  title: ''
  type: Blog
  url: https://openresearch.wp.st-andrews.ac.uk/
- group: company
  title: ''
  type: BlogRSS
  url: https://openresearch.wp.st-andrews.ac.uk/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.st-andrews.ac.uk/it-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.st-andrews.ac.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.st-andrews.ac.uk/terms/data-protection/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-st-andrews/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-st-andrews-education-standards.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-st-andrews-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-st-andrews-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-st-andrews-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-st-andrews-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-st-andrews-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'St Andrews authors no public API and operates no developer portal, and after a full probe sweep on 2026-09-01 that is the correct measurement rather than a gap in the search. The four conventional developer hostnames - api., data., opendata. and developer.st-andrews.ac.uk - are all NXDOMAIN. The institution''s genuinely own machine-readable surfaces are protocol endpoints rather than products: a working DSpace OAI-PMH 2.0 interface with twelve metadata formats, a UK Access Management Federation Shibboleth IdP that serves its own SAML metadata, and registrant records in DataCite, Crossref and ROR. Three negative findings are recorded rather than smoothed over. First, https://www.st-andrews.ac.uk/llms.txt returns 200 with content-type text/plain but its body is byte-identical to sitemap.xml - it is an XML sitemap misfiled under an llms.txt name, so no llms.txt credit is taken. Second, https://timetables.st-andrews.ac.uk/ returns 200 on every path including /robots.txt with the same
    24,707-byte Angular shell (title "Publish", a Scientia web-timetabling product): a soft-200 SPA, not a machine surface, and its bundle exposes no institution API endpoint. Third, the Pure OAI-PMH endpoint recorded in this repository since June 2026 is gone - risweb.st-andrews.ac.uk/ws/oai 301s to the portal home page and research-portal /ws/oai 301s to /error/. Two live vendor tenancies remain recorded as relationships: Elsevier Pure for the research portal and SorryApp for the status page. The status API''s three OpenAPI documents and their derived artifacts were removed on 2026-09-01 because the contract is SorryApp''s product template, not St Andrews'' engineering; the repository therefore holds no contract, which is the honest state.'
  evidence:
  - note: OAI-PMH 2.0, repositoryName "St Andrews Research Repository", granularity to the second
    status: 200
    url: https://research-repository.st-andrews.ac.uk/oai/request?verb=Identify
  - note: twelve prefixes including uketd_dc, mods, mets, ore, rdf, marc, etdms
    status: 200
    url: https://research-repository.st-andrews.ac.uk/oai/request?verb=ListMetadataFormats
  - note: community/collection set hierarchy under handle prefix 10023
    status: 200
    url: https://research-repository.st-andrews.ac.uk/oai/request?verb=ListSets
  - note: live SAML metadata, application/xml, entityID https://idp.st-andrews.ac.uk/shibboleth
    status: 200
    url: https://login.st-andrews.ac.uk/idp/shibboleth
  - note: carries uk000278 St Andrews IdP (registered 2008-01-16, Sirtfi) plus the MacTutor SP
    status: 200
    url: http://metadata.ukfederation.org.uk/ukfederation-metadata.xml
  - note: DataCite provider NAHY, consortium_organization, rorId 02wn5qz54, client bl.standrew
    status: 200
    url: https://api.datacite.org/providers/nahy
  - note: single match, member 6332 University of St. Andrews Library, 688 DOIs
    status: 200
    url: https://api.crossref.org/members?query=st+andrews
  - note: active, types education + funder, domain st-andrews.ac.uk
    status: 200
    url: https://api.ror.org/organizations/02wn5qz54
  - note: live; host CNAMEs to a5b404ba.sorryapp.com - SorryApp tenancy, contract not St Andrews'
    status: 200
    url: https://status.st-andrews.ac.uk/api/v1/status
  - note: CNAMEs to standrews.elsevierpure.com - Elsevier Pure tenancy
    status: 200
    url: https://research-portal.st-andrews.ac.uk/
  - note: redirects to /error/ - no Pure web service is publicly reachable
    status: 301
    url: https://research-portal.st-andrews.ac.uk/ws/oai?verb=Identify
  - note: dead - redirects to the research portal home page; pointer removed from this profile
    status: 301
    url: https://risweb.st-andrews.ac.uk/ws/oai?verb=Identify
  - note: body is byte-identical to sitemap.xml - a misfiled sitemap, not an llms.txt
    status: 200
    url: https://www.st-andrews.ac.uk/llms.txt
  - note: Angular SPA shell returned for every path including /robots.txt - soft-200, no API
    status: 200
    url: https://timetables.st-andrews.ac.uk/
  - note: NXDOMAIN
    status: 0
    url: https://api.st-andrews.ac.uk/
  - note: NXDOMAIN
    status: 0
    url: https://data.st-andrews.ac.uk/
  - note: NXDOMAIN
    status: 0
    url: https://opendata.st-andrews.ac.uk/
  - note: NXDOMAIN
    status: 0
    url: https://developer.st-andrews.ac.uk/
  - note: no RFC 9116 security.txt served
    status: 403
    url: https://www.st-andrews.ac.uk/.well-known/security.txt
  - note: University of St Andrews Research Computing, 60 public repos
    status: 200
    url: https://api.github.com/orgs/StAResComp
  reason: no_public_api
  state: none
created: '2026-06-03'
description: 'The University of St Andrews is Scotland''s first university, chartered in 1413 with teaching from 1410, and a public research institution in Fife with ROR identifier https://ror.org/02wn5qz54. It authors no public API and operates no developer portal: probes on 2026-09-01 found no host at api.st-andrews.ac.uk, data.st-andrews.ac.uk, opendata.st-andrews.ac.uk or developer.st-andrews.ac.uk, all four NXDOMAIN. What St Andrews genuinely operates itself, on its own registrable domain, is metadata and identity infrastructure rather than product APIs. Three surfaces are the institution''s own. Its DSpace research repository serves a fully working OAI-PMH 2.0 interface at research-repository.st-andrews.ac.uk/oai/request with twelve metadata formats including the UK electronic-theses profile uketd_dc. Its Shibboleth Identity Provider, entityID https://idp.st-andrews.ac.uk/shibboleth, has been registered in the UK Access Management Federation since January 2008, carries REFEDS Sirtfi
  assurance, and serves its own live SAML metadata at login.st-andrews.ac.uk/idp/shibboleth. And it is an enrolled registrant in the scholarly identifier registries, as DataCite provider NAHY and Crossref member 6332. Everything else that looks like a St Andrews API is a vendor''s contract running under a St Andrews name: the research portal at research-portal.st-andrews.ac.uk is an Elsevier Pure tenancy, and the service status page at status.st-andrews.ac.uk is a SorryApp tenancy. Both are recorded here as tenant relationships, which they are, and neither vendor''s contract is saved under this slug.'
finops:
- name: University Of St Andrews Finops
  service_category: Education
  slug: university-of-st-andrews-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-st-andrews.png
layout: provider
modified: '2026-09-01'
name: University of St Andrews
nav: Providers
network: true
overview: 'University of St Andrews publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Public Research University, and United Kingdom.


  University of St Andrews'' developer surface includes status page, engineering blog, support, and 21 more developer resources.'
plans:
- name: University Of St Andrews Plans Pricing
  plan_count: 2
  slug: university-of-st-andrews-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of St Andrews Rate Limits
  slug: university-of-st-andrews-rate-limits
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.8
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 4.4
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 33.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-st-andrews/refs/heads/main/screenshots/university-of-st-andrews-2026-06-20T200233.png
security:
- kind: domain-security
  name: University Of St Andrews Domain Security
  slug: university-of-st-andrews-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of St Andrews Vulnerability Disclosure
  slug: university-of-st-andrews-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-st-andrews
tags:
- Education
- Higher Education
- University
- Public Research University
- United Kingdom
- Scotland
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Shibboleth
- Persistent Identifiers
website: https://www.st-andrews.ac.uk/
---
