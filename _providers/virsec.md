---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The Virsec Security Platform Centralized Management Server (CMS) exposes a RESTful API for procuring information from CMS. From VSP 3.0.0 and above, the available APIs are listed by category in the CM
  name: Virsec Security Platform CMS API
  slug: virsec-cms-api
- description: The Centralized Probe Management (CPM) API simplifies upgrade and troubleshooting of VSP Probes deployed across application platforms. Served from the customer's CMS host under /rms, it covers probe i
  name: Virsec Centralized Probe Management (CPM) API
  slug: virsec-cpm-api
artifact_total: 5
asyncapis:
- description: ''
  name: Virsec Cms Webhooks
  slug: virsec-cms-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virsec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://virsec.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virsec.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.virsec.com/docs/available-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.virsec.com/docs/vsp-introduction
- group: operate
  title: ''
  type: Support
  url: https://docs.virsec.com/docs/download-and-support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virsec.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virsec
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Virsec
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virsec-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/virsec-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virsec-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virsec-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virsec-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virsec-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/virsec-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/virsec-cms-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virsec-conformance.yml
created: '2026-08-05'
description: 'Virsec Systems is a San Jose, California cybersecurity company that builds the Virsec Security Platform (VSP), a deny-by-default, allow-on-trust zero trust runtime defense for cloud and legacy server workloads. VSP combines host protection, memory exploit protection and web protection with a Centralized Management Server (CMS) and distributed Probes, stopping ransomware, remote code execution, living-off-the-land and zero-day attacks at runtime without patching. The platform is customer-deployed (on-prem VM, EC2/Azure/GCP, Kubernetes/Helm or SaaS CMS) and exposes a customer-facing REST surface: a CMS API reference served from the CMS console under Help > API Documentation, the Centralized Probe Management (CPM) API under /rms for probe install, upgrade, migration, log/stat/data collection and vsp-cli execution, and configurable outbound webhooks that push detected incidents into existing SIEM, ITSM and ticketing systems (QRadar, Splunk, Syslog, Zendesk).'
image: https://virsec.com/__l5e/assets-v1/f87abfa8-cf1d-4877-98d4-aecff7f5f2c3/virsec-logo.png
layout: provider
modified: '2026-08-05'
name: Virsec
nav: Providers
network: true
overview: 'Virsec publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Application Security, and Workload Protection.


  The Virsec catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Virsec''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, CLI, and 11 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 32.5
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virsec/refs/heads/main/screenshots/virsec-2026-09-02T170011.png
security:
- kind: authentication
  name: Virsec Authentication
  slug: virsec-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Virsec Domain Security
  slug: virsec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virsec
tags:
- Company
- Security
- Cybersecurity
- Application Security
- Workload Protection
- Runtime Application Self-Protection
- Zero Trust
- Endpoint Security
- Memory Protection
- Ransomware
- Vulnerability Management
- On-Premise
website: https://virsec.com
---
