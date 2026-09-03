---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
  scored_at: '2026-09-02'
api_count: 7
apis:
- description: 'The University of Sydney''s federation entity serves signed SAML 2.0 metadata from federation.sydney.edu.au: entityID https://federation.sydney.edu.au/idp/shibboleth, an IDPSSODescriptor advertising ur'
  name: Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: Sydney eScholarship is the university's own institutional repository, running on the university-owned usyd.edu.au domain (usyd.edu.au redirects to www.sydney.edu.au). It is a registered DataCite repos
  name: Sydney eScholarship Repository (institutional repository, OAI-PMH)
  slug: escholarship-repository
- description: CUSP is the University of Sydney's own course and unit-of-study catalog, served from cusp.sydney.edu.au behind Cloudflare and cross-linked from the sydney.edu.au course and unit finders. It is the reg
  name: CUSP — Course & Unit of Study Portal
  slug: cusp-course-catalog
- description: The myUni student portal runs on the university's own domain, served through CloudFront, and is backed by internal JSON endpoints consumed by the authenticated student single-page application. Those e
  name: myUni Student Portal (session-gated internal APIs)
  slug: myuni
- description: api.sydney.edu.au resolves in DNS to usyd-lb-p.lb.anypointdns.net — a MuleSoft Anypoint Platform dedicated load balancer named for the University of Sydney production environment — which is direct evi
  name: api.sydney.edu.au — MuleSoft Anypoint gateway (not publicly reachable)
  slug: anypoint-gateway
- description: The University of Sydney Library runs on the Ex Libris Alma library services platform with the Primo VE discovery layer, on the institution-specific tenant sydney.primo.exlibrisgroup.com (view id 61US
  name: Library Discovery — Ex Libris Primo VE / Alma (tenant)
  slug: primo-alma
- description: 'canvas.sydney.edu.au is a vanity hostname on the university''s own domain that CNAMEs to sydney-vanity.instructure.com, and it redirects unauthenticated visitors into the university''s Okta tenant with '
  name: Canvas LMS (tenant)
  slug: canvas-lms
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.sydney.edu.au/
- group: company
  title: ''
  type: Blog
  url: https://educational-innovation.sydney.edu.au/teaching@sydney/
- group: company
  title: ''
  type: News
  url: https://www.sydney.edu.au/news-opinion/latest-news.html
- group: operate
  title: ''
  type: Support
  url: https://www.sydney.edu.au/contact-us.html
- group: start
  title: ''
  type: ServicePortal
  url: https://sydneyuni.service-now.com/sm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sydney.edu.au/disclaimer.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sydney.edu.au/about-us/governance-and-structure/privacy-and-university-information/privacy-at-the-university/privacy-notices/website-privacy-collection-notice.html
- group: other
  title: ''
  type: Governance
  url: https://www.sydney.edu.au/about-us/governance-and-structure/university-policies.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sydney-Informatics-Hub
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-sydney/
- group: other
  title: ''
  type: IdentityFederation
  url: https://federation.sydney.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://ses.library.usyd.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://sydney.primo.exlibrisgroup.com/
- group: build
  title: ''
  type: Library
  url: https://www.library.sydney.edu.au/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://cusp.sydney.edu.au/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.sydney.edu.au/research/facilities/sydney-informatics-hub.html
- group: other
  title: ''
  type: AIPolicy
  url: https://www.sydney.edu.au/students/academic-integrity/artificial-intelligence.html
- group: build
  title: ''
  type: AITooling
  url: https://cogniti.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-sydney-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-sydney-education-standards.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-sydney-organization.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-sydney-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-sydney-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-sydney-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-sydney-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: The University of Sydney operates real institutional surfaces but publishes none of them for third-party consumption. The one machine-readable artifact it serves openly is SAML 2.0 identity-provider metadata, which is consumable only by federation members. Its institutional repository documents an OAI-PMH interface on its own host but answers 403 to every automated client behind Cloudflare bot management. Its course catalog is HTML only. Its student portal APIs require a session. Its MuleSoft Anypoint production gateway resolves in DNS but filters TCP 443 from the public internet. Its library, LMS and sign-in run on Ex Libris, Instructure and Okta tenants whose contracts belong to those vendors. No OpenAPI, no developer portal, no credential self-service, no llms.txt and no security.txt were found — sydney.edu.au serves a soft-404 (HTTP 200 redirecting to /errors/404.html) for both well-known paths, so neither is credited. This is a correct thin profile, not a failed harvest.
  evidence:
  - note: Live SAML 2.0 / Shibboleth IdP metadata, application/xml, 4506 bytes. Hosted by AAF (CNAME to idp-cname.aaf.edu.au, CloudFront + ALB + Jetty 12.1.0, Amazon-issued cert), so the operator is tenant even though the hostname is the institution's.
    status: 200
    url: https://federation.sydney.edu.au/idp/shibboleth
  - note: Australian Access Federation aggregate contains the Sydney IdP entity.
    status: 200
    url: https://md.aaf.edu.au/aaf-metadata.xml
  - note: eduGAIN interfederation aggregate contains federation.sydney.edu.au.
    status: 200
    url: https://mds.edugain.org/edugain-v2.xml
  - note: Cloudflare bot management; blocked to default UA, browser UA and XML Accept header alike.
    status: 403
    url: https://ses.library.usyd.edu.au/oai/request?verb=Identify
  - note: Same host answers robots.txt — the repository is live, we are blocked from it.
    status: 200
    url: https://ses.library.usyd.edu.au/robots.txt
  - note: DataCite client ARDCX.USYD "Sydney eScholarship", 2146 DOIs, @sydney.edu.au contacts.
    status: 200
    url: https://api.datacite.org/clients/ardcx.usyd
  - note: Crossref member "The University of Sydney Library", prefix 10.30722, 654 DOIs.
    status: 200
    url: https://api.crossref.org/members/12184
  - note: Institution course/unit catalog, HTML only; no JSON or feed representation found.
    status: 200
    url: https://cusp.sydney.edu.au/
  - note: Student portal; backing JSON endpoints require an authenticated session.
    status: 200
    url: https://myuni.sydney.edu.au/
  - note: DNS resolves to usyd-lb-p.lb.anypointdns.net (MuleSoft Anypoint production LB, 13.210.51.115 / 13.55.148.172); TCP 443 filtered, HTTP and HTTPS both time out.
    status: 0
    url: https://api.sydney.edu.au/
  - note: Soft-404 — 200 redirecting to /errors/404.html. No llms.txt. Not credited.
    status: 200
    url: https://www.sydney.edu.au/llms.txt
  - note: Soft-404 — 200 redirecting to /errors/404.html. No security.txt. Not credited.
    status: 200
    url: https://www.sydney.edu.au/.well-known/security.txt
  - note: Funnelback JSON output not exposed; only the HTML search page responds.
    status: 502
    url: https://www.sydney.edu.au/s/search.json?collection=Usyd&query=library
  - note: AWS WAF challenge on a Figshare wildcard host. NOT the University of Sydney's repository — the Sydney-region Figshare customer is UTS (uts.figshare.com). Rejected as vendor; no Figshare contract saved under this slug.
    status: 202
    url: https://sydney.figshare.com/
  - note: NXDOMAIN — no institutional open data portal.
    status: 0
    url: https://data.sydney.edu.au/
  - note: NXDOMAIN — no developer portal.
    status: 0
    url: https://developer.sydney.edu.au/
  reason: no_public_developer_program
  state: gated
created: '2026-06-03'
description: The University of Sydney is Australia's first university, founded in 1850, a Group of Eight member and ranked in the QS world top 40. Its programmable footprint is small, and most of what looks like a University of Sydney API is a vendor's contract running under the university's name. Re-profiled on 2026-08-19 with operator attribution settled first, the institution operates no public developer portal, publishes no OpenAPI, and offers no self-service developer credential. The only openly machine-readable artifact served under a University of Sydney hostname is SAML 2.0 federation metadata at federation.sydney.edu.au — and even that is a tenant surface, because the host CNAMEs to the Australian Access Federation's hosted Rapid IdP. The entity, scope and signing key are the university's; the infrastructure is AAF's. Beyond that it operates the Sydney eScholarship institutional repository (a DataCite repository client with 2,146 DOIs, whose documented OAI-PMH endpoint is currently
  behind Cloudflare bot management), the CUSP course and unit-of-study catalog as HTML only, the myUni student portal on session-gated internal JSON endpoints, and a MuleSoft Anypoint API gateway at api.sydney.edu.au whose production load balancer resolves in DNS but refuses connections from the public internet. Its library discovery, learning management and identity brokering all run on vendor platforms — Ex Libris Primo/Alma, Instructure Canvas and Okta — where the data is the university's and the contract is not. An earlier profile of this cohort risked attributing a Figshare repository here; sydney.figshare.com was checked and is not the University of Sydney's, and no Figshare contract has been saved under this slug.
finops:
- name: University Of Sydney Finops
  service_category: Education
  slug: university-of-sydney-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-sydney.png
jsonld:
- class_count: 9
  name: University Of Sydney Context
  property_count: 9
  slug: university-of-sydney-context
- class_count: 0
  name: University Of Sydney Organization Context
  property_count: 0
  slug: university-of-sydney-organization
layout: provider
modified: '2026-08-19'
name: University of Sydney
nav: Providers
network: true
overview: 'University of Sydney publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Australia, and Group of Eight.


  The University of Sydney catalog on APIs.io includes 2 JSON-LD contexts.


  University of Sydney''s developer surface includes engineering blog, product news, support, authentication, and 22 more developer resources.'
plans:
- name: University Of Sydney Plans Pricing
  plan_count: 2
  slug: university-of-sydney-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Sydney Rate Limits
  slug: university-of-sydney-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 30.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-sydney/refs/heads/main/screenshots/university-of-sydney-2026-06-20T200254.png
security:
- kind: authentication
  name: University Of Sydney Authentication
  slug: university-of-sydney-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: University Of Sydney Domain Security
  slug: university-of-sydney-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-sydney
tags:
- University
- Higher Education
- Education
- Australia
- Group of Eight
- Research
- Identity Federation
- Research Repository
- Course Catalog
- Library
website: https://www.sydney.edu.au/
---
