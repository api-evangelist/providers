---
access_model:
  confidence: high
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 28.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lufthansa Agentic Access
  operation_count: 15
  slug: lufthansa-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: 'The Lufthansa Partner API exposes deeplinks, fares, pricing offers, and seat details for integration partners. NDC capabilities including Smart Offer, NDC Bonus, Servicing, and Technology are part of '
  name: Lufthansa Partner API
  slug: partner-api
- description: The FlightOps and Crew API provides crew-specific services including check-in times, duty events, and weather information for operational use cases.
  name: Lufthansa FlightOps and Crew API
  slug: flightops-crew
- description: The Lufthansa Cargo API provides shipment tracking and LH CARGO flight routings.
  name: Lufthansa Cargo API
  slug: cargo
- description: The Notifications API delivers FlightUpdate notifications and JWT-based authentication tokens for streaming flight events.
  name: Lufthansa Notifications API
  slug: notifications
- baseURL: https://api.lufthansa.com/v1
  baseurl_source: declared
  description: The Cargo API from Lufthansa — 2 operation(s) for cargo.
  name: Lufthansa Cargo API
  slug: lufthansa-cargo-api
- baseURL: https://api.lufthansa.com/v1
  baseurl_source: declared
  description: The Offers API from Lufthansa — 2 operation(s) for offers.
  name: Lufthansa Offers API
  slug: lufthansa-offers-api
- baseURL: https://api.lufthansa.com/v1
  baseurl_source: declared
  description: The Operations API from Lufthansa — 5 operation(s) for operations.
  name: Lufthansa Operations API
  slug: lufthansa-operations-api
- baseURL: https://api.lufthansa.com/v1
  baseurl_source: declared
  description: The Reference Data API from Lufthansa — 6 operation(s) for reference data.
  name: Lufthansa Reference Data API
  slug: lufthansa-reference-data-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lufthansa LH Public Cargo API
  slug: open-lufthansa-cargo-api
- collection_type: open
  name: Lufthansa LH Public Cargo Offers API
  slug: open-lufthansa-offers-api
- collection_type: open
  name: Lufthansa LH Public Cargo Operations API
  slug: open-lufthansa-operations-api
- collection_type: open
  name: Lufthansa LH Public Cargo Reference Data API
  slug: open-lufthansa-reference-data-api
- collection_type: open
  name: Lufthansa LH Public API
  slug: open-lufthansa
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lufthansa-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lufthansa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lufthansa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lufthansa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lufthansa-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lufthansa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lufthansa
- group: company
  title: ''
  type: Website
  url: https://www.lufthansagroup.com
- group: start
  title: ''
  type: Portal
  url: https://developer.lufthansa.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lufthansa.com/docs/read/api_details
- group: auth
  title: ''
  type: Authentication
  url: https://developer.lufthansa.com/docs/read/Authentication
- group: start
  title: ''
  type: Signup
  url: https://developer.lufthansa.com/user/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.lufthansa.com/docs/read/General_Terms_and_Conditions
created: '2024-07-02'
description: The Lufthansa Group is a global aviation group that plays a leading role in its European home market. The Lufthansa Open API developer portal exposes reference data, flight operations, offers, notifications, and cargo APIs secured with OAuth2 for partner and public consumers.
finops:
- name: Lufthansa Finops
  service_category: Travel
  slug: lufthansa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lufthansa.png
json_schemas:
- name: Airport
  property_count: 8
  slug: lufthansa-airport
- name: AirportResource
  property_count: 2
  slug: lufthansa-airportresource
- name: AirportResponse
  property_count: 1
  slug: lufthansa-airportresponse
- name: Coordinate
  property_count: 2
  slug: lufthansa-coordinate
- name: Link
  property_count: 2
  slug: lufthansa-link
- name: Name
  property_count: 2
  slug: lufthansa-name
json_structures:
- name: Lufthansa Structure
  property_count: 0
  slug: lufthansa-structure
layout: provider
modified: '2026-05-19'
name: Lufthansa
nav: Providers
network: true
overview: 'Lufthansa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cargo API, Offers API, Operations API, and 1 more. Tagged areas include Airlines, Travel, Aviation, and Flights.


  The Lufthansa catalog on APIs.io includes 1 Spectral governance ruleset.


  Lufthansa''s developer surface includes authentication, developer portal, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Lufthansa Plans Pricing
  plan_count: 2
  slug: lufthansa-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Lufthansa Rate Limits
  slug: lufthansa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lufthansa API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lufthansa-jsonschema-spectral-rules
scopes:
- name: Lufthansa Scopes
  scope_count: 1
  slug: lufthansa-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 72.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 50.9
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lufthansa/refs/heads/main/screenshots/lufthansa-2026-06-20T184749.png
security:
- kind: authentication
  name: Lufthansa Authentication
  slug: lufthansa-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lufthansa Domain Security
  slug: lufthansa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lufthansa
tags:
- Airlines
- Travel
- Aviation
- Flights
website: https://www.lufthansagroup.com
---
