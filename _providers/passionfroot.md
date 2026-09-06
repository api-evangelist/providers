---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.passionfroot.me/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.passionfroot.me/en/
- group: operate
  title: ''
  type: Support
  url: https://help.passionfroot.me/en/
- group: company
  title: ''
  type: Blog
  url: https://www.passionfroot.me/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.passionfroot.me/creator-pricing
- group: start
  title: ''
  type: SignUp
  url: https://workspace.passionfroot.me/select-workspace
- group: start
  title: ''
  type: Login
  url: https://workspace.passionfroot.me/select-workspace
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.passionfroot.me/en/articles/11570199-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.passionfroot.me/en/articles/11569203-privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/passionfroot
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passionfroot-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.passionfroot.me/
- group: auth
  title: ''
  type: Compliance
  url: https://help.passionfroot.me/en/articles/11570259-gdpr-passionfroot
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/passionfroot-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/passionfroot-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/passionfroot-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/passionfroot-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/passionfroot-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/passionfroot-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/passionfroot-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: Passionfroot is an end-user SaaS marketplace with no platform API — api., docs. and developers.passionfroot.me have no DNS record at all, /developers and /api 404 on the marketing site, and the workspace app talks to its own origin over a Rocicorp Zero sync endpoint (/api/zero/push) rather than a documented public interface.
  evidence:
  - status: 404
    url: https://www.passionfroot.me/developers
  - status: 404
    url: https://www.passionfroot.me/api
  - status: 404
    url: https://workspace.passionfroot.me/openapi.json
  - status: 0
    url: https://api.passionfroot.me/openapi.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Passionfroot is a Berlin-based platform for creator-led go-to-market (GTM), pairing a self-service marketplace where business, productivity, and thought-leadership creators sell sponsorships, ad placements, and brand collaborations with an AI agent ("Zest") that helps brands discover creators, plan campaigns, run outreach, process payments (via its FrootWallet), and measure performance across Twitter/X, YouTube, Instagram, TikTok, LinkedIn, Beehiiv, and Substack. Creators manage storefronts, pricing, bookings, invoicing, and payouts in one place; the company monetizes by taking a commission on completed deals rather than charging a subscription. As of this enrichment pass Passionfroot exposes no public developer API, SDK, or developer documentation — it is an end-user SaaS product, not an API provider. Its only public developer surface is open-source tooling extracted from its own stack and published under the @passionfroot npm scope: an MIT-licensed PostgreSQL MCP server with
  Prisma-aware schema introspection (plus a companion Agent Skill) and a Prisma-to-Zero schema generator. Those run against the operator''s own database and do not reach Passionfroot platform data.'
image: https://res.cloudinary.com/passionfroot/image/upload/w_1200,h_630,c_fill/f_jpg/website/og-image
layout: provider
mcp_servers:
- description: ''
  name: PostgreSQL MCP server (first-party open source; NOT a Passionfroot platform surface)
  slug: postgresql-mcp-server-first-party-open-source-not-a-passionfroot-platform-surface
modified: '2026-08-13'
name: Passionfroot
nav: Providers
network: true
overview: 'Passionfroot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Creator Economy, Marketplace, and Sponsorships.


  Passionfroot''s developer surface includes support, engineering blog, pricing, signup flow, changelog, and 16 more developer resources.'
plans:
- name: Passionfroot Plans Pricing
  plan_count: 1
  slug: passionfroot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Passionfroot Rate Limits
  slug: passionfroot-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 30.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passionfroot/refs/heads/main/screenshots/passionfroot-2026-08-07T191536.png
security:
- kind: domain-security
  name: Passionfroot Domain Security
  slug: passionfroot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: passionfroot
tags:
- Company
- Software-as-a-Service
- Creator Economy
- Marketplace
- Sponsorships
- Brand Partnerships
- Payments
- AI Agent
- Go-To-Market
website: https://www.passionfroot.me/
---
