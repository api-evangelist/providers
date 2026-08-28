---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 1
  name: University Of Edinburgh Agentic Access
  operation_count: 14
  slug: university-of-edinburgh-agentic-access
  summary_line: 14 operations · 1 human-in-the-loop
api_count: 10
apis:
- description: 'DSpace 8.3 REST API for Edinburgh DataShare, the University''s open-access research-data repository. Anonymous callers may read communities (110), collections, browse indexes and the discovery search; '
  name: Edinburgh DataShare REST API
  slug: datashare-repository-api
- description: OAI-PMH 2.0 metadata harvesting endpoint for Edinburgh DataShare. Fully anonymous, no key, twelve metadata prefixes including the UK research formats rioxx and uketd_dc. Records carry DataCite DOIs un
  name: Edinburgh DataShare OAI-PMH
  slug: datashare-oai
- description: 'DSpace 8.3 REST API for the Edinburgh Research Archive, the University''s institutional repository of theses, dissertations and research publications. 54 communities readable anonymously; items return '
  name: Edinburgh Research Archive (ERA) REST API
  slug: era-repository-api
- description: OAI-PMH 2.0 endpoint for the Edinburgh Research Archive. Thirteen metadata prefixes including etdms for electronic theses alongside rioxx and uketd_dc. DOIs under 10.7488/era. Earliest datestamp 2003-
  name: Edinburgh Research Archive (ERA) OAI-PMH
  slug: era-oai
- description: 'CKAN 2.11.3 Action API for the Edinburgh International Data Facility Data Catalogue, operated by EPCC at the University of Edinburgh. 14 public datasets across 13 EIDF project organisations, readable '
  name: EIDF Data Catalogue API
  slug: eidf-data-catalogue-api
- description: OpenAI-compatible generative-AI gateway built and run by EDINA at the University of Edinburgh, described by its own metadata as delivering generative AI to UK tertiary education. /api/v1/models and /a
  name: ELM — Edinburgh Language Models API
  slug: elm-api
- description: 'Shibboleth Identity Provider publishing SAML 2.0 entity metadata unauthenticated at a stable URL, entityID https://idp.ed.ac.uk/shibboleth. Advertises the full SAML 2.0 binding set for SSO and Single '
  name: University of Edinburgh Shibboleth Identity Provider
  slug: identity-federation
- description: The University's Enterprise APIs programme — Student Records, Timetabling and Staff APIs — runs on a WSO2 Choreo gateway at api.ed.ac.uk. The gateway is live and Edinburgh-operated, but every probed p
  name: Enterprise API Gateway (gated)
  slug: enterprise-api-gateway
- description: Edinburgh Research Explorer is the University's public research information portal, running on Elsevier Pure. The research outputs, the people and the DOIs are Edinburgh's; the API contract is Elsevie
  name: Edinburgh Research Explorer (Elsevier Pure) — tenant
  slug: pure-research-explorer
- description: DiscoverEd is the University Library's discovery layer, an Ex Libris Primo tenancy on an Edinburgh subdomain. The holdings are Edinburgh's; the search API is Ex Libris's product and is not saved under
  name: DiscoverEd Library Discovery (Ex Libris Primo) — tenant
  slug: discovered-primo
artifact_total: 28
common:
- group: company
  title: ''
  type: Website
  url: https://www.ed.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ed.ac.uk/information-services/enterprise-architecture/application-integration/apis-and-connectors
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uoe-is-apps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-edinburgh/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ed.ac.uk/about/website/website-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ed.ac.uk/data-protection
- group: operate
  title: ''
  type: Support
  url: https://www.ed.ac.uk/information-services/help-consultancy
- group: company
  title: ''
  type: Blog
  url: https://libraryblogs.is.ed.ac.uk/datablog/
- group: other
  title: ''
  type: ResearchRepository
  url: https://datashare.ed.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://era.ed.ac.uk/
- group: other
  title: ''
  type: OpenData
  url: https://catalogue.eidf.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.ed.ac.uk/idp/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.drps.ed.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://discovered.ed.ac.uk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.epcc.ed.ac.uk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://portal.eidf.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ed.ac.uk/ai/guidance
- group: build
  title: ''
  type: AITooling
  url: https://information-services.ed.ac.uk/computing/comms-and-collab/elm
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-edinburgh-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-edinburgh-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-edinburgh-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-edinburgh-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-edinburgh-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-edinburgh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-edinburgh-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-edinburgh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-edinburgh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-edinburgh-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Edinburgh is a public research university in Scotland, founded in 1582, a member of the Russell Group and ranked #19 in the QS World University Rankings. Its programmable footprint is real but narrow, and it is not where the catalog previously said it was. Re-profiled on 2026-08-19 against the operator axis, the institution genuinely operates: two DSpace 8.3 research repositories on its own domain (Edinburgh DataShare and the Edinburgh Research Archive) each with a REST API and an OAI-PMH 2.0 endpoint minting DataCite DOIs under the University prefix 10.7488; a Shibboleth Identity Provider publishing SAML 2.0 metadata unauthenticated; a CKAN 2.11.3 open-data catalogue for the Edinburgh International Data Facility; and ELM (Edinburgh Language Models), an OpenAI-compatible generative-AI gateway that EDINA operates for UK tertiary education — the one surface here where Edinburgh is clearly a producer rather than a buyer. An Enterprise API programme runs on a
  WSO2 Choreo gateway at api.ed.ac.uk, which is live but exposes no public route, catalogue or developer portal, and whose own public project pages returned HTTP 500 on every probe. The library discovery layer (Ex Libris Primo) and the research information system (Elsevier Pure) are vendor platforms recorded here as tenant relationships, not as Edinburgh contracts. This profile is deliberately smaller than the June 2026 one: the seven OpenAPI documents previously held for this institution described the DSpace 6 legacy /rest API, which is retired and now returns 404.'
examples:
- key_count: 2
  name: University Of Edinburgh Datashare 401 Example
  slug: university-of-edinburgh-datashare-401-example
- key_count: 2
  name: University Of Edinburgh Datashare Collections Example
  slug: university-of-edinburgh-datashare-collections-example
- key_count: 2
  name: University Of Edinburgh Datashare Communities Example
  slug: university-of-edinburgh-datashare-communities-example
- key_count: 2
  name: University Of Edinburgh Datashare Root Example
  slug: university-of-edinburgh-datashare-root-example
- key_count: 2
  name: University Of Edinburgh Eidf Package Show Example
  slug: university-of-edinburgh-eidf-package-show-example
- key_count: 2
  name: University Of Edinburgh Era Communities Example
  slug: university-of-edinburgh-era-communities-example
finops:
- name: University Of Edinburgh Finops
  service_category: Education
  slug: university-of-edinburgh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-edinburgh.png
json_schemas:
- name: EIDF Data Catalogue Dataset (CKAN package)
  property_count: 16
  slug: university-of-edinburgh-ckan-package
- name: DSpace 8 Community (Edinburgh DataShare / ERA)
  property_count: 8
  slug: university-of-edinburgh-dspace-community
jsonld:
- class_count: 4
  name: University Of Edinburgh Context
  property_count: 5
  slug: university-of-edinburgh-context
layout: provider
modified: '2026-08-19'
name: University of Edinburgh
nav: Providers
network: true
overview: 'University of Edinburgh publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Edinburgh DataShare REST API, Edinburgh DataShare OAI-PMH, Edinburgh Research Archive (ERA) REST API, and 3 more. Tagged areas include University, Higher Education, Education, United Kingdom, and Scotland.


  The University of Edinburgh catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Edinburgh''s developer surface includes documentation, GitHub presence, support, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: University Of Edinburgh Plans Pricing
  plan_count: 2
  slug: university-of-edinburgh-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: University Of Edinburgh Rate Limits
  slug: university-of-edinburgh-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Edinburgh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-edinburgh-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: University of Edinburgh API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: university-of-edinburgh-rules
scopes:
- name: University Of Edinburgh Scopes
  scope_count: 0
  slug: university-of-edinburgh-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 56.3
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-edinburgh/refs/heads/main/screenshots/university-of-edinburgh-2026-06-20T200145.png
security:
- kind: authentication
  name: University Of Edinburgh Authentication
  slug: university-of-edinburgh-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Edinburgh Domain Security
  slug: university-of-edinburgh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-edinburgh
tags:
- University
- Higher Education
- Education
- United Kingdom
- Scotland
- Russell Group
- Research Repository
- Open Data
- Identity Federation
- Research Computing
- OAI-PMH
- Artificial Intelligence
website: https://www.ed.ac.uk/
---
