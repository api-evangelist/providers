---
access_model:
  confidence: medium
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://usetaizen.com/book
  - plans/taizen-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Taizen's remote Model Context Protocol server — the company's only machine-callable surface. Per the provider's own manifest it lets an agent connect once instead of wiring fifteen-plus individual MCP
  name: Taizen MCP Server
  slug: taizen-mcp-server
artifact_total: 31
common:
- group: operate
  href: https://artifacts.apis.io/taizen/rate-limits/taizen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/taizen-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://usetaizen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usetaizen.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usetaizen.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://usetaizen.com/book
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usetaizen.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usetaizen.com/privacy
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://usetaizen.com/dpa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taizen-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/taizenai
- group: auth
  href: https://artifacts.apis.io/taizen/security/taizen-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/taizen-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.usetaizen.com/
- group: auth
  href: https://artifacts.apis.io/taizen/security/taizen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taizen-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/taizen/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/taizen/llms/taizen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taizen-llms.txt
- group: design
  href: https://artifacts.apis.io/taizen/conformance/taizen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/taizen-conformance.yml
- group: build
  href: https://artifacts.apis.io/taizen/packages/taizen-packages.yml
  title: ''
  type: Packages
  url: packages/taizen-packages.yml
- group: commercial
  href: https://artifacts.apis.io/taizen/plans/taizen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/taizen-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/taizen/lifecycle/taizen-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/taizen-lifecycle.yml
created: '2026-07-17'
description: 'Taizen is a managed agentic AI platform for go-to-market teams that automates win/loss analysis, competitive intelligence and sales-asset production. Its agents continuously read recorded sales calls (Gong, Fireflies, tl;dv, Granola, Genesys Cloud), CRM deal data (Salesforce, HubSpot, Attio, Clari), survey and review signal (Typeform, SurveyMonkey, G2) and existing collateral (Google Drive, SharePoint) to detect recurring objections and competitor moves, then auto-generate battlecards, rep-training drills and AI-roleplay scenarios, and deliver them into Slack. Taizen also books and runs AI-led interviews with lost buyers. Its machine surface is not a REST API but an agent surface: a remote, OAuth-protected MCP server at eu.mcp.usetaizen.com positioned as one connection in place of fifteen-plus individual MCP connectors, and a first-party open-source Claude plugin of thirty GTM Agent Skills. Backed by Techstars, the company emphasizes built-in governance, no model-vendor lock-in,
  SOC 2 / ISO 27001 / GDPR posture with an EU data region, and open sources supporting retrieval tooling on GitHub.'
image: https://usetaizen.com/assets/taizen.svg
layout: provider
mcp_servers:
- description: Taizen's hosted MCP server. Per the provider's own manifest it exists to "connect once instead of 15+ individual MCP connectors" — it indexes the customer's Gong calls, CRM records and documents so an
  name: Taizen MCP Server
  slug: taizen-mcp-server
modified: '2026-08-14'
name: Taizen
nav: Providers
network: true
overview: 'Taizen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Win-Loss Analysis, Competitive Intelligence, Sales Enablement, and Revenue Intelligence.


  Taizen''s developer surface includes documentation, getting-started guide, signup flow, and 16 more developer resources.'
plans:
- name: Taizen Plans Pricing
  plan_count: 0
  slug: taizen-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Taizen Rate Limits
  slug: taizen-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 29.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/taizen/taizen-2026-09-02T162453.png
security:
- kind: authentication
  name: Taizen Authentication
  slug: taizen-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Taizen Domain Security
  slug: taizen-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Taizen Trust Center
  slug: taizen-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 30
skills:
- name: account-lifecycle
  slug: taizen-account-lifecycle
- name: account-research
  slug: taizen-account-research
- name: brand-voice
  slug: taizen-brand-voice
- name: buyer-profiles
  slug: taizen-buyer-profiles
- name: case-study-builder
  slug: taizen-case-study-builder
- name: community-signals
  slug: taizen-community-signals
- name: competitive-intelligence
  slug: taizen-competitive-intelligence
- name: content-reviewer
  slug: taizen-content-reviewer
- name: copywriting
  slug: taizen-copywriting
- name: customer-advocacy
  slug: taizen-customer-advocacy
- name: customer-research
  slug: taizen-customer-research
- name: discovery-prep
  slug: taizen-discovery-prep
- name: email-sequences
  slug: taizen-email-sequences
- name: executive-briefings
  slug: taizen-executive-briefings
- name: feedback-collector
  slug: taizen-feedback-collector
- name: go-to-market
  slug: taizen-go-to-market
- name: gtm-messaging
  slug: taizen-gtm-messaging
- name: industry-insights
  slug: taizen-industry-insights
- name: messaging-positioning
  slug: taizen-messaging-positioning
- name: newsletter-writer
  slug: taizen-newsletter-writer
- name: objections-prep
  slug: taizen-objections-prep
- name: outreach-templates
  slug: taizen-outreach-templates
- name: pricing-packaging
  slug: taizen-pricing-packaging
- name: product-context
  slug: taizen-product-context
slug: taizen
tags:
- Company
- Win-Loss Analysis
- Competitive Intelligence
- Sales Enablement
- Revenue Intelligence
- Go-To-Market
- AI Agents
- Battlecards
- Sales
- MCP
- Agent Skills
- Conversation Intelligence
- Product Marketing
website: https://usetaizen.com/
---
