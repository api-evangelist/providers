---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Blobpedia Org Agentic Access
  operation_count: 36
  slug: blobpedia-org-agentic-access
  summary_line: 36 operations · 1 acting
api_count: 1
apis:
- description: Public, unauthenticated REST API over the BLOBPEDIA corpus.
  name: BLOBPEDIA REST API
  slug: blobpedia-rest-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: Search popularity, CSP violations
  name: BLOBPEDIA Analytics API
  slug: blobpedia-org-analytics-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: Celestia Improvement Proposals
  name: BLOBPEDIA CIPs API
  slug: blobpedia-org-cips-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: Activity stream, sources catalog
  name: BLOBPEDIA Discovery API
  slug: blobpedia-org-discovery-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: Forum, GitHub Discussions
  name: BLOBPEDIA Discussions API
  slug: blobpedia-org-discussions-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: docs.celestia.org pages, whitepapers
  name: BLOBPEDIA Documentation API
  slug: blobpedia-org-documentation-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: Issues, PRs, releases, repos
  name: BLOBPEDIA GitHub API
  slug: blobpedia-org-github-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: API self-description
  name: BLOBPEDIA Meta API
  slug: blobpedia-org-meta-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: On-chain state, market data, stats
  name: BLOBPEDIA Network API
  slug: blobpedia-org-network-api
- baseURL: https://blobpedia.org
  baseurl_source: declared
  description: Full-text + fuzzy search across all sources
  name: BLOBPEDIA Search API
  slug: blobpedia-org-search-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/blobpedia-org/agentic-access/blobpedia-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blobpedia-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blobpedia-org/rules/blobpedia-org-rules.yml
  title: ''
  type: Spectral
  url: rules/blobpedia-org-rules.yml
- group: design
  href: https://artifacts.apis.io/blobpedia-org/json-ld/blobpedia-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blobpedia-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/blobpedia-org/vocabulary/blobpedia-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blobpedia-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blobpedia-org/data-model/blobpedia-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blobpedia-org-data-model.yml
- group: build
  href: https://artifacts.apis.io/blobpedia-org/cli/blobpedia-org-cli.yml
  title: ''
  type: CLI
  url: cli/blobpedia-org-cli.yml
- group: auth
  href: https://artifacts.apis.io/blobpedia-org/authentication/blobpedia-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blobpedia-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/blobpedia-org/errors/blobpedia-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blobpedia-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blobpedia-org/conformance/blobpedia-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blobpedia-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blobpedia-org/llms/blobpedia-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blobpedia-org-llms.txt
- group: auth
  href: https://artifacts.apis.io/blobpedia-org/well-known/blobpedia-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blobpedia-org-security.txt
- group: agent
  href: https://artifacts.apis.io/blobpedia-org/well-known/blobpedia-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blobpedia-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/blobpedia-org/hosts/blobpedia-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blobpedia-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/blobpedia-org/vendors/blobpedia-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blobpedia-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blobpedia.org/terms
- group: auth
  title: ''
  type: Security
  url: https://blobpedia.org/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blobpedia.org/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evstack
- group: docs
  title: ''
  type: Documentation
  url: https://blobpedia.org/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://blobpedia.org/releases
- group: company
  title: ''
  type: Blog
  url: https://blobpedia.org/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://blobpedia.org/docs/50
- group: docs
  title: ''
  type: APIReference
  url: https://blobpedia.org/api/v1/reference
- group: auth
  href: https://artifacts.apis.io/blobpedia-org/security/blobpedia-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blobpedia-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blobpedia-org/security/blobpedia-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blobpedia-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blobpedia.org/
created: '2026-11-02'
description: BLOBPEDIA is the central knowledge hub for the Celestia ecosystem, providing indexed, searchable CIPs, documentation, whitepapers, discussions and ecosystem activity. It offers a unified full‑text search across the modular data‑availability layer and node documentation, serving developers and community members.
image: https://blobpedia.org/opengraph-image?f92c5701a536284a
jsonld:
- class_count: 3
  name: Blobpedia Org Context
  property_count: 13
  slug: blobpedia-org-context
layout: provider
modified: '2026-11-02'
name: BLOBPEDIA
nav: Providers
network: true
overview: 'BLOBPEDIA publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, CIPs API, Discovery API, and 7 more. Tagged areas include Company, Celestia, Knowledge Hub, Documentation, and Community.


  The BLOBPEDIA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BLOBPEDIA''s developer surface includes CLI, authentication, documentation, changelog, engineering blog, getting-started guide, API reference, and 19 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: BLOBPEDIA API Rules
  rule_count: 46
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 4
  slug: blobpedia-org-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.6
    developer_ergonomics: 34.5
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blobpedia Org Authentication
  slug: blobpedia-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blobpedia Org Domain Security
  slug: blobpedia-org-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Blobpedia Org Vulnerability Disclosure
  slug: blobpedia-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blobpedia-org
tags:
- Company
- Celestia
- Knowledge Hub
- Documentation
- Community
- Open Source
website: https://blobpedia.org/
---
