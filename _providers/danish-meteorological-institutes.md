---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Danish Meteorological Institutes Agentic Access
  operation_count: 5
  slug: danish-meteorological-institutes-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: Quality-checked climate data at multiple aggregation levels.
  name: Danish Meteorological Institutes climateData API
  slug: danish-meteorological-institutes-climatedata-api
- description: Lightning strike observations.
  name: Danish Meteorological Institutes lightningData API
  slug: danish-meteorological-institutes-lightningdata-api
- description: Raw weather observations from Danish and Greenlandic stations.
  name: Danish Meteorological Institutes metObs API
  slug: danish-meteorological-institutes-metobs-api
- description: Sea-level and water-temperature observations.
  name: Danish Meteorological Institutes oceanObs API
  slug: danish-meteorological-institutes-oceanobs-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DMI Open Data climateData API
  slug: open-danish-meteorological-institutes-climatedata-api
- collection_type: open
  name: DMI Open Data climateData lightningData API
  slug: open-danish-meteorological-institutes-lightningdata-api
- collection_type: open
  name: DMI Open Data climateData metObs API
  slug: open-danish-meteorological-institutes-metobs-api
- collection_type: open
  name: DMI Open Data climateData oceanObs API
  slug: open-danish-meteorological-institutes-oceanobs-api
- collection_type: open
  name: DMI Open Data API
  slug: open-dmi-open-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/danish-meteorological-institutes-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/danish-meteorological-institutes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/danish-meteorological-institutes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/danish-meteorological-institutes-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dmi-danmarks-meteorologiske-institut
- group: company
  title: ''
  type: Website
  url: https://www.dmi.dk/
- group: start
  title: ''
  type: Open Data Portal
  url: https://opendatadocs.dmi.govcloud.dk/
- group: operate
  title: ''
  type: Open Data FAQ
  url: https://opendatadocs.dmi.govcloud.dk/en/FAQ
- group: other
  title: ''
  type: AWS Open Data
  url: https://registry.opendata.aws/dmi-opendata/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dmidk
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dmi-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dmi-vocabulary.yml
created: '2025-02-06'
description: The Danish Meteorological Institute is a government agency responsible for providing meteorological and climate services in Denmark. DMI publishes weather observations, climate data, ocean observations, and lightning data through its Open Data API and supplies forecast products via the AWS Open Data registry. The agency operates weather stations, radar systems, and satellites to monitor and forecast weather across Denmark, Greenland, and the Faroe Islands.
finops:
- name: Danish Meteorological Institutes Finops
  service_category: API
  slug: danish-meteorological-institutes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/danish-meteorological-institutes.png
json_schemas:
- name: Observation
  property_count: 4
  slug: observation
- name: Station
  property_count: 4
  slug: station
jsonld:
- class_count: 2
  name: Dmi Context
  property_count: 8
  slug: dmi-context
layout: provider
modified: '2026-05-19'
name: Danish Meteorological Institutes
nav: Providers
network: true
overview: 'Danish Meteorological Institutes publishes 4 APIs on the [APIs.io](https://apis.io/) network, including climateData API, lightningData API, metObs API, and 1 more. Tagged areas include Climate, Environment, Lightning, Meteorological, and Ocean.


  The Danish Meteorological Institutes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Danish Meteorological Institutes'' developer surface includes authentication and 11 more developer resources.'
plans:
- name: Danish Meteorological Institutes Plans Pricing
  plan_count: 3
  slug: danish-meteorological-institutes-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Danish Meteorological Institutes Rate Limits
  slug: danish-meteorological-institutes-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Danish Meteorological Institutes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: danish-meteorological-institutes-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Danish Meteorological Institutes API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dmi-open-data-api-rules
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 62.6
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/danish-meteorological-institutes/refs/heads/main/screenshots/danish-meteorological-institutes-2026-06-20T175450.png
security:
- kind: authentication
  name: Danish Meteorological Institutes Authentication
  slug: danish-meteorological-institutes-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Danish Meteorological Institutes Domain Security
  slug: danish-meteorological-institutes-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Danish Meteorological Institutes Vulnerability Disclosure
  slug: danish-meteorological-institutes-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: danish-meteorological-institutes
tags:
- Climate
- Environment
- Lightning
- Meteorological
- Ocean
- Open Data
- Weather
website: https://www.dmi.dk/
---
