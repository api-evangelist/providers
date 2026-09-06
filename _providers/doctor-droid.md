---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-05'
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
  name: Doctor Droid MCP Server
  slug: doctor-droid-mcp-server
- description: ''
  name: Doctor Droid MCP Server
  slug: doctor-droid-mcp-server-2
modified: '2026-07-18'
name: Doctor Droid
nav: Providers
network: true
overview: 'Doctor Droid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AIOps, SRE, and Incident Response.


  Doctor Droid''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 20 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 35.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doctor-droid/refs/heads/main/screenshots/doctor-droid-2026-07-25T212214.png
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
- Artificial Intelligence
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
