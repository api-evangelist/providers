---
access_model:
  confidence: high
  label: Free · partially public, no registration offered
  onboarding: unknown
  pricing: free
  public: true
  source:
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://www.bu.edu/wp-json
  baseurl_source: declared
  description: The WordPress REST API on Boston University's own web platform, and the one substantial machine-readable interface the institution both operates and authors. Its discovery document advertises 237 rout
  name: Boston University WordPress REST API
  slug: wordpress-rest-api
- description: Boston University's SAML 2.0 identity provider, publishing machine-readable entity metadata at its own host. The EntityDescriptor carries entityID https://shib.bu.edu/idp/shibboleth, the Shibboleth sc
  name: Boston University Shibboleth Identity Provider
  slug: shibboleth-identity-federation
- description: OpenBU is Boston University Libraries' open-access institutional repository. The content, the collections and the 2144 Handle prefix are Boston University's; the software is DSpace 7.6 and the deploym
  name: OpenBU Repository — OAI-PMH and DSpace REST (Atmire-operated)
  slug: openbu-oai
- description: Boston University Libraries' discovery layer runs on Ex Libris Primo under Boston University's tenant view 01BOSU_INST:BULS. The catalogue data is the library's; the discovery API surface belongs to E
  name: BU Libraries Discovery (Ex Libris Primo)
  slug: primo-discovery
- description: Boston University's learning management system is Blackboard Learn, running on the vendor's infrastructure behind a bu.edu hostname. The Learn public REST API responds at /learn/api/public/v1/ — the u
  name: Blackboard Learn REST API (BU tenant)
  slug: blackboard-learn
- description: Boston University IS&T brokers Large Language Model API keys to affiliated faculty, researchers, staff and departments, reselling access to Microsoft Azure OpenAI and Amazon Bedrock (including Anthrop
  name: AI API Access (Azure OpenAI / Amazon Bedrock)
  slug: ai-api-access
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.bu.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bu-ist
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bu-rcs
- group: other
  title: ''
  type: IdentityFederation
  url: https://shib.bu.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://open.bu.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://bu.primo.exlibrisgroup.com/discovery/search?vid=01BOSU_INST:BULS
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.bu.edu/tech/support/research/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.bu.edu/aida/ai-education/ai-at-work/generative-ai-guidelines-for-bu-faculty-staff/
- group: build
  title: ''
  type: AITooling
  url: https://www.bu.edu/aida/
- group: operate
  title: ''
  type: Support
  url: https://www.bu.edu/tech/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bu.edu/policies/conditions-of-use-policy-computing-ethics/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bu.edu/policies/digital-privacy-statement/
- group: company
  title: ''
  type: Blog
  url: https://www.bu.edu/today/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bu.edu/today/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/boston-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/boston-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boston-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/boston-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boston-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/boston-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/boston-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boston-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/boston-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boston-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/boston-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Boston University is a private research university in Boston, Massachusetts, chartered in 1869, serving roughly 37,000 students across three campuses. Like most universities it is a federation of buyers rather than an API producer, and its programmable footprint has to be read that way. The one substantial machine-readable interface Boston University both operates AND authors is the WordPress REST API on www.bu.edu: nine of its fifteen namespaces are BU IS&T''s own plugins — bu-alert, bu-blocks, bu-navigation, bu-slideshow, bu-tts and others — open-sourced at github.com/bu-ist and documented at developer.bu.edu, with some routes public and some returning 401. Alongside it, Boston University operates a Shibboleth SAML 2.0 identity provider at shib.bu.edu whose entity metadata is public, registered by InCommon and exported to eduGAIN with the REFEDS Research & Scholarship and SIRTFI entity categories. Everything else that looks like a Boston University API is a vendor''s contract
  running under BU''s name: OpenBU is a DSpace 7.6 instance operated by Atmire (open.bu.edu CNAMEs to boston-prod.cname.atmire.com and its OAI-PMH Identify returns the vendor''s admin email), the library discovery layer is Ex Libris Primo, and the LMS is Blackboard Learn. Those are recorded here as tenant relationships, not as Boston University engineering. There is no central developer portal, no API key programme, no published API changelog, and the internal WEB APIs portal at webapi.bu.edu is NXDOMAIN.'
finops:
- name: Boston Finops
  service_category: Education
  slug: boston-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boston.png
json_schemas:
- name: Boston University WordPress REST API schemas
  property_count: 0
  slug: boston-wordpress-schemas
jsonld:
- class_count: 25
  name: Boston Context
  property_count: 5
  slug: boston-context
layout: provider
modified: '2026-08-30'
name: Boston University
nav: Providers
network: true
overview: 'Boston University publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include University, Higher Education, Education, United States, and Massachusetts.


  The Boston University catalog on APIs.io includes 1 JSON-LD context.


  Boston University''s developer surface includes documentation, support, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Boston Plans Pricing
  plan_count: 2
  slug: boston-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Boston Rate Limits
  slug: boston-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 3.8
    contract_quality: 28.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 3.8
    operational_transparency: 26.3
  previous_composite: 35.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/boston/refs/heads/main/screenshots/boston-2026-06-20T173612.png
security:
- kind: authentication
  name: Boston Authentication
  slug: boston-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Boston Domain Security
  slug: boston-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boston
tags:
- University
- Higher Education
- Education
- United States
- Massachusetts
- Private Research University
- Research
- Research Data
- Library
- Identity Federation
- Content Management
- Open Access
website: https://www.bu.edu/
---
