---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Difficat Com Agentic Access
  operation_count: 17
  slug: difficat-com-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- baseURL: https://app.difficat.com/api/v1
  baseurl_source: declared
  description: The Balance API from DiffiCat — 1 operation(s) for balance.
  name: DiffiCat Balance API
  slug: difficat-com-balance-api
- baseURL: https://app.difficat.com/api/v1
  baseurl_source: declared
  description: The Compares API from DiffiCat — 1 operation(s) for compares.
  name: DiffiCat Compares API
  slug: difficat-com-compares-api
- baseURL: https://app.difficat.com/api/v1
  baseurl_source: declared
  description: The Discover API from DiffiCat — 1 operation(s) for discover.
  name: DiffiCat Discover API
  slug: difficat-com-discover-api
- baseURL: https://app.difficat.com/api/v1
  baseurl_source: declared
  description: The Feedback API from DiffiCat — 1 operation(s) for feedback.
  name: DiffiCat Feedback API
  slug: difficat-com-feedback-api
- baseURL: https://app.difficat.com/api/v1
  baseurl_source: declared
  description: The Jobs API from DiffiCat — 6 operation(s) for jobs.
  name: DiffiCat Jobs API
  slug: difficat-com-jobs-api
- baseURL: https://app.difficat.com/api/v1
  baseurl_source: declared
  description: The Screenshots API from DiffiCat — 1 operation(s) for screenshots.
  name: DiffiCat Screenshots API
  slug: difficat-com-screenshots-api
- baseURL: https://app.difficat.com/api/v1
  baseurl_source: declared
  description: The Snapshots API from DiffiCat — 5 operation(s) for snapshots.
  name: DiffiCat Snapshots API
  slug: difficat-com-snapshots-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://app.difficat.com/mcp
- group: agent
  href: https://artifacts.apis.io/difficat-com/agentic-access/difficat-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/difficat-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/difficat-com/rate-limits/difficat-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/difficat-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/difficat-com/plans/difficat-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/difficat-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/rules/difficat-com-rules.yml
  title: ''
  type: Spectral
  url: rules/difficat-com-rules.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/json-ld/difficat-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/difficat-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/difficat-com/vocabulary/difficat-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/difficat-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/difficat-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/data-model/difficat-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/difficat-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/difficat-com/cli/difficat-com-cli.yml
  title: ''
  type: CLI
  url: cli/difficat-com-cli.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/conventions/difficat-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/difficat-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/conventions/difficat-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/difficat-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/difficat-com/sandbox/difficat-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/difficat-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/difficat-com/security/difficat-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/difficat-com-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/difficat-com/lifecycle/difficat-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/difficat-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/lifecycle/difficat-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/difficat-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/errors/difficat-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/difficat-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/difficat-com/conformance/difficat-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/difficat-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/difficat-com/overlays/difficat-com-agent-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/difficat-com-agent-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/difficat-com/llms/difficat-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/difficat-com-llms.txt
- group: other
  href: https://artifacts.apis.io/difficat-com/a2a/difficat-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/difficat-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/difficat-com/mcp/difficat-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/difficat-com-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/difficat-com/well-known/difficat-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/difficat-com-security.txt
- group: auth
  href: https://artifacts.apis.io/difficat-com/well-known/difficat-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/difficat-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/difficat-com/well-known/difficat-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/difficat-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/difficat-com/hosts/difficat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/difficat-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/difficat-com/integrations/difficat-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/difficat-com-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/difficat-com/packages/difficat-com-packages.yml
  title: ''
  type: SDKs
  url: packages/difficat-com-packages.yml
- group: build
  href: https://artifacts.apis.io/difficat-com/packages/difficat-com-packages.yml
  title: ''
  type: Packages
  url: packages/difficat-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/difficat-com/authentication/difficat-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/difficat-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/difficat-com/security/difficat-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/difficat-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/difficat-com/security/difficat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/difficat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://difficat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://difficat.com/agents
- group: agent
  title: ''
  type: LLMsTxt
  url: https://difficat.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/difficat
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/difficat/difficat
- group: start
  title: ''
  type: Login
  url: https://app.difficat.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.difficat.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://difficat.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://difficat.com/privacy
created: '2026-11-05'
description: 'DiffiCat is a browser-based website migration testing and visual regression tool. It compares a source site (Site A) against a target site (Site B) page by page across three checks: page existence (HTTP status, broken pages and redirects), content accuracy (text and SEO changes) and pixel-level visual regression at widths from 320 to 2560px, with ZIP exports of text/CSV reports and screenshots. A free trial runs in the browser at app.difficat.com with no install or card. DiffiCat also offers an Agent API for AI agents over REST or MCP, with a free allowance needing no key and paid use via prepaid keys, Pro accounts or USDC on Base (x402).'
image: https://difficat.com/assets/og-image.png
json_schemas:
- name: BalanceResponse
  property_count: 6
  slug: difficat-com-balance-response
- name: SnapshotCompareRequest
  property_count: 6
  slug: difficat-com-snapshot-compare-request
- name: SnapshotDetail
  property_count: 4
  slug: difficat-com-snapshot-detail
- name: SnapshotPage
  property_count: 5
  slug: difficat-com-snapshot-page
- name: StartJobRequest
  property_count: 18
  slug: difficat-com-start-job-request
- name: StoredCompareRequest
  property_count: 7
  slug: difficat-com-stored-compare-request
jsonld:
- class_count: 31
  name: Difficat Com Context
  property_count: 123
  slug: difficat-com-context
layout: provider
mcp_servers:
- description: ''
  name: DiffiCat MCP Server
  slug: mcp
modified: '2026-11-05'
name: DiffiCat
nav: Providers
network: true
overview: 'DiffiCat publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Compares API, Discover API, and 4 more. Tagged areas include Company, Website Migration, Visual Regression, Testing, and QA.


  The DiffiCat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DiffiCat''s developer surface includes CLI, sandbox, authentication, documentation, and 37 more developer resources.'
plans:
- name: Difficat Com Plans Pricing
  plan_count: 5
  slug: difficat-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Difficat Com Rate Limits
  slug: difficat-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: DiffiCat API Rules
  rule_count: 49
  severity_counts:
    error: 41
    hint: 0
    info: 2
    warn: 6
  slug: difficat-com-rules
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 62.3
    developer_ergonomics: 44.6
    discoverability: 71.7
    operational_transparency: 71.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Difficat Com Authentication
  slug: difficat-com-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Difficat Com Domain Security
  slug: difficat-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Difficat Com Vulnerability Disclosure
  slug: difficat-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: discover-and-screenshot
  slug: difficat-com-discover-and-screenshot
- name: migration-comparison
  slug: difficat-com-migration-comparison
- name: prepaid-balance-and-history
  slug: difficat-com-prepaid-balance-and-history
- name: difficat
  slug: difficat-com-provider-skill-difficat
- name: snapshot-baseline-compare
  slug: difficat-com-snapshot-baseline-compare
slug: difficat-com
tags:
- Company
- Website Migration
- Visual Regression
- Testing
- QA
- SEO
- MCP
- AI Agents
- x402
website: https://difficat.com/
---
