---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 7
asyncapis:
- description: ''
  name: Rox Webhooks
  slug: rox-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.rox.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rox.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rox.com/development/product/product-overview
- group: company
  title: ''
  type: Blog
  url: https://docs.rox.com/development/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rox.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://run.rox.com/api/auth/signup
- group: start
  title: ''
  type: Login
  url: https://run.rox.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rox.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rox.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://docs.rox.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rox-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rox.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.rox.com/development/about-rox/release-notes
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.rox.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.rox.com/
- group: auth
  title: ''
  type: Security
  url: https://www.rox.com/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.rox.com/vulnerability-disclosure-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rox-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rox-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rox-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rox-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rox-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rox.com/development/product/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/rox-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rox-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rox-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/rox-packages.yml
- group: other
  title: ''
  type: Downloads
  url: https://www.rox.com/downloads
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/Rox-Data-Corp
- group: company
  title: ''
  type: Twitter
  url: https://x.com/rox_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rox-ai/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@rox-agent/videos
created: '2026-07-17'
description: Rox is an AI-native revenue operating system for enterprise sales teams, built around an Agent Swarm layer that turns unified revenue context into autonomous go-to-market action. The platform automates pipeline generation, account research, prospecting and outreach, meeting briefings, deal management and forecasting, running these revenue workflows "on autopilot" across a company's book of business. Rox unifies structured and unstructured revenue data through a warehouse-native data fabric and connector hub, integrating with Salesforce, HubSpot, Gmail, Microsoft Outlook and Graph, Slack, Zoom, Snowflake, Databricks and BigQuery, then applies workflow- specific agents (research, outreach, deal, meet, monitor) governed by a unified permissions engine. Founded in San Francisco by Ishan Mukherjee and backed by Sequoia, GV, General Catalyst and 40+ angels, Rox surfaced in the API Evangelist network as a portfolio company and is profiled here as a product/company profile — it publishes
  extensive product and engineering documentation, a security trust center and a weekly changelog, but no public REST API, OpenAPI, GraphQL schema or MCP server at the time of enrichment. The one externally callable HTTP surface Rox documents is an inbound Agent Workflow webhook endpoint that an outside system POSTs JSON to in order to trigger a workflow; its extensibility program, App Studio, is a sales-gated private beta.
image: https://framerusercontent.com/images/AYj16lWuLsXAaHXzCmZgJyUrIs.png
layout: provider
modified: '2026-08-13'
name: Rox
nav: Providers
network: true
overview: 'Rox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Sales, and Revenue Operations.


  The Rox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rox''s developer surface includes documentation, engineering blog, pricing, signup flow, support, changelog, getting-started guide, and 26 more developer resources.'
plans:
- name: Rox Plans Pricing
  plan_count: 3
  slug: rox-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rox Rate Limits
  slug: rox-rate-limits
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 38.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 44.2
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rox/refs/heads/main/screenshots/rox-2026-08-17T081645.png
security:
- kind: authentication
  name: Rox Authentication
  slug: rox-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rox Domain Security
  slug: rox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rox Vulnerability Disclosure
  slug: rox-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Rox Trust Center
  slug: rox-trust-center
  summary_line: SOC 2 Type II, CASA Tier 2
slug: rox
tags:
- Company
- Artificial Intelligence
- AI Agents
- Sales
- Revenue Operations
- Go-To-Market
- CRM
- Sales Intelligence
- Enterprise
- Revenue Intelligence
website: https://www.rox.com
---
