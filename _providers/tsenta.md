---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Tsenta's backend API (api.autojobs.me) powers the job-matching, resume tailoring, and application-submission agent, and is exposed to AI clients as a hosted MCP server authorized over OAuth 2.0 (autho
  name: Tsenta API
  slug: tsenta-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://tsenta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tsenta.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tsenta.com
- group: start
  title: ''
  type: GettingStarted
  url: https://tsenta.com/mcp
- group: company
  title: ''
  type: Blog
  url: https://tsenta.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tsenta.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://tsenta.com/start
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tsenta.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tsenta.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://tsenta.com/#faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tsenta
- group: operate
  title: ''
  type: ChangeLog
  url: https://tsenta.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tsenta-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tsenta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tsenta-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tsenta-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tsenta-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tsenta-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tsenta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://tsenta.com/bug-bounty
- group: design
  title: ''
  type: Conformance
  url: conformance/tsenta-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tsenta-domain-security.yml
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/tsenta/id6760728258
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.tsenta.tsenta
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tsenta/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.ycombinator.com/companies/tsenta
created: '2026-07-17'
description: Tsenta is a Y Combinator-backed (S26) AI job-application agent that watches 50,000+ company career pages, tailors a resume and cover letter per role from the actual job description, and submits applications across 19 applicant tracking systems (Workday, Greenhouse, Lever, Ashby, Rippling, iCIMS, BambooHR, Workable, JazzHR, Jobvite, BreezyHR, Oracle Cloud, SmartRecruiters, Paylocity, UltiPro, ADP, Dover, Gem, Zoho Recruit). Every change is shown to the user before it goes out ("Review Before Submit"), or it can run headless. Tsenta is available on web, native iOS and Android apps, desktop, iMessage, WhatsApp, a Chrome extension, and as a hosted Model Context Protocol (MCP) server / CLI at api.autojobs.me for Claude, Cursor, Codex and any tool-using AI agent, authorized over OAuth 2.0 with PKCE and dynamic client registration.
image: https://tsenta.com/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Tsenta MCP Server
  slug: tsenta-mcp-server
modified: '2026-07-21'
name: Tsenta
nav: Providers
network: true
overview: 'Tsenta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Job, Recruiting, Job Search, and AI Agents.


  Tsenta''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 19 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 32.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tsenta/refs/heads/main/screenshots/tsenta-2026-09-02T164443.png
security:
- kind: authentication
  name: Tsenta Authentication
  slug: tsenta-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tsenta Domain Security
  slug: tsenta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tsenta Vulnerability Disclosure
  slug: tsenta-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tsenta
tags:
- Company
- Job
- Recruiting
- Job Search
- AI Agents
- Automation
- Applicant Tracking
- Career
- MCP
- Y Combinator
website: https://tsenta.com
---
