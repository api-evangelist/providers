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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Opensanctions Agentic Access
  operation_count: 12
  slug: opensanctions-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: Endpoints for fetching data from the API, either related to individual entities, or for bulk data access in various forms.
  name: OpenSanctions Data access API
  slug: opensanctions-data-access-api
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: Endpoints for conducting a user-facing entity search or matching a local data store against the given dataset.
  name: OpenSanctions Matching API
  slug: opensanctions-matching-api
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: The Reconciliation Service provides four separate endpoints that work in concert to implement the data matching API used by OpenRefine, Wikidata and several other services and utilities.
  name: OpenSanctions Reconciliation API
  slug: opensanctions-reconciliation-api
- baseURL: https://api.opensanctions.org
  baseurl_source: declared
  description: Service metadata endpoints for health checking and getting the application metadata to be used in client applications.
  name: OpenSanctions System information API
  slug: opensanctions-system-information-api
artifact_total: 12
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/overlays/opensanctions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opensanctions-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/agentic-access/opensanctions-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opensanctions-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/security/opensanctions-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/security/opensanctions-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/opensanctions-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/security/opensanctions-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/opensanctions-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.opensanctions.org/docs/security/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/conformance/opensanctions-conformance.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/lifecycle/opensanctions-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opensanctions-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/changelog/opensanctions-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opensanctions-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/authentication/opensanctions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opensanctions-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/errors/opensanctions-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opensanctions-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/conventions/opensanctions-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opensanctions-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/rate-limits/opensanctions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opensanctions-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/plans/opensanctions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opensanctions-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/packages/opensanctions-packages.yml
  title: ''
  type: Packages
  url: packages/opensanctions-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/packages/opensanctions-packages.yml
  title: ''
  type: SDKs
  url: packages/opensanctions-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/cli/opensanctions-cli.yml
  title: ''
  type: CLI
  url: cli/opensanctions-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/sandbox/opensanctions-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/opensanctions-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/mcp/opensanctions-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/opensanctions-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/llms/opensanctions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opensanctions-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/data-model/opensanctions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opensanctions-data-model.yml
created: '2026-05-28'
description: OpenSanctions is an open database of international sanctions, watchlists, criminal designations and politically exposed persons (PEPs), published as a screening API, bulk data downloads and MIT-licensed open-source software from Berlin. It consolidates hundreds of primary government sources — OFAC, the EU consolidated list, UN Security Council, UK FCDO, procurement debarment registers, regulatory enforcements and national PEP registers — into a single de-duplicated entity graph expressed in the FollowTheMoney ontology it stewards. The hosted Screening API at api.opensanctions.org offers query-by-example entity matching with scored, per-feature explanations, free-text search, entity fetch with relationship traversal, statement-level provenance for every asserted value, and an OpenRefine reconciliation manifest. It is used for customer due diligence, transaction monitoring, supply-chain and vessel screening, KYB, and investigative journalism. The dataset is free for non-commercial
  use under CC BY-NC 4.0; commercial use is licensed, and the API is metered at EUR 0.10 per query.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opensanctions.png
layout: provider
mcp_servers:
- description: ''
  name: OpenSanctions MCP Server
  slug: opensanctions-mcp-server
modified: '2026-08-27'
name: OpenSanctions
nav: Providers
network: true
overview: 'OpenSanctions publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data access API, Matching API, Reconciliation API, and 1 more. Tagged areas include Sanctions Screening, Anti-Money Laundering, Politically Exposed Persons, Compliance, and Financial Crime.


  OpenSanctions'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Opensanctions Plans Pricing
  plan_count: 4
  slug: opensanctions-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Opensanctions Rate Limits
  slug: opensanctions-rate-limits
score:
  band: exemplar
  composite: 73.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 48.3
    developer_ergonomics: 80.4
    discoverability: 83.3
    operational_transparency: 76.3
  previous_composite: 74.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/screenshots/opensanctions-2026-06-20T191029.png
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
slug: opensanctions
tags:
- Sanctions Screening
- Anti-Money Laundering
- Politically Exposed Persons
- Compliance
- Financial Crime
- Know Your Customer
- Entity Resolution
- Open Data
- Risk Data
- Due Diligence
- Public APIs
- agent-native
website: https://www.opensanctions.org/
---
