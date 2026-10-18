---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Istreamplanet Agentic Access
  operation_count: 73
  slug: istreamplanet-agentic-access
  summary_line: 73 operations · 29 acting
api_count: 2
apis:
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Audit Operations for Organization API from iStreamPlanet — 1 operation(s) for audit operations for organization.
  name: iStreamPlanet Audit Operations for Organization API
  slug: istreamplanet-audit-operations-for-organization-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Available Sources API from iStreamPlanet — 2 operation(s) for available sources.
  name: iStreamPlanet Available Sources API
  slug: istreamplanet-available-sources-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Channel Operations for Organization API from iStreamPlanet — 12 operation(s) for channel operations for organization.
  name: iStreamPlanet Channel Operations for Organization API
  slug: istreamplanet-channel-operations-for-organization-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Channels API from iStreamPlanet — 1 operation(s) for channels.
  name: iStreamPlanet Channels API
  slug: istreamplanet-channels-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Channels for Organization API from iStreamPlanet — 4 operation(s) for channels for organization.
  name: iStreamPlanet Channels for Organization API
  slug: istreamplanet-channels-for-organization-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Deprecated Live2VOD API from iStreamPlanet — 8 operation(s) for deprecated live2vod.
  name: iStreamPlanet Deprecated Live2VOD API
  slug: istreamplanet-deprecated-live2vod-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Live2VOD for Organization API from iStreamPlanet — 26 operation(s) for live2vod for organization.
  name: iStreamPlanet Live2VOD for Organization API
  slug: istreamplanet-live2vod-for-organization-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Organizations API from iStreamPlanet — 1 operation(s) for organizations.
  name: iStreamPlanet Organizations API
  slug: istreamplanet-organizations-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Source Previews API from iStreamPlanet — 4 operation(s) for source previews.
  name: iStreamPlanet Source Previews API
  slug: istreamplanet-source-previews-api
- baseURL: https://api.istreamplanet.com
  baseurl_source: declared
  description: The Transcoder Telemetry API from iStreamPlanet — 5 operation(s) for transcoder telemetry.
  name: iStreamPlanet Transcoder Telemetry API
  slug: istreamplanet-transcoder-telemetry-api
artifact_total: 25
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/agentic-access/istreamplanet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/istreamplanet-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/rules/istreamplanet-rules.yml
  title: ''
  type: Spectral
  url: rules/istreamplanet-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/rules/istreamplanet-rest-api-lint-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/istreamplanet-rest-api-lint-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/json-ld/istreamplanet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/istreamplanet-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/vocabulary/istreamplanet-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/istreamplanet-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/data-model/istreamplanet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/istreamplanet-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/cli/istreamplanet-cli.yml
  title: ''
  type: CLI
  url: cli/istreamplanet-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/conventions/istreamplanet-conventions.yml
  title: ''
  type: Conventions
  url: conventions/istreamplanet-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/lifecycle/istreamplanet-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/istreamplanet-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/lifecycle/istreamplanet-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/istreamplanet-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/errors/istreamplanet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/istreamplanet-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/conformance/istreamplanet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/istreamplanet-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/overlays/istreamplanet-aventus-channels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/istreamplanet-aventus-channels-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/hosts/istreamplanet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/istreamplanet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/vendors/istreamplanet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/istreamplanet-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/packages/istreamplanet-packages.yml
  title: ''
  type: SDKs
  url: packages/istreamplanet-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/packages/istreamplanet-packages.yml
  title: ''
  type: Packages
  url: packages/istreamplanet-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/scopes/istreamplanet-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/istreamplanet-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/authentication/istreamplanet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/istreamplanet-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/istreamplanet/refs/heads/main/security/istreamplanet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/istreamplanet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.istreamplanet.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/istreamlabs/rest-api-lint/blob/98553242c3d8d4e64c628aa53ce33f9d27dde10b/isp-rules.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/istreamlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/istreamplanet
created: '2026-10-09'
description: iStreamPlanet was a Las Vegas-based live video streaming company, founded in 2000, whose cloud-based Aventus live video workflow platform delivered live events and linear channels over the internet to multiple platforms and devices. Turner Broadcasting took a majority stake in 2015; the company later sat under WarnerMedia and then Warner Bros. Discovery, which shut it down in August 2023. Its open-source arm, iStreamPlanet Labs (github.com/istreamlabs), publishes Apache 2.0 projects including the rest-api-lint Spectral ruleset.
image: https://avatars.githubusercontent.com/u/30184888?v=4
json_schemas:
- name: Channel
  property_count: 19
  slug: istreamplanet-channel
- name: GenericSignal
  property_count: 10
  slug: istreamplanet-generic-signal
- name: GetSourcePreviewStreamResponseBody
  property_count: 7
  slug: istreamplanet-get-source-preview-stream-response-body
- name: GetTaskResponseBody
  property_count: 16
  slug: istreamplanet-get-task-response-body
- name: PutChannelRequestBody
  property_count: 19
  slug: istreamplanet-put-channel-request-body
- name: Segment
  property_count: 8
  slug: istreamplanet-segment
jsonld:
- class_count: 120
  name: Istreamplanet Context
  property_count: 313
  slug: istreamplanet-context
layout: provider
modified: '2026-10-09'
name: iStreamPlanet
nav: Providers
network: true
overview: 'iStreamPlanet publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit Operations for Organization API, Available Sources API, Channel Operations for Organization API, and 7 more. Tagged areas include Company, Video Streaming, Live Streaming, Media, and Cloud Video.


  The iStreamPlanet catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  iStreamPlanet''s developer surface includes CLI, authentication, and 23 more developer resources.'
plans:
- name: Istreamplanet Plans Pricing
  plan_count: 0
  slug: istreamplanet-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Istreamplanet Rate Limits
  slug: istreamplanet-rate-limits
rules:
- authorship: provider
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: iStreamPlanet — rest api lint rules
  rule_count: 19
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 5
  slug: istreamplanet-rest-api-lint-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: iStreamPlanet API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: istreamplanet-rules
scopes:
- name: Istreamplanet Scopes
  scope_count: 2
  slug: istreamplanet-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 76.3
    catalog_earned_first_party: 18.0
    catalog_gap: 38.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.2
  facets:
    access_clarity: 0.0
    contract_governance: 76.5
    contract_quality: 63.7
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Istreamplanet Authentication
  slug: istreamplanet-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Istreamplanet Domain Security
  slug: istreamplanet-domain-security
  summary_line: no transport/DNS hardening detected
slug: istreamplanet
tags:
- Company
- Video Streaming
- Live Streaming
- Media
- Cloud Video
- Spectral
- API Governance
website: https://www.istreamplanet.com/
---
