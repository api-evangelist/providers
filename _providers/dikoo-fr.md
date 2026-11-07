---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public, read-only, unauthenticated Model Context Protocol server (streamable HTTP, stateless, JSON responses, open CORS) that lets AI assistants search verified French lawyers by place, specialty, mod
  name: DIKOO MCP Server
  slug: dikoo-mcp-server
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/dikoo-fr/rate-limits/dikoo-fr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dikoo-fr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dikoo-fr/plans/dikoo-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dikoo-fr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dikoo-fr/conventions/dikoo-fr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dikoo-fr-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dikoo-fr/authentication/dikoo-fr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dikoo-fr-authentication.yml
- group: design
  href: https://artifacts.apis.io/dikoo-fr/lifecycle/dikoo-fr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dikoo-fr-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/dikoo-fr/llms/dikoo-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dikoo-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/dikoo-fr/mcp/dikoo-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dikoo-fr-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dikoo-fr/well-known/dikoo-fr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dikoo-fr-security.txt
- group: auth
  href: https://artifacts.apis.io/dikoo-fr/well-known/dikoo-fr-dikoo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dikoo-fr-dikoo-security.txt
- group: agent
  href: https://artifacts.apis.io/dikoo-fr/well-known/dikoo-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dikoo-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/dikoo-fr/hosts/dikoo-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dikoo-fr-hosts.yml
- group: build
  href: https://artifacts.apis.io/dikoo-fr/integrations/dikoo-fr-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dikoo-fr-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dikoo-fr/vendors/dikoo-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dikoo-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dikoo-fr/security/dikoo-fr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dikoo-fr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dikoo-fr/security/dikoo-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dikoo-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dikoo.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dikoo.fr/guides
- group: operate
  title: ''
  type: Support
  url: https://www.dikoo.fr/aide
- group: company
  title: ''
  type: Blog
  url: https://www.dikoo.fr/actualites
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dikoo.fr/cgu
- group: commercial
  title: ''
  type: TermsOfSale
  url: https://www.dikoo.fr/cgv
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dikoo.fr/confidentialite
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.dikoo.fr/mentions-legales
- group: company
  title: ''
  type: About
  url: https://www.dikoo.fr/a-propos
- group: auth
  title: ''
  type: Security
  url: https://www.dikoo.fr/securite
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dikoo.fr/ia
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.dikoo.fr/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dikoo-fr/
- group: other
  title: ''
  type: X
  url: https://x.com/Dikoo_fr
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@dikoo_fr
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/dikoo.fr/
created: '2026-11-05'
description: DIKOO (www.dikoo.fr) is a French legal platform that lets the public find a verified lawyer (avocat) by city or specialty, see their availability and book an appointment at the office or by video. For lawyers it offers a software suite (national CNB directory listing, AI tools such as DIKSII, THERESAII, DIXOO and JURIOO, CRM, messaging, invoicing) hosted in Europe. DIKOO also publishes a public, read-only, unauthenticated MCP server at https://www.dikoo.fr/mcp for AI assistants. The site is published by MILINA AI, S.L. (Sociedad Unipersonal), Málaga, Spain; DIKOO is a registered trademark.
image: https://www.dikoo.fr/og/dikoo-apercu-v2-fr-FR.png
layout: provider
mcp_servers:
- description: 'Serveur MCP public de DIKOO (France) : recherche d’avocats par ville, spécialité, langue et disponibilité, fiches publiques, créneaux des avocats inscrits et liens dikoo.fr pour demander ou réserver u'
  name: DIKOO MCP Server
  slug: dikoo
modified: '2026-11-05'
name: DIKOO
nav: Providers
network: true
overview: 'DIKOO is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Lawyers, Legal Directory, and Appointment Booking.


  DIKOO''s developer surface includes authentication, documentation, support, engineering blog, getting-started guide, YouTube channel, and 25 more developer resources.'
plans:
- name: Dikoo Fr Plans Pricing
  plan_count: 1
  slug: dikoo-fr-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Dikoo Fr Rate Limits
  slug: dikoo-fr-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 71.7
    operational_transparency: 42.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dikoo Fr Authentication
  slug: dikoo-fr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dikoo Fr Domain Security
  slug: dikoo-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dikoo Fr Vulnerability Disclosure
  slug: dikoo-fr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dikoo-fr
tags:
- Company
- Legal
- Lawyers
- Legal Directory
- Appointment Booking
- Legal Tech
- MCP
- Artificial Intelligence
- France
website: https://dikoo.fr/
---
