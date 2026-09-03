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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'REST API for the Stairwell threat-intelligence platform: manage assets and forwarders, query object metadata/detonation/sightings/variants, manage and scan YARA rules, upload and correlate threat repo'
  name: Stairwell API
  slug: stairwell-api
artifact_total: 6
asyncapis:
- description: ''
  name: Stairwell Events Webhooks
  slug: stairwell-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.stairwell.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.stairwell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stairwell.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stairwell.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stairwell.com/docs/api-quickstart
- group: company
  title: ''
  type: Blog
  url: https://stairwell.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://docs.stairwell.com/docs/who-to-contact
- group: start
  title: ''
  type: Login
  url: https://app.stairwell.com/login
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.stairwell.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stairwell.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stairwell.com/website-terms-and-conditions/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stairwell-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stairwell-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stairwell-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/stairwell-events-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stairwell-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stairwell-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stairwell-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stairwell-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stairwell-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stairwell-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stairwell-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Stairwell is a private-by-design threat intelligence and detection platform that gives security teams a continuously reanalyzed, isolated store of their own files as an alternative to crowdsourced public services like VirusTotal. Its products span AI triage and static/behavioral malware analysis, malware variant discovery, Run-to-Ground incident scoping, and an encrypted Private Vault with retroactive detection as threat intelligence evolves. Stairwell exposes a REST API at app.stairwell.com/v1 (bearer-token auth) covering assets and forwarders, objects and detonation, sightings and variants, YARA rule management and ad-hoc scanning, threat reports and IOC correlation, network intelligence (hostname/IP/ASN WHOIS, cloud-provider lookups), plus outbound event-notification webhooks and an official hosted MCP server for read-only agent access. Added to the API Evangelist network from Accel's portfolio and enriched from Stairwell's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stairwell.png
layout: provider
mcp_servers:
- description: ''
  name: Stairwell MCP Server
  slug: stairwell-mcp-server
modified: '2026-07-21'
name: Stairwell
nav: Providers
network: true
overview: 'Stairwell publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Threat Intelligence, Malware Analysis, and Cybersecurity.


  The Stairwell catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Stairwell''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 17 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 34.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stairwell/refs/heads/main/screenshots/stairwell-2026-08-17T082059.png
security:
- kind: authentication
  name: Stairwell Authentication
  slug: stairwell-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stairwell Domain Security
  slug: stairwell-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Stairwell Trust Center
  slug: stairwell-trust-center
  summary_line: trust center published
slug: stairwell
tags:
- Company
- Security
- Threat Intelligence
- Malware Analysis
- Cybersecurity
- Threat Detection
- YARA
- Incident Response
website: https://www.stairwell.com/
---
