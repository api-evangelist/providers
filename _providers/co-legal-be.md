---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Agent2Agent 1.0 surface of Co-Legal's public legal/fiscal assistant. The agent card at https://agent.co-legal.be/.well-known/agent-card.json (version 1.27.9, JWS ES256-signed, verified against /.well-
  name: Co-Legal Public Assistant (A2A Agent)
  slug: co-legal-public-assistant-a2a-agent
- description: Remote Model Context Protocol server at https://agent.co-legal.be/mcp (Streamable HTTP, POST only, negotiated protocol version 2025-06-18, serverInfo colegal-legal-lookup 1.27.9). initialize and tools
  name: Co-Legal Legal Lookup MCP Server
  slug: co-legal-legal-lookup-mcp-server
artifact_total: 13
common:
- group: auth
  href: https://artifacts.apis.io/co-legal-be/security/co-legal-be-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/co-legal-be-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://co-legal.be/security
- group: auth
  href: https://artifacts.apis.io/co-legal-be/security/co-legal-be-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/co-legal-be-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://co-legal.be/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agent.co-legal.be/
- group: docs
  title: ''
  type: Documentation
  url: https://co-legal.be/agent
- group: docs
  title: ''
  type: APIReference
  url: https://agent.co-legal.be/.well-known/agent-card.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agent.co-legal.be/
- group: operate
  title: ''
  type: FAQ
  url: https://co-legal.be/veelgestelde-vragen
- group: operate
  title: ''
  type: Support
  url: https://co-legal.be/contact
- group: company
  title: ''
  type: Blog
  url: https://co-legal.be/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://co-legal.be/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://agent.co-legal.be/.well-known/payment-options.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://co-legal.be/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agent.co-legal.be/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://co-legal.be/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://co-legal.be/platform-privacy
- group: auth
  href: https://artifacts.apis.io/co-legal-be/well-known/co-legal-be-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/co-legal-be-security.txt
- group: agent
  href: https://artifacts.apis.io/co-legal-be/well-known/co-legal-be-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/co-legal-be-well-known.yml
- group: other
  href: https://artifacts.apis.io/co-legal-be/a2a/co-legal-be-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/co-legal-be-a2a.yml
- group: agent
  href: https://artifacts.apis.io/co-legal-be/mcp/co-legal-be-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/co-legal-be-mcp.yml
- group: build
  href: https://artifacts.apis.io/co-legal-be/mcp/co-legal-be-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/co-legal-be-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/co-legal-be/llms/co-legal-be-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/co-legal-be-llms.txt
- group: auth
  href: https://artifacts.apis.io/co-legal-be/authentication/co-legal-be-authentication.yml
  title: ''
  type: Authentication
  url: authentication/co-legal-be-authentication.yml
- group: design
  href: https://artifacts.apis.io/co-legal-be/conventions/co-legal-be-conventions.yml
  title: ''
  type: Conventions
  url: conventions/co-legal-be-conventions.yml
- group: design
  href: https://artifacts.apis.io/co-legal-be/errors/co-legal-be-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/co-legal-be-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/co-legal-be/rate-limits/co-legal-be-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/co-legal-be-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/co-legal-be/plans/co-legal-be-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/co-legal-be-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/co-legal-be/conformance/co-legal-be-conformance.yml
  title: ''
  type: Conformance
  url: conformance/co-legal-be-conformance.yml
- group: design
  href: https://artifacts.apis.io/co-legal-be/lifecycle/co-legal-be-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/co-legal-be-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/co-legal-be/packages/co-legal-be-packages.yml
  title: ''
  type: Packages
  url: packages/co-legal-be-packages.yml
- group: agent
  href: https://artifacts.apis.io/co-legal-be/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: AccessibilityConformance
  url: https://co-legal.be/legal
- group: other
  title: ''
  type: Subprocessors
  url: https://co-legal.be/security
- group: operate
  title: ''
  type: IncidentNotification
  url: https://co-legal.be/security
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://co-legal.be/legal
- group: other
  title: ''
  type: DataResidency
  url: https://co-legal.be/security
- group: other
  title: ''
  type: AITransparency
  url: https://agent.co-legal.be/.well-known/agent-card.json
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://co-legal.be/legal
- group: other
  title: ''
  type: ExitAssistance
  url: https://co-legal.be/security
created: '2026-09-19'
description: 'Co-Legal B.V. is a Dutch company (KvK 42135345, Delft) building AI-native legal software and dossier support for Belgian and cross-border Belgium–Netherlands matters — wealth planning and succession, company law and transactions, tax and finance, real estate — sold to law firms, notaries, accountants and tax advisers by proposal, with the private platform behind Cloudflare Access and Microsoft Entra. Alongside it Co-Legal runs a public, free, anonymous, read-only agent at agent.co-legal.be for informational Belgian and Dutch legal and fiscal source questions: an A2A 1.0 agent card signed with JWS ES256 (verifiable against a published JWKS) declaring 17 skills — KBO/BCE company lookup, EU VIES VAT validation, Belgian and Dutch ECLI case-law resolvers, EUR-Lex/CELEX and Justel/wetten.overheid.nl statute resolvers, Flemish inheritance-tax brackets, ECB reference rates, IBAN validation, public legal-corpus search and read, a citation verifier, DOCX concept drafting and a natural-language
  answer skill — and a remote MCP server at https://agent.co-legal.be/mcp that answers an anonymous tools/list with 12 of those as read-only, idempotent tools. Everything runs on Google Cloud in the EU with the model (claude-opus-5 via Vertex AI) disclosed inside the card. No OpenAPI is published; the MCP tools/list and the card''s tool-schema extension are the machine-readable contract.'
finops:
- has_sources: true
  method: derived
  name: Co Legal Be Finops
  primary_unit: ''
  service_category: ''
  slug: co-legal-be-finops
  template: true
image: https://co-legal.be/assets/icon-512.png
layout: provider
mcp_servers:
- description: 'Co-Legal operates ONE remote MCP server at https://agent.co-legal.be/mcp — the same Cloud Run host that serves its A2A agent card and JSON-RPC endpoint. It is POST-only Streamable HTTP (a GET returns '
  name: Co-Legal MCP Server
  slug: co-legal-be-mcp-yml
- description: ''
  name: MCP discovery pointer
  slug: mcp-discovery-pointer
modified: '2026-09-19'
name: Co-Legal
nav: Providers
network: true
overview: 'Co-Legal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Research, Tax, Case Law, and Legislation.


  Co-Legal''s developer surface includes documentation, API reference, getting-started guide, FAQ, support, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Co Legal Be Plans Pricing
  plan_count: 1
  slug: co-legal-be-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Co Legal Be Rate Limits
  slug: co-legal-be-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.8
    discoverability: 75.0
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 42.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 53.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/co-legal-be/co-legal-be-2026-10-11T103104.png
security:
- kind: authentication
  name: Co Legal Be Authentication
  slug: co-legal-be-authentication
  summary_line: none/apiKey/http · 3 schemes
- kind: domain-security
  name: Co Legal Be Domain Security
  slug: co-legal-be-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Co Legal Be Vulnerability Disclosure
  slug: co-legal-be-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: co-legal-be-ask-legal-question
  slug: co-legal-be-ask-legal-question
- name: co-legal-be-resolve-legal-citation
  slug: co-legal-be-resolve-legal-citation
- name: co-legal-be-verify-belgian-company
  slug: co-legal-be-verify-belgian-company
slug: co-legal-be
tags:
- Legal
- Legal Research
- Tax
- Case Law
- Legislation
- Company Registry
- VAT Validation
- Belgium
- Netherlands
- European Union
- A2A
- MCP
- Agent-Native
- Artificial Intelligence
- Legal Tech
website: https://co-legal.be/
---
