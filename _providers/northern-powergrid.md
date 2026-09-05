---
access_model:
  confidence: high
  label: Free · Anonymous read, free registration for full data
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - probe
  - portal
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Northern Powergrid Agentic Access
  operation_count: 32
  slug: northern-powergrid-agentic-access
  summary_line: 32 operations
api_count: 2
apis:
- description: The original Opendatasoft Search API, still live on the portal and still carrying its own interactive console. Confirmed anonymously on 2026-07-27 — GET /api/datasets/1.0/search/?rows=1 returned nhits
  name: Northern Powergrid Open Data Search API v1
  slug: northern-powergrid-open-data-search-api-v1
- baseURL: https://northernpowergrid.opendatasoft.com/api/explore/v2.1
  baseurl_source: declared
  description: API to enumerate datasets
  name: Northern Powergrid Catalog API
  slug: northern-powergrid-catalog-api
- baseURL: https://northernpowergrid.opendatasoft.com/api/explore/v2.1
  baseurl_source: declared
  description: API to work on records
  name: Northern Powergrid Dataset API
  slug: northern-powergrid-dataset-api
artifact_total: 11
collections:
- collection_type: open
  name: Explore API
  slug: open-northern-powergrid-open-data-explore-api-v2-0
- collection_type: open
  name: Explore API
  slug: open-northern-powergrid-open-data-explore-api-v2-1
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/northern-powergrid-open-data-explore-api-v2-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/northern-powergrid-open-data-explore-api-v2-0-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/northern-powergrid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northern-powergrid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/northern-powergrid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/northern-powergrid-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/northern-powergrid-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/northern-powergrid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/northern-powergrid-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/northern-powergrid-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/northern-powergrid-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.huwise.com/apis/ods-explore-v2/#section/Versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/northern-powergrid-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/northern-powergrid-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/northern-powergrid-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/northern-powergrid-examples.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/northern-powergrid-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/northern-powergrid-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/northern-powergrid-packages.yml
- group: design
  title: ''
  type: Components
  url: components/northern-powergrid-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/northern-powergrid-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/northern-powergrid-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/northern-powergrid-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/northern-powergrid-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/northern-powergrid-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/northern-powergrid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://northernpowergrid.opendatasoft.com/.well-known/security.txt
- group: docs
  title: ''
  type: APIReference
  url: https://help.huwise.com/apis/ods-explore-v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.huwise.com/apis/ods-explore-v2/#section/Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://northernpowergrid.opendatasoft.com/pages/contactform/
- group: start
  title: ''
  type: SignUp
  url: https://northernpowergrid.opendatasoft.com/signup/
- group: start
  title: ''
  type: Login
  url: https://northernpowergrid.opendatasoft.com/account/login/
- group: operate
  title: ''
  type: Roadmap
  url: https://northernpowergrid.opendatasoft.com/explore/dataset/data-roadmap/information/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.northernpowergrid.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.northernpowergrid.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.northernpowergrid.com/
- group: start
  title: ''
  type: Portal
  url: https://northernpowergrid.opendatasoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://northernpowergrid.opendatasoft.com/pages/tutorial_page/
- group: start
  title: ''
  type: APIConsole
  url: https://northernpowergrid.opendatasoft.com/api-console/explore/v2.1/
- group: commercial
  title: ''
  type: License
  url: https://northernpowergrid.opendatasoft.com/p/opendatalicence/
- group: other
  title: ''
  type: Explore
  url: https://northernpowergrid.opendatasoft.com/explore/
- group: other
  title: ''
  type: Map
  url: https://northernpowergrid.opendatasoft.com/map/
- group: other
  title: ''
  type: Dashboards
  url: https://northernpowergrid.opendatasoft.com/pages/portal_dashboards/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/northernpowergrid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northern-powergrid/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.brkenergy.com/our-businesses/northern-powergrid
created: '2026-07-27'
description: 'Northern Powergrid is the electricity distribution network operator (DNO) for the North East of England, Yorkshire and northern Lincolnshire, owning and running the poles, wires, substations and low-voltage network that deliver power to 4 million homes and businesses across roughly 10,000 square miles. It is a Berkshire Hathaway Energy company and it does not sell electricity — it moves it, so it holds no retail customer accounts and no billing relationship. Its API posture reflects that split exactly: the market and network side is genuinely open, with a live Opendatasoft-hosted open data portal publishing 102 datasets under the Northern Powergrid Open Data Licence v1.0 and a fully documented Explore REST API that answers anonymously at 5,000 requests a day, including live power cut incidents, operational metering, embedded capacity registers, network capacity headroom and aggregated smart meter consumption; the consumer side is empty, because Britain has no energy consumer
  data right equivalent to the Australian Consumer Data Right and a DNO would not be the obligated party if it did. The open data programme exists because Ofgem''s Data Best Practice Guidance is a licence condition under the RIIO-ED2 price control, and unlike many mandates in this sector it is visibly implemented rather than merely claimed. Roughly 44 of the 102 datasets are metadata-visible but records-gated to anonymous callers and require a free self-serve portal registration to read.'
image: https://s3-eu-central-1.amazonaws.com/aws-ec2-eu-central-1-opendatasoft-staticfileset/northernpowergrid/logo?tstamp=1668505636764573
layout: provider
modified: '2026-07-27'
name: Northern Powergrid
nav: Providers
network: true
overview: 'Northern Powergrid publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Grid.


  Northern Powergrid''s developer surface includes authentication, changelog, code examples, sandbox, API reference, getting-started guide, support, and 40 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Northern Powergrid Rate Limits
  slug: northern-powergrid-rate-limits
scopes:
- name: Northern Powergrid Scopes
  scope_count: 1
  slug: northern-powergrid-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 59.9
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 75.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/northern-powergrid/refs/heads/main/screenshots/northern-powergrid-2026-08-07T185523.png
security:
- kind: authentication
  name: Northern Powergrid Authentication
  slug: northern-powergrid-authentication
  summary_line: none/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Northern Powergrid Domain Security
  slug: northern-powergrid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Northern Powergrid Vulnerability Disclosure
  slug: northern-powergrid-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: northern-powergrid
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Open Data
- Distribution Network Operator
- Smart Metering
- Network Capacity
- Flexibility
- DER
- Renewables
website: https://www.northernpowergrid.com/
---
