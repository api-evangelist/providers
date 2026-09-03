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
  scored_at: '2026-09-03'
api_count: 7
apis:
- description: IIT Madras's own SAML 2.0 identity provider, entityID https://idp.iitm.ac.in/idp/shibboleth, registered by INFED (the INFLIBNET Access Management Federation) and published into eduGAIN as entity 67269
  name: IIT Madras Shibboleth Identity Provider (INFED / eduGAIN)
  slug: idp
- description: The institute's self-hosted Moodle at courses.iitm.ac.in. Its LTI 1.3 public JWKS at /mod/lti/certs.php returns HTTP 200 application/json with an RS256 signing key and no credentials required; the LTI
  name: IIT Madras Moodle — LTI 1.3 platform and Moodle Web Services
  slug: moodle-lti
- description: A Django REST Framework API operated by AI4Bharat, IIT Madras's language-AI centre, behind the Shoonya data-annotation platform. The API root returns a browsable JSON index of /task/, /annotation/ and
  name: Shoonya annotation platform API (AI4Bharat, IIT Madras)
  slug: shoonya
- description: 'The discussion forum for the IIT Madras BS in Data Science and Applications programme, running on Discourse''s hosted service. Discourse''s JSON API is present at every route — /site.json, /latest.json '
  name: IIT Madras Online Degree community forum (Discourse tenant)
  slug: discourse
- description: IIT Madras's instance of IRINS, the Indian Research Information Network System operated by the INFLIBNET Centre, linked from the Central Library as the institute's research-profile directory. The host
  name: IIT Madras research profiles (IRINS tenant)
  slug: irins
- description: IIT Madras is a Crossref member in its own right — member 49493, primary name "Indian Institute of Technology Madras", location Chennai, Tamil Nadu, India, DOI prefix 10.70002, 11 current DOIs as of 2
  name: Crossref membership (member 49493)
  slug: crossref
- description: IIT Madras is registered in the Research Organization Registry as https://ror.org/03v0r5n49, established 1959, domain iitm.ac.in, with cross-references to Funder ID 501100003845, GRID grid.417969.4, I
  name: ROR registration (03v0r5n49)
  slug: ror
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.iitm.ac.in/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/iit-madras-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iit-madras-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iit-madras-lti-platform.yml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.iitm.ac.in/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://webopac.iitm.ac.in/
- group: other
  title: ''
  type: ResearchRepository
  url: https://iitm.irins.org/
- group: other
  title: ''
  type: AIPolicy
  url: https://cerai.iitm.ac.in/
- group: start
  title: ''
  type: Registry
  url: https://ror.org/03v0r5n49
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iitm.ac.in/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.iitm.ac.in/happenings/press-releases-and-coverages
- group: build
  title: ''
  type: GitHub
  url: https://github.com/IIT-Madras
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/AI4Bharat
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/school/reachiitm/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iit-madras-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iit-madras-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iit-madras-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iit-madras-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/iit-madras-context.jsonld
coverage:
  detail: 'IIT Madras operates real machine-readable surfaces and publishes no contract for any of them. Three are institution-run and were confirmed live on 2026-09-01: the Shibboleth SAML identity provider at idp.iitm.ac.in, registered by INFED and visible in eduGAIN as entity 672697 with scope iitm.ac.in; the self-hosted Moodle at courses.iitm.ac.in, whose LTI 1.3 JWKS is served unauthenticated at HTTP 200 while its web-services REST server returns a structured invalidtoken exception; and the AI4Bharat Shoonya API, whose /task/, /annotation/ and /prediction/ resources all return HTTP 401 with a JSON detail body. The Shoonya drf-yasg docs page renders, but every machine-readable form of that specification — /swagger.json, /swagger.yaml, /swagger/?format=openapi — returns HTTP 500, so no contract could be harvested and none was invented.

    Nothing here is a vendor contract wearing an IIT Madras name. Two surfaces are genuine tenancies and are recorded as relationships rather than as institute contracts: the online-degree Discourse forum, which CNAMEs to iitm.hosted-by-discourse.com and returns 403 not-logged-in on every JSON route, and the IRINS research-profile instance at iitm.irins.org, which is behind a Cloudflare managed challenge — live-but-unreadable to a non-browser client, a limit of our probe rather than a finding about the institute. Two registry memberships are facts about the institution and are kept as such: Crossref member 49493 (prefix 10.70002) and ROR 03v0r5n49. DataCite returns zero providers and zero repositories for IIT Madras.

    The gaps are real and probed, not assumed. api.iitm.ac.in, data.iitm.ac.in, dspace.iitm.ac.in, ir.iitm.ac.in and repository.iitm.ac.in do not resolve. No OAI-PMH endpoint exists: cenlib.iitm.ac.in/oai and webopac.iitm.ac.in/oai/request?verb=Identify both 404, and irepose.iitm.ac.in — the DSpace-CRIS "Knowledge Repository at IIT Madras" still linked from the Central Library — is NXDOMAIN from IIT Madras''s own authoritative nameservers, so the institute''s institutional repository is currently off the air. The library discovery layer at webopac.iitm.ac.in is a live SirsiDynix Enterprise deployment on IIT Madras address space with no RSS or OAI output. www.iitm.ac.in answers 200 for unknown paths with the site homepage, so /sso, /terms-of-use, /sitemap.xml and /.well-known/security.txt are soft-404s; the previously recorded ProductPage pointer to https://www.iitm.ac.in/sso has been removed for exactly that reason.'
  evidence:
  - status: 200
    url: https://technical.edugain.org/api.php?action=list_entities&format=json
  - status: 200
    url: https://idp.iitm.ac.in/
  - status: 403
    url: https://idp.iitm.ac.in/idp/shibboleth
  - status: 200
    url: https://courses.iitm.ac.in/mod/lti/certs.php
  - status: 400
    url: https://courses.iitm.ac.in/mod/lti/token.php
  - status: 200
    url: https://courses.iitm.ac.in/webservice/rest/server.php
  - status: 200
    url: https://backend.shoonya.ai4bharat.org/
  - status: 200
    url: https://backend.shoonya.ai4bharat.org/swagger/
  - status: 500
    url: https://backend.shoonya.ai4bharat.org/swagger.json
  - status: 401
    url: https://backend.shoonya.ai4bharat.org/task/
  - status: 403
    url: https://discourse.onlinedegree.iitm.ac.in/site.json
  - status: 403
    url: https://iitm.irins.org/
  - status: 200
    url: https://api.crossref.org/members/49493
  - status: 200
    url: https://api.ror.org/organizations?query=Indian+Institute+of+Technology+Madras
  - status: 200
    url: https://api.datacite.org/providers?query=Indian+Institute+of+Technology+Madras
  - status: 200
    url: https://webopac.iitm.ac.in/
  - status: 200
    url: https://ai4bharat.iitm.ac.in/
  - status: 200
    url: https://cerai.iitm.ac.in/
  - status: 200
    url: https://www.iitm.ac.in/privacy-policy
  - status: 200
    url: https://www.iitm.ac.in/happenings/press-releases-and-coverages
  - status: 404
    url: https://cenlib.iitm.ac.in/oai
  - status: 404
    url: https://webopac.iitm.ac.in/oai/request?verb=Identify
  - status: 404
    url: https://courses.iitm.ac.in/.well-known/openid-configuration
  - status: 0
    url: https://irepose.iitm.ac.in/
  - status: 0
    url: https://api.iitm.ac.in/
  - status: 0
    url: https://data.iitm.ac.in/
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Indian Institute of Technology Madras is a public institute of technology in Chennai, India, founded in 1959 and consistently ranked first in India''s NIRF engineering rankings. It publishes no developer portal, no open data portal and no OpenAPI, AsyncAPI or other open specification of its own — api.iitm.ac.in does not resolve — but it is not empty, and the June 2026 profile that recorded "no APIs" missed the surfaces it does operate. Three are institution-run and machine readable: a Shibboleth SAML identity provider at idp.iitm.ac.in, registered in the INFLIBNET Access Management Federation (INFED) and flowing into eduGAIN since 2018; a self-hosted Moodle at courses.iitm.ac.in that serves a live, unauthenticated LTI 1.3 JWKS and an LTI Advantage token endpoint alongside the standard Moodle web-services REST server; and the Shoonya annotation platform API run by AI4Bharat, the institute''s language-AI centre, which ships a live drf-yasg documentation surface over a credentialed
  Django REST API. IIT Madras is also a Crossref member (49493, prefix 10.70002) and holds ROR 03v0r5n49. Two further surfaces are real institutional facts running on someone else''s platform and are recorded as tenancies, not as IIT Madras contracts: the online-degree Discourse forum, which CNAMEs to iitm.hosted-by-discourse.com, and the institute''s IRINS research-profile instance at iitm.irins.org, operated by INFLIBNET. Everything callable here is credentialed; the institute''s own institutional repository host, irepose.iitm.ac.in, no longer resolves at all.'
finops:
- name: Iit Madras Finops
  service_category: Education
  slug: iit-madras-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iit-madras.png
jsonld:
- class_count: 15
  name: Iit Madras Context
  property_count: 4
  slug: iit-madras-context
layout: provider
modified: '2026-09-01'
name: Indian Institute of Technology Madras
nav: Providers
network: true
overview: 'Indian Institute of Technology Madras publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Institute of Technology, and Research.


  The Indian Institute of Technology Madras catalog on APIs.io includes 1 JSON-LD context.


  Indian Institute of Technology Madras'' developer surface includes authentication, engineering blog, GitHub presence, and 17 more developer resources.'
plans:
- name: Iit Madras Plans Pricing
  plan_count: 2
  slug: iit-madras-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Iit Madras Rate Limits
  slug: iit-madras-rate-limits
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iit-madras/refs/heads/main/screenshots/iit-madras-2026-06-20T183233.png
security:
- kind: domain-security
  name: Iit Madras Domain Security
  slug: iit-madras-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iit-madras
tags:
- Education
- Higher Education
- University
- Institute of Technology
- Research
- India
- IIT
- Identity Federation
- Learning Management
- Artificial Intelligence
website: https://www.iitm.ac.in/
---
