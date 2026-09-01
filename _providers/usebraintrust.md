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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Public Braintrust network statistics.
  name: Braintrust (Talent Network) dashboard API
  slug: usebraintrust-dashboard-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Braintrust Network Stats dashboard API
  slug: open-usebraintrust-dashboard-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/usebraintrust-network-stats-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.usebraintrust.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usebraintrust.com/communitydocs/
- group: company
  title: ''
  type: Blog
  url: https://www.usebraintrust.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usebraintrust.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.usebraintrust.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.usebraintrust.com/auth/sign_up/
- group: start
  title: ''
  type: Login
  url: https://app.usebraintrust.com/auth/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usebraintrust.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usebraintrust.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/usebraintrust-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/usebraintrust-well-known.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/usebraintrust-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/usebraintrust-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usebraintrust.com/products/air/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/usebraintrust-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usebraintrust-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/usebraintrust-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Braintrust (usebraintrust.com) is an AI-powered talent network and hiring platform founded in 2018 in San Francisco. It runs three enterprise products: Braintrust AIR, conversational AI interview software with semantic resume scoring and a third-party-audited bias posture; the Talent Marketplace, a network of 2M+ vetted professionals across engineering, ML, data science, design, and finance with zero agency markup; and Braintrust Nexus, enterprise workflow automation. The network is governed in part by the BTRST token, and its public Network Stats dashboard is backed by an open, unauthenticated JSON API captured in this profile. Distinct from braintrust.dev, the AI evaluation platform.'
examples:
- key_count: 3
  name: Usebraintrust Dashboard Response
  slug: usebraintrust-dashboard-response
image: https://www.usebraintrust.com/braintrust-logo.png
layout: provider
mcp_servers:
- description: Braintrust (usebraintrust.com) publishes no official MCP server (no MCP registry entry, no @modelcontextprotocol package, no docs mention found). This is a CANDIDATE tool list derived from the observe
  name: Braintrust (Talent Network) MCP Server
  slug: braintrust-talent-network-mcp-server
modified: '2026-07-21'
name: Braintrust (Talent Network)
nav: Providers
network: true
overview: 'Braintrust (Talent Network) publishes 1 API on the [APIs.io](https://apis.io/) network: dashboard API. Tagged areas include Company, Talent Marketplace, AI Recruiting, Hiring, and Freelancing.


  Braintrust (Talent Network)''s developer surface includes documentation, engineering blog, pricing, support, signup flow, changelog, and 13 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 15.8
    developer_ergonomics: 18.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 30.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Usebraintrust Domain Security
  slug: usebraintrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Usebraintrust Trust Center
  slug: usebraintrust-trust-center
  summary_line: SOC 2 Type II
slug: usebraintrust
tags:
- Company
- Talent Marketplace
- AI Recruiting
- Hiring
- Freelancing
- Workforce Automation
- BTRST Token
- Web3
website: https://www.usebraintrust.com
---
