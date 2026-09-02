---
access_model:
  confidence: high
  label: Free · Keyless for PV_Live reads, registration for PV_Forecast
  onboarding: open
  pricing: free
  public: true
  source:
  - authentication
  - probed
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
    error_semantics: verified
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
  score: 26.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The University of Sheffield's own research API, built and run by the Sheffield Solar group in the Department of Physics and Astronomy. It publishes PV_Live — near-real-time and historical estimates of
  name: Sheffield Solar API
  slug: sheffield-solar-api
- description: The institution's own SAML 2.0 identity provider, entityID https://idp.shef.ac.uk/shibboleth, serving live Shibboleth metadata from Sheffield's own domain. Machine-readable, institution-operated by de
  name: University of Sheffield Shibboleth Identity Provider
  slug: shibboleth-idp
- description: ORDA is the University of Sheffield's research data repository at orda.shef.ac.uk. The records, the DOIs and the curation are Sheffield's; the platform and the API contract are figshare's. Sheffield i
  name: ORDA — Online Research Data (figshare tenant)
  slug: orda
- description: White Rose Research Online is the shared open-access outputs repository of the Universities of Leeds, Sheffield and York, running on EPrints and administered by the White Rose consortium rather than b
  name: White Rose Research Online OAI-PMH
  slug: wrro-oai
- description: White Rose eTheses Online is the shared electronic theses repository of the same three universities, running on EPrints. Its OAI-PMH 2.0 interface Identifies as "White Rose eTheses Online" and harvest
  name: White Rose eTheses Online OAI-PMH
  slug: wreo-oai
artifact_total: 19
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/SheffieldSolar/PV_Live-API/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.sheffield.ac.uk/
- group: docs
  title: ''
  type: APIReference
  url: https://api.solar.sheffield.ac.uk/redoc
- group: docs
  title: ''
  type: Documentation
  url: https://www.solar.sheffield.ac.uk/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sheffield.ac.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sheffield.ac.uk/privacy
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.shef.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://orda.shef.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.whiterose.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://find.shef.ac.uk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.hpc.shef.ac.uk/en/latest/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.sheffield.ac.uk/it-services/research/hpc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SheffieldUni
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/rcgsheffield
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/RSE-Sheffield
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/SheffieldSolar
- group: operate
  title: ''
  type: Support
  url: https://api.solar.sheffield.ac.uk/pvlive/contact
- group: operate
  title: ''
  type: Status
  url: https://api.solar.sheffield.ac.uk/pvlive/uptime
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-sheffield/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sheffielduni
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-sheffield-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-sheffield-lifecycle.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-sheffield-errors.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-sheffield-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-sheffield-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-sheffield-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-sheffield-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-sheffield-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-sheffield-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Sheffield is a public research university in Sheffield, United Kingdom, and a member of the Russell Group. Its programmable footprint is small, decentralised and mostly indirect, and this profile says so rather than padding it. There is no central developer portal, no API gateway, no self-service key issuance and no documented course, timetable or student-information API. What the institution genuinely operates is one first-party research API — the Sheffield Solar API at api.solar.sheffield.ac.uk, which publishes its own OpenAPI 3.1 document and serves keyless PV_Live estimates of GB solar generation — and its own Shibboleth SAML identity provider at idp.shef.ac.uk, the authentication surface through which every bought platform is reached. Everything else that looks like a Sheffield API is a vendor''s contract running under Sheffield''s name: ORDA is figshare, White Rose Research Online and White Rose eTheses Online are EPrints instances shared with Leeds
  and York, and library discovery is Ex Libris Primo. Those are recorded here as tenant relationships, which they are, and not as Sheffield engineering, which they are not.'
examples:
- key_count: 6
  name: University Of Sheffield Pvforecast Auth Required Example
  slug: university-of-sheffield-pvforecast-auth-required-example
- key_count: 6
  name: University Of Sheffield Pvlive Gsp Example
  slug: university-of-sheffield-pvlive-gsp-example
- key_count: 6
  name: University Of Sheffield Pvlive Peakgeneration Example
  slug: university-of-sheffield-pvlive-peakgeneration-example
- key_count: 6
  name: University Of Sheffield Pvlive Pes List Example
  slug: university-of-sheffield-pvlive-pes-list-example
finops:
- name: University Of Sheffield Finops
  service_category: Education
  slug: university-of-sheffield-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-sheffield.png
json_schemas:
- name: PVLiveGenerationRow
  property_count: 4
  slug: university-of-sheffield-pvlive-generation-row
- name: SheffieldSolarTabularResponse
  property_count: 2
  slug: university-of-sheffield-pvlive-response
jsonld:
- class_count: 4
  name: University Of Sheffield Context
  property_count: 5
  slug: university-of-sheffield-context
layout: provider
modified: '2026-08-30'
name: University of Sheffield
nav: Providers
network: true
overview: 'University of Sheffield publishes 1 API on the [APIs.io](https://apis.io/) network: Sheffield Solar API. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  The University of Sheffield catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Sheffield''s developer surface includes API reference, documentation, support, status page, authentication, and 25 more developer resources.'
plans:
- name: University Of Sheffield Plans Pricing
  plan_count: 2
  slug: university-of-sheffield-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: University Of Sheffield Rate Limits
  slug: university-of-sheffield-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: University of Sheffield API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: university-of-sheffield-rules
scopes:
- name: University Of Sheffield Scopes
  scope_count: 0
  slug: university-of-sheffield-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 32.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -7.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 34.1
    contract_quality: 28.1
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 34.1
    operational_transparency: 23.7
  previous_composite: 52.4
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
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-sheffield/refs/heads/main/screenshots/university-of-sheffield-2026-06-20T200244.png
security:
- kind: authentication
  name: University Of Sheffield Authentication
  slug: university-of-sheffield-authentication
  summary_line: oauth2/apiKey/http/saml2 · 5 schemes
- kind: domain-security
  name: University Of Sheffield Domain Security
  slug: university-of-sheffield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-sheffield
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Research Data
- Open Access
- OAI-PMH
- Identity Federation
- Solar Energy
- Energy Data
- Research Computing
website: https://www.sheffield.ac.uk/
---
