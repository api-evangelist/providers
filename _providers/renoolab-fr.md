---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: 'Official remote MCP server (streamable HTTP, JSON-RPC 2.0, MCP 2025-06-18, serverInfo renoolab-mcp 1.4.0) exposing four French-language tools over the marketplace: rechercher_artisans (one trade withi'
  name: RenooLab MCP Server
  slug: renoolab-mcp-server
- description: 'Read-only Agent2Agent surface: an A2A 1.0 JSON-RPC endpoint at https://a2a.renoolab.fr/a2a whose card (served at /.well-known/agent-card.json on both renoolab.fr and a2a.renoolab.fr, version 1.0.2) de'
  name: RenooLab A2A Agent
  slug: renoolab-a2a-agent
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://renoolab.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://renoolab.fr/mcp/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/llms/renoolab-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/renoolab-fr-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://renoolab.fr/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://renoolab.fr/blog/
- group: operate
  title: ''
  type: Support
  url: https://renoolab.fr/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://renoolab.fr/cgu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://renoolab.fr/privacy/
- group: commercial
  title: ''
  type: Legal
  url: https://renoolab.fr/mentions-legales/
- group: start
  title: ''
  type: Signup
  url: https://app.renoolab.fr/register
- group: start
  title: ''
  type: Login
  url: https://app.renoolab.fr/login
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mehdimicra/renoolab-mcp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mehdimicra/renoolab-agent-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/renoolab
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/renoolab/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/renoolab
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/mcp/renoolab-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/renoolab-fr-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/a2a/renoolab-fr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/renoolab-fr-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/well-known/renoolab-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/renoolab-fr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/well-known/renoolab-fr-ard.json
  title: ''
  type: AICatalog
  url: well-known/renoolab-fr-ard.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/authentication/renoolab-fr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/renoolab-fr-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/scopes/renoolab-fr-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/renoolab-fr-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/conventions/renoolab-fr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/renoolab-fr-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/conformance/renoolab-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/renoolab-fr-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/lifecycle/renoolab-fr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/renoolab-fr-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/changelog/renoolab-fr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/renoolab-fr-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/rate-limits/renoolab-fr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/renoolab-fr-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/plans/renoolab-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/renoolab-fr-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/packages/renoolab-fr-packages.yml
  title: ''
  type: Packages
  url: packages/renoolab-fr-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/components/renoolab-fr-components.yml
  title: ''
  type: Components
  url: components/renoolab-fr-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/data-model/renoolab-fr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/renoolab-fr-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/errors/renoolab-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/renoolab-fr-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/security/renoolab-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/renoolab-fr-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/security/renoolab-fr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/renoolab-fr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/mehdimicra/renoolab-mcp/blob/main/SECURITY.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/renoolab-fr/refs/heads/main/regulatory/renoolab-fr-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/renoolab-fr-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://renoolab.fr/privacy/
- group: other
  title: ''
  type: DataResidency
  url: https://renoolab.fr/privacy/
- group: other
  title: ''
  type: Subprocessors
  url: https://renoolab.fr/privacy/
- group: other
  title: ''
  type: NoticeAndAction
  url: https://renoolab.fr/cgu/
created: '2026-09-19'
description: 'RenooLab ("le réseau social de la rénovation") is a French marketplace, published by Marseille-based sole trader Mehdi Boukenouche, that connects homeowners with building tradespeople across 19 trades - free for both sides, no commission on jobs, no lead reselling; tradespeople can buy optional in-app Pro/Premium visibility. Its developer surface is agent-native rather than REST: an official remote MCP server at https://mcp.renoolab.fr/mcp (streamable HTTP, protocol 2025-06-18, four tools - two anonymous read-only searches by trade/city or multi-trade project, two OAuth 2.1-gated writes for moderated contact requests and inactive profile creation, with dynamic client registration and PKCE; on the MCP Registry as fr.renoolab/mcp v1.4.0 and in the ChatGPT app directory), a read-only A2A 1.0 agent at https://a2a.renoolab.fr/a2a with its card at /.well-known/agent-card.json, ten provider-published Agent Skills discoverable at /.well-known/agent-skills/index.json, an ARD / ai-catalog
  federation manifest, WebMCP tools registered in-page via document.modelContext, and an llms.txt. No OpenAPI, SDK or REST reference is published; the tools/list contract is the machine-readable core. Deployment is national with the PACA region first.'
image: https://renoolab.fr/logo-128.webp
layout: provider
mcp_servers:
- description: RenooLab operates an official remote MCP server at https://mcp.renoolab.fr/mcp (streamable HTTP, JSON-RPC 2.0, MCP protocol 2025-06-18) exposing four tools over its French building-tradespeople market
  name: RenooLab MCP Server
  slug: renoolab-mcp-server
modified: '2026-09-19'
name: RenooLab
nav: Providers
network: true
overview: 'RenooLab publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Home Services, Construction, Building Trades, Renovation, and Marketplace.


  RenooLab''s developer surface includes documentation, engineering blog, support, legal docs, signup flow, authentication, changelog, and 34 more developer resources.'
plans:
- name: Renoolab Fr Plans Pricing
  plan_count: 4
  slug: renoolab-fr-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Renoolab Fr Rate Limits
  slug: renoolab-fr-rate-limits
scopes:
- name: Renoolab Fr Scopes
  scope_count: 0
  slug: renoolab-fr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.9
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.0
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 38.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 55.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Renoolab Fr Authentication
  slug: renoolab-fr-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Renoolab Fr Domain Security
  slug: renoolab-fr-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Renoolab Fr Vulnerability Disclosure
  slug: renoolab-fr-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 10
skills:
- name: renoolab-chiffrer-piloter-rentabilite
  slug: renoolab-chiffrer-piloter-rentabilite
- name: renoolab-creer-profil-artisan
  slug: renoolab-creer-profil-artisan
- name: renoolab-developper-clientele-visibilite-btp
  slug: renoolab-developper-clientele-visibilite-btp
- name: renoolab-diagnostiquer-securiser-logement
  slug: renoolab-diagnostiquer-securiser-logement
- name: renoolab-imaginer-arbitrer-renovation
  slug: renoolab-imaginer-arbitrer-renovation
- name: renoolab-lancer-entreprise-artisanale
  slug: renoolab-lancer-entreprise-artisanale
- name: renoolab-organiser-chantier-equipe-btp
  slug: renoolab-organiser-chantier-equipe-btp
- name: renoolab-piloter-receptionner-travaux
  slug: renoolab-piloter-receptionner-travaux
- name: renoolab-planifier-budgeter-travaux
  slug: renoolab-planifier-budgeter-travaux
- name: renoolab-trouver-choisir-artisans
  slug: renoolab-trouver-choisir-artisans
slug: renoolab-fr
tags:
- Home Services
- Construction
- Building Trades
- Renovation
- Marketplace
- Local Services
- MCP
- A2A
- AI Agents
- Agent Skills
- France
website: https://renoolab.fr/
---
