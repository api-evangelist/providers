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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/per-vices-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/per-vices-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/per-vices-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/per-vices-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.pervices.com
- group: company
  title: ''
  type: Blog
  url: https://www.pervices.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.pervices.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pervices
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pervices/examples
- group: docs
  title: ''
  type: Documentation
  url: https://support.pervices.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.pervices.com/how-to/pvht-1-physicalsetup/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.pervices.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pervices.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pervices.com/terms-conditions/
- group: commercial
  title: ''
  type: Plans
  url: plans/per-vices-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/per-vices-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/per-vices-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/per-vices-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/per-vices-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/per-vices-lifecycle.yml
coverage:
  checked: '2026-08-14'
  detail: Per Vices manufactures software defined radio hardware — the product is a radio, and its control plane is device-local (an on-device web UI and socket.io channel on the SDR management port, default 192.168.10.2, plus the UHD state tree), so there is no internet-facing API to publish; every /.well-known/, /openapi.json, /swagger.json and /llms.txt path returned a genuine 404 on both www.pervices.com and support.pervices.com.
  evidence:
  - status: 404
    url: https://www.pervices.com/openapi.json
  - status: 404
    url: https://www.pervices.com/.well-known/agent-card.json
  - status: 404
    url: https://support.pervices.com/openapi.json
  - status: 200
    url: https://support.pervices.com/how-to/pvht-15-get-set-paths-uhd/
  reason: not-a-software-company
  state: none
created: '2026-07-17'
description: 'Per Vices Corporation is a Toronto-based company that designs and manufactures high-performance software defined radio (SDR) platforms, where signal tuning is handled in hardware while the remaining radio functionality runs in software so a single application-agnostic platform can serve many markets. Its product line includes Cyan (up to 16 independent radio chains, near-DC to 18 GHz), Crimson TNG (4 Rx / 4 Tx, near-DC to 6 GHz), Chestnut (near-DC to 9 GHz on an Intel Stratix 10 FPGA), and Calamine (receive-only, near-DC to 40 GHz). Per Vices ships open-source host software and firmware built on the UHD (USRP Hardware Driver) framework rather than a public web API; developers program the radios through the UHD C++ driver, GNU Radio integration, and example applications published on its GitHub org, with full integration support provided directly to customers. Control of the radio is device-local rather than internet-facing: an on-device web UI and socket.io channel on the SDR
  management port, plus the UHD state tree read and written with the uhd_manual_get / uhd_manual_set utilities. Unusually for its market, Per Vices publishes list prices for every platform configuration on a public pricing page. It publishes no public REST/OpenAPI web API surface, no MCP server and no A2A agent card; every /.well-known/ path returned 404 on both hosts on 2026-08-14.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/per-vices.png
layout: provider
modified: '2026-08-14'
name: Per Vices
nav: Providers
network: true
overview: 'Per Vices is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Defined Radio, SDR, Radio Frequency, and Wireless.


  Per Vices'' developer surface includes engineering blog, support, documentation, getting-started guide, pricing, changelog, CLI, and 13 more developer resources.'
plans:
- name: Per Vices Plans Pricing
  plan_count: 13
  slug: per-vices-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Per Vices Rate Limits
  slug: per-vices-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 24.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/per-vices/refs/heads/main/screenshots/per-vices-2026-09-02T151029.png
security:
- kind: domain-security
  name: Per Vices Domain Security
  slug: per-vices-domain-security
  summary_line: TLSv1.3 · DMARC
slug: per-vices
tags:
- Company
- Software Defined Radio
- SDR
- Radio Frequency
- Wireless
- Hardware
- FPGA
- Telecommunications
- Embedded Systems
website: https://www.pervices.com
---
