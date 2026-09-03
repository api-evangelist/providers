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
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: The Tan Sri Musa Mohamad Library runs a Koha open-source integrated library system whose OPAC is served from koha.ucsiuniversity.edu.my — UCSI's own registrable domain, so the deployment is the instit
  name: UCSI University Library Catalog (Koha)
  slug: library-catalog
- description: UCSI operates a Microsoft Entra ID tenant, 3c5f2d31-81d8-4455-a2bf-531fbc398144, region AS, whose FederationBrandName is "UCSI University" and whose realm for ucsiuniversity.edu.my is NameSpaceType "M
  name: UCSI University Identity Federation (Microsoft Entra ID)
  slug: entra-identity-federation
- description: 'UCSI''s learning management system is a tenancy on CourseNetworking (The CN): the institution host lms.ucsiuniversity.edu.my is a CNAME to ucsi.thecn.com and redirects there with HTTP 301, landing on a'
  name: UCSI University LMS Tenancy (CourseNetworking)
  slug: lms-coursenetworking
- description: UCSI University is registered in the Research Organization Registry as ror.org/019787q29, active, located in Kuala Lumpur, Malaysia, established 1986, typed education and funder, and cross-walked to C
  name: UCSI University ROR Registration
  slug: ror-registration
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.ucsiuniversity.edu.my/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://koha.ucsiuniversity.edu.my/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.microsoftonline.com/ucsiuniversity.edu.my/v2.0/.well-known/openid-configuration
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ucsi-education/
- group: design
  title: ''
  type: Conformance
  url: conformance/ucsi-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucsi-authentication.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ucsi-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsi-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsi-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'UCSI''s own hosts cannot be read by any automated client. Every probe against ucsiuniversity.edu.my and its subdomains on 2026-09-01 returned HTTP 403 from Cloudflare — with a plain client and again with a full Chrome User-Agent, Accept, Accept-Language and Upgrade-Insecure-Requests header set — and the main site''s response carries `cf-mitigated: challenge`. The hosts are LIVE (Google indexes the Koha catalogue as "UCSI University Library catalog"); they are unreadable to us. That is a finding about our access, not a claim that UCSI publishes nothing there, and the Koha OAI-PMH / ILS-DI / REST question is therefore recorded as unverifiable in conformance/ rather than as absent. The surfaces that COULD be read were all read off-host and are all recorded: the Entra ID identity tenant, the CourseNetworking LMS tenancy, the ROR registration, and the confirmed absence of eduGAIN/SIFULAN, Crossref and DataCite records. No contract was saved for any of them, because none of them is
    UCSI''s engineering.'
  evidence:
  - status: 403
    url: https://www.ucsiuniversity.edu.my/
  - status: 403
    url: https://lib.ucsiuniversity.edu.my/
  - status: 403
    url: https://koha.ucsiuniversity.edu.my/
  - status: 403
    url: https://koha.ucsiuniversity.edu.my/cgi-bin/koha/oai.pl?verb=Identify
  - status: 403
    url: https://koha.ucsiuniversity.edu.my/api/v1/
  - status: 403
    url: https://iis.ucsiuniversity.edu.my/
  - status: 403
    url: https://www.ucsiuniversity.edu.my/llms.txt
  - status: 403
    url: https://www.ucsiuniversity.edu.my/.well-known/security.txt
  - status: 200
    url: https://login.microsoftonline.com/ucsiuniversity.edu.my/v2.0/.well-known/openid-configuration
  - status: 200
    url: https://login.microsoftonline.com/3c5f2d31-81d8-4455-a2bf-531fbc398144/federationmetadata/2007-06/federationmetadata.xml
  - status: 200
    url: https://ucsi.thecn.com/
  - status: 200
    url: https://api.ror.org/v2/organizations/019787q29
  - status: 200
    url: https://api.crossref.org/members?query=UCSI
  - status: 200
    url: https://api.datacite.org/clients?query=UCSI
  - status: 200
    url: https://md.seamlessaccess.org/entities/?q=ucsi
  - status: 0
    url: https://api.ucsiuniversity.edu.my/
  - status: 0
    url: https://developer.ucsiuniversity.edu.my/
  - status: 0
    url: https://data.ucsiuniversity.edu.my/
  - status: 0
    url: https://courses.ucsiuniversity.edu.my/
  reason: bot_blocked
  state: unreadable
created: '2026-06-03'
description: 'UCSI University is a private, multi-campus university in Kuala Lumpur, Terengganu and Sarawak, Malaysia, established in 1986 and ranked #265 in the QS World University Rankings 2025. It operates no developer portal, no public API programme, no open data portal, no institutional repository on its own domain and no verifiable public code: the GitHub organisations matching "UCSI" carry no identifying metadata and zero public repositories. Its entire ucsiuniversity.edu.my estate — the main site, the library services site, the Koha catalogue, the IIS student portal, the alumni and mobile hosts — sits behind a Cloudflare bot-management challenge that answers HTTP 403 to every automated client, including one presenting full browser headers, so nothing hosted by the institution can be read programmatically. Three surfaces are nonetheless established off-host: a Microsoft Entra ID tenant (3c5f2d31-81d8-4455-a2bf-531fbc398144, branded "UCSI University") whose SAML 2.0 and OpenID Connect
  metadata are publicly retrievable and which is the institution''s own identity provider; a CourseNetworking learning-management tenancy at ucsi.thecn.com that lms.ucsiuniversity.edu.my redirects into; and a ROR registration. UCSI is NOT in eduGAIN and holds no entity in Malaysia''s SIFULAN federation, and no Crossref or DataCite membership exists under its name. The Koha library catalogue is institution-operated and may expose OAI-PMH, ILS-DI or REST services, but that cannot be confirmed through the bot challenge and is recorded as unverifiable rather than as either present or absent.'
finops:
- name: Ucsi Finops
  service_category: Education
  slug: ucsi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsi.png
jsonld:
- class_count: 12
  name: Ucsi Context
  property_count: 3
  slug: ucsi-context
layout: provider
modified: '2026-09-01'
name: UCSI University
nav: Providers
network: true
overview: 'UCSI University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Private University, and Malaysia.


  The UCSI University catalog on APIs.io includes 1 JSON-LD context.


  UCSI University''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Ucsi Plans Pricing
  plan_count: 2
  slug: ucsi-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Ucsi Rate Limits
  slug: ucsi-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucsi/refs/heads/main/screenshots/ucsi-2026-06-20T195950.png
security:
- kind: authentication
  name: Ucsi Authentication
  slug: ucsi-authentication
  summary_line: oauth2/openIdConnect/saml2 · 2 schemes
- kind: domain-security
  name: Ucsi Domain Security
  slug: ucsi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ucsi
tags:
- Education
- Higher Education
- University
- Private University
- Malaysia
- Asia
- Library
- Library Catalog
- Koha
- Identity Federation
- Learning Management
- Registry
website: https://www.ucsiuniversity.edu.my/
---
