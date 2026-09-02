---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tela-innovations-domain-security.yml
coverage:
  checked: '2026-08-29'
  detail: Tela Innovations' corporate host www.tela-inc.com still resolves to 129.121.136.207 but accepts no TCP connections on port 80 or 443, and the Internet Archive's last capture with content predates 2022, so the company has no reachable web presence, no docs host and no developer, api or app subdomain in DNS to run contract discovery against.
  evidence:
  - status: 0
    url: https://www.tela-inc.com/
  - status: 0
    url: https://www.tela-inc.com/openapi.json
  - status: 0
    url: https://www.tela-inc.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/tela-innovations
  - status: 404
    url: https://registry.npmjs.org/tela-inc
  - status: 403
    url: https://forgeglobal.com/tela-innovations_stock/
  reason: defunct
  state: none
created: '2026-08-29'
description: Tela Innovations, Inc. is a semiconductor design-technology and intellectual-property company founded in 2005 and headquartered in Los Gatos, California. It developed gridded, straight-line, one-dimensional layout structures and the pre-defined physical topologies built on them, sold as standard-cell libraries and embedded-SRAM peripheral circuits intended to let logic, memory, analog and I/O blocks scale to advanced process nodes with improvements in variability, performance, leakage and area — without forcing customers to change their existing design methodology, equipment set or process technology. Alongside the libraries it sold physical IC design services and layout- and power-optimization software; in 2009 it acquired Blaze DFM, adding patented design-for-manufacturing and power-optimization capability for digital logic in SoCs and ASICs. It was backed by Intel Capital, Cadence Design Systems, Qualcomm, KT Venture Group, Malloy & Company and Black Diamond Ventures, and
  a substantial share of its later activity was patent licensing, including a portfolio licence taken by Samsung in 2016. Tela never operated a developer program, public API, SDK, webhook surface or machine-readable specification — its products were delivered as licensed cell libraries, EDA software and design services under commercial agreement, not as a callable service. Its corporate host, www.tela-inc.com, still resolves in DNS but no longer runs a web service (ports 80 and 443 both refuse connections) and has no Internet Archive capture with content after January 2022, so it is deliberately not wired as a Website pointer. This profile is retained as a historical record; there is no API surface to enrich.
layout: provider
modified: '2026-08-29'
name: Tela Innovations
nav: Providers
network: true
overview: Tela Innovations is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Electronic Design Automation, Chip Design, and Intellectual Property.
random_paper: 16
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Tela Innovations Domain Security
  slug: tela-innovations-domain-security
  summary_line: HSTS
slug: tela-innovations
tags:
- Company
- Semiconductors
- Electronic Design Automation
- Chip Design
- Intellectual Property
- Standard Cell Libraries
- Design For Manufacturing
- Patent Licensing
- Defunct
---
