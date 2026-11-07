---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The DrDroid platform surface — the hosted Model Context Protocol (MCP) server and DroidAgent investigation API at aiops.drdroid.io, authenticated with a Bearer API key generated from the dashboard (Se
  name: DrDroid Platform (MCP + Agent)
  slug: drdroid-platform-mcp-agent
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/doctor-droid/plans/doctor-droid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doctor-droid-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/doctor-droid/security/doctor-droid-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/doctor-droid-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/doctor-droid/security/doctor-droid-domain-security.yml
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
  href: https://artifacts.apis.io/doctor-droid/mcp/doctor-droid-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doctor-droid-mcp.yml
- group: agent
  href: https://artifacts.apis.io/doctor-droid/llms/doctor-droid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doctor-droid-llms.txt
- group: auth
  href: https://artifacts.apis.io/doctor-droid/authentication/doctor-droid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doctor-droid-authentication.yml
- group: agent
  href: https://artifacts.apis.io/doctor-droid/well-known/doctor-droid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doctor-droid-well-known.yml
- group: design
  href: https://artifacts.apis.io/doctor-droid/conformance/doctor-droid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doctor-droid-conformance.yml
- group: build
  href: https://artifacts.apis.io/doctor-droid/packages/doctor-droid-packages.yml
  title: ''
  type: Packages
  url: packages/doctor-droid-packages.yml
- group: build
  href: https://artifacts.apis.io/doctor-droid/cli/doctor-droid-cli.yml
  title: ''
  type: CLI
  url: cli/doctor-droid-cli.yml
- group: operate
  href: https://artifacts.apis.io/doctor-droid/changelog/doctor-droid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/doctor-droid-changelog.yml
created: '2026-07-17'
description: Doctor Droid (DrDroid), built by Deep Sea Tech Inc., is an AI-powered SRE and on-call agent that builds a knowledge graph of your technology stack — cloud, code, and telemetry — to accelerate incident response and root-cause analysis. DroidAgent runs automated investigations from the dashboard, from Slack, or through a hosted Model Context Protocol (MCP) server in tools like Cursor and Claude Desktop, correlating alerts across observability sources (Datadog, Grafana, Prometheus, CloudWatch, Sentry, New Relic, SigNoz and dozens more) and suggesting or executing remediation. The platform ships open-source tooling including the PlayBooks runbook-automation engine and the droidctx infrastructure-context CLI, and is SOC 2 Type II and ISO 27001 certified.
finops:
- has_sources: true
  method: derived
  name: Doctor Droid Finops
  primary_unit: subscription
  service_category: ''
  slug: doctor-droid-finops
  template: false
image: https://drdroid.io/drdroid-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Doctor Droid MCP Server
  slug: drdroid-mcp-server
- description: Remote MCP server at aiops.drdroid.io over HTTP.
  name: Doctor Droid MCP Server
  slug: drdroid
modified: '2026-07-18'
name: Doctor Droid
nav: Providers
network: true
overview: 'Doctor Droid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AIOps, SRE, and Incident Response.


  Doctor Droid''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 21 more developer resources.'
plans:
- name: Doctor Droid Plans Pricing
  plan_count: 4
  slug: doctor-droid-plans-pricing
- name: Doctor Droid Price Estimates
  plan_count: 0
  slug: doctor-droid-price-estimates
random_paper: 2
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 45.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/doctor-droid/doctor-droid-2026-07-25T212214.png
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
- Incident Management
website: https://drdroid.io/
---
