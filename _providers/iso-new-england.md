---
access_model:
  confidence: high
  label: Free - Self-serve ISO Express account required for the API
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - probe
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Iso New England Agentic Access
  operation_count: 489
  slug: iso-new-england-agentic-access
  summary_line: 489 operations
api_count: 1
apis:
- description: ISO New England's RESTful interface to energy and market data, deployed November 2013 and still the current version. The public Enunciate-generated technical documentation at webservices.iso-ne.com/do
  name: ISO New England Web Services API v1.1
  slug: iso-ne-web-services-api
arazzos:
- description: Build a complete current picture of the New England power system - resolve the location registry, check feed freshness, then pull system load, generation fuel mix, Hub price and the hourly load foreca
  name: ISO New England grid snapshot
  slug: iso-new-england-grid-snapshot
- description: 'Explain a price event on a past operating day: pull the day-ahead hourly prices, the day''s transmission constraints, the fuel mix and the demand-response dispatch, then correlate the congestion compon'
  name: ISO New England price spike diagnosis
  slug: iso-new-england-price-spike-diagnosis
artifact_total: 23
collections:
- collection_type: open
  name: ISO New England Web Services API v1.1
  slug: open-iso-new-england-web-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iso-new-england-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iso-new-england-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iso-new-england-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/iso-new-england-web-services-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iso-new-england-web-services-schemas.json
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/iso-new-england-vocabulary.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iso-new-england-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/iso-new-england-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iso-new-england-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/iso-new-england-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iso-new-england-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.iso-ne.com/participate/rules-procedures/nerc-npcc
- group: build
  title: ''
  type: Packages
  url: packages/iso-new-england-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/iso-new-england-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/iso-new-england-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/iso-new-england-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/iso-new-england-web-services-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iso-new-england-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/iso-new-england-grid-snapshot.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/iso-new-england-price-spike-diagnosis.yml
- group: company
  title: ''
  type: Website
  url: https://www.iso-ne.com/
- group: start
  title: ''
  type: Portal
  url: https://www.iso-ne.com/isoexpress/
- group: docs
  title: ''
  type: APIReference
  url: https://webservices.iso-ne.com/docs/v1.1/
- group: docs
  title: ''
  type: Documentation
  url: https://www.iso-ne.com/participate/support/web-services-data
- group: start
  title: ''
  type: SignUp
  url: https://www.iso-ne.com/signup
- group: docs
  title: ''
  type: Documentation
  url: https://www.iso-ne.com/markets-operations/iso-express
- group: other
  title: ''
  type: Regulation
  url: https://www.iso-ne.com/markets-operations/transmission-operations-services/oasis
- group: company
  title: ''
  type: Blog
  url: https://isonewswire.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://isonewswire.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iso-new-england/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/isonewengland
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@isonewengland
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iso-ne
- group: operate
  title: ''
  type: Support
  url: https://askiso.iso-ne.com/s/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.iso-ne.com/participate/support/web-services-data
- group: start
  title: ''
  type: GettingStarted
  url: https://www.iso-ne.com/participate/applications-status-changes/access-software-systems#data-feeds
- group: operate
  title: ''
  type: FAQ
  url: https://www.iso-ne.com/participate/support/faq
- group: other
  title: ''
  type: Glossary
  url: https://www.iso-ne.com/participate/support/glossary-acronyms
- group: operate
  title: ''
  type: Roadmap
  url: https://www.iso-ne.com/committees/key-projects/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iso-ne.com/legal-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iso-ne.com/legal-privacy
created: '2026-07-27'
description: ISO New England Inc. is the independent, nonprofit regional transmission organization authorized by the Federal Energy Regulatory Commission to operate the high-voltage power system, administer the wholesale electricity markets, and plan the power system for Connecticut, Rhode Island, Massachusetts, Vermont, New Hampshire, and most of Maine. Home market is the United States. It sits at the wholesale layer of the value chain, between generators, transmission owners, interconnections with New York and Canada, and the load-serving entities that resell power to retail customers - and it states on its own site that handling retail electricity is something it does not do. Its API posture is the sector's classic split, read from the wholesale end. Market and system data is genuinely open, so open that the ISO Express portal serves full nodal day-ahead LMP files as anonymous CSV and the public dashboards are backed by an anonymous JSON feed. Consumer data does not exist here at all,
  and cannot, because ISO New England holds no retail customer relationships and no Green Button, ESPI, or consumer data-portability mandate reaches it. The one documented programmatic contract, the Web Services API v1.1, is a real, richly documented RESTful surface of 477 path templates across 90 market and operations resources, but it answers 401 to anonymous callers - a developer must first create a free, self-serve ISO Express account, which the ISO says automatically grants access to the data feeds, and then authenticate with HTTP Basic over SSL.
examples:
- key_count: 1
  name: Iso New England Actualinterchange_Current
  slug: iso-new-england-actualinterchange_current
- key_count: 1
  name: Iso New England Dayaheadconstraints_Current
  slug: iso-new-england-dayaheadconstraints_current
- key_count: 1
  name: Iso New England Dayaheadhourlydemand_Current
  slug: iso-new-england-dayaheadhourlydemand_current
- key_count: 1
  name: Iso New England Fifteenminutelmp_Final_Current
  slug: iso-new-england-fifteenminutelmp_final_current
- key_count: 1
  name: Iso New England Fiveminutelmp_Current
  slug: iso-new-england-fiveminutelmp_current
- key_count: 1
  name: Iso New England Fiveminutelmp_Info
  slug: iso-new-england-fiveminutelmp_info
- key_count: 1
  name: Iso New England Fiveminutesystemload_Current
  slug: iso-new-england-fiveminutesystemload_current
- key_count: 1
  name: Iso New England Genfuelmix_Current
  slug: iso-new-england-genfuelmix_current
- key_count: 1
  name: Iso New England Genfuelmix_Info
  slug: iso-new-england-genfuelmix_info
- key_count: 1
  name: Iso New England Hourlyloadforecast_Current
  slug: iso-new-england-hourlyloadforecast_current
- key_count: 1
  name: Iso New England Locations_All
  slug: iso-new-england-locations_all
- key_count: 1
  name: Iso New England Morningreport_Current
  slug: iso-new-england-morningreport_current
- key_count: 1
  name: Iso New England Realtimehourlydemand_Current
  slug: iso-new-england-realtimehourlydemand_current
- key_count: 1
  name: Iso New England Sevendayforecast_Current
  slug: iso-new-england-sevendayforecast_current
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
json_schemas:
- name: ISO New England Web Services API v1.1 data model
  property_count: 0
  slug: iso-new-england-web-services-schemas
layout: provider
mcp_servers:
- description: ''
  name: ISO New England MCP Server
  slug: iso-new-england-mcp-server
modified: '2026-07-27'
name: ISO New England
nav: Providers
network: true
overview: 'ISO New England publishes 1 API on the [APIs.io](https://apis.io/) network: Web Services API v1.1. Tagged areas include Energy, United States, Electricity, Energy Markets, and Grid.


  ISO New England''s developer surface includes authentication, code examples, changelog, developer portal, API reference, documentation, signup flow, and 36 more developer resources.'
random_paper: 10
score:
  band: strong
  composite: 55.9
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 65.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 23.7
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 51.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iso-new-england/refs/heads/main/screenshots/iso-new-england-2026-08-07T170922.png
security:
- kind: authentication
  name: Iso New England Authentication
  slug: iso-new-england-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Iso New England Domain Security
  slug: iso-new-england-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iso-new-england
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- Open Data
- Wholesale Markets
- Demand Response
- Renewables
- New England
website: https://www.iso-ne.com/
---
