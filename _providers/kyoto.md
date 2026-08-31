---
access_model:
  confidence: high
  label: Free · No registration for the institution-operated public reads
  onboarding: unknown
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
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kyoto Agentic Access
  operation_count: 21
  slug: kyoto-agentic-access
  summary_line: 21 operations
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for KURENAI, the Kyoto University Research Information Repository. Anonymous, verb-driven, and serving 15 metadata formats including jpcoar_2.0 and jpcoar_1.0
  name: KURENAI OAI-PMH API
  slug: kyoto-oai-pmh-api
- description: The DSpace 7.6 HAL+JSON REST API of the Kyoto University Research Information Repository. The root document at /server/api advertises every endpoint as HAL links and reports dspaceVersion "DSpace 7.6"
  name: KURENAI DSpace REST API
  slug: kyoto-rest-api
- description: PandA is the Kyoto University Learning Support System, a Sakai deployment operated by the Institute for Information Management and Communication and published by the IIMC as the university's own educa
  name: PandA Learning Support System API (Sakai Entity Broker + IMS LTI)
  slug: kyoto-lms-api
- description: Kyoto University operates its own Shibboleth SAML 2.0 identity provider, run by the Institute for Information Management and Communication, with public machine-readable metadata at the canonical /idp/
  name: Kyoto University Shibboleth Identity Provider (GakuNin)
  slug: sso
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KURENAI Repository API (DSpace 7.6 REST + ) OAI-PMH API
  slug: open-kyoto-oai-pmh-api
- collection_type: open
  name: KURENAI Repository API (DSpace 7.6 + ) OAI-PMH REST API
  slug: open-kyoto-rest-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kyoto-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.kyoto-u.ac.jp/en
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.kulib.kyoto-u.ac.jp/
- group: other
  title: ''
  type: IdentityFederation
  url: https://authidp1.iimc.kyoto-u.ac.jp/idp/shibboleth
- group: learn
  title: ''
  type: Learning
  url: https://www.iimc.kyoto-u.ac.jp/en/services/education/lms
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.iimc.kyoto-u.ac.jp/en/services/comp
- group: build
  title: ''
  type: LibraryCatalog
  url: https://kuline.kulib.kyoto-u.ac.jp/opac/opac_search/
- group: build
  title: ''
  type: Library
  url: https://www.kulib.kyoto-u.ac.jp/
- group: start
  title: ''
  type: ResearchPortal
  url: https://kdb.iimc.kyoto-u.ac.jp/
- group: build
  title: ''
  type: AITooling
  url: https://www.iimc.kyoto-u.ac.jp/en/services/gen-ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.iimc.kyoto-u.ac.jp/en/services
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kyoto-u
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kyoto-u.ac.jp/en/site-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kyoto-u.ac.jp/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.kyoto-u.ac.jp/en/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kyoto-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/KyotoU_News
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/KyotoUniversityOfficial
- group: design
  title: ''
  type: Conformance
  url: conformance/kyoto-education-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kyoto-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/kyoto-errors.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/kyoto-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kyoto-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kyoto-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kyoto-context.jsonld
- group: design
  title: ''
  type: Rules
  url: rules/kyoto-rules.yml
- group: design
  title: ''
  type: Rules
  url: rules/kyoto-jsonschema-spectral-rules.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kyoto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyoto-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kyoto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kyoto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kyoto-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Kyoto University (京都大学) is a national research university in Kyoto, Japan, established in 1897 and ranked #36 in the QS World University Rankings. It operates no developer portal, no API gateway, no API terms of service and no OpenAPI of its own, and this profile records that plainly. What it does run, on its own hosts and its own network, is a small set of genuinely institution-operated machine-readable surfaces: KURENAI, the Kyoto University Research Information Repository, a self-hosted DSpace 7.6 with an anonymous HAL+JSON REST API and an OAI-PMH 2.0 endpoint serving 15 metadata formats including JPCOAR and junii2, holding content back to 2006; PandA, the university''s Sakai Learning Support System, whose Entity Broker answers JSON on 53 registered entity prefixes and which is a live IMS LTI 1.3 platform publishing its own signing keyset alongside a working LTI 1.1 outcomes service; and its own Shibboleth SAML 2.0 identity provider, registered in GakuNin, the Japanese academic
  federation, which participates in eduGAIN. Those surfaces sit on hosts inside 133.3.0.0/16, registered by JPNIC to Kyoto University as KUINS, or in the university''s own AWS account. Five of the twelve Kin Score education-regime standards are met with live evidence — oai-pmh, shibboleth, saml, lti and orcid — which is unusual for this cohort and entirely first-party. Everything else is a human-facing service: the KULINE library catalogue, the KDB researcher database, OpenCourseWare, and the generative-AI tooling the IIMC brokers from Google and Microsoft. Student information, course registration and timetable systems are behind campus accounts and are not public APIs.'
examples:
- key_count: 7
  name: Kyoto Getroot Example
  slug: kyoto-getRoot-example
- key_count: 3
  name: Kyoto Listcommunities Example
  slug: kyoto-listCommunities-example
- key_count: 3
  name: Kyoto Lti13 Keyset Example
  slug: kyoto-lti13-keyset-example
- key_count: 4
  name: Kyoto Oaiidentify Example
  slug: kyoto-oaiIdentify-example
- key_count: 3
  name: Kyoto Panda Session Example
  slug: kyoto-panda-session-example
- key_count: 3
  name: Kyoto Panda Tool Example
  slug: kyoto-panda-tool-example
finops:
- name: Kyoto Finops
  service_category: Education
  slug: kyoto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kyoto.png
json_schemas:
- name: KURENAI Collection
  property_count: 6
  slug: kyoto-collection
- name: KURENAI Community
  property_count: 9
  slug: kyoto-community
- name: PandA Entity Broker Collection
  property_count: 1
  slug: kyoto-panda-entity-collection
- name: PandA Tool
  property_count: 14
  slug: kyoto-panda-tool
json_structures:
- name: Kyoto Collection Structure
  property_count: 5
  slug: kyoto-collection-structure
- name: Kyoto Community Structure
  property_count: 7
  slug: kyoto-community-structure
jsonld:
- class_count: 12
  name: Kyoto Context
  property_count: 9
  slug: kyoto-context
layout: provider
modified: '2026-08-19'
name: Kyoto University
nav: Providers
network: true
overview: 'Kyoto University publishes 3 APIs on the [APIs.io](https://apis.io/) network: KURENAI OAI-PMH API, KURENAI DSpace REST API, and PandA Learning Support System API (Sakai Entity Broker + IMS LTI). Tagged areas include University, Higher Education, Education, Japan, and National University.


  The Kyoto University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Kyoto University''s developer surface includes documentation, GitHub presence, support, YouTube channel, authentication, and 28 more developer resources.'
plans:
- name: Kyoto Plans Pricing
  plan_count: 2
  slug: kyoto-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Kyoto Rate Limits
  slug: kyoto-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kyoto University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kyoto-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Kyoto University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: kyoto-rules
scopes:
- name: Kyoto Scopes
  scope_count: 0
  slug: kyoto-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 17.4
    contract_quality: 61.7
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 17.4
    operational_transparency: 10.5
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyoto/refs/heads/main/screenshots/kyoto-2026-06-20T184226.png
security:
- kind: authentication
  name: Kyoto Authentication
  slug: kyoto-authentication
  summary_line: none/saml/session · 6 schemes
- kind: domain-security
  name: Kyoto Domain Security
  slug: kyoto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kyoto
tags:
- University
- Higher Education
- Education
- Japan
- National University
- Research Repository
- Research Data
- Identity Federation
- Learning Management
- Open Access
- Research Computing
- Scholarly
website: https://www.kyoto-u.ac.jp/en
---
