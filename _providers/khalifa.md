---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://khazna.ku.ac.ae/ws/oai
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata harvesting endpoint for Khazna, Khalifa University's research portal, at https://khazna.ku.ac.ae/ws/oai. Open and anonymous. Identify (probed 2026-09-01, HTTP 200) reports reposit
  name: Khazna OAI-PMH Repository
  slug: khazna-oai-pmh
- description: Khalifa University operates its own Microsoft Entra ID tenant for the ku.ac.ae namespace — tenant id 08fe1c0a-19f5-4f24-a662-fdd5dd460025, getuserrealm.srf reporting NameSpaceType=Managed, DomainName=
  name: Khalifa University Identity Federation (Microsoft Entra ID)
  slug: entra-identity-federation
- description: The university's own web host at www.ku.ac.ae runs WordPress and answers its REST discovery root anonymously — HTTP 200, name "Khalifa University", 17 namespaces, 202 routes (probed 2026-09-01). Acces
  name: Khalifa University Website REST API (WordPress)
  slug: ku-web-rest
- description: 'Khalifa University''s CRIS and research portal, Khazna, is an Elsevier Pure tenancy: khazna.ku.ac.ae is a CNAME to khalifauniversity.elsevierpure.com, which is a CNAME to eu.prod.elsevierpure.com. The '
  name: Khazna Research Portal (Elsevier Pure tenant)
  slug: khazna-pure
- description: Khalifa University's learning management system is an Anthology Blackboard Learn SaaS tenancy named "khalifauni". elearn.ku.ac.ae is a CNAME to khalifauni.blackboard.com, which resolves into learn.5e7
  name: Blackboard Learn (khalifauni tenant)
  slug: blackboard-learn
- description: Library discovery runs on an Ex Libris Primo VE tenancy at khalifa.primo.exlibrisgroup.com with view id 971KUOSTAR_INST:KU — the institution code still carrying the legacy KUSTAR name. Probed 2026-09-
  name: Library Discovery (Ex Libris Primo VE tenant)
  slug: primo-discovery
- description: Three Springshare tenancies serve the Khalifa University library. library.ku.ac.ae is a CNAME to region-us.libguides.com (LibGuides; page title "Library Home - LibGuides at Khalifa University of Scien
  name: Library Web, Calendar and Reference (Springshare tenant)
  slug: springshare
- description: Off-campus access to licensed library resources runs on an OCLC EZproxy tenancy under the named account khalifa.idm.oclc.org (HTTP 200 on /login, probed 2026-09-01). Proxied database links appear thro
  name: Off-Campus Access (OCLC EZproxy tenant)
  slug: ezproxy
- description: Khalifa University of Science and Technology is registered in the Research Organization Registry as https://ror.org/05hffr360, with the alternate names KUSTAR and Khalifa University and country United
  name: ROR Registration
  slug: ror
- description: Public open-source repositories from the Khalifa University Center for Autonomous Robotic Systems (KUCARS) — 71 public repos covering coverage path planning, soft manipulator dynamics, collision detec
  name: KUCARS Open-Source Robotics Research (GitHub)
  slug: kucars
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.ku.ac.ae
- group: company
  title: ''
  type: Blog
  url: https://www.ku.ac.ae/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ku.ac.ae/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.ku.ac.ae/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ku.ac.ae/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ku.ac.ae/disclaimer
- group: other
  title: ''
  type: ResearchRepository
  url: https://khazna.ku.ac.ae
- group: build
  title: ''
  type: LibraryCatalog
  url: https://khalifa.primo.exlibrisgroup.com/discovery/search?vid=971KUOSTAR_INST:KU
- group: build
  title: ''
  type: Library
  url: https://library.ku.ac.ae/lib
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.microsoftonline.com/ku.ac.ae/v2.0/.well-known/openid-configuration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kucars
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/khalifauniversity/
- group: auth
  title: ''
  type: Authentication
  url: authentication/khalifa-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/khalifa-education-standards-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/khalifa-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/khalifa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/khalifa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/khalifa-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Khalifa University of Science and Technology is a research-intensive public university in Abu Dhabi, United Arab Emirates (ROR 05hffr360), formed from the 2017 merger of KUSTAR, the Masdar Institute and the Petroleum Institute. Its programmable footprint is small, real, and almost entirely indirect. Two surfaces are genuinely institution-operated: an OAI-PMH 2.0 endpoint for the Khazna research portal at khazna.ku.ac.ae/ws/oai, live and anonymous with an institution admin contact, and the university''s own Microsoft Entra ID tenant for the ku.ac.ae namespace, which issues OpenID Connect and SAML 2.0 for institution systems. A third, partial surface is the WordPress REST API on www.ku.ac.ae, whose discovery root and a handful of routes answer publicly while the core collections are closed with HTTP 401. Everything else a search turns up is a vendor contract running under the university''s name: Khazna itself is an Elsevier Pure tenant (khazna.ku.ac.ae CNAMEs to khalifauniversity.elsevierpure.com)
  and Elsevier''s own Pure API spec is served from that host; the LMS is a Blackboard Learn tenant behind elearn.ku.ac.ae; discovery is Ex Libris Primo VE; the library web presence, calendar and ask-a-librarian service are Springshare; off-campus access is OCLC EZproxy. Those relationships are recorded here as tenancies. None of their contracts are catalogued as Khalifa''s. There is no central developer portal, no published API program, no open-data portal, and no institution-operated API reference.'
examples:
- key_count: 3
  name: Khalifa Entra Openid Configuration
  slug: khalifa-entra-openid-configuration
finops:
- name: Khalifa Finops
  service_category: Education
  slug: khalifa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/khalifa.png
jsonld:
- class_count: 14
  name: Khalifa Context
  property_count: 2
  slug: khalifa-context
layout: provider
modified: '2026-09-01'
name: Khalifa University
nav: Providers
network: true
overview: 'Khalifa University publishes 1 API on the [APIs.io](https://apis.io/) network: Khazna OAI-PMH Repository. Tagged areas include University, Higher Education, Education, Research, and Research Data.


  The Khalifa University catalog on APIs.io includes 1 JSON-LD context.


  Khalifa University''s developer surface includes engineering blog, support, authentication, and 16 more developer resources.'
plans:
- name: Khalifa Plans Pricing
  plan_count: 2
  slug: khalifa-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Khalifa Rate Limits
  slug: khalifa-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 22.0
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/khalifa/refs/heads/main/screenshots/khalifa-2026-06-20T184031.png
security:
- kind: authentication
  name: Khalifa Authentication
  slug: khalifa-authentication
  summary_line: none/oauth2/saml/apiKey · 7 schemes
- kind: domain-security
  name: Khalifa Domain Security
  slug: khalifa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: khalifa
tags:
- University
- Higher Education
- Education
- Research
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- Robotics
- United Arab Emirates
- Abu Dhabi
website: https://www.ku.ac.ae
---
