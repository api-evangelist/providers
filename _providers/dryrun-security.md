---
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://simple-api.dryrun.security
  baseurl_source: declared
  description: Programmatic access to DryRun Security findings, scans, configurations, and insights via the Simple API.
  name: DryRun Simple API
  slug: dryrun-simple-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/dryrun-security/conformance/dryrun-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dryrun-security-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dryrun-security/mcp/dryrun-security-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dryrun-security-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dryrun-security/well-known/dryrun-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dryrun-security-well-known.yml
- group: other
  href: https://artifacts.apis.io/dryrun-security/hosts/dryrun-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dryrun-security-hosts.yml
- group: other
  href: https://artifacts.apis.io/dryrun-security/vendors/dryrun-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dryrun-security-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dryrun-security/security/dryrun-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dryrun-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-10-24'
description: DryRun Security provides automated security testing tools that simulate attacks on applications and infrastructure to identify vulnerabilities before they can be exploited. Their platform offers continuous penetration testing, vulnerability scanning, and compliance reporting, enabling organizations to integrate security into DevOps pipelines and maintain a strong security posture. By leveraging real-world attack techniques, DryRun Security helps teams prioritize remediation efforts and reduce risk across cloud, on-premises, and hybrid environments.
layout: provider
mcp_servers:
- description: Remote MCP server at insights-mcp.dryrun.security requiring an API key.
  name: DryRun Security MCP Server
  slug: dryrun-security-mcp-yml
modified: '2026-10-24'
name: DryRun Security
nav: Providers
network: true
overview: 'DryRun Security is listed with 1 API on the [APIs.io](https://apis.io/) network: DryRun Simple API. Tagged areas include Security, DevOps, PenetrationTesting, VulnerabilityScanning, and Compliance.'
random_paper: 1
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 32.9
    developer_ergonomics: 0.0
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dryrun Security Domain Security
  slug: dryrun-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dryrun-security
tags:
- Security
- DevOps
- PenetrationTesting
- VulnerabilityScanning
- Compliance
website: https://www.nasdaqprivatemarket.com/
---
