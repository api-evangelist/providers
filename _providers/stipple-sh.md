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
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: unknown
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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 45
  human_in_the_loop: 2
  name: Stipple Sh Agentic Access
  operation_count: 117
  slug: stipple-sh-agentic-access
  summary_line: 117 operations · 45 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Agent Card.json API from stipple-sh — 1 operation(s) for agent card.json.
  name: stipple-sh Agent Card.json API
  slug: stipple-sh-agent-card-json-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Agent.json API from stipple-sh — 1 operation(s) for agent.json.
  name: stipple-sh Agent.json API
  slug: stipple-sh-agent-json-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Agents.md API from stipple-sh — 1 operation(s) for agents.md.
  name: stipple-sh Agents.md API
  slug: stipple-sh-agents-md-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: Sign-in sessions for the web app (magic link + Google).
  name: stipple-sh Auth API
  slug: stipple-sh-auth-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Bids API from stipple-sh — 35 operation(s) for bids.
  name: stipple-sh Bids API
  slug: stipple-sh-bids-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Companies API from stipple-sh — 1 operation(s) for companies.
  name: stipple-sh Companies API
  slug: stipple-sh-companies-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Health API from stipple-sh — 1 operation(s) for health.
  name: stipple-sh Health API
  slug: stipple-sh-health-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Healthz API from stipple-sh — 1 operation(s) for healthz.
  name: stipple-sh Healthz API
  slug: stipple-sh-healthz-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: Self-serve API keys and usage metering.
  name: stipple-sh Keys & usage API
  slug: stipple-sh-keys-usage-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Livez API from stipple-sh — 1 operation(s) for livez.
  name: stipple-sh Livez API
  slug: stipple-sh-livez-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Llms.txt API from stipple-sh — 1 operation(s) for llms.txt.
  name: stipple-sh Llms.txt API
  slug: stipple-sh-llms-txt-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: Health, discovery, feedback, and cache-check endpoints.
  name: stipple-sh Meta API
  slug: stipple-sh-meta-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Orgs API from stipple-sh — 7 operation(s) for orgs.
  name: stipple-sh Orgs API
  slug: stipple-sh-orgs-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The Tenders API from stipple-sh — 24 operation(s) for tenders.
  name: stipple-sh Tenders API
  slug: stipple-sh-tenders-api
- baseURL: https://www.stipple.sh
  baseurl_source: declared
  description: The .well Known API from stipple-sh — 2 operation(s) for .well known.
  name: stipple-sh .well Known API
  slug: stipple-sh-well-known-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/stipple-sh/agentic-access/stipple-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stipple-sh-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/stipple-sh/rules/stipple-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/stipple-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/stipple-sh/json-ld/stipple-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stipple-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/stipple-sh/vocabulary/stipple-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stipple-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/stipple-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/stipple-sh/data-model/stipple-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stipple-sh-data-model.yml
- group: operate
  href: https://artifacts.apis.io/stipple-sh/changelog/stipple-sh-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stipple-sh-changelog.yml
- group: auth
  href: https://artifacts.apis.io/stipple-sh/authentication/stipple-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stipple-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/stipple-sh/errors/stipple-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stipple-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stipple-sh/conformance/stipple-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stipple-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stipple-sh/llms/stipple-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stipple-sh-llms.txt
- group: other
  href: https://artifacts.apis.io/stipple-sh/a2a/stipple-sh-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/stipple-sh-a2a.yml
- group: agent
  href: https://artifacts.apis.io/stipple-sh/mcp/stipple-sh-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stipple-sh-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stipple-sh/well-known/stipple-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stipple-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/stipple-sh/hosts/stipple-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stipple-sh-hosts.yml
- group: auth
  href: https://artifacts.apis.io/stipple-sh/security/stipple-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stipple-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stipple.sh/
- group: docs
  title: ''
  type: APIReference
  url: https://www.stipple.sh/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.stipple.sh/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stipple.sh/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stipple.sh/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.stipple.sh/login?from=front_page
- group: start
  title: ''
  type: Login
  url: https://www.stipple.sh/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stipple.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stipple.sh/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.stipple.sh/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.stipple.sh/changelog
created: '2026-10-29'
description: Stipple.sh is an Australian‑focused platform that aggregates and publishes government procurement opportunities, tenders, and grant programmes across all Australian states and territories. It provides searchable listings, detailed resource pages, and tools for businesses and consultants to discover, track, and respond to public sector contracts and funding opportunities. The service includes up‑to‑date data on tender release dates, response timelines, and buyer information, helping users stay informed and competitive in the public procurement market.
image: https://www.stipple.sh/og-image.png
json_schemas:
- name: Body_upload_bid_files_v1_bids__bid__files_post
  property_count: 3
  slug: stipple-sh-body-upload-bid-files-v1-bids-bid-files-post
- name: ContactBody
  property_count: 7
  slug: stipple-sh-contact-body
- name: RequestLinkBody
  property_count: 4
  slug: stipple-sh-request-link-body
- name: TenderMatchBody
  property_count: 7
  slug: stipple-sh-tender-match-body
- name: TenderWatchBody
  property_count: 14
  slug: stipple-sh-tender-watch-body
- name: ToolFeedbackBody
  property_count: 5
  slug: stipple-sh-tool-feedback-body
jsonld:
- class_count: 22
  name: Stipple Sh Context
  property_count: 57
  slug: stipple-sh-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.stipple.sh.
  name: stipple-sh MCP Server
  slug: stipple-sh-mcp-yml
modified: '2026-10-29'
name: stipple-sh
nav: Providers
network: true
overview: 'stipple-sh publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Card.json API, Agent.json API, Agents.md API, and 12 more. Tagged areas include Company, Government, Procurement, Tenders, and Australia.


  The stipple-sh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  stipple-sh''s developer surface includes changelog, authentication, API reference, documentation, getting-started guide, pricing, signup flow, and 20 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 0
  name: Stipple Sh Rate Limits
  slug: stipple-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: stipple-sh API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: stipple-sh-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 58.5
    developer_ergonomics: 32.6
    discoverability: 75.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stipple-sh/stipple-sh-2026-11-03T143937.png
security:
- kind: authentication
  name: Stipple Sh Authentication
  slug: stipple-sh-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stipple Sh Domain Security
  slug: stipple-sh-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: getting-started
  slug: stipple-sh-getting-started
slug: stipple-sh
tags:
- Company
- Government
- Procurement
- Tenders
- Australia
- Grants
website: https://stipple.sh/
---
