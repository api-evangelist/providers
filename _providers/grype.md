---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Grype is an open source vulnerability scanner for container images and filesystems developed by Anchore. It scans container images, filesystems, and SBOMs for known vulnerabilities, supporting Docker,
  name: Grype
  slug: grype
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grype-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anchore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/anchore/grype/blob/main/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://oss.anchore.com/docs/guides/vulnerability/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anchore
- group: other
  title: ''
  type: Open Source
  url: https://anchore.com/opensource/
- group: company
  title: ''
  type: Blog
  url: https://anchore.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://anchore.com/pricing/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/anchore/grype-mcp
created: '2026-03-26'
description: Grype is an open source vulnerability scanner for container images and filesystems developed by Anchore. It works with Syft-generated SBOMs and supports major OS package ecosystems and language-specific packages including Go, Java, JavaScript, Python, Ruby, Rust, and .NET.
finops:
- name: Grype Finops
  service_category: API
  slug: grype-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grype.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Grype
nav: Providers
network: true
overview: 'Grype publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Container Images, Containers, Open Source, SBOM, and Security.


  Grype''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 5 more developer resources.'
plans:
- name: Grype Plans Pricing
  plan_count: 3
  slug: grype-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Grype Rate Limits
  slug: grype-rate-limits
score:
  band: emerging
  composite: 17.3
  delta: -1.7
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grype/refs/heads/main/screenshots/grype-2026-06-20T182422.png
security:
- kind: domain-security
  name: Grype Domain Security
  slug: grype-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: grype
tags:
- Container Images
- Containers
- Open Source
- SBOM
- Security
- Vulnerability Scanning
website: https://anchore.com/
---
