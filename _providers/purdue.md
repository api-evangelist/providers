---
access_model:
  confidence: high
  label: Free - one keyless surface, the rest gated by Purdue institutional identity
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Rosen Center for Advanced Computing publishes its own OpenAPI 3.0.0 description at www.rcac.purdue.edu/api - 206 paths and 452 operations covering research computing groups and their members, depa
  name: Purdue RCAC API
  slug: purdue-rcac-api
- baseURL: https://api.hfs.purdue.edu/menus/v2
  baseurl_source: declared
  description: A public, keyless HTTP API operated by Purdue University Housing and Food Services at api.hfs.purdue.edu, serving dining-court locations, published daily menus by location and date, and per-item nutri
  name: Purdue HFS Dining Menus API
  slug: purdue-hfs-dining-menus-api
- description: The Purdue University Research Repository exposes an OAI-PMH 2.0 endpoint for harvesting research dataset metadata, supporting the standard verbs (Identify, ListSets, ListMetadataFormats, ListIdentifi
  name: PURR OAI-PMH Metadata API
  slug: purr-oaipmh
- description: 'Purdue operates its own Shibboleth identity provider, entityID https://idp.purdue.edu/idp/shibboleth, with SAML 2.0 SSO endpoints under sso.purdue.edu. The IdP is registered in InCommon and therefore '
  name: Purdue Shibboleth Identity Provider
  slug: purdue-shibboleth-idp
- description: 'Purdue e-Pubs is the university''s institutional repository for scholarly output, reachable at docs.lib.purdue.edu with a working OAI-PMH 2.0 endpoint. The content, the collections and the scholarship '
  name: Purdue e-Pubs OAI-PMH (bepress Digital Commons tenant)
  slug: purdue-epubs-oaipmh
- description: Purdue's public events calendar at events.purdue.edu serves a live JSON events API on the Localist v2 contract. The events are Purdue's; the API is Localist's. events.purdue.edu is a CNAME chain to pu
  name: Purdue Events Calendar API (Localist tenant)
  slug: purdue-events-api
- description: Purdue.io is an OData v4 API over Purdue's course catalog, started in 2015 as a Computer Science senior design project and still maintained by its community. It is genuinely useful and genuinely about
  name: Purdue.io Course Catalog API (community-built, third-party)
  slug: purdueio-course-catalog-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.purdue.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Purdue
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/purdue-university/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.rcac.purdue.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://purr.purdue.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.purdue.edu/idp/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.purdue.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.purdue.edu/ai/ai-governance-and-review/
- group: build
  title: ''
  type: AITooling
  url: https://www.purdue.edu/ai/enterprise-ai-toolkit/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.purdue.edu/purdue/about/privacy-notice.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.purdue.edu/home/disclaimer/
- group: operate
  title: ''
  type: Support
  url: https://www.rcac.purdue.edu/help
- group: company
  title: ''
  type: Blog
  url: https://www.purdue.edu/newsroom/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rcac.purdue.edu/knowledge
- group: docs
  title: ''
  type: APIReference
  url: https://www.rcac.purdue.edu/api
- group: auth
  title: ''
  type: Authentication
  url: authentication/purdue-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/purdue-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/purdue-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/purdue-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/purdue-openapi-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/purdue-vocabulary.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/purdue-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/purdue-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/purdue-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/purdue-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Purdue University is a public land-grant research university in West Lafayette, Indiana, United States, a member of the Association of American Universities and the Big Ten Academic Alliance. Purdue operates no central developer portal, no API gateway and no self-service key issuance, and its programmable footprint is small, scattered across service units, and almost entirely undocumented. Four surfaces were confirmed institution-operated by live probe: the Rosen Center for Advanced Computing (RCAC) publishes its own OpenAPI 3.0 document at www.rcac.purdue.edu/api covering 206 paths and 452 operations behind Purdue Web Authentication; Housing and Food Services runs an open, keyless dining menus API at api.hfs.purdue.edu/menus/v2; the Purdue University Research Repository exposes an OAI-PMH 2.0 endpoint at purr.purdue.edu/oaipmh; and Purdue runs its own Shibboleth identity provider, registered in InCommon, whose SAML 2.0 metadata is public. Three further surfaces are recorded
  as tenant relationships, not Purdue engineering - Purdue e-Pubs on bepress Digital Commons, the events calendar on Localist, and the community-built Purdue.io course-catalog API, which runs on a privately registered domain and DigitalOcean hosting with no evidence of institutional operation or endorsement. The Purdue Libraries API host resolves but has served only a placeholder page since at least June 2026.'
examples:
- key_count: 2
  name: Purdue Hfs Location Menu Example
  slug: purdue-hfs-location-menu-example
- key_count: 2
  name: Purdue Hfs Locations Example
  slug: purdue-hfs-locations-example
finops:
- name: Purdue Finops
  service_category: Education
  slug: purdue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/purdue.png
json_schemas:
- name: Purdue HFS Published Daily Menu
  property_count: 5
  slug: purdue-hfs-location-menu
- name: Purdue HFS Dining Location
  property_count: 11
  slug: purdue-hfs-location
layout: provider
modified: '2026-08-30'
name: Purdue University
nav: Providers
network: true
overview: 'Purdue University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Purdue RCAC API and Purdue HFS Dining Menus API. Tagged areas include University, Higher Education, Education, United States, and Indiana.


  The Purdue University catalog on APIs.io includes 1 Spectral governance ruleset.


  Purdue University''s developer surface includes support, engineering blog, documentation, API reference, authentication, and 21 more developer resources.'
plans:
- name: Purdue Plans Pricing
  plan_count: 2
  slug: purdue-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Purdue Rate Limits
  slug: purdue-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Purdue University API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 3
  slug: purdue-openapi-spectral-rules
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 29.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 58.3
    contract_quality: 44.4
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 23.7
  previous_composite: 47.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/screenshots/purdue-2026-06-20T192313.png
security:
- kind: authentication
  name: Purdue Authentication
  slug: purdue-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Purdue Domain Security
  slug: purdue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: purdue
tags:
- University
- Higher Education
- Education
- United States
- Indiana
- Public Research University
- Land-Grant University
- Association of American Universities
- Big Ten Academic Alliance
- Research Computing
- Research Repository
- Identity Federation
- OAI-PMH
- Campus Life
- Course Catalog
website: https://www.purdue.edu/
---
