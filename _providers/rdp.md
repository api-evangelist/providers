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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 7
common:
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-schema/rdp-connection.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-schema/rdp-session-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-structure/rdp-connection-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/json-ld/rdp-context.jsonld
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/examples/rdp-connection-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/examples/rdp-session-example.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/vocabulary/rdp-vocabulary.yml
- group: docs
  title: ''
  type: Specification
  url: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/
- group: docs
  title: ''
  type: Specification
  url: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdsod/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis
created: '2025-01-01'
description: The Remote Desktop Protocol (RDP) is a proprietary network protocol developed by Microsoft that provides a graphical interface to connect to another computer over a network. RDP transmits keyboard, mouse, display, and audio data between client and host, enabling remote administration, virtual desktops, and remote work scenarios. The protocol typically operates on TCP and UDP port 3389 and is defined in the MS-RDPBCGR open specification. It is implemented by Microsoft's Remote Desktop Services as well as third-party clients across Windows, macOS, Linux, iOS, and Android. The RDP acronym is also shared with the Refinitiv Data Platform (LSEG), a cloud REST API platform for financial market data, historical pricing, ESG, and analytics.
examples:
- key_count: 18
  name: Rdp Connection Example
  slug: rdp-connection-example
- key_count: 12
  name: Rdp Session Example
  slug: rdp-session-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rdp.png
json_schemas:
- name: RDP Connection
  property_count: 17
  slug: rdp-connection
- name: RDP Session
  property_count: 11
  slug: rdp-session
json_structures:
- name: Rdp Connection Structure
  property_count: 0
  slug: rdp-connection-structure
jsonld:
- class_count: 9
  name: Rdp Context
  property_count: 18
  slug: rdp-context
layout: provider
modified: '2026-05-02'
name: RDP
nav: Providers
network: true
overview: 'RDP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Data, LSEG, Microsoft, Networking, and RDP.


  The RDP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RDP''s developer surface includes code examples, documentation, and 9 more developer resources.'
random_paper: 11
rules:
- effective_rule_count: 5
  extends: []
  name: RDP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rdp-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 68.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 21.3
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 15.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rdp/refs/heads/main/screenshots/rdp-2026-06-20T192627.png
slug: rdp
tags:
- Financial Data
- LSEG
- Microsoft
- Networking
- RDP
- Remote Access
- Remote Desktop
- Refinitiv
---
