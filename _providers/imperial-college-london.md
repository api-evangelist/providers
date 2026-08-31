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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Imperial College London Agentic Access
  operation_count: 8
  slug: imperial-college-london-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: Imperial's own Shibboleth IdP, and the one unambiguously institution-operated machine-readable contract it publishes. The metadata document at /idp/shibboleth is a live 12.5KB SAML 2.0 EntityDescripto
  name: Imperial Shibboleth Identity Provider (SAML 2.0)
  slug: shibboleth-idp
- description: 'Imperial''s institutional open-access repository, exposed over the DSpace 7 HAL+JSON REST API at https://spiral.imperial.ac.uk/server/api. The read-oriented subset is genuinely public: /core/communitie'
  name: Spiral Open Access Repository (DSpace 7 REST API)
  slug: spiral-dspace-rest
- description: A fully functional OAI-PMH 2.0 harvesting interface — the standards-based way Imperial's research outputs reach OpenAIRE, CORE, BASE and the rest of the aggregator layer. Identify, ListMetadataFormats
  name: Spiral OAI-PMH Metadata Harvesting Endpoint
  slug: spiral-oai-pmh
- description: 'Imperial''s Canvas tenancy publishes the two documents an LTI 1.3 tool integrator actually needs, unauthenticated, on Imperial''s own hostname: an LTI platform JWKS at /api/lti/security/jwks (200, 1,408'
  name: Imperial Canvas LTI 1.3 / OIDC Platform Endpoints
  slug: canvas-lti-platform
- description: Imperial runs a second LMS alongside Canvas. Its Blackboard Learn REST API is reachable at https://bb.imperial.ac.uk/learn/api/public/v1/; the version endpoint answers 200 without authentication and r
  name: Imperial Blackboard Learn REST API
  slug: blackboard-learn-rest
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spiral Open Access Repository (DSpace 7 REST API) Core API
  slug: open-imperial-college-london-core-api
- collection_type: open
  name: Spiral Open Access Repository (DSpace 7 REST API) Core Discover API
  slug: open-imperial-college-london-discover-api
- collection_type: open
  name: Spiral Open Access Repository (DSpace 7 REST API) Core Root API
  slug: open-imperial-college-london-root-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/imperial-college-london-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.imperial.ac.uk/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.imperial.ac.uk/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.imperial.ac.uk/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ImperialCollegeLondon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/imperial-college-london/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/imperialcollege
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imperial.ac.uk/about-the-site/privacy/
- group: operate
  title: ''
  type: Support
  url: https://servicemgt.imperial.ac.uk/ask
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.imperial.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://spiral.imperial.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library-search.imperial.ac.uk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.imperial.ac.uk/study/courses/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.imperial.ac.uk/computing/people/csg/services/hpc/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.imperial.ac.uk/admin-services/library/learning-support/generative-ai-guidance/
- group: design
  title: ''
  type: Conformance
  url: conformance/imperial-college-london-education-standards.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imperial-college-london-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imperial-college-london-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/imperial-college-london-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imperial-college-london-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/imperial-college-london-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Verified institution-operated and machine-readable: the Shibboleth IdP metadata document (200, 12,549 bytes of SAML 2.0 EntityDescriptor, entityID https://shibboleth.imperial.ac.uk/shibboleth, present in the UK Access Management Federation aggregate alongside 11,112 other entities) and www.imperial.ac.uk/llms.txt (200, 5,803 bytes, self-dated 2026-06-23, with per-section crawl priorities and attribution rules). Verified live but tenant-operated: the Spiral DSpace 7.6.1 REST API and its OAI-PMH endpoint (11 metadata prefixes, OpenAIRE CERIF 1.1), the Canvas LTI 1.3 JWKS and OIDC discovery documents, and the Blackboard Learn public REST version endpoint. Institution-operated but gated: api.imperial.ac.uk resolves to 20.77.142.125 (Azure) and answers every path — /, /v1, /docs, /openapi.json, /swagger.json, /health, /.well-known/openapi.json — with `{"statusCode":404,"message":"Resource not found"}` as application/json. That is a live API gateway with no published surface, not a
    dead host. Confirmed dead or absent, and removed from or never added to this profile: data.imperial.ac.uk, developer.imperial.ac.uk and openaccess.imperial.ac.uk (no DNS); www.imperial.ac.uk/business-school/icbs-apis/ (403 that renders a "Page not found" body — soft-404, and robots.txt disallows it); profiles.imperial.ac.uk (200 but the identical 4,151-byte SPA shell at /, /api and /server/api — soft-200, no API); /.well-known/security.txt and /news/rss/ (404 HTML).'
  evidence:
  - status: 200
    url: https://shibboleth.imperial.ac.uk/idp/shibboleth
  - status: 200
    url: http://metadata.ukfederation.org.uk/ukfederation-metadata.xml
  - status: 200
    url: https://www.imperial.ac.uk/llms.txt
  - status: 200
    url: https://spiral.imperial.ac.uk/server/api
  - status: 200
    url: https://spiral.imperial.ac.uk/server/oai/request?verb=Identify
  - status: 200
    url: https://spiral.imperial.ac.uk/server/oai/request?verb=ListMetadataFormats
  - status: 200
    url: https://spiral.imperial.ac.uk/server/api/core/communities
  - status: 200
    url: https://spiral.imperial.ac.uk/server/api/discover/search/objects?query=climate
  - status: 401
    url: https://spiral.imperial.ac.uk/server/api/core/items
  - status: 200
    url: https://canvas.imperial.ac.uk/api/lti/security/jwks
  - status: 200
    url: https://canvas.imperial.ac.uk/.well-known/openid-configuration
  - status: 401
    url: https://canvas.imperial.ac.uk/api/v1/accounts/self
  - status: 200
    url: https://bb.imperial.ac.uk/learn/api/public/v1/system/version
  - status: 401
    url: https://bb.imperial.ac.uk/learn/api/public/v1/courses
  - status: 200
    url: https://api.datacite.org/providers/urks
  - status: 404
    url: https://api.imperial.ac.uk/
  - status: 404
    url: https://api.imperial.ac.uk/openapi.json
  - status: 403
    url: https://www.imperial.ac.uk/business-school/icbs-apis/
  - status: 200
    url: https://profiles.imperial.ac.uk/server/api
  - status: 0
    url: https://data.imperial.ac.uk/
  - status: 0
    url: https://developer.imperial.ac.uk/
  - status: 404
    url: https://www.imperial.ac.uk/.well-known/security.txt
  - status: 200
    url: https://api.crossref.org/members?query=Imperial+College+London
  reason: Imperial publishes no developer portal, no API catalogue and no OpenAPI of its own. Every callable surface found under imperial.ac.uk is either vendor software running under an Imperial hostname, or an institution-operated endpoint whose useful operations require federated authentication. Nothing was blocked to us — 27 hosts and paths were probed successfully and the thinness is the institution's, not a fetch failure.
  state: gated
created: '2026-06-03'
description: 'Imperial College London is a UK public research university and Russell Group member specialising in science, engineering, medicine and business. Re-profiled 2026-08-19 under the API Evangelist university pipeline, which settles WHO OPERATES each surface before crediting it. The finding is that Imperial operates no public developer portal, no open data portal (data.imperial.ac.uk does not resolve) and no self-service API programme — and that almost every machine-readable surface running under an imperial.ac.uk hostname is a vendor tenancy: Spiral, the open-access repository, is DSpace-CRIS hosted by 4Science; library-search is Ex Libris Primo; profiles is Symplectic Elements; canvas and bb are Instructure Canvas and Blackboard Learn; servicemgt is ServiceNow. Imperial''s data, DOIs, Handle prefix (10044) and administrative contacts sit behind all of them, but the contracts do not belong to Imperial. Exactly two machine-readable surfaces are Imperial-operated: the Shibboleth
  SAML 2.0 identity provider at shibboleth.imperial.ac.uk, registered in the UK Access Management Federation, and an llms.txt agent-guidance file the institution authored and maintains. A third, an Azure-hosted JSON gateway at api.imperial.ac.uk, answers with structured JSON but publishes no documented or discoverable operation. The programmable footprint is genuinely thin, and it is thin in the way universities are thin — a federation of buyers, not a producer.'
examples:
- key_count: 9
  name: Imperial College London Getcommunity Example
  slug: imperial-college-london-getCommunity-example
- key_count: 10
  name: Imperial College London Searchobjects Example
  slug: imperial-college-london-searchObjects-example
finops:
- name: Imperial College London Finops
  service_category: Education
  slug: imperial-college-london-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imperial-college-london.png
json_schemas:
- name: Spiral DSpace Community
  property_count: 8
  slug: imperial-college-london-community
- name: Spiral DSpace Item
  property_count: 12
  slug: imperial-college-london-item
json_structures:
- name: Imperial College London Community Structure
  property_count: 7
  slug: imperial-college-london-community-structure
- name: Imperial College London Item Structure
  property_count: 11
  slug: imperial-college-london-item-structure
jsonld:
- class_count: 20
  name: Imperial College London Context
  property_count: 0
  slug: imperial-college-london-context
layout: provider
modified: '2026-08-19'
name: Imperial College London
nav: Providers
network: true
overview: 'Imperial College London publishes 1 API on the [APIs.io](https://apis.io/) network: Spiral Open Access Repository (DSpace 7 REST API). Tagged areas include University, Higher Education, Education, Russell Group, and United Kingdom.


  The Imperial College London catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Imperial College London''s developer surface includes engineering blog, support, and 20 more developer resources.'
plans:
- name: Imperial College London Plans Pricing
  plan_count: 2
  slug: imperial-college-london-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Imperial College London Rate Limits
  slug: imperial-college-london-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Imperial College London API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: imperial-college-london-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Imperial College London API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 2
  slug: imperial-college-london-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 27.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imperial-college-london/refs/heads/main/screenshots/imperial-college-london-2026-06-20T183255.png
security:
- kind: domain-security
  name: Imperial College London Domain Security
  slug: imperial-college-london-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: imperial-college-london
tags:
- University
- Higher Education
- Education
- Russell Group
- United Kingdom
- London
- Research
- Institutional Repository
- Open Access
- Identity Federation
- Learning Management
- Library
website: https://www.imperial.ac.uk/
---
