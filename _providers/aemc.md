---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aemc Agentic Access
  operation_count: 9
  slug: aemc-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: The undocumented JSON API behind AEMC's Energy Rules application. It serves the consolidated, versioned text of the National Electricity Rules, National Gas Rules and National Energy Retail Rules — ev
  name: AEMC Energy Rules API
  slug: aemc-energy-rules-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.aemc.gov.au/
- group: company
  title: ''
  type: About
  url: https://www.aemc.gov.au/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.aemc.gov.au/contact-us
- group: operate
  title: ''
  type: Support
  url: https://www.aemc.gov.au/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.aemc.gov.au/regulation/energy-rules
- group: start
  title: ''
  type: DataPortal
  url: https://www.aemc.gov.au/news-centre/data-portal
- group: company
  title: ''
  type: Blog
  url: https://www.aemc.gov.au/news-centre/media-releases
- group: other
  title: ''
  type: RSS
  url: https://www.aemc.gov.au/rss.xml
- group: other
  title: ''
  type: Regulation
  url: https://www.aemc.gov.au/regulation/energy-rules/national-electricity-rules
- group: other
  title: ''
  type: RuleChanges
  url: https://www.aemc.gov.au/our-work/changing-energy-rules/rule-changes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aemc.gov.au/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aemc.gov.au/terms-use/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/aemc-energy-rules-openapi-derived.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aemc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aemc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aemc-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aemc-rate-limits.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aemc-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aemc-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aemc-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aemc-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aemc-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aemc-energy-rules-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aemc-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aemc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aemc-domain-security.yml
created: '2026-07-27'
description: The Australian Energy Market Commission (AEMC) is the independent statutory rule maker for Australia's energy markets, established in 2005 and based in Sydney. It makes and amends the National Electricity Rules, National Gas Rules and National Energy Retail Rules, conducts market reviews, and advises the Energy and Climate Change Ministerial Council. It sits upstream of every other body in the Australian energy value chain — it writes the obligations that AEMO operates, that the AER enforces, and that retailers and networks must meet — but it operates no market systems and holds no consumer data itself. AEMC publishes no developer portal, no documented API, no OpenAPI and no open data product, and the corporate Drupal site at www.aemc.gov.au returns 404 for /api, /openapi.json, /swagger.json, /api-docs, /jsonapi and /graphql. It does, however, run one real machine-readable surface that it does not advertise — the Energy Rules application at energy-rules.aemc.gov.au is backed
  by an undocumented, entirely anonymous JSON API at /api/v1 that serves the full versioned text of all three rule books — 304 versions of the National Electricity Rules, 115 of the National Gas Rules and 65 of the National Energy Retail Rules — with a table of contents, per-clause content, full-text search, a complete defined-terms glossary and links to every published PDF and DOCX. That API is captured here as a derived OpenAPI built from AEMC's own production JavaScript bundle plus live probes. The other finding that matters is regulatory rather than technical — on 18 December 2025 the AEMC made a final rule giving all consumers and their AEMO-accredited representatives a right to real-time data from smart meters, with AEMO required to publish the technical procedures by 30 November 2026 and the meter obligation commencing 30 November 2028 — a mandate designated but not live, and separate from the Consumer Data Right, which is administered by Treasury, the ACCC and the Data Standards
  Body, with retailers as primary and AEMO as secondary data holder. AEMC is not a CDR data holder.
examples:
- key_count: 1
  name: Aemc Energy Rules Getglossarymenu
  slug: aemc-energy-rules-getGlossaryMenu
- key_count: 3
  name: Aemc Energy Rules Getglossaryterm
  slug: aemc-energy-rules-getGlossaryTerm
- key_count: 2
  name: Aemc Energy Rules Getrulecontent
  slug: aemc-energy-rules-getRuleContent
- key_count: 3
  name: Aemc Energy Rules Getruletableofcontents
  slug: aemc-energy-rules-getRuleTableOfContents
- key_count: 1
  name: Aemc Energy Rules Listglossarytermsbyletter A
  slug: aemc-energy-rules-listGlossaryTermsByLetter-a
- key_count: 3
  name: Aemc Energy Rules Listruleversions Ner
  slug: aemc-energy-rules-listRuleVersions-ner
- key_count: 2
  name: Aemc Energy Rules Searchruleversion
  slug: aemc-energy-rules-searchRuleVersion
image: https://www.aemc.gov.au/sites/default/files/AEMC_RGB_Favicon_swirl_STRONG_512x512px.png
layout: provider
mcp_servers:
- description: ''
  name: aemc-mcp.yml
  slug: aemc-mcpyml
modified: '2026-07-27'
name: Australian Energy Market Commission
nav: Providers
network: true
overview: 'Australian Energy Market Commission publishes 1 API on the [APIs.io](https://apis.io/) network: AEMC Energy Rules API. Tagged areas include Energy, Australia, Energy Markets, Electricity, and Gas.


  Australian Energy Market Commission''s developer surface includes support, documentation, engineering blog, authentication, code examples, changelog, and 22 more developer resources.'
random_paper: 58
rate_limits:
- limit_count: 0
  name: Aemc Rate Limits
  slug: aemc-rate-limits
score:
  band: emerging
  composite: 26.2
  delta: -2.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 14.4
    developer_ergonomics: 29.9
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Aemc Authentication
  slug: aemc-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Aemc Domain Security
  slug: aemc-domain-security
  summary_line: TLSv1.2 · DMARC
slug: aemc
tags:
- Energy
- Australia
- Energy Markets
- Electricity
- Gas
- Utilities
- Regulation
- Smart Metering
- Consumer Data Right
- Government
- Legal
- Rules
website: https://www.aemc.gov.au/
---
