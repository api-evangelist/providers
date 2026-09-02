---
access_model:
  confidence: medium
  label: Free tier for King's affiliates · metered beyond it · no public signup
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
api_count: 6
apis:
- description: An OpenAI-compatible LLM inference API operated by King's e-Research for researchers, students and staff. Per King's documentation it serves chat completions against a curated set of hosted models, im
  name: King's e-Research AI Hub API
  slug: er-ai-hub
- description: The standards-based harvesting interface for the King's Research Portal, the front end of Pure — how King's research outputs reach OpenAIRE, CORE, BASE and the rest of the aggregator layer. Identify r
  name: King's Research Portal (Pure) OAI-PMH
  slug: pure-oai
- description: King's research data repository, operated for King's by Figshare. The data, the DOIs, the DataCite membership and the curation decisions are King's; the REST API, the OAI-PMH endpoint and every line o
  name: King's College London Research Data Repository (Figshare tenancy)
  slug: figshare-repository
- description: King's federated identity, and the surface class this pipeline flags as most often missed. The entity is registered in the UK Access Management Federation (uk001282, registered 2010-04-22, registratio
  name: King's UK Access Management Federation / eduGAIN Identity Provider
  slug: uk-federation-idp
- description: Library discovery for King's, on Ex Libris Primo. GET / returns 200 and redirects to /discovery/search?vid=44KCL_INST:44KCL_INST. Recorded as a tenancy because the catalog and the holdings are King's,
  name: King's LibrarySearch (Ex Libris Primo)
  slug: librarysearch-primo
- description: 'King''s VLE exposes the standard Moodle machine interfaces on a King''s hostname: /webservice/rest/server.php answers 200 with an XML `invalidtoken` fault, /lib/ajax/service.php answers 200 with a JSON '
  name: KEATS Virtual Learning Environment (Moodle) web services
  slug: keats-moodle
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.kcl.ac.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.kcl.ac.uk/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kcl-eresearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/king's-college-london/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.er.kcl.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.er.kcl.ac.uk/CREATE/ai_hub/
- group: operate
  title: ''
  type: Support
  url: https://docs.er.kcl.ac.uk/CREATE/getting_help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kcl.ac.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kcl.ac.uk/terms/privacy
- group: other
  title: ''
  type: IdentityFederation
  url: https://met.refeds.org/met/entity/https%3A%2F%2Fkclidp.kcl.ac.uk%2Fidp%2Fshibboleth/
- group: other
  title: ''
  type: ResearchRepository
  url: https://kcl.figshare.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://librarysearch.kcl.ac.uk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.kcl.ac.uk/study/undergraduate/courses
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.er.kcl.ac.uk/CREATE/cloud/cloud_overview/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.kcl.ac.uk/about/strategy/learning-and-teaching/ai-guidance
- group: build
  title: ''
  type: AITooling
  url: https://docs.er.kcl.ac.uk/CREATE/ai_hub/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kings-college-london-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/kings-college-london-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kings-college-london-education-standards.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kings-college-london-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kings-college-london-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kings-college-london-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kings-college-london-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Verified institution-operated and live: https://ai.create.kcl.ac.uk/api/v1/models returns 401 application/json with the OpenAI error envelope ({"error":{"message":"Unauthorized — no bearer token provided","type":"invalid_request_error", "param":null,"code":"invalid_api_key"}}) from nginx/1.30.4, and a request bearing an unknown key returns a different message ("invalid API key"), which establishes the token is validated rather than merely required. King''s own documentation at docs.er.kcl.ac.uk/CREATE/ai_hub/ describes it as "King''s College London''s AI inference platform for researchers", OpenAI- compatible, with chat completions, image generation, streaming, RAG, agent workflows and MCP integration, free starter tokens and project budgets thereafter. No contract is published for it: /openapi.json, /api/openapi.json, /v1/models and /.well-known/openapi all return the application''s 404. Institution-operated but unreachable: cloud.er.kcl.ac.uk, the CREATE Cloud OpenStack API
    documented at docs.er.kcl.ac.uk/CREATE/cloud/openstack_api/, has no public DNS record on 1.1.1.1 or 8.8.8.8 — it is VPN-only, and its application-credential and root-CA flow is documented but not probeable. Institution-authored but internal: the KCL e-Research Authentication API (github.com/kcl-eresearch/auth_api) documents its own REST surface for SSH keys, OpenVPN certificates and MFA requests in a public README, with no public base URL; and kcl-eresearch/artemis is a King''s-authored Perplexity-compatible research API server. Neither ships an OpenAPI. Verified live but tenant-operated: kclpure.kcl.ac.uk (CNAME kings.elsevierpure.com), kcl.figshare.com (CNAME figshare.com), librarysearch.kcl.ac.uk (CNAME kcl.primo.exlibrisgroup.com), keats.kcl.ac.uk (CNAME kcl-vle.bloom.ulcc.ac.uk) and the UK federation IdP whose SSO endpoints are on login.openathens.net. Confirmed absent: no DNS for data.kcl.ac.uk, developer.kcl.ac.uk, courses.kcl.ac.uk, sis.kcl.ac.uk, idp.kcl.ac.uk or sso.kcl.ac.uk;
    api.kcl.ac.uk resolves to 137.73.130.161 but accepts no TCP connection on 80 or 443 across three attempts at 30s, 40s and 60s; www.kcl.ac.uk/llms.txt and /.well-known/security.txt both 404. The development identity provider https://kclidpdev.kcl.ac.uk/idp/shibboleth is registered in the UK federation but carries the hide-from-discovery entity category and is treated as a placeholder, not a surface.'
  evidence:
  - status: 401
    url: https://ai.create.kcl.ac.uk/api/v1/models
  - status: 200
    url: https://ai.create.kcl.ac.uk/
  - status: 200
    url: https://ai.create.kcl.ac.uk/docs
  - status: 404
    url: https://ai.create.kcl.ac.uk/openapi.json
  - status: 404
    url: https://ai.create.kcl.ac.uk/api/openapi.json
  - status: 200
    url: https://docs.er.kcl.ac.uk/CREATE/ai_hub/
  - status: 200
    url: https://docs.er.kcl.ac.uk/CREATE/cloud/openstack_api/
  - status: 200
    url: https://docs.er.kcl.ac.uk/sitemap.xml
  - status: 200
    url: https://kclpure.kcl.ac.uk/ws/oai?verb=Identify
  - status: 200
    url: https://kclpure.kcl.ac.uk/ws/oai?verb=ListMetadataFormats
  - status: 200
    url: https://kclpure.kcl.ac.uk/ws/oai?verb=ListSets
  - status: 200
    url: https://kclpure.kcl.ac.uk/ws/oai?verb=ListRecords&metadataPrefix=oai_dc&set=persons:all
  - status: 200
    url: http://metadata.ukfederation.org.uk/ukfederation-metadata.xml
  - status: 200
    url: https://met.refeds.org/met/entity/https%3A%2F%2Fkclidp.kcl.ac.uk%2Fidp%2Fshibboleth/
  - status: 200
    url: https://api.datacite.org/providers/hcbr
  - status: 200
    url: https://api.datacite.org/dois?provider-id=hcbr
  - status: 200
    url: https://api.crossref.org/members?query=king%27s+college+london
  - status: 200
    url: https://librarysearch.kcl.ac.uk/
  - status: 200
    url: https://keats.kcl.ac.uk/webservice/rest/server.php
  - status: 200
    url: https://keats.kcl.ac.uk/mod/lti/auth.php
  - status: 404
    url: https://keats.kcl.ac.uk/.well-known/openid-configuration
  - status: 202
    url: https://kcl.figshare.com/
  - status: 200
    url: https://portal.er.kcl.ac.uk/
  - status: 200
    url: https://github.com/kcl-eresearch
  - status: 200
    url: https://raw.githubusercontent.com/kcl-eresearch/auth_api/main/README.md
  - status: 404
    url: https://www.kcl.ac.uk/llms.txt
  - status: 404
    url: https://www.kcl.ac.uk/.well-known/security.txt
  - status: 0
    url: https://api.kcl.ac.uk/
  - status: 0
    url: https://cloud.er.kcl.ac.uk/
  reason: 'King''s operates exactly one public-internet API of its own, and it requires a King''s credential. The e-Research AI Hub answers 401 with a structured error envelope, which proves it is live and callable, but its API reference, model list, rate limits and billing rules all sit behind Microsoft Entra ID sign-in and cannot be read from outside. The rest of the programmable footprint is either vendor software running under a kcl.ac.uk hostname or, in the case of the CREATE Cloud OpenStack API, on a hostname that publishes no public DNS at all. Nothing blocked us: 40+ hosts and paths were probed successfully and the thinness is the institution''s, not a fetch failure.'
  state: gated
created: '2026-06-03'
description: 'King''s College London is a UK public research university and Russell Group member, founded in 1829, ranked #40 in the QS World University Rankings. Re-profiled on 2026-08-19 under the API Evangelist university pipeline, which settles WHO OPERATES a surface before crediting it to the institution. The June 2026 profile credited King''s with eleven API entries and ten OpenAPI contracts; every one of them was api.figshare.com/v2 — a single Figshare document that the same pass attributed to twenty-five different universities — split by tag into eleven apparent surfaces. Those contracts, and the collections and agentic-access artifacts derived from them, have been removed. What is left is what King''s actually operates. The genuine find is the e-Research AI Hub at ai.create.kcl.ac.uk: King''s own OpenAI-compatible LLM inference platform for researchers, live, bearer-authenticated, metered and billed, running on King''s own infrastructure — a real institution-operated API, and a
  rare one in this cohort. Alongside it sit four tenancies that are real institutional facts but somebody else''s engineering: the King''s Research Portal OAI-PMH endpoint (Elsevier Pure), the research data repository (Figshare), LibrarySearch (Ex Libris Primo) and the UK federation identity provider (OpenAthens). King''s holds its own DataCite membership and prefix, and is registered in the UK Access Management Federation and eduGAIN. It publishes no OpenAPI, no developer portal, no open data portal, no llms.txt and no security.txt.'
finops:
- name: Kings College London Finops
  service_category: Education
  slug: kings-college-london-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kings-college-london.png
layout: provider
modified: '2026-08-19'
name: King's College London
nav: Providers
network: true
overview: 'King''s College London publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Russell Group, and United Kingdom.


  King''s College London''s developer surface includes engineering blog, documentation, support, authentication, and 20 more developer resources.'
plans:
- name: Kings College London Plans Pricing
  plan_count: 3
  slug: kings-college-london-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Kings College London Rate Limits
  slug: kings-college-london-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 57.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.1
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 8.0
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 36.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kings-college-london/refs/heads/main/screenshots/kings-college-london-2026-08-17T083326.png
security:
- kind: authentication
  name: Kings College London Authentication
  slug: kings-college-london-authentication
  summary_line: http/openIdConnect/saml/none · 5 schemes
- kind: domain-security
  name: Kings College London Domain Security
  slug: kings-college-london-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kings-college-london
tags:
- University
- Higher Education
- Education
- Russell Group
- United Kingdom
- London
- Research
- Research Computing
- Artificial Intelligence
- Institutional Repository
- Identity Federation
- OAI-PMH
- Library
website: https://www.kcl.ac.uk/
---
