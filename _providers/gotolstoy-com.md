---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Gotolstoy Com Agentic Access
  operation_count: 37
  slug: gotolstoy-com-agentic-access
  summary_line: 37 operations · 23 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.gotolstoy.com
  baseurl_source: declared
  description: AI tool invocations (LLM, image, audio)
  name: gotolstoy-com AI Tools API
  slug: gotolstoy-com-ai-tools-api
- baseURL: https://api.gotolstoy.com
  baseurl_source: declared
  description: 'Product catalog: search, media, Shopify collections'
  name: gotolstoy-com Products API
  slug: gotolstoy-com-products-api
- baseURL: https://api.gotolstoy.com
  baseurl_source: declared
  description: Stores connected to the authenticated workspace
  name: gotolstoy-com Stores API
  slug: gotolstoy-com-stores-api
- baseURL: https://api.gotolstoy.com
  baseurl_source: declared
  description: Studio-generated asset management
  name: gotolstoy-com Studio API
  slug: gotolstoy-com-studio-api
- baseURL: https://api.gotolstoy.com
  baseurl_source: declared
  description: VOD asset search and mutations
  name: gotolstoy-com Video API
  slug: gotolstoy-com-video-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/gotolstoy-com/agentic-access/gotolstoy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gotolstoy-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/gotolstoy-com/plans/gotolstoy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gotolstoy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gotolstoy-com/rules/gotolstoy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/gotolstoy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/gotolstoy-com/vocabulary/gotolstoy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gotolstoy-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gotolstoy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/gotolstoy-com/cli/gotolstoy-com-cli.yml
  title: ''
  type: CLI
  url: cli/gotolstoy-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/gotolstoy-com/authentication/gotolstoy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gotolstoy-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/gotolstoy-com/errors/gotolstoy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gotolstoy-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gotolstoy-com/conformance/gotolstoy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gotolstoy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gotolstoy-com/llms/gotolstoy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gotolstoy-com-llms.txt
- group: other
  href: https://artifacts.apis.io/gotolstoy-com/a2a/gotolstoy-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gotolstoy-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/gotolstoy-com/mcp/gotolstoy-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gotolstoy-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gotolstoy-com/mcp/gotolstoy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gotolstoy-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/gotolstoy-com/well-known/gotolstoy-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gotolstoy-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/gotolstoy-com/well-known/gotolstoy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gotolstoy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gotolstoy-com/hosts/gotolstoy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gotolstoy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gotolstoy-com/vendors/gotolstoy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gotolstoy-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/gotolstoy-com/packages/gotolstoy-com-packages.yml
  title: ''
  type: SDKs
  url: packages/gotolstoy-com-packages.yml
- group: build
  href: https://artifacts.apis.io/gotolstoy-com/packages/gotolstoy-com-packages.yml
  title: ''
  type: Packages
  url: packages/gotolstoy-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gotolstoy.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoTolstoy
- group: auth
  href: https://artifacts.apis.io/gotolstoy-com/security/gotolstoy-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gotolstoy-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gotolstoy-com/security/gotolstoy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gotolstoy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gotolstoy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gotolstoy.com/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gotolstoy.com/welcome
- group: operate
  title: ''
  type: Support
  url: https://help.gotolstoy.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.gotolstoy.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gotolstoy.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gotolstoy.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gotolstoy.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://help.gotolstoy.com/en/collections/19680720-getting-started
- group: start
  title: ''
  type: SignUp
  url: https://platform.gotolstoy.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.gotolstoy.com/login
created: '2026-10-29'
description: Tolstoy (operating at gotolstoy.com) provides an AI-native ecommerce platform that empowers brands to create AI Studios and Shop Bots, offers hands‑on support through Tolstoy Forward, and publishes original AI commerce research. The platform enables merchants to build AI‑driven shopping experiences, automate product photography, and scale their brand with AI‑generated content and personalized storefronts.
image: https://tolstoy-assets.gotolstoy.com/www/webflow/686b80fe5aeca3c0b7ff34b3/689b4f7054ff393e20a1e536_logo%20tolstoy.svg
layout: provider
mcp_servers:
- description: Remote MCP server at developers.gotolstoy.com.
  name: gotolstoy-com MCP Server
  slug: gotolstoy-com-mcp-yml
modified: '2026-10-29'
name: gotolstoy-com
nav: Providers
network: true
overview: 'gotolstoy-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Tools API, Products API, Stores API, and 2 more. Tagged areas include AI, Ecommerce, Platform, Automation, and Marketing.


  The gotolstoy-com catalog on APIs.io includes 1 Spectral governance ruleset.


  gotolstoy-com''s developer surface includes CLI, authentication, documentation, support, engineering blog, pricing, getting-started guide, and 27 more developer resources.'
plans:
- name: Gotolstoy Com Plans Pricing
  plan_count: 4
  slug: gotolstoy-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Gotolstoy Com Rate Limits
  slug: gotolstoy-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: gotolstoy-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: gotolstoy-com-rules
scopes:
- name: Gotolstoy Com Scopes
  scope_count: 0
  slug: gotolstoy-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 46.5
    developer_ergonomics: 70.7
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gotolstoy Com Authentication
  slug: gotolstoy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gotolstoy Com Domain Security
  slug: gotolstoy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gotolstoy Com Vulnerability Disclosure
  slug: gotolstoy-com-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 2
skills:
- name: getting-started
  slug: gotolstoy-com-getting-started
- name: sdks-tools
  slug: gotolstoy-com-sdks-tools
slug: gotolstoy-com
tags:
- AI
- Ecommerce
- Platform
- Automation
- Marketing
website: https://gotolstoy.com/
---
