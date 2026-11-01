---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Gbg Agentic Access
  operation_count: 29
  slug: gbg-agentic-access
  summary_line: 29 operations · 17 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: GBG's ID3global identity verification SOAP web service (WCF), served from id3global.com (site titled "GBG | ID3global", copyright GB Group plc), with 179 operations; a pilot environment is at pilot.id
  name: GBG ID3global
  slug: gbg-id3global
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The As API from GBG — 1 operation(s) for as.
  name: GBG As API
  slug: gbg-as-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Authentication API from GBG — 1 operation(s) for authentication.
  name: GBG Authentication API
  slug: gbg-authentication-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Customer APIs API from GBG — 6 operation(s) for customer apis.
  name: GBG Customer APIs API
  slug: gbg-customer-apis-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Device API from GBG — 4 operation(s) for device.
  name: GBG Device API
  slug: gbg-device-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The End User APIs API from GBG — 3 operation(s) for end user apis.
  name: GBG End User APIs API
  slug: gbg-end-user-apis-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Health API from GBG — 1 operation(s) for health.
  name: GBG Health API
  slug: gbg-health-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Interaction API from GBG — 6 operation(s) for interaction.
  name: GBG Interaction API
  slug: gbg-interaction-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Interaction Service API from GBG — 2 operation(s) for interaction service.
  name: GBG Interaction Service API
  slug: gbg-interaction-service-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Journey API from GBG — 9 operation(s) for journey.
  name: GBG Journey API
  slug: gbg-journey-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Journey execution API from GBG — 1 operation(s) for journey execution.
  name: GBG Journey execution API
  slug: gbg-journey-execution-api
- baseURL: https://eu.platform.go.gbgplc.com/v2/captain
  baseurl_source: declared
  description: The Sandbox API from GBG — 2 operation(s) for sandbox.
  name: GBG Sandbox API
  slug: gbg-sandbox-api
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/gbg/capabilities/gbg-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gbg-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gbg/agentic-access/gbg-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gbg-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/gbg/rules/gbg-rules.yml
  title: ''
  type: Spectral
  url: rules/gbg-rules.yml
- group: design
  href: https://artifacts.apis.io/gbg/json-ld/gbg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gbg-context.jsonld
- group: design
  href: https://artifacts.apis.io/gbg/vocabulary/gbg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gbg-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gbg/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gbg/data-model/gbg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gbg-data-model.yml
- group: operate
  href: https://artifacts.apis.io/gbg/changelog/gbg-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gbg-changelog.yml
- group: design
  href: https://artifacts.apis.io/gbg/lifecycle/gbg-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gbg-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gbg/errors/gbg-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gbg-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gbg/conformance/gbg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gbg-conformance.yml
- group: other
  href: https://artifacts.apis.io/gbg/overlays/gbg-go-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gbg-go-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/gbg/llms/gbg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gbg-llms.txt
- group: other
  href: https://artifacts.apis.io/gbg/a2a/gbg-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gbg-a2a.yml
- group: build
  href: https://artifacts.apis.io/gbg/mcp/gbg-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gbg-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gbg/mcp/gbg-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gbg-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gbg/well-known/gbg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gbg-well-known.yml
- group: other
  href: https://artifacts.apis.io/gbg/hosts/gbg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gbg-hosts.yml
- group: other
  href: https://artifacts.apis.io/gbg/vendors/gbg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gbg-vendors.yml
- group: build
  href: https://artifacts.apis.io/gbg/packages/gbg-packages.yml
  title: ''
  type: SDKs
  url: packages/gbg-packages.yml
- group: build
  href: https://artifacts.apis.io/gbg/packages/gbg-packages.yml
  title: ''
  type: Packages
  url: packages/gbg-packages.yml
- group: auth
  href: https://artifacts.apis.io/gbg/authentication/gbg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gbg-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gbg/security/gbg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gbg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gbgplc.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.go.gbgplc.com/docs/go-v2/homepage
- group: docs
  title: ''
  type: Documentation
  url: https://docs.go.gbgplc.com/docs/go-v2/homepage
- group: docs
  title: ''
  type: APIReference
  url: https://docs.go.gbgplc.com/docs/go-v2/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.go.gbgplc.com/docs/go-v2/get-started/quickstart/quickstartdev
- group: operate
  title: ''
  type: Support
  url: https://docs.go.gbgplc.com/docs/go-v2/get-started/troubleshooting-and-support
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.go.gbgplc.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.gbg.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GBGPLC
- group: operate
  title: ''
  type: Contact
  url: https://www.gbgplc.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gbgplc.com/legal-and-regulatory/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gbgplc.com/legal-and-regulatory/privacy-policy/
created: '2026-10-18'
description: GBG (gbgplc.com, which also runs investor relations pages) is an identity verification, location intelligence and fraud prevention company. Its site describes solutions that help organisations quickly validate and verify the identity and location of their customers. Developers integrate through the GBG GO identity verification platform, whose documented REST API covers access tokens, starting customer journeys, retrieving and submitting tasks, and fetching journey state.
image: https://www.gbgplc.com/media/fj1baavn/facebook-profile-picture.png
json_schemas:
- name: ClientCredentialsGrantRequest
  property_count: 4
  slug: gbg-client-credentials-grant-request
- name: CreateSandboxScenarioRequest
  property_count: 2
  slug: gbg-create-sandbox-scenario-request
- name: InteractionFetchResponse
  property_count: 11
  slug: gbg-interaction-fetch-response
- name: PasswordGrantRequest
  property_count: 5
  slug: gbg-password-grant-request
- name: SlimInteractionFetchResponse
  property_count: 10
  slug: gbg-slim-interaction-fetch-response
- name: UpdateSandboxScenarioRequest
  property_count: 1
  slug: gbg-update-sandbox-scenario-request
jsonld:
- class_count: 33
  name: Gbg Context
  property_count: 86
  slug: gbg-context
layout: provider
mcp_servers:
- description: 'GBG publishes a remote MCP server for the GBG Go documentation (Mintlify-hosted docs site). It lets MCP clients search the docs and read page/OpenAPI content. It is a DOCUMENTATION server: it does not'
  name: GBG Go Documentation MCP Server
  slug: gbg-go-documentation-mcp-server
modified: '2026-10-18'
name: GBG
nav: Providers
network: true
overview: 'GBG publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including As API, Authentication API, Customer APIs API, and 9 more. Tagged areas include Company, Identity Verification, Fraud Prevention, KYC, and Location Intelligence.


  The GBG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GBG''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: GBG API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 2
  slug: gbg-rules
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 65.4
    developer_ergonomics: 71.4
    discoverability: 76.7
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gbg Authentication
  slug: gbg-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gbg Domain Security
  slug: gbg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gbg
tags:
- Company
- Identity Verification
- Fraud Prevention
- KYC
- Location Intelligence
- Compliance
- Digital Identity
website: https://gbgplc.com
---
