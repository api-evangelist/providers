---
access_model:
  confidence: high
  label: Self-serve signup with a 30-day trial
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - https://www.opensanctions.org/api/
  - https://www.opensanctions.org/docs/api/authentication/
  - https://www.opensanctions.org/docs/api/faq/
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Opensanctions Agentic Access
  operation_count: 12
  slug: opensanctions-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: Endpoints for fetching data from the API, either related to individual entities, or for bulk data access in various forms.
  name: OpenSanctions Data access API
  phrasing_intents:
  - id: fetch_entity_entities__entity_id__get
    intent: Look up a sanctioned person or company by ID
    question: How do I pull the full OpenSanctions record for one entity when I already have its ID?
  - id: Fetch_Adjacent_Entities__entities__entity_id__adjacent_get
    intent: Page through everything linked to an entity
    question: Can I page through all the passports, sanctions and associates linked to an entity when there are too many to load at once?
  - id: Fetch_Adjacent_by_Property__entities__entity_id__adjacent__property_name__get
    intent: List an entity's links for one property
    question: Is there a way to get only the sanctions attached to an entity, rather than every linked record?
  - id: catalog_catalog_get
    intent: List the datasets the service indexes
    question: Which sanctions and PEP datasets are loaded into this yente instance?
  - id: statements_statements_get
    intent: Query raw statement-level entity data
    question: Where can I see the raw statements behind an entity, including which dataset asserted each property value?
  phrasing_ops: 5
  slug: opensanctions-data-access-api
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: Endpoints for conducting a user-facing entity search or matching a local data store against the given dataset.
  name: OpenSanctions Matching API
  phrasing_intents:
  - id: match_match__dataset__post
    intent: Screen people or companies against sanctions lists
    question: How do I screen a customer by name, date of birth and nationality against sanctions lists?
  - id: search_search__dataset__get
    intent: Search entities by a name or text
    question: Can I do a quick free-text name search across sanctioned and politically exposed people?
  phrasing_ops: 2
  slug: opensanctions-matching-api
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: The Reconciliation Service provides four separate endpoints that work in concert to implement the data matching API used by OpenRefine, Wikidata and several other services and utilities.
  name: OpenSanctions Reconciliation API
  phrasing_intents:
  - id: reconcile_reconcile__dataset__get
    intent: Get the OpenRefine reconciliation service manifest
    question: How do I connect OpenRefine to OpenSanctions to bulk match names in a spreadsheet?
  phrasing_ops: 1
  slug: opensanctions-reconciliation-api
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: Service metadata endpoints for health checking and getting the application metadata to be used in client applications.
  name: OpenSanctions System information API
  phrasing_intents:
  - id: healthz_healthz_get
    intent: Check that the service is responsive
    question: Is the screening service up and responding to requests?
  - id: readyz_readyz_get
    intent: Check whether the search index is built
    question: Has the search index finished building so queries will return results?
  - id: algorithms_algorithms_get
    intent: List the supported matching algorithms
    question: Which scoring algorithms can the matcher use?
  - id: force_update_updatez_post
    intent: Force the search index to rebuild
    question: How do I trigger a rebuild of the index on my self-hosted instance?
  phrasing_ops: 4
  slug: opensanctions-system-information-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/opensanctions/overlays/opensanctions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opensanctions-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/opensanctions/agentic-access/opensanctions-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opensanctions-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/opensanctions/security/opensanctions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opensanctions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opensanctions.org/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.opensanctions.org/articles/rss/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.opensanctions.org/docs/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.opensanctions.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.opensanctions.org/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.opensanctions.org/docs/api/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://www.opensanctions.org/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://discuss.opensanctions.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opensanctions
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/opensanctions/api-examples
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opensanctions.org/api/
- group: start
  title: ''
  type: SignUp
  url: https://www.opensanctions.org/api/
- group: start
  title: ''
  type: Login
  url: https://www.opensanctions.org/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opensanctions.org/docs/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opensanctions.org/docs/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.opensanctions.org/docs/security/
- group: auth
  href: https://artifacts.apis.io/opensanctions/security/opensanctions-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/opensanctions-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/opensanctions/security/opensanctions-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/opensanctions-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opensanctions.org/docs/security/
- group: design
  href: https://artifacts.apis.io/opensanctions/conformance/opensanctions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opensanctions-conformance.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opensanctions.org/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.opensanctions.org/docs/data/changes/
- group: design
  href: https://artifacts.apis.io/opensanctions/lifecycle/opensanctions-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opensanctions-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/opensanctions/changelog/opensanctions-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opensanctions-changelog.yml
- group: auth
  href: https://artifacts.apis.io/opensanctions/authentication/opensanctions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opensanctions-authentication.yml
- group: design
  href: https://artifacts.apis.io/opensanctions/errors/opensanctions-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opensanctions-problem-types.yml
- group: design
  href: https://artifacts.apis.io/opensanctions/conventions/opensanctions-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opensanctions-conventions.yml
- group: operate
  href: https://artifacts.apis.io/opensanctions/rate-limits/opensanctions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opensanctions-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/opensanctions/plans/opensanctions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opensanctions-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/opensanctions/packages/opensanctions-packages.yml
  title: ''
  type: Packages
  url: packages/opensanctions-packages.yml
- group: build
  href: https://artifacts.apis.io/opensanctions/packages/opensanctions-packages.yml
  title: ''
  type: SDKs
  url: packages/opensanctions-packages.yml
- group: build
  href: https://artifacts.apis.io/opensanctions/cli/opensanctions-cli.yml
  title: ''
  type: CLI
  url: cli/opensanctions-cli.yml
- group: start
  href: https://artifacts.apis.io/opensanctions/sandbox/opensanctions-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/opensanctions-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/opensanctions/mcp/opensanctions-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/opensanctions-mcp.yml
- group: agent
  href: https://artifacts.apis.io/opensanctions/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/opensanctions/llms/opensanctions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opensanctions-llms.txt
- group: design
  href: https://artifacts.apis.io/opensanctions/data-model/opensanctions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opensanctions-data-model.yml
created: '2026-05-28'
description: OpenSanctions is an open database of international sanctions, watchlists, criminal designations and politically exposed persons (PEPs), published as a screening API, bulk data downloads and MIT-licensed open-source software from Berlin. It consolidates hundreds of primary government sources — OFAC, the EU consolidated list, UN Security Council, UK FCDO, procurement debarment registers, regulatory enforcements and national PEP registers — into a single de-duplicated entity graph expressed in the FollowTheMoney ontology it stewards. The hosted Screening API at api.opensanctions.org offers query-by-example entity matching with scored, per-feature explanations, free-text search, entity fetch with relationship traversal, statement-level provenance for every asserted value, and an OpenRefine reconciliation manifest. It is used for customer due diligence, transaction monitoring, supply-chain and vessel screening, KYB, and investigative journalism. The dataset is free for non-commercial
  use under CC BY-NC 4.0; commercial use is licensed, and the API is metered at EUR 0.10 per query.
finops:
- has_sources: true
  method: derived
  name: Opensanctions Finops
  primary_unit: credit bundle
  service_category: ''
  slug: opensanctions-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opensanctions.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 10 tools listed.
  name: OpenSanctions MCP Server
  slug: yente
modified: '2026-08-27'
name: OpenSanctions
nav: Providers
network: true
overview: 'OpenSanctions publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data access API, Matching API, Reconciliation API, and 1 more. Tagged areas include Sanctions Screening, AML, Politically Exposed Persons, Compliance, and Financial Crime.


  The OpenSanctions catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenSanctions'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Opensanctions Plans Pricing
  plan_count: 6
  slug: opensanctions-plans-pricing
- name: Opensanctions Price Estimates
  plan_count: 0
  slug: opensanctions-price-estimates
random_paper: 20
rate_limits:
- limit_count: 3
  name: Opensanctions Rate Limits
  slug: opensanctions-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: OpenSanctions API Rules
  rule_count: 50
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 2
  slug: opensanctions-rules
score:
  band: exemplar
  composite: 72.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 48.3
    developer_ergonomics: 80.4
    discoverability: 78.3
    operational_transparency: 76.3
  previous_composite: 71.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/opensanctions/opensanctions-2026-06-20T191029.png
security:
- kind: authentication
  name: Opensanctions Authentication
  slug: opensanctions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opensanctions Domain Security
  slug: opensanctions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opensanctions Vulnerability Disclosure
  slug: opensanctions-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Opensanctions Trust Center
  slug: opensanctions-trust-center
  summary_line: ISO/IEC 27001:2022
skill_count: 3
skills:
- name: Investigate an entity and audit where each claim came from
  slug: opensanctions-investigate-entity
- name: Keep a screening integration fresh and monitor for changes
  slug: opensanctions-monitor-datasets
- name: Screen a person or company against sanctions and PEP lists
  slug: opensanctions-screen-entity
slug: opensanctions
tags:
- Sanctions Screening
- AML
- Politically Exposed Persons
- Compliance
- Financial Crime
- KYC
- Entity Resolution
- Open Data
- Risk Data
- Due Diligence
- Public APIs
- Agent-Native
website: https://www.opensanctions.org/
---
