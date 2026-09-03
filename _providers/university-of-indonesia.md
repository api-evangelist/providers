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
  scored_at: '2026-09-03'
api_count: 8
apis:
- description: api.ui.ac.id is a Kong Enterprise 3.3.1.0 API gateway operated by the university on its own network. Every probed path — /, /v1, /status, /docs, /openapi.json, /oauth2/token, /.well-known/openid-confi
  name: UI API Gateway (Kong Enterprise)
  slug: api-gateway
- description: Sistem Akun UI, the university-wide Single Sign-On, implemented with the Apereo CAS protocol at sso.ui.ac.id. https://sso.ui.ac.id/ redirects to /cas/login and returns a live CAS login form (title "SS
  name: SSO UI (CAS Single Sign-On)
  slug: sso-cas
- description: 'EMAS2 (E-learning Management System) at emas2.ui.ac.id is an institution-hosted Moodle instance. Three machine surfaces answer anonymously and identify themselves as live-but-gated rather than absent:'
  name: EMAS2 Learning Platform (Moodle Web Services + LTI 1.3)
  slug: emas2-moodle
- description: 'OAI-PMH 2.0 metadata-harvesting interface for UI Scholars Hub, the university''s institutional research repository. Verified live: ?verb=Identify returns repositoryName "UI Scholars Hub", protocolVersi'
  name: UI Scholars Hub OAI-PMH (bepress Digital Commons tenant)
  slug: scholarhub-oai
- description: 'scholar.ui.ac.id is University of Indonesia''s Elsevier Pure Portal — HTTP response header x-product "Pure Portal", title "Universitas Indonesia", Elsevier CSP origins. It carries two machine surfaces:'
  name: UI Research Portal (Elsevier Pure tenant)
  slug: pure-portal
- description: The University of Indonesia Library online public access catalogue, served at lib.ui.ac.id (lontar.ui.ac.id redirects to it), title "OPAC - Universitas Indonesia Library". LONTAR is library software d
  name: LONTAR Library OPAC
  slug: lontar-opac
- description: 'University of Indonesia is a Crossref member and DOI registrant. Verified against the Crossref REST API: https://api.crossref.org/members/4386 returns primary-name "Universitas Indonesia", location "U'
  name: Crossref Member 4386 (Universitas Indonesia)
  slug: crossref-member
- description: Research Organization Registry record for University of Indonesia, https://ror.org/0116zj450, verified against the ROR v2 API with ror_display name "University of Indonesia" and links http://www.ui.ac
  name: ROR Identifier 0116zj450
  slug: ror
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.ui.ac.id/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-indonesia/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.ui.ac.id/cas/login
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholarhub.ui.ac.id/
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholar.ui.ac.id/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.ui.ac.id/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-indonesia-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-indonesia-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-indonesia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-indonesia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-indonesia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-indonesia-context.jsonld
- group: company
  title: ''
  type: x-blog
  url: blogs/blogs.json
coverage:
  checked: '2026-09-01'
  detail: 'University of Indonesia operates real machine surfaces on its own network and publishes a contract for none of them. api.ui.ac.id is a Kong Enterprise 3.3.1.0 gateway that answers HTTP 401 {"message":"Unauthorized"} on every probed path including /docs and /openapi.json; the institution-hosted Moodle at emas2.ui.ac.id answers /webservice/rest/server.php with a moodle_exception invalidtoken and /login/token.php with missingparam, both live and both token-gated; sso.ui.ac.id serves a working CAS login but returns the same HTML page with HTTP 200 for /cas/p3/serviceValidate, /cas/idp/metadata and /cas/oidc/.well-known/openid-configuration, which is a soft-200, not a documented endpoint. No developer portal, API reference, OpenAPI, key issuance or client registration exists anywhere on ui.ac.id, and none has been generated to stand in for one. The two surfaces that DO answer anonymously — the OAI-PMH providers on scholarhub.ui.ac.id and scholar.ui.ac.id — are vendor tenancies (bepress
    Digital Commons and Elsevier Pure) recorded as such rather than credited to UI. A secondary obstacle, which does not change the finding: www.ui.ac.id sits behind an F5 Shape/TSPD JavaScript interstitial that returns HTTP 200 with a bot-defense body for every path, so /robots.txt, /llms.txt, /.well-known/security.txt and invented paths all "succeed" and none of them was treated as evidence.'
  evidence:
  - status: 401
    url: https://api.ui.ac.id/
  - status: 401
    url: https://api.ui.ac.id/openapi.json
  - status: 401
    url: https://api.ui.ac.id/docs
  - status: 200
    url: https://emas2.ui.ac.id/webservice/rest/server.php
  - status: 200
    url: https://emas2.ui.ac.id/login/token.php
  - status: 200
    url: https://emas2.ui.ac.id/mod/lti/auth.php
  - status: 200
    url: https://sso.ui.ac.id/cas/login
  - status: 503
    url: https://sso.ui.ac.id/account/node/3
  - status: 200
    url: https://scholarhub.ui.ac.id/do/oai/?verb=Identify
  - status: 200
    url: https://scholar.ui.ac.id/ws/oai?verb=Identify
  - status: 200
    url: https://scholar.ui.ac.id/ws/api/openapi.yaml
  - status: 200
    url: https://lib.ui.ac.id/
  - status: 200
    url: https://www.ui.ac.id/.well-known/security.txt
  - status: 200
    url: https://data.ui.ac.id/
  - status: 200
    url: https://api.crossref.org/members/4386
  - status: 200
    url: https://api.ror.org/v2/organizations?query=Universitas%20Indonesia
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'University of Indonesia (Universitas Indonesia, UI) is a public research university in Depok and Salemba, Jakarta, the highest-ranked university in Indonesia. Its programmable footprint is real but almost entirely closed. UI operates its own Kong Enterprise API gateway at api.ui.ac.id on its own network allocation (152.118.0.0/16, APNIC "INDONESIAUNI-ID"), a campus-wide CAS Single Sign-On at sso.ui.ac.id, an institution-hosted Moodle learning platform at emas2.ui.ac.id exposing Moodle Web Services and an LTI 1.3 platform endpoint, and the LONTAR library OPAC at lib.ui.ac.id. Every one of those is credential-gated: the gateway answers 401 {"message":"Unauthorized"} on every probed path, the LMS web service rejects anonymous calls with invalidtoken, and no developer portal, API reference, OpenAPI description, key issuance or client registration exists anywhere on the public surface. The two research-discovery surfaces that DO answer anonymously are vendor tenancies on UI hostnames,
  not UI engineering — scholarhub.ui.ac.id CNAMEs to bepress (Digital Commons) and scholar.ui.ac.id CNAMEs to ui.elsevierpure.com (Elsevier Pure Portal) — and are recorded here as tenant relationships with the vendor contracts deliberately left in the vendors'' own repositories. UI is a Crossref member (4386, prefix 10.7454) and carries a ROR identifier. The main web estate at www.ui.ac.id sits behind an F5 bot-defense interstitial that returns HTTP 200 for every path including ones that do not exist, so no claim in this profile rests on a status code from that host.'
finops:
- name: University Of Indonesia Finops
  service_category: Education
  slug: university-of-indonesia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-indonesia.png
jsonld:
- class_count: 25
  name: University Of Indonesia Context
  property_count: 4
  slug: university-of-indonesia-context
layout: provider
modified: '2026-09-01'
name: University of Indonesia
nav: Providers
network: true
overview: 'University of Indonesia publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Indonesia, and Southeast Asia.


  The University of Indonesia catalog on APIs.io includes 1 JSON-LD context.


  University of Indonesia''s developer surface includes authentication and 13 more developer resources.'
plans:
- name: University Of Indonesia Plans Pricing
  plan_count: 2
  slug: university-of-indonesia-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: University Of Indonesia Rate Limits
  slug: university-of-indonesia-rate-limits
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 25.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: University Of Indonesia Domain Security
  slug: university-of-indonesia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-indonesia
tags:
- Education
- Higher Education
- University
- Indonesia
- Southeast Asia
- Research
- Research Repository
- OAI-PMH
- Identity
- Single Sign-On
- Learning Management
- Library
- API Gateway
website: https://www.ui.ac.id/
---
