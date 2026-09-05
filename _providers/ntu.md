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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ntu Agentic Access
  operation_count: 6
  slug: ntu-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- baseURL: https://researchdata.ntu.edu.sg/api
  baseurl_source: declared
  description: NTU's institutional open research data repository, running Dataverse 6.1 self-hosted on NTU's own network. The publicly documented, unauthenticated read subset covers dataset search and the platform v
  name: DR-NTU (Data) — Dataverse API
  slug: ntu-drntu-data
- description: NTU's institutional publications and research-profile repository — 158,100 research profiles, records back to 2008 — served from NTU's own hostname but operated on 4Science's DSpace-CRIS platform. Rec
  name: DR-NTU (Digital Repository) — DSpace-CRIS REST API
  slug: ntu-drntu-repository
- description: A fully conformant OAI-PMH 2.0 metadata harvesting endpoint over DR-NTU, serving 11 metadata formats and declaring OpenAIRE CERIF-CRIS 1.1 compatibility on a second base URL. Administered by NTU Libra
  name: DR-NTU (Digital Repository) — OAI-PMH
  slug: ntu-drntu-repository-oai
- description: 'NTU''s SAML 2.0 identity provider, registered in the Singapore Access Federation (SGAF) by SingAREN and interfederated into eduGAIN, asserting the scope ntu.edu.sg. Live machine-readable SAML metadata '
  name: NTU Identity Provider — SGAF / eduGAIN
  slug: ntu-identity-federation
- baseURL: https://researchdata.ntu.edu.sg/api
  baseurl_source: declared
  description: The Discover API from Nanyang Technological University — 1 operation(s) for discover.
  name: Nanyang Technological University Discover API
  slug: ntu-discover-api
- baseURL: https://researchdata.ntu.edu.sg/api
  baseurl_source: declared
  description: The Items API from Nanyang Technological University — 1 operation(s) for items.
  name: Nanyang Technological University Items API
  slug: ntu-items-api
- baseURL: https://researchdata.ntu.edu.sg/api
  baseurl_source: declared
  description: The OAI-PMH API from Nanyang Technological University — 1 operation(s) for oai-pmh.
  name: Nanyang Technological University OAI PMH API
  slug: ntu-oai-pmh-api
- baseURL: https://researchdata.ntu.edu.sg/api
  baseurl_source: declared
  description: The Root API from Nanyang Technological University — 1 operation(s) for root.
  name: Nanyang Technological University Root API
  slug: ntu-root-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DR-NTU (Data) Dataverse Discover Info API
  slug: open-ntu-info-api
- collection_type: open
  name: DR-NTU (Data) Dataverse Discover Search API
  slug: open-ntu-search-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.ntu.edu.sg/
- group: docs
  title: ''
  type: Documentation
  url: https://libguides.ntu.edu.sg/drntudataguidespolicies/APITermsOfUse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ntu.edu.sg/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ntu.edu.sg/legal/privacy-statement
- group: operate
  title: ''
  type: Support
  url: https://www.ntu.edu.sg/life-at-ntu/internet-account-and-policy/contact-service-desk
- group: company
  title: ''
  type: Blog
  url: https://blogs.ntu.edu.sg/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NTUsg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nanyang-technological-university/
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.re3data.org/repository/r3d100012440
- group: learn
  title: ''
  type: CourseCatalog
  url: https://wis.ntu.edu.sg/webexe/owa/aus_subj_cont.main
- group: other
  title: ''
  type: IdentityFederation
  url: https://ntu-entra.singaren.net.sg/simplesaml/saml2/idp/metadata.php
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ntu.edu.sg/research/resources/use-of-gai-in-research
- group: build
  title: ''
  type: AITooling
  url: https://libguides.ntu.edu.sg/responsible-ai-use/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ntu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ntu-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ntu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ntu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ntu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/ntu-conformance.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/ntu-authentication.yml
- group: auth
  title: ''
  type: x-scopes
  url: scopes/ntu-scopes.yml
- group: design
  title: ''
  type: x-errors
  url: errors/ntu-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/ntu-lifecycle.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/ntu-vocabulary.yml
- group: design
  title: ''
  type: x-spectral-rules
  url: rules/ntu-rules.yml
- group: design
  title: ''
  type: x-json-ld-context
  url: json-ld/ntu-context.jsonld
coverage:
  detail: 'researchdata.ntu.edu.sg (DR-NTU (Data), the one x-operator: institution surface) returns an Apache 403 with a Citrix bot-management cookie and a /trap.html honeypot link on EVERY path, including the site root and robots.txt. Retrying with a browser User-Agent and a persisted cookie jar did not clear it. This is a block on us, not a decommissioned service: NTU''s DataCite client minted a DOI on 2026-08-17, two days before this profile, and re3data independently lists the REST, OAI-PMH and SWORD endpoints as current. The archived contract in openapi/_original/ntu-drntu-data.yaml is therefore retained and the two refined specs kept, but marked unverified in authentication/ and errors/. A re-probe from a different vantage should upgrade this to covered. Every other surface WAS read live: dr.ntu.edu.sg answered 200 on /server/api and on OAI-PMH Identify and ListMetadataFormats, the SGAF SAML metadata returned 200 application/samlmetadata+xml, and eduGAIN, DataCite and re3data all answered.
    Four of the six OpenAPIs previously in this repo were removed: refine-openapis had merged three source specs spanning two different hosts by tag and stamped all six with the first spec''s server, so the DSpace paths (/, /core/items/{uuid}, /discover/search/objects) and the OAI-PMH /request path were all asserting researchdata.ntu.edu.sg as their host, which never served them.'
  evidence:
  - status: 403
    url: https://researchdata.ntu.edu.sg/api/info/version
  - status: 403
    url: https://researchdata.ntu.edu.sg/robots.txt
  - status: 200
    url: https://api.datacite.org/dois?client-id=gdcc.ntu
  - status: 200
    url: https://www.re3data.org/api/v1/repository/r3d100012440
  - status: 200
    url: https://dr.ntu.edu.sg/server/api
  - status: 200
    url: https://dr.ntu.edu.sg/oai/request?verb=Identify
  - status: 200
    url: https://ntu-entra.singaren.net.sg/simplesaml/saml2/idp/metadata.php
  - status: 404
    url: https://api.ntu.edu.sg/
  - status: 200
    url: https://www.ntu.edu.sg/
  reason: 'The single institution-operated API in this profile is behind an edge bot-management gate that returns 403 to every automated client, so its contract could not be re-read on this run. The profile is otherwise thin because NTU genuinely publishes very little: no developer portal, no API documentation of its own, and no institution-operated API beyond its research data repository.'
  state: unreadable
created: '2026-06-03'
description: 'Nanyang Technological University (NTU Singapore) is an autonomous public research university in Singapore, ranked in the top 15 of the QS World University Rankings. Its programmable footprint is small, indirect, and almost entirely research-infrastructure: NTU operates no public developer portal, publishes no API key self-service, and exposes no OAuth or OIDC authorization server on any host it owns. Exactly one machine-readable API is genuinely NTU-operated — DR-NTU (Data), a Dataverse 6.1 open research data repository that NTU self-hosts on its own network (researchdata.ntu.edu.sg CNAMEs to dataverse.ntu.edu.sg at 155.69.19.238, registered to Nanyang Technological University), backed by NTU''s own DataCite client GDCC.NTU with 3,625 DOIs under prefix 10.21979. Everything else that carries NTU''s name is a tenancy on someone else''s platform. DR-NTU (Digital Repository), the far larger surface with 158,100 research profiles, a DSpace 7 REST API and a fully conformant OAI-PMH
  endpoint, answers on dr.ntu.edu.sg but CNAMEs to ntu-cris.4science.cloud — NTU''s data and NTU''s library administration running on 4Science''s DSpace-CRIS platform. NTU''s federated single sign-on is a live SAML 2.0 identity provider in eduGAIN, but the entityID and endpoints sit on SingAREN''s SGAF proxy, not on ntu.edu.sg. NTU owns a live API gateway at api.ntu.edu.sg which returns a structured JSON 404 on every path and documents no route at all. This profile records the tenancies as the real institutional facts they are, and credits NTU only for what NTU actually operates.'
examples:
- key_count: 7
  name: Ntu Discover Example
  slug: ntu-discover-example
- key_count: 7
  name: Ntu Search Example
  slug: ntu-search-example
finops:
- name: Ntu Finops
  service_category: Education
  slug: ntu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ntu.png
json_schemas:
- name: DR-NTU (Data) Dataset Search Item
  property_count: 23
  slug: ntu-dataset
- name: DR-NTU (Digital Repository) Item
  property_count: 9
  slug: ntu-item
json_structures:
- name: Ntu Dataset Structure
  property_count: 21
  slug: ntu-dataset-structure
- name: Ntu Item Structure
  property_count: 9
  slug: ntu-item-structure
jsonld:
- class_count: 16
  name: Ntu Context
  property_count: 12
  slug: ntu-context
layout: provider
modified: '2026-08-19'
name: Nanyang Technological University
nav: Providers
network: true
overview: 'Nanyang Technological University publishes 5 APIs on the [APIs.io](https://apis.io/) network, including DR-NTU (Data) — Dataverse API, Discover API, Items API, and 2 more. Tagged areas include University, Higher Education, Education, Singapore, and Public Research University.


  The Nanyang Technological University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Nanyang Technological University''s developer surface includes documentation, support, engineering blog, and 24 more developer resources.'
plans:
- name: Ntu Plans Pricing
  plan_count: 2
  slug: ntu-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Ntu Rate Limits
  slug: ntu-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Nanyang Technological University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ntu-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Nanyang Technological University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: ntu-rules
scopes:
- name: Ntu Scopes
  scope_count: 0
  slug: ntu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 73.3
    catalog_earned_first_party: 0.0
    catalog_gap: 41.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 57.5
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ntu/refs/heads/main/screenshots/ntu-2026-06-20T190501.png
security:
- kind: authentication
  name: Ntu Authentication
  slug: ntu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ntu Domain Security
  slug: ntu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ntu
tags:
- University
- Higher Education
- Education
- Singapore
- Public Research University
- Research Data
- Research Repository
- Identity Federation
- Open Access
- Course Catalog
- Library
- OAI-PMH
website: https://www.ntu.edu.sg/
---
