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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.seekout.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seekout-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seekout-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/seekout-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seekout-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seekout-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/seekout-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/seekout
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.seekout.com/
- group: company
  title: ''
  type: Blog
  url: https://www.seekout.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.seekout.com/release-notes
- group: operate
  title: ''
  type: Support
  url: https://support.seekout.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.seekout.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.seekout.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seekout.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seekout.com/privacy
created: '2026-07-17'
description: SeekOut is an agentic AI recruiting platform, founded in 2017 and headquartered in Bellevue, Washington, that helps talent acquisition teams source, screen, and engage candidates at scale across a database of 1B+ candidate profiles. Its products include SeekOut Recruit (AI sourcing, screening, and personalized outreach), SeekOut Spot (an AI recruiting service pairing agentic AI with expert recruiters), SeekOut Sam (AI inbound applicant evaluation), and SeekOut MCP, a hosted Model Context Protocol server that brings 14 built-in recruiting workflows into Claude, ChatGPT, Gemini, and Microsoft 365 Copilot. SeekOut is used by 750+ customers including Microsoft, DocuSign, Sony, and Thomson Reuters.
image: https://www.seekout.com/hubfs/seekout-logo.svg
layout: provider
mcp_servers:
- description: Hosted MCP server that exposes SeekOut's recruiting platform (1B+ candidate profiles across 6 data sources) to MCP-compatible AI assistants. 14 built-in recruiting workflows.
  name: SeekOut MCP
  slug: seekout-mcp
modified: '2026-07-21'
name: SeekOut
nav: Providers
network: true
overview: 'SeekOut is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruiting, Talent Acquisition, HR Tech, and Sourcing.


  SeekOut''s developer surface includes engineering blog, changelog, support, pricing, signup flow, and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.5
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seekout/refs/heads/main/screenshots/seekout-2026-09-02T154749.png
security:
- kind: domain-security
  name: Seekout Domain Security
  slug: seekout-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Seekout Vulnerability Disclosure
  slug: seekout-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: seekout
tags:
- Company
- Recruiting
- Talent Acquisition
- HR Tech
- Sourcing
- Artificial Intelligence
- Candidate Search
- MCP
- Recruiting Automation
website: https://www.seekout.com
---
