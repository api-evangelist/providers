---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.macromedia.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.adobe.com/ — a different registrable domain (macromedia.com -> adobe.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/macromedia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://helpx.adobe.com/security.html/security/policy.ug.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macromedia-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/macromedia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/macromedia-security.txt
- group: company
  title: ''
  type: Website
  url: http://www.macromedia.com
created: '2026-07-17'
description: Macromedia was a developer-tools and interactive-media software company (Flash, Dreamweaver, ColdFusion, Shockwave, Director, Fireworks) surfaced as a portfolio company of accel and kleiner-perkins. Adobe acquired Macromedia in 2005; www.macromedia.com now 301-redirects to www.adobe.com and the domain serves Adobe's canonical security.txt / PSIRT disclosure surface. This profile is a legacy company lead in the API Evangelist network with no independent live API surface of its own.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/macromedia.png
layout: provider
modified: '2026-07-20'
name: Macromedia
nav: Providers
network: true
overview: Macromedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Software, Adobe, and Interactive Media.
random_paper: 13
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/macromedia/refs/heads/main/screenshots/macromedia-2026-07-25T225827.png
security:
- kind: domain-security
  name: Macromedia Domain Security
  slug: macromedia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Macromedia Vulnerability Disclosure
  slug: macromedia-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: macromedia
tags:
- Company
- Developer Tools
- Software
- Adobe
- Interactive Media
- Web Development
- Legacy
website: http://www.macromedia.com
---
