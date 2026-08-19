---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wegtultrarich Agentic Access
  operation_count: 6
  slug: wegtultrarich-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: Hosted, no-auth Model Context Protocol server (Streamable HTTP) exposing the same five wealth computations as agent tools with published JSON Schema inputs. Answers protocol revisions 2025-03-26 throu
  name: We > Ultrarich MCP Server
  slug: wegtultrarich-mcp-server
- description: Compare any wealth expression for two wealths ('yours' and 'theirs') in a single call — get both results as well as the ratio between them.
  name: We > Ultrarich Comparison API
  slug: wegtultrarich-comparison-api
- description: Discover (list) the available endpoints.
  name: We > Ultrarich Discovery API
  slug: wegtultrarich-discovery-api
- description: Express a single wealth through one of four lenses (daily spending, physical size, purchasing power, or compound interest).
  name: We > Ultrarich Wealth Expression API
  slug: wegtultrarich-wealth-expression-api
arazzos:
- description: Discover the available wealth expressions, run a direction-aware them-vs-you comparison, then add a purchasing-power lens on the ultrarich side — the three calls behind a quotable inequality briefing.
  name: We > Ultrarich — wealth inequality briefing
  slug: wegtultrarich-wealth-inequality-briefing
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: We > Ultrarich Comparison API
  slug: open-wegtultrarich-comparison-api
- collection_type: open
  name: We > Ultrarich Discovery API
  slug: open-wegtultrarich-discovery-api
- collection_type: open
  name: We > Ultrarich Wealth Expression API
  slug: open-wegtultrarich-wealth-expression-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wegtultrarich-mcp.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://wegtultrarich.instatus.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://wegtultrarich.org/pricing.html
- group: other
  title: ''
  type: Overlay
  url: overlays/wegtultrarich-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://wegtultrarich.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.wegtultrarich.org/
- group: docs
  title: ''
  type: Documentation
  url: https://api.wegtultrarich.org/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://api.wegtultrarich.org/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://api.wegtultrarich.org/README.md#quick-start
- group: operate
  title: ''
  type: Support
  url: https://wegtultrarich.org/faq.html
- group: operate
  title: ''
  type: FAQ
  url: https://wegtultrarich.org/faq.html
- group: company
  title: ''
  type: About
  url: https://wegtultrarich.org/about.html
- group: operate
  title: ''
  type: Contact
  url: https://wegtultrarich.org/partners.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/wegtultrarich/we-ultrarich-extreme-wealth-api-mcp-server/collection/kcacxo9/start-here-four-ways-to-understand-extreme-wealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wegtultrarich.org/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wegtultrarich.org/privacy-policy.html
- group: commercial
  title: ''
  type: License
  url: https://wegtultrarich.org/LICENSE.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://wegtultrarich.org/CHANGELOG.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wegtultrarich-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wegtultrarich-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://wegtultrarich.org/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wegtultrarich-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://api.wegtultrarich.org/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wegtultrarich-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wegtultrarich-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wegtultrarich-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wegtultrarich-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/wegtultrarich-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wegtultrarich-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wegtultrarich-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wegtultrarich-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wegtultrarich-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wegtultrarich-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/wegtultrarich-packages.yml
- group: design
  title: ''
  type: Rules
  url: rules/wegtultrarich-spectral.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AgentPrompt
  url: skills/wegtultrarich-agent-prompt.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wegtultrarich-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wegtultrarich-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://wegtultrarich.org/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://wegtultrarich.org/llms-full.txt
- group: other
  title: ''
  type: APIsJSON
  url: https://api.wegtultrarich.org/apis.json
created: '2026-07-25'
description: 'A free, non-commercial tool and public API that visualize extreme wealth inequality by comparing any wealth to ultrarich/billionaire/trillionaire wealth through four lenses: Duration Of Daily Spend, Height Of Stacked Money, Number Of Items Paid For, and Growth Of Compound Interest. All comparisons are deterministic arithmetic returning ready-to-quote figures, sentences, and them-vs-you ratios; no user data is collected. The surface is agent-native: a no-auth OpenAPI 3.0.4 REST API, a hosted Streamable-HTTP MCP server exposing the same five computations as tools, llms.txt and llms-full.txt, a published agent prompt, an APIs.json 0.21 index, and the Spectral ruleset the spec is linted against. Published by Blonde Rocket Scientist LLC; results are licensed CC BY 4.0 with a required attribution string.'
examples:
- key_count: 2
  name: Wegtultrarich Comparison Durationofdailyspend Example
  slug: wegtultrarich-comparison-durationOfDailySpend-example
- key_count: 2
  name: Wegtultrarich Comparison Example
  slug: wegtultrarich-comparison-example
- key_count: 2
  name: Wegtultrarich Durationofdailyspend Example
  slug: wegtultrarich-durationOfDailySpend-example
- key_count: 2
  name: Wegtultrarich Error 400 Example
  slug: wegtultrarich-error-400-example
- key_count: 2
  name: Wegtultrarich Expressions Example
  slug: wegtultrarich-expressions-example
- key_count: 2
  name: Wegtultrarich Growthofcompoundinterest Example
  slug: wegtultrarich-growthOfCompoundInterest-example
- key_count: 2
  name: Wegtultrarich Heightofmoneystack Example
  slug: wegtultrarich-heightOfMoneyStack-example
- key_count: 2
  name: Wegtultrarich Numberofitems Example
  slug: wegtultrarich-numberOfItems-example
image: https://wegtultrarich.org/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: wegtultrarich-mcp.yml
  slug: wegtultrarich-mcpyml
modified: '2026-08-09'
name: We > Ultrarich
nav: Providers
network: true
overview: 'We > Ultrarich publishes 4 APIs on the [APIs.io](https://apis.io/) network, including MCP Server, Comparison API, Discovery API, and 1 more. Tagged areas include wealth inequality, economic inequality, finance, economics, and education.


  The We > Ultrarich catalog on APIs.io includes 1 Spectral governance ruleset.


  We > Ultrarich''s developer surface includes pricing, documentation, API reference, getting-started guide, support, FAQ, changelog, and 35 more developer resources.'
random_paper: 72
rate_limits:
- limit_count: 3
  name: Wegtultrarich Rate Limits
  slug: wegtultrarich-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: We > Ultrarich API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 2
  slug: wegtultrarich-spectral
score:
  band: strong
  composite: 61.6
  delta: 2.1
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 65.9
    contract_quality: 55.2
    developer_ergonomics: 61.3
    discoverability: 100.0
    governance: 65.9
    operational_transparency: 52.6
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wegtultrarich/refs/heads/main/screenshots/wegtultrarich-2026-08-17T082904.png
security:
- kind: authentication
  name: Wegtultrarich Authentication
  slug: wegtultrarich-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Wegtultrarich Domain Security
  slug: wegtultrarich-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wegtultrarich Vulnerability Disclosure
  slug: wegtultrarich-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: wegtultrarich
tags:
- wealth inequality
- economic inequality
- finance
- economics
- education
- journalism
- open data
- comparison
- mcp
- model context protocol
- agents
website: https://wegtultrarich.org/
---
