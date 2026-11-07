---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Certscore Ai Agentic Access
  operation_count: 15
  slug: certscore-ai-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 1
apis:
- description: Public API for CertScore.ai services.
  name: CertScore AI API
  slug: certscore-ai-api
- baseURL: https://certscore.ai
  baseurl_source: declared
  description: The Auth API from certscore-ai — 2 operation(s) for auth.
  name: certscore-ai Auth API
  slug: certscore-ai-auth-api
- baseURL: https://certscore.ai
  baseurl_source: declared
  description: The Diagnostics API from certscore-ai — 1 operation(s) for diagnostics.
  name: certscore-ai Diagnostics API
  slug: certscore-ai-diagnostics-api
- baseURL: https://certscore.ai
  baseurl_source: declared
  description: The Domains API from certscore-ai — 2 operation(s) for domains.
  name: certscore-ai Domains API
  slug: certscore-ai-domains-api
- baseURL: https://certscore.ai
  baseurl_source: declared
  description: The Findings API from certscore-ai — 2 operation(s) for findings.
  name: certscore-ai Findings API
  slug: certscore-ai-findings-api
- baseURL: https://certscore.ai
  baseurl_source: declared
  description: The Pulse API from certscore-ai — 1 operation(s) for pulse.
  name: certscore-ai Pulse API
  slug: certscore-ai-pulse-api
- baseURL: https://certscore.ai
  baseurl_source: declared
  description: The Runtime Inventory API from certscore-ai — 4 operation(s) for runtime inventory.
  name: certscore-ai Runtime Inventory API
  slug: certscore-ai-runtime-inventory-api
- baseURL: https://certscore.ai
  baseurl_source: declared
  description: The Scans API from certscore-ai — 7 operation(s) for scans.
  name: certscore-ai Scans API
  slug: certscore-ai-scans-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/certscore-ai/agentic-access/certscore-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/certscore-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/certscore-ai/rate-limits/certscore-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/certscore-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/certscore-ai/rules/certscore-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/certscore-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/certscore-ai/json-ld/certscore-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/certscore-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/certscore-ai/vocabulary/certscore-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/certscore-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/certscore-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/certscore-ai/data-model/certscore-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/certscore-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/certscore-ai/authentication/certscore-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/certscore-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/certscore-ai/errors/certscore-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/certscore-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/certscore-ai/conformance/certscore-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/certscore-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/certscore-ai/llms/certscore-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/certscore-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/certscore-ai/mcp/certscore-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/certscore-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/certscore-ai/mcp/certscore-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/certscore-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/certscore-ai/well-known/certscore-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/certscore-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/certscore-ai/well-known/certscore-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/certscore-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/certscore-ai/hosts/certscore-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certscore-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/certscore-ai/vendors/certscore-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/certscore-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/certscore-ai/packages/certscore-ai-packages.yml
  title: ''
  type: Packages
  url: packages/certscore-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/certscore-ai/security/certscore-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/certscore-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/certscore-ai/security/certscore-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certscore-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://certscore.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://certscore.ai/developers/reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://certscore.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://certscore.ai/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://certscore.ai/developers/quickstart
- group: start
  title: ''
  type: Login
  url: https://certscore.ai/login
- group: commercial
  title: ''
  type: Pricing
  url: https://certscore.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://certscore.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://certscore.ai/privacy
- group: auth
  title: ''
  type: Security
  url: https://certscore.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://certscore.ai/trust
- group: operate
  title: ''
  type: ChangeLog
  url: https://certscore.ai/releases
- group: company
  title: ''
  type: Newsroom
  url: https://certscore.ai/press
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@certscore/sdk
created: '2026-10-29'
description: CertScore.ai provides automated privacy and security scanning for public websites, detecting cookies, trackers, consent mechanisms, and privacy policy signals. Users can run free scans, review detailed evidence, and integrate findings into compliance workflows, helping organizations understand data collection practices and improve transparency for visitors.
image: https://certscore.ai/images/social/website-privacy-scanner.png
jsonld:
- class_count: 36
  name: Certscore Ai Context
  property_count: 263
  slug: certscore-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.certscore.ai requiring OAuth.
  name: certscore-ai MCP Server
  slug: certscore-ai-mcp-yml
modified: '2026-10-29'
name: certscore-ai
nav: Providers
network: true
overview: 'certscore-ai publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Diagnostics API, Domains API, and 5 more. Tagged areas include Company, Privacy, Security, Scanning, and Compliance.


  The certscore-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  certscore-ai''s developer surface includes authentication, API reference, documentation, getting-started guide, pricing, changelog, and 28 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 2
  name: Certscore Ai Rate Limits
  slug: certscore-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: certscore-ai API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: certscore-ai-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.8
    catalog_earned_first_party: 8.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 57.0
    developer_ergonomics: 44.5
    discoverability: 75.8
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/certscore-ai/certscore-ai-2026-11-03T123732.png
security:
- kind: authentication
  name: Certscore Ai Authentication
  slug: certscore-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Certscore Ai Domain Security
  slug: certscore-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Certscore Ai Vulnerability Disclosure
  slug: certscore-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: certscore-ai-scan-site
  slug: certscore-ai-scan-site
slug: certscore-ai
tags:
- Company
- Privacy
- Security
- Scanning
- Compliance
website: https://certscore.ai/
---
