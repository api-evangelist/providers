---
access_model:
  confidence: high
  label: No self-service access - institutional affiliation or federation membership required
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 10
apis:
- description: api.exeter.ac.uk is an institution-operated AWS API Gateway deployment in eu-west-2 that serves the MyExeter student app (the Flutter PWA at m.exeter.ac.uk and the iOS and Android builds). Routes evid
  name: MyExeter Platform API
  slug: myexeter-platform-api
- description: Exeter operates its own SAML 2.0 Shibboleth identity provider with entityID https://elibrary.exeter.ac.uk/idp/shibboleth. The IdP publishes its own metadata directly (200, application/xml, 10,370 byte
  name: University of Exeter Shibboleth Identity Provider
  slug: shibboleth-idp
- description: Exeter runs a Microsoft Entra ID tenant (912a5d77-fb98-4eee-af32-1334d8f04a53) used for staff and student single sign-on; mytimetable.exeter.ac.uk redirects into it over SAML 2.0. The tenant publishes
  name: University of Exeter Microsoft Entra ID Tenant
  slug: entra-id-tenant
- description: 'ELE is Exeter''s virtual learning environment, a Moodle deployment on the institution''s own host ele.exeter.ac.uk. Two machine-readable surfaces are live: the Moodle Web Services REST endpoint at /webs'
  name: Exeter Learning Environment (ELE) - Moodle Web Services and LTI 1.3 Platform
  slug: ele-moodle
- description: 'The public WordPress REST API (wp-json) of the University of Exeter website at news.exeter.ac.uk: the route index of the site''s content management system, catalogued as one site surface rather than as'
  name: University of Exeter Website (WordPress REST)
  slug: news-exeter-ac-uk-website-wordpress-rest
- description: Open Research Exeter is Exeter's institutional research repository and it is a Figshare tenancy, not institution-run software. ore.exeter.ac.uk is a CNAME to proxy-eu-01.figshare.com; the host's AWS W
  name: Open Research Exeter (ORE) - Figshare Tenancy
  slug: ore-figshare-tenancy
- description: experts.exeter.ac.uk is the university's staff expertise, publications and research output directory, and Exeter's own llms.txt names it as the authoritative source for attributing research to named a
  name: Exeter Experts Directory - Symplectic Elements Discovery Tenancy
  provenance: unpublished
  slug: experts-symplectic-tenancy
- description: Exeter is a registered DataCite member - provider symbol VUEX, name "University of Exeter", memberType consortium_organization, rorId https://ror.org/03yghzc09, created 2020-09-01, with its DataCite c
  name: DataCite Membership and Open Research Exeter DOI Registration
  slug: datacite-membership
- description: The university's publishing arm is a Crossref member - member id 27616, primary name "University of Exeter Press" - registering DOIs under prefixes 10.58182 and 10.47788. This is an institutional memb
  name: University of Exeter Press Crossref Membership
  slug: crossref-membership
- description: Exeter is registered in the Research Organization Registry with ROR identifier https://ror.org/03yghzc09, the identifier DataCite carries on the institution's VUEX provider record. ROR's API is ROR's;
  name: University of Exeter ROR Registration
  slug: ror-registration
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.exeter.ac.uk/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.exeter.ac.uk/llms.txt
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Uni-of-Exeter
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Uni-of-Exeter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Uni-of-Exeter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-exeter/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UniofExeter
- group: company
  title: ''
  type: Blog
  url: https://news.exeter.ac.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.exeter.ac.uk/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exeter.ac.uk/about/oursite/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exeter.ac.uk/about/oursite/copyright/
- group: other
  title: ''
  type: Accessibility
  url: https://www.exeter.ac.uk/about/oursite/accessibility/
- group: other
  title: ''
  type: DataProtection
  url: https://www.exeter.ac.uk/about/oursite/dataprotection/
- group: auth
  title: ''
  type: Authentication
  url: https://libguides.exeter.ac.uk/eresources/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://elibrary.exeter.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://ore.exeter.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.exeter.ac.uk/departments/library
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.exeter.ac.uk/undergraduate-degrees/
- group: other
  title: ''
  type: OpenData
  url: https://news.exeter.ac.uk/wp-json/
- group: auth
  href: https://artifacts.apis.io/university-of-exeter/security/university-of-exeter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-exeter-domain-security.yml
- group: design
  href: https://artifacts.apis.io/university-of-exeter/conformance/university-of-exeter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-exeter-conformance.yml
- group: auth
  href: https://artifacts.apis.io/university-of-exeter/authentication/university-of-exeter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-exeter-authentication.yml
- group: design
  href: https://artifacts.apis.io/university-of-exeter/errors/university-of-exeter-errors.yml
  title: ''
  type: Errors
  url: errors/university-of-exeter-errors.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-exeter/plans/university-of-exeter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-exeter-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/university-of-exeter/rate-limits/university-of-exeter-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-exeter-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-exeter/finops/university-of-exeter-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-exeter-finops.yml
- group: design
  href: https://artifacts.apis.io/university-of-exeter/json-ld/university-of-exeter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/university-of-exeter-context.jsonld
- group: other
  href: https://artifacts.apis.io/university-of-exeter/review.yml
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-09-01'
  detail: Exeter operates a real institution-owned API - api.exeter.ac.uk, an AWS API Gateway deployment in eu-west-2 behind the MyExeter app - but every one of its routes is OAuth2/Cognito gated and returns 401, no documentation, registration path or specification is published anywhere on exeter.ac.uk, and there is no developer portal (developer.exeter.ac.uk and developers.exeter.ac.uk do not resolve). Its identity federation, Moodle web services and news WordPress REST API are readable but are upstream contracts (Shibboleth, Moodle, WordPress) rather than Exeter-authored ones, so no OpenAPI is saved under this institution. Its research repository ore.exeter.ac.uk is a Figshare tenancy sitting behind an AWS WAF challenge that returns 202 with a zero-length body to every client, so it is unreadable as well as vendor-contracted. No specification, no self-service credential, no public contract - the footprint is real but entirely credentialed.
  evidence:
  - status: 401
    url: https://api.exeter.ac.uk/content/posts/news
  - status: 401
    url: https://api.exeter.ac.uk/spaces/get-occupancy-data
  - status: 400
    url: https://api.exeter.ac.uk/application-settings
  - status: 403
    url: https://api.exeter.ac.uk/openapi.json
  - status: 200
    url: https://elibrary.exeter.ac.uk/idp/shibboleth
  - status: 200
    url: https://ele.exeter.ac.uk/mod/lti/certs.php
  - status: 200
    url: https://ele.exeter.ac.uk/webservice/rest/server.php
  - status: 200
    url: https://news.exeter.ac.uk/wp-json/
  - status: 200
    url: https://www.exeter.ac.uk/llms.txt
  - status: 202
    url: https://ore.exeter.ac.uk/repository/oai/request?verb=Identify
  - status: 200
    url: https://experts.exeter.ac.uk/ws/api
  - status: 200
    url: https://api.datacite.org/clients/bl.exeter
  reason: auth-required
  state: gated
created: '2026-06-03'
description: 'The University of Exeter is a public research university in Devon, United Kingdom, and a member of the Russell Group, with campuses at Streatham and St Luke''s in Exeter and Penryn in Cornwall. It operates no public developer portal and publishes no OpenAPI, and most of what appears to be an Exeter API is a vendor platform running under an exeter.ac.uk hostname. What Exeter genuinely operates is: a Cognito-protected platform API at api.exeter.ac.uk behind the MyExeter app (campus events, space occupancy, notifications, profile - every route returns 401 without a token and none are documented); its own Shibboleth SAML identity provider, published in both the UK Access Management Federation and InCommon/eduGAIN metadata; a Microsoft Entra ID tenant fronting SSO for timetabling; a Moodle VLE at ele.exeter.ac.uk that is a live LTI 1.3 platform and exposes Moodle''s own web-service endpoint; and a public WordPress REST API on its news site. Its research repository Open Research
  Exeter is a Figshare tenancy, and its expert profiles are a Symplectic Elements tenancy - neither contract is Exeter''s engineering. Exeter also maintains a hand-authored llms.txt with explicit guidance for agents, which is rare in this cohort.'
finops:
- has_sources: true
  method: derived
  name: University Of Exeter Finops
  primary_unit: ''
  service_category: Education
  slug: university-of-exeter-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-exeter.png
jsonld:
- class_count: 17
  name: University Of Exeter Context
  property_count: 9
  slug: university-of-exeter-context
layout: provider
modified: '2026-09-01'
name: University of Exeter
nav: Providers
network: true
overview: 'University of Exeter is listed with 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and United Kingdom.


  The University of Exeter catalog on APIs.io includes 1 JSON-LD context.


  University of Exeter''s developer surface includes GitHub presence, engineering blog, support, authentication, and 24 more developer resources.'
plans:
- name: University Of Exeter Plans Pricing
  plan_count: 2
  slug: university-of-exeter-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Exeter Rate Limits
  slug: university-of-exeter-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 69.6
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 26.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/university-of-exeter/university-of-exeter-2026-06-20T200146.png
security:
- kind: authentication
  name: University Of Exeter Authentication
  slug: university-of-exeter-authentication
  summary_line: oauth2/openIdConnect/saml2/token · 5 schemes
- kind: domain-security
  name: University Of Exeter Domain Security
  slug: university-of-exeter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-exeter
tags:
- University
- Higher Education
- Education
- Research
- United Kingdom
- Russell Group
- Identity Federation
- Research Repository
- LMS
- Campus Life
website: https://www.exeter.ac.uk/
---
