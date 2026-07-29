---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Endor Labs Agentic Access
  operation_count: 16
  slug: endor-labs-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 7
apis:
- description: Exchange API key and secret for a bearer access token.
  name: Endor Labs Authentication API
  slug: endor-labs-authentication-api
- description: Detected problems requiring remediation.
  name: Endor Labs Findings API
  slug: endor-labs-findings-api
- description: Tenants and child namespaces a token may access.
  name: Endor Labs Namespaces API
  slug: endor-labs-namespaces-api
- description: PackageVersion and dependency resources.
  name: Endor Labs Packages API
  slug: endor-labs-packages-api
- description: Governance rules over resources.
  name: Endor Labs Policies API
  slug: endor-labs-policies-api
- description: Project resources - the root of scanned source code.
  name: Endor Labs Projects API
  slug: endor-labs-projects-api
- description: Scan execution results and metrics.
  name: Endor Labs Scan Results API
  slug: endor-labs-scan-results-api
artifact_total: 14
collections:
- collection_type: open
  name: Endor Labs REST API
  slug: open-endor-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/endor-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/endor-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/endor-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/endorlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/endor-labs
- group: company
  title: ''
  type: Website
  url: https://www.endorlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.endorlabs.com/rest-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/endor-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/endor-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/endor-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.endorlabs.com/learn/rss.xml
created: '2026-06-20'
description: Endor Labs is a software supply chain security and application security platform built around reachability-based Software Composition Analysis (SCA), SBOM/VEX, secrets and SAST scanning, CI/CD discovery, and AI security. Its public REST API at https://api.endorlabs.com/v1 is a uniform resource API over namespaces, exposing projects, packages, findings, policies, scan results, and more, driven by the endorctl CLI.
finops:
- name: Endor Labs Finops
  service_category: Security
  slug: endor-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/endor-labs.png
layout: provider
modified: '2026-06-20'
name: Endor Labs
nav: Providers
network: true
overview: 'Endor Labs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Findings API, Namespaces API, and 4 more. Tagged areas include Security, Software Supply Chain, SCA, Reachability, and AppSec.


  Endor Labs'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Endor Labs Plans Pricing
  plan_count: 2
  slug: endor-labs-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 2
  name: Endor Labs Rate Limits
  slug: endor-labs-rate-limits
score:
  band: thin
  composite: 34.7
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/endor-labs/refs/heads/main/screenshots/endor-labs-2026-06-20T180657.png
security:
- kind: authentication
  name: Endor Labs Authentication
  slug: endor-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Endor Labs Domain Security
  slug: endor-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: endor-labs
tags:
- Security
- Software Supply Chain
- SCA
- Reachability
- AppSec
- AI Security
website: https://www.endorlabs.com
---
