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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 30.8
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The DrDroid platform surface — the hosted Model Context Protocol (MCP) server and DroidAgent investigation API at aiops.drdroid.io, authenticated with a Bearer API key generated from the dashboard (Se
  name: DrDroid Platform (MCP + Agent)
  slug: drdroid-platform-mcp-agent
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/doctor-droid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doctor-droid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drdroid.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.drdroid.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.drdroid.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.drdroid.io/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://drdroid.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://drdroid.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://aiops.drdroid.io/sign-in
- group: operate
  title: ''
  type: Support
  url: mailto:support@drdroid.io
- group: operate
  title: ''
  type: HelpCenter
  url: https://discord.gg/AQ3tusPtZn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DrDroidLab
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.drdroid.io/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.drdroid.io/policies/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://drdroid.io/security
- group: auth
  title: ''
  type: Compliance
  url: https://security.drdroid.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.drdroid.io/changelog
- group: design
  title: ''
  type: Webhooks
  url: https://docs.drdroid.io/monitor/webhook-alerts
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@DrDroidDev
- group: agent
  title: ''
  type: MCPServer
  url: mcp/doctor-droid-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doctor-droid-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/doctor-droid-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doctor-droid-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doctor-droid-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/doctor-droid-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/doctor-droid-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/doctor-droid-changelog.yml
created: '2026-07-17'
description: Doctor Droid (DrDroid), built by Deep Sea Tech Inc., is an AI-powered SRE and on-call agent that builds a knowledge graph of your technology stack — cloud, code, and telemetry — to accelerate incident response and root-cause analysis. DroidAgent runs automated investigations from the dashboard, from Slack, or through a hosted Model Context Protocol (MCP) server in tools like Cursor and Claude Desktop, correlating alerts across observability sources (Datadog, Grafana, Prometheus, CloudWatch, Sentry, New Relic, SigNoz and dozens more) and suggesting or executing remediation. The platform ships open-source tooling including the PlayBooks runbook-automation engine and the droidctx infrastructure-context CLI, and is SOC 2 Type II and ISO 27001 certified.
image: https://drdroid.io/drdroid-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: drdroid-mcp-server
  slug: drdroid-mcp-server
- description: ''
  name: doctor-droid-mcp.yml
  slug: doctor-droid-mcpyml
modified: '2026-07-18'
name: Doctor Droid
nav: Providers
network: true
overview: 'Doctor Droid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, AIOps, SRE, and Incident Response.


  Doctor Droid''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 20 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 38.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Doctor Droid Authentication
  slug: doctor-droid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doctor Droid Domain Security
  slug: doctor-droid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Doctor Droid Trust Center
  slug: doctor-droid-trust-center
  summary_line: SOC 2, ISO 27001
slug: doctor-droid
tags:
- Company
- Ai
- AIOps
- SRE
- Incident Response
- On-Call
- Observability
- DevOps
- Monitoring
- MCP
website: https://drdroid.io/
---
