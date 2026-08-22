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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Web API for submitting files (PE, PDF, Office documents, Flash, Java applets, Android applications, archives) and URLs to the Lastline analysis cloud for high-resolution behavioral malware analysis, t
  name: Lastline Analyst API
  slug: analyst-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.lastline.com/
- group: start
  title: ''
  type: Portal
  url: https://user.lastline.com/portal
- group: build
  title: ''
  type: Packages
  url: packages/lastline-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lastline-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lastline-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lastline-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lastline-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/lastline-cli.yml
- group: docs
  title: ''
  type: Documentation
  url: https://analysis.lastline.com/analysis/api-docs/html/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://analysis.lastline.com/analysis/api-docs/html/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://analysis.lastline.com/analysis/api-docs/html/overview.html#getting-started
- group: operate
  title: ''
  type: Support
  url: https://my.vmware.com/group/vmware/get-help
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lastline-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lastline-llms.txt
created: '2026-07-17'
description: Lastline was a Santa Barbara, California cybersecurity company founded in 2011, building high-resolution malware analysis and network detection and response (NDR) technology based on full-system emulation sandboxing. Its developer-facing surface is the Lastline Analyst API (marketed in the company's earliest years as the Previct Analyst API), an asynchronous web API for submitting files and URLs to the Lastline analysis cloud and retrieving detailed behavioral analysis reports, indicators of compromise and analysis artifacts. Lastline was acquired by VMware in 2020 and the technology was folded into VMware NSX Network Detection and Response; VMware was subsequently acquired by Broadcom. The lastline.com marketing site is retired and no longer answers HTTP, but the customer portal at user.lastline.com is live and branded "NSX - Network Detection and Response" behind a Broadcom Inc. TLS certificate, and the full Analyst API reference plus its first-party Python client downloads
  remain served. This profile captures that surviving API surface from the live first-party documentation, together with probes recording what is no longer published.
image: https://user.lastline.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Lastline
nav: Providers
network: true
overview: 'Lastline publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Malware Analysis, Sandboxing, and Threat Intelligence.


  Lastline''s developer surface includes developer portal, changelog, CLI, documentation, API reference, getting-started guide, support, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 21.1
  delta: 0.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 20.5
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lastline/refs/heads/main/screenshots/lastline-2026-07-25T224746.png
security:
- kind: authentication
  name: Lastline Authentication
  slug: lastline-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Lastline Domain Security
  slug: lastline-domain-security
  summary_line: TLSv1.3
slug: lastline
tags:
- Company
- Cybersecurity
- Malware Analysis
- Sandboxing
- Threat Intelligence
- Network Detection and Response
- Security
- Acquired
website: http://www.lastline.com/
---
