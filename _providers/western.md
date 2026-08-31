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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-30'
api_count: 6
apis:
- description: Western's institutional identity provider, publishing machine-readable SAML 2.0 metadata through the Canadian Access Federation. entityID https://shibidp.uwo.ca/idp/shibboleth, mdui:DisplayName "Unive
  name: Western University Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: Western Technology Services operates an Apereo CAS server at ssocas.uwo.ca. The CAS 3.0 protocol is publicly reachable — /cas/p3/serviceValidate returns a well-formed cas:serviceResponse to an anonymo
  name: Western Single Sign-On (Apereo CAS — CAS 3.0, SAML2, OIDC)
  slug: sso-cas
- description: The HAL+JSON REST API of Western University's Open Repository, reachable anonymously at https://uwo.scholaris.ca/server/api. The root document self-reports dspaceName "Western University's Open Reposi
  name: Scholarship@Western on Scholaris — DSpace REST API (tenant)
  slug: scholaris-rest
- description: OAI-PMH 2.0 metadata harvesting for Western University's Open Repository. Identify returns repositoryName "Western University's Open Repository", repositoryIdentifier uwo.scholaris.ca, adminEmail rscl
  name: Scholarship@Western OAI-PMH 2.0 provider (tenant)
  slug: scholaris-oai-pmh
- description: Western's research data repository, a Dataverse collection with alias "westernu" and affiliation "Western University" on Borealis, the Canadian Dataverse Repository operated by Scholars Portal. Reacha
  name: Western University Repository on Borealis — Dataverse API (tenant)
  slug: borealis-dataverse
- description: Western Libraries' discovery layer is Omni, the Ontario Council of University Libraries' shared Ex Libris Alma/Primo VE deployment. Western's view is ocul-uwo.primo.exlibrisgroup.com with vid=01OCUL_U
  name: Omni library discovery — Ex Libris Primo VE (tenant)
  slug: omni-primo
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.uwo.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://wts.uwo.ca/services/index.html
- group: operate
  title: ''
  type: Support
  url: https://wts.uwo.ca/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uwo.ca/legalcounsel/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/school/westernuniversity/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/westernu
- group: company
  title: ''
  type: Blog
  url: https://news.westernu.ca/
- group: company
  title: ''
  type: BlogRSS
  url: https://news.westernu.ca/feed
- group: other
  title: ''
  type: IdentityFederation
  url: https://ssocas.uwo.ca/cas/idp/metadata
- group: other
  title: ''
  type: ResearchRepository
  url: https://uwo.scholaris.ca/home
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ocul-uwo.primo.exlibrisgroup.com/discovery/search?vid=01OCUL_UWO:UWO_DEFAULT
- group: learn
  title: ''
  type: CourseCatalog
  url: https://westerncalendar.uwo.ca/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.uwo.ca/governance/policies.html
- group: build
  title: ''
  type: AITooling
  url: https://ai.uwo.ca/resources/ai-tools.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/western-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/western-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/western-shibboleth-idp-caf-metadata-example.xml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/western-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/western-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/western-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/western-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Western University is a public research university in London, Ontario, Canada, ranked #120 in the QS World University Rankings order used by this cohort. Like almost every university, Western is a federation of buyers rather than an API producer: it runs no developer portal, no institutional API gateway (api.uwo.ca and developer.uwo.ca do not resolve), publishes no OpenAPI for anything, and serves no llms.txt or security.txt. What it genuinely operates is identity. Western Technology Services runs a Shibboleth Identity Provider, entityID https://shibidp.uwo.ca/idp/shibboleth, registered in the Canadian Access Federation since 2012 under CANARIE and exported to eduGAIN, declaring the REFEDS Research and Scholarship entity category and Sirtfi assurance — machine-readable SAML 2.0 metadata that is the single most consequential surface Western publishes. Alongside it runs an Apereo CAS server at ssocas.uwo.ca with a live CAS 3.0 validation endpoint and a second SAML descriptor
  whose entityID is still the stock Apereo placeholder. Both are end-user login federations, not developer authorization surfaces; OIDC is advertised by WTS but its discovery document returns 403. Western''s two readable data surfaces are tenancies, not engineering: Scholarship@Western moved in 2025 to Scholaris, the national shared DSpace 8.4 service run by Scholars Portal (OCUL), exposing a HAL REST API and a conformant OAI-PMH 2.0 provider across thirteen metadata formats at uwo.scholaris.ca; and Western''s research data lives in a 1,504-dataset collection on Borealis, the Canadian Dataverse Repository, minting DataCite DOIs on Scholars Portal''s 10.5683 prefix. Library discovery is an Ex Libris Primo VE view on OCUL''s shared platform. All four are recorded here as tenant relationships and deliberately not credited as Western engineering. There is no official course, timetable or open-data API: the academic calendar at westerncalendar.uwo.ca blocks every AI and search crawler in robots.txt,
  the undergraduate timetable is scrape-only, and the only APIs over that data are unofficial student projects on GitHub that Western does not endorse.'
finops:
- name: Western Finops
  service_category: Education
  slug: western-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western.png
jsonld:
- class_count: 7
  name: Western Context
  property_count: 9
  slug: western-context
layout: provider
modified: '2026-08-30'
name: Western University
nav: Providers
network: true
overview: 'Western University publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and Canada.


  The Western University catalog on APIs.io includes 1 JSON-LD context.


  Western University''s developer surface includes documentation, support, engineering blog, authentication, code examples, and 18 more developer resources.'
plans:
- name: Western Plans Pricing
  plan_count: 2
  slug: western-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Western Rate Limits
  slug: western-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 10.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 17.3
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/western/refs/heads/main/screenshots/western-2026-06-20T201359.png
security:
- kind: authentication
  name: Western Authentication
  slug: western-authentication
  summary_line: saml2/cas/oauth2/oidc · 4 schemes
- kind: domain-security
  name: Western Domain Security
  slug: western-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: western
tags:
- University
- Higher Education
- Education
- Research
- Canada
- Ontario
- U15
- Identity Federation
- Research Repository
- Research Data
- Open Access
- OAI-PMH
- Library
website: https://www.uwo.ca/
---
