---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 8.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: An OAuth-protected Model Context Protocol endpoint served from the vi.co host and advertised through RFC 9728 protected resource metadata. It is the WordPress MCP adapter running on the Vi Labs corpor
  name: Vi Labs MCP Server
  slug: vi-labs-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vi-labs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vi-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vi.co/
- group: company
  title: ''
  type: Blog
  url: https://vi.co/learn/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://vi.co/learn/blog/feed/
- group: operate
  title: ''
  type: Contact
  url: https://vi.co/contact-vi/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vi.co/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vi.co/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vi-technologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vi
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Vi_Labs_AI
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Vi_Labs_AI
- group: company
  title: ''
  type: Careers
  url: https://vi.co/careers/
- group: auth
  title: ''
  type: Compliance
  url: security/vi-labs-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vi-labs-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vi-labs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vi-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vi-labs-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vi-labs-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vi-labs-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vi-labs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vi-labs-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vi-labs-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/vi-labs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vi-labs-llms.txt
created: '2026-09-02'
description: 'Vi Labs (vi.co) is a New York-headquartered enterprise AI company for health, founded in 2011 and led by co-founder and CEO Omri Yoffe, with offices in Brooklyn, Los Angeles, Boston and Tel Aviv. Its platform is an AI orchestration layer for healthcare systems, payers, biopharma and wellness enterprises, built on the Vi Data Web — a privacy-safe network of de-identified patient and member profiles enriched with behavioral and consumer signals — and delivered through four applications: Vi Activate (patient acquisition and targeting), Vi Engage (predictive patient and provider engagement), Vi Operate (an agentic suite for operational workflows) and Vi Pulse (analytics and ROI reporting). The company says it serves more than 100 enterprise customers and supports over 190 million lives, and in May 2026 it completed a $145M transaction at a $1.64B valuation. Vi Labs publishes no developer program, documentation or machine-readable API contract; its only anonymously reachable machine
  surface is an OAuth-protected Model Context Protocol endpoint served from vi.co and advertised through RFC 8414 and RFC 9728 metadata.'
image: https://vi.co/wp-content/uploads/2023/12/vi-social-share-light.png
layout: provider
mcp_servers:
- description: Vi Labs serves a live, OAuth-protected Model Context Protocol endpoint from its own host at https://vi.co/wp-json/mcp/mcp-oauth-server. It was discovered through RFC 9728 protected resource metadata p
  name: Vi Labs MCP Server
  slug: vi-labs-mcp-server
modified: '2026-09-02'
name: Vi Labs
nav: Providers
network: true
overview: 'Vi Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Health, Healthcare, and Life Sciences.


  Vi Labs'' developer surface includes engineering blog, YouTube channel, authentication, and 22 more developer resources.'
plans:
- name: Vi Labs Plans Pricing
  plan_count: 0
  slug: vi-labs-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Vi Labs Rate Limits
  slug: vi-labs-rate-limits
scopes:
- name: Vi Labs Scopes
  scope_count: 0
  slug: vi-labs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 26.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Vi Labs Authentication
  slug: vi-labs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vi Labs Domain Security
  slug: vi-labs-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Vi Labs Trust Center
  slug: vi-labs-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, HIPAA, HITRUST
slug: vi-labs
tags:
- Company
- Artificial Intelligence
- Health
- Healthcare
- Life Sciences
- Pharmaceuticals
- Patient Engagement
- Enterprise AI
- AI Agents
- Model Context Protocol
- Data
website: https://vi.co/
---
