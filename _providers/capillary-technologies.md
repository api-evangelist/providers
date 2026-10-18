---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: API documented at Capillary Documentation hub
  name: Capillary API
  slug: capillary-api
- baseURL: http://eu.api.capillarytech.com
  baseurl_source: declared
  description: The Events API from Capillary Technologies — 2 operation(s) for events.
  name: Capillary Technologies Events API
  slug: capillary-technologies-events-api
- baseURL: http://eu.api.capillarytech.com
  baseurl_source: declared
  description: The Simulation API from Capillary Technologies — 1 operation(s) for simulation.
  name: Capillary Technologies Simulation API
  slug: capillary-technologies-simulation-api
- baseURL: http://eu.api.capillarytech.com
  baseurl_source: declared
  description: The Webhooks API from Capillary Technologies — 1 operation(s) for webhooks.
  name: Capillary Technologies Webhooks API
  slug: capillary-technologies-webhooks-api
- baseURL: http://eu.api.capillarytech.com
  baseurl_source: declared
  description: The X API from Capillary Technologies — 1 operation(s) for x.
  name: Capillary Technologies X API
  slug: capillary-technologies-x-api
artifact_total: 13
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/rate-limits/capillary-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/capillary-technologies-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/rules/capillary-technologies-rules.yml
  title: ''
  type: Spectral
  url: rules/capillary-technologies-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/json-ld/capillary-technologies-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capillary-technologies-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/vocabulary/capillary-technologies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capillary-technologies-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/data-model/capillary-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capillary-technologies-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/sandbox/capillary-technologies-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/capillary-technologies-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/authentication/capillary-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capillary-technologies-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/conformance/capillary-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capillary-technologies-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/llms/capillary-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capillary-technologies-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/mcp/capillary-technologies-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/capillary-technologies-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/hosts/capillary-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capillary-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/vendors/capillary-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capillary-technologies-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.capillarytech.com/docs/getting-started-with-capillary
- group: docs
  title: ''
  type: Documentation
  url: https://docs.capillarytech.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capillary-technologies/refs/heads/main/security/capillary-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capillary-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.capillarytech.com/
coverage:
  checked: '2026-10-07'
  detail: Documentation is provided as markdown pages without a published OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.capillarytech.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Capillary Technologies provides enterprise loyalty management software, enabling brands to engage customers through personalized rewards, campaigns, and analytics. The platform offers tools for omnichannel loyalty, AI-driven insights, and integration with e‑commerce and CRM systems, serving global enterprises across retail, travel, and finance sectors.
json_schemas:
- name: GetV2EventsEventidResponse
  property_count: 3
  slug: capillary-technologies-get-v2-events-eventid-response
- name: PostXNeoCustomeridTierupgradeRequest
  property_count: 1
  slug: capillary-technologies-post-xneo-customerid-tierupgrade-request
jsonld:
- class_count: 2
  name: Capillary Technologies Context
  property_count: 3
  slug: capillary-technologies-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.capillarytech.com.
  name: Capillary Technologies MCP Server
  slug: capillary-technologies-mcp-yml
modified: '2026-10-06'
name: Capillary Technologies
nav: Providers
network: true
overview: 'Capillary Technologies is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Events API, Simulation API, Webhooks API, and 2 more. Tagged areas include Loyalty, Marketing, Software-as-a-Service, Enterprise, and Customer-Engagement.


  The Capillary Technologies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Capillary Technologies'' developer surface includes sandbox, authentication, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 1
  name: Capillary Technologies Rate Limits
  slug: capillary-technologies-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Capillary Technologies API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: capillary-technologies-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.5
    developer_ergonomics: 40.5
    discoverability: 68.3
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Capillary Technologies Authentication
  slug: capillary-technologies-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Capillary Technologies Domain Security
  slug: capillary-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: capillary-technologies
tags:
- Loyalty
- Marketing
- Software-as-a-Service
- Enterprise
- Customer-Engagement
website: https://www.capillarytech.com/
---
