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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'openHAB Configuration Overview API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: openHAB Configuration Overview API
  slug: configuration-api
- description: 'openHAB Installation Overview API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: openHAB Installation Overview API
  slug: installation-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/openhab/rules/openhab-rules.yml
  title: ''
  type: Spectral
  url: rules/openhab-rules.yml
- group: design
  href: https://artifacts.apis.io/openhab/vocabulary/openhab-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openhab-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/openhab/conformance/openhab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openhab-conformance.yml
- group: agent
  href: https://artifacts.apis.io/openhab/llms/openhab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openhab-llms.txt
- group: agent
  href: https://artifacts.apis.io/openhab/mcp/openhab-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/openhab-mcp.yml
- group: other
  href: https://artifacts.apis.io/openhab/hosts/openhab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openhab-hosts.yml
- group: other
  href: https://artifacts.apis.io/openhab/vendors/openhab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openhab-vendors.yml
- group: build
  href: https://artifacts.apis.io/openhab/packages/openhab-packages.yml
  title: ''
  type: SDKs
  url: packages/openhab-packages.yml
- group: build
  href: https://artifacts.apis.io/openhab/packages/openhab-packages.yml
  title: ''
  type: Packages
  url: packages/openhab-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/openhab/openhab-google-assistant/releases/tag/v5.1.0
- group: auth
  href: https://artifacts.apis.io/openhab/security/openhab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openhab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openhab.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.openhab.org/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openhab.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.openhab.org/docs/tutorial/first_steps
- group: operate
  title: ''
  type: Support
  url: https://community.openhab.org
- group: company
  title: ''
  type: Blog
  url: https://www.openhab.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openhab
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openhab.org/privacy
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec is publicly available.
  evidence:
  - status: 200
    url: https://www.openhab.org/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: openHAB is an open-source, vendor‑agnostic home automation platform that enables users to integrate a wide range of smart devices and technologies into a unified system. It offers a flexible architecture, extensive documentation, and a vibrant community supporting installation, configuration, and automation across Linux, Windows, macOS, and embedded hardware.
image: https://www.openhab.org/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at demo.openhab.org.
  name: openHAB MCP Server
  slug: openhab-mcp-yml
modified: '2026-10-28'
name: openHAB
nav: Providers
network: true
overview: 'openHAB is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Configuration Overview API and Installation Overview API. Tagged areas include Home Automation, Open Source, IoT, Smart Home, and Vendor Agnostic.


  The openHAB catalog on APIs.io includes 1 Spectral governance ruleset.


  openHAB''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: openHAB API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: openhab-rules
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 45.2
    discoverability: 56.7
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Openhab Domain Security
  slug: openhab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openhab
tags:
- Home Automation
- Open Source
- IoT
- Smart Home
- Vendor Agnostic
website: https://openhab.org/
---
