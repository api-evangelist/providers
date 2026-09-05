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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oligo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oligo.security
- group: docs
  title: ''
  type: Documentation
  url: https://support.oligo.security
- group: company
  title: ''
  type: Blog
  url: https://www.oligo.security/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oligo.security/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oligo.security/legal/privacy-policy
created: '2026-07-17'
description: Oligo Security is a runtime security platform built for the AI era, giving security teams real-time visibility and protection across applications, cloud infrastructure, and AI systems. Oligo combines Cloud Application Detection and Response (CADR), runtime software composition analysis (SCA) and SBOM generation, container scanning, and AI security posture management to detect and stop attacks at the application layer before they spread. By observing which vulnerable code actually executes at runtime, Oligo proves exploitability and reduces vulnerability noise by up to 90-99%, letting teams prioritize the small fraction of findings that are truly reachable. The platform covers apps, workloads, hosts, and cloud infrastructure, and adds runtime protection for AI agents and models. Oligo is a portfolio company of Lightspeed Venture Partners and counts organizations such as Databricks, Salesforce, ServiceNow, Instacart, and Cresta among its customers. Its customer platform and API
  documentation are gated behind authentication; no public REST API, OpenAPI specification, SDK, CLI, or MCP server is published on the open web at the time of this enrichment pass.
image: https://oligo.security/favicon.ico
layout: provider
modified: '2026-07-20'
name: Oligo
nav: Providers
network: true
overview: 'Oligo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Application Security, Runtime Security, and Cloud Security.


  Oligo''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oligo/refs/heads/main/screenshots/oligo-2026-08-07T190117.png
security:
- kind: domain-security
  name: Oligo Domain Security
  slug: oligo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oligo
tags:
- Company
- Security
- Application Security
- Runtime Security
- Cloud Security
- AI Security
- Vulnerability Management
- CADR
- SBOM
- Software Composition Analysis
website: https://oligo.security
---
