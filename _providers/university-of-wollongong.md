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
api_count: 8
apis:
- description: The University of Wollongong's own SAML 2.0 Identity Provider. Its EntityDescriptor is served publicly and unauthenticated at https://idp.uow.edu.au/idp/shibboleth (HTTP 200, application/xml, 4,358 by
  name: UOW Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: idp-saml-metadata
- description: 'Research Online is UOW''s open access institutional repository, and since its 2025 platform migration it is a Figshare tenancy, not the bepress Digital Commons instance the June 2026 profile recorded. '
  name: Research Online (Figshare tenancy)
  slug: research-online-figshare
- description: UOW Scholars is the university's public researcher-profile portal, running on Symplectic Elements with the Symplectic Discovery front end. scholars.uow.edu.au CNAMEs through uow.discovery.symplectic.o
  name: UOW Scholars (Symplectic Elements / Discovery tenancy)
  slug: uow-scholars-symplectic
- description: The UOW Library runs on the Ex Libris Alma library services platform with the Primo discovery layer, on the institution-specific tenant host uow.primo.exlibrisgroup.com (HTTP 200). Primo and Alma expo
  name: UOW Library Discovery (Ex Libris Primo / Alma tenancy)
  slug: library-primo-alma
- description: The UOW Handbook at courses.uow.edu.au is a Next.js application served from CloudFront on UOW's own registrable domain and backed by an AWS API Gateway at courses.uow.edu.au/api/. Every anonymous requ
  name: UOW Handbook course catalog API (undocumented)
  slug: course-handbook-api
- description: The University of Wollongong is a DataCite consortium organization, symbol UOW, provider id uow, created 2024-08-26, holding the DOI prefix 10.71747 and operating the DataCite repository client uow.fi
  name: DataCite membership (repository uow.figshare)
  slug: datacite-membership
- description: The University of Wollongong Library is Crossref member 5587, holding the DOI prefix 10.14453 with 1,611 registered DOIs (277 current, 1,334 backfile) as of 2026-09-01. The prefix predates the Figshar
  name: Crossref membership (University of Wollongong Library, member 5587)
  slug: crossref-membership
- description: The University of Wollongong is registered in the Research Organization Registry as https://ror.org/00jtmb277 (status active, established 1951), cross-walked to Crossref Funder ID 501100001777, GRID g
  name: ROR registration (00jtmb277)
  slug: ror-registration
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.uow.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.uow.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://ro.uow.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.uow.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://uow.primo.exlibrisgroup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uowits
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-wollongong/
- group: docs
  title: ''
  type: Documentation
  url: https://www.uow.edu.au/about/policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uow.edu.au/about/governance/copyright-and-disclaimer/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uow.edu.au/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.uow.edu.au/about/contacts/
- group: operate
  title: ''
  type: Status
  url: https://www.uow.edu.au/its/scheduled-maintenance/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uow.edu.au/about/governance/academic-integrity/genai-in-assessment/
- group: build
  title: ''
  type: AITooling
  url: https://ltc.uow.edu.au/hub/collection/ai-in-education
- group: company
  title: ''
  type: Blog
  url: https://www.uow.edu.au/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.uow.edu.au/media/rss/
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-wollongong-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-wollongong-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-wollongong-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-wollongong-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-wollongong-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-wollongong-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-wollongong-context.jsonld
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-09-01'
  detail: UOW publishes no API specification and no developer portal, and every callable interface it operates itself is credential-gated. The AWS API Gateway behind the UOW Handbook answers every anonymous path with HTTP 403 "Missing Authentication Token"; the Symplectic Discovery /api mount on scholars.uow.edu.au answers HTTP 403 "Access denied"; and api.uow.edu.au resolves in DNS to a MuleSoft CloudHub endpoint (v4fkkn.aus-s1.cloudhub.io) whose TCP 443 and 80 both time out from the public internet, so an institution API gateway exists but is not publicly reachable. What is public and machine-readable is the SAML 2.0 metadata for UOW's own Shibboleth IdP (HTTP 200, application/xml) plus its DataCite, Crossref and ROR registry records. Research Online and UOW Scholars are Figshare and Symplectic tenancies and their contracts belong to those vendors; ro.uow.edu.au additionally sits behind an AWS WAF challenge (HTTP 202) that blocks anonymous probing of any path, including OAI-PMH.
  evidence:
  - status: 200
    url: https://idp.uow.edu.au/idp/shibboleth
  - status: 200
    url: https://md.aaf.edu.au/aaf-metadata.xml
  - status: 200
    url: https://api.datacite.org/providers/uow
  - status: 200
    url: https://api.crossref.org/members/5587
  - status: 200
    url: https://api.ror.org/v2/organizations/00jtmb277
  - status: 403
    url: https://courses.uow.edu.au/api/search
  - status: 403
    url: https://scholars.uow.edu.au/api/config
  - status: 0
    url: https://api.uow.edu.au/
  - status: 202
    url: https://ro.uow.edu.au/do/oai/?verb=Identify
  - status: 202
    url: https://ro.uow.edu.au/oai?verb=Identify
  - status: 404
    url: https://www.uow.edu.au/llms.txt
  - status: 404
    url: https://www.uow.edu.au/.well-known/security.txt
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'The University of Wollongong (UOW) is a public research university in Wollongong, New South Wales, Australia, established in 1951 (ROR 00jtmb277, GRID grid.1007.6, ISNI 0000 0004 0486 528X). UOW operates no public, self-service developer portal and publishes no API specification: www.uow.edu.au carries no /api, /apis or /developer page across its 5,092-URL sitemap, and there is no llms.txt or .well-known/security.txt. What it does operate that is machine-readable is an identity surface, not a data surface — a Shibboleth SAML 2.0 Identity Provider at idp.uow.edu.au whose EntityDescriptor is served publicly and is registered in the Australian Access Federation aggregate — plus registry memberships in DataCite, Crossref and ROR that carry its own DOI prefixes. Its research and library platforms are vendor tenancies: Research Online (ro.uow.edu.au) is a Figshare instance, UOW Scholars (scholars.uow.edu.au) is a Symplectic Elements/Discovery instance, and library discovery runs
  on Ex Libris Primo/Alma. Two institution-hosted API gateways exist under uow.edu.au — an AWS API Gateway behind the UOW Handbook at courses.uow.edu.au/api and a MuleSoft CloudHub endpoint at api.uow.edu.au — but neither is publicly documented and neither answers an anonymous request.'
finops:
- name: University Of Wollongong Finops
  service_category: Education
  slug: university-of-wollongong-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-wollongong.png
jsonld:
- class_count: 26
  name: University Of Wollongong Context
  property_count: 3
  slug: university-of-wollongong-context
layout: provider
modified: '2026-09-01'
name: University of Wollongong
nav: Providers
network: true
overview: 'University of Wollongong publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Australia, and New South Wales.


  The University of Wollongong catalog on APIs.io includes 1 JSON-LD context.


  University of Wollongong''s developer surface includes documentation, support, status page, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: University Of Wollongong Plans Pricing
  plan_count: 2
  slug: university-of-wollongong-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: University Of Wollongong Rate Limits
  slug: university-of-wollongong-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 12.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 19.1
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
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-wollongong/refs/heads/main/screenshots/university-of-wollongong-2026-06-20T200355.png
security:
- kind: authentication
  name: University Of Wollongong Authentication
  slug: university-of-wollongong-authentication
  summary_line: saml2 · 1 scheme
- kind: domain-security
  name: University Of Wollongong Domain Security
  slug: university-of-wollongong-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-wollongong
tags:
- Education
- Higher Education
- University
- Australia
- New South Wales
- Public Research University
- Identity Federation
- Research Repository
- Library
- Course Catalog
- Open Access
- Persistent Identifiers
website: https://www.uow.edu.au/
---
