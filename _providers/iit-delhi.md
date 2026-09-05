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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: IIT Delhi runs its own Shibboleth identity provider at idp.iitd.ac.in and self-publishes its SAML 2.0 metadata as a machine-readable EntityDescriptor. The document names the institute as the organisat
  name: IIT Delhi Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: idp-shibboleth
- description: 'OAI-PMH 2.0 metadata-harvesting interface for the IIT Delhi DSpace 8 institutional repository, on the institute''s own host. Verified functional on 2026-08-30, not merely mounted: Identify, ListMetadat'
  name: IIT Delhi Institutional Repository OAI-PMH
  slug: oai-pmh
- baseURL: https://convocation.iitd.ac.in/api
  baseurl_source: declared
  description: Undocumented JSON API behind the shared React/Express site platform IIT Delhi runs across departmental and unit subdomains. Anonymous reads were confirmed on 2026-08-30 across three deployments — conv
  name: IIT Delhi Departmental Site Platform API
  slug: site-platform
- description: The IIT Delhi Central Library institutional repository runs on DSpace 8.0 and exposes the standard DSpace REST/HAL API at /server/api on the institute's own host. The root endpoint is public and adver
  name: IIT Delhi Institutional Repository DSpace REST API
  slug: dspace-rest
- description: IIT Delhi operates an OAuth 2 authorization server that lets developers register their own campus apps and authenticate users with IIT Delhi credentials, and it is the real gate for the institute's ow
  name: IIT Delhi OAuth 2 Authentication Server
  slug: oauth2
- description: 'IIT Delhi self-hosts Moodle for the 2025-2026 academic year at moodle.iitd.ac.in, and its web-services endpoint is live: an anonymous call to /webservice/rest/server.php returns Moodle''s structured in'
  name: IIT Delhi Moodle Web Services
  slug: moodle-webservices
- description: IIT Delhi's research information management portal is an institution-specific tenant on IRINS, the Indian Research Information Network System operated by the INFLIBNET Centre, an Inter-University Cent
  name: IIT Delhi Research Profiles on IRINS
  slug: irins
- description: 'Backend API for IITD Connect, the student-built IIT Delhi campus app maintained by DevClub, documented via Postman with User, Event, Club/Hostel/Body, News and Calendar collections and a bearer-token '
  name: IITD Connect API (DevClub) — retired
  slug: iitd-connect
artifact_total: 16
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/devclub-iitd/IITDConnectServer/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://home.iitd.ac.in/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.iitd.ac.in/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://ir.iitd.ac.in/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.iitd.ac.in/
- group: other
  title: ''
  type: AIPolicy
  url: https://academics.iitd.ac.in/wp-content/uploads/2025/09/IITD-AI-Guidelines.pdf
- group: auth
  title: ''
  type: Authentication
  url: https://oauth.iitd.ac.in/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iit-delhi
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/devclub-iitd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/iitdelhi/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/iit-delhi-site-platform-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iit-delhi-site-platform-schemas.json
- group: build
  title: ''
  type: Examples
  url: examples/iit-delhi-site-platform-examples.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/iit-delhi-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/iit-delhi-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iit-delhi-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iit-delhi-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iit-delhi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iit-delhi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iit-delhi-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'IIT Delhi is genuinely thin, and the thinness is a documentation gap rather than an absence of surfaces. Five institution-operated machine-readable surfaces were confirmed live on 2026-08-30 — a Shibboleth SAML 2.0 identity provider, an OAI-PMH 2.0 harvesting endpoint, a DSpace 8 REST API, a Moodle web-service endpoint and an undocumented departmental JSON API — and the institute documents none of them. The two that would most repay description are gated: the OAuth 2 apps server at oauth.iitd.ac.in is entirely behind an interactive login and returns 404 for both OpenID Connect discovery and RFC 8414 authorization-server metadata, so its endpoints, grants and scopes are unreadable from outside; and the DSpace content endpoints return 401 to anonymous callers even though the root document and discovery search are public. No contract in this repo is a vendor''s, and none was saved from a vendor host. The one tenant relationship recorded — IIT Delhi''s research information portal
    on INFLIBNET''s IRINS platform — sits behind a Cloudflare bot challenge and was confirmed by name from third-party sources rather than read directly.'
  evidence:
  - status: 200
    url: https://idp.iitd.ac.in/idp/shibboleth
  - status: 200
    url: https://ir.iitd.ac.in/server/oai/request?verb=Identify
  - status: 200
    url: https://ir.iitd.ac.in/server/api
  - status: 401
    url: https://ir.iitd.ac.in/server/api/core/items
  - status: 200
    url: https://oauth.iitd.ac.in/
  - status: 404
    url: https://oauth.iitd.ac.in/.well-known/openid-configuration
  - status: 404
    url: https://oauth.iitd.ac.in/.well-known/oauth-authorization-server
  - status: 200
    url: https://convocation.iitd.ac.in/api/news
  - status: 401
    url: https://convocation.iitd.ac.in/api/gallery
  - status: 200
    url: https://moodle.iitd.ac.in/webservice/rest/server.php
  - status: 403
    url: https://iitd.irins.org/
  - status: 302
    url: http://api.devclub.in/
  - status: 404
    url: https://home.iitd.ac.in/.well-known/security.txt
  - status: 404
    url: https://home.iitd.ac.in/llms.txt
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Indian Institute of Technology Delhi (IIT Delhi) is a public technical and research university in Hauz Khas, New Delhi — an Institute of National Importance and an Institution of Eminence, ranked #118 in the QS World University Rankings 2025. IIT Delhi operates no developer portal, publishes no API documentation, no OpenAPI, no terms of service for machine access and no security.txt or llms.txt, and nothing in this profile was published by the institute as a developer-facing product. What it does operate, and what this profile records, is a small set of genuinely institution-run machine-readable surfaces found by probing its own domain: a Shibboleth SAML 2.0 identity provider at idp.iitd.ac.in whose metadata is self-published and registered in the Indian access-management federation INFED and interfederated through eduGAIN since 2020 — the institute''s strongest and least-known standards conformance; a DSpace 8 institutional repository at ir.iitd.ac.in with a functional OAI-PMH
  2.0 harvesting endpoint advertising thirteen metadata formats; an OAuth 2 apps server at oauth.iitd.ac.in that lets campus developers register applications but publishes no discovery document, endpoint list or scope vocabulary; a Moodle deployment whose web-service endpoint answers but is token-gated; and an undocumented JSON API behind the shared React/Express site platform its departments run, which answers anonymous reads on convocation.iitd.ac.in, ird.iitd.ac.in and csc.iitd.ac.in. Its research information system is a tenant on INFLIBNET''s national IRINS platform, and its library discovery runs through the DELNET consortium — both real institutional facts, neither IIT Delhi''s engineering. The 2019-era student DevClub API that earlier profiles listed as a surface is dead: its host redirects to a domain that no longer resolves and its TLS certificate expired in August 2025.'
examples:
- key_count: 2
  name: Iit Delhi Site Platform Examples
  slug: iit-delhi-site-platform-examples
finops:
- name: Iit Delhi Finops
  service_category: Education
  slug: iit-delhi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iit-delhi.png
json_schemas:
- name: IIT Delhi Departmental Site Platform — response schemas
  property_count: 0
  slug: iit-delhi-site-platform-schemas
jsonld:
- class_count: 20
  name: Iit Delhi Context
  property_count: 4
  slug: iit-delhi-context
layout: provider
modified: '2026-08-30'
name: Indian Institute of Technology Delhi
nav: Providers
network: true
overview: 'Indian Institute of Technology Delhi publishes 1 API on the [APIs.io](https://apis.io/) network: IIT Delhi Departmental Site Platform API. Tagged areas include Education, Higher Education, University, Institute of Technology, and Research.


  The Indian Institute of Technology Delhi catalog on APIs.io includes 1 JSON-LD context.


  Indian Institute of Technology Delhi''s developer surface includes authentication, code examples, and 19 more developer resources.'
plans:
- name: Iit Delhi Plans Pricing
  plan_count: 2
  slug: iit-delhi-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Iit Delhi Rate Limits
  slug: iit-delhi-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 28.6
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 26.8
  provenance:
    conformance: derived
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
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iit-delhi/refs/heads/main/screenshots/iit-delhi-2026-06-20T183235.png
security:
- kind: authentication
  name: Iit Delhi Authentication
  slug: iit-delhi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Iit Delhi Domain Security
  slug: iit-delhi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iit-delhi
tags:
- Education
- Higher Education
- University
- Institute of Technology
- Research
- India
- Open Access
- Library
- Research Repository
- Identity Federation
website: https://home.iitd.ac.in/
---
