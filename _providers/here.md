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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Here Agentic Access
  operation_count: 8
  slug: here-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 7
apis:
- description: The Autocomplete API from HERE — 1 operation(s) for autocomplete.
  name: HERE Autocomplete API
  slug: here-autocomplete-api
- description: The Autosuggest API from HERE — 1 operation(s) for autosuggest.
  name: HERE Autosuggest API
  slug: here-autosuggest-api
- description: The Browse API from HERE — 1 operation(s) for browse.
  name: HERE Browse API
  slug: here-browse-api
- description: The Discover API from HERE — 1 operation(s) for discover.
  name: HERE Discover API
  slug: here-discover-api
- description: The Geocode API from HERE — 1 operation(s) for geocode.
  name: HERE Geocode API
  slug: here-geocode-api
- description: The Lookup API from HERE — 1 operation(s) for lookup.
  name: HERE Lookup API
  slug: here-lookup-api
- description: The Reverse Geocode API from HERE — 2 operation(s) for reverse geocode.
  name: HERE Reverse Geocode API
  slug: here-reverse-geocode-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HERE Geocoding & Search API v7 Autocomplete API
  slug: open-here-autocomplete-api
- collection_type: open
  name: HERE Geocoding & Search API v7 Autocomplete Autosuggest API
  slug: open-here-autosuggest-api
- collection_type: open
  name: HERE Geocoding & Search API v7 Autocomplete Browse API
  slug: open-here-browse-api
- collection_type: open
  name: HERE Geocoding & Search API v7 Autocomplete Discover API
  slug: open-here-discover-api
- collection_type: open
  name: HERE Geocoding & Search API v7 Autocomplete Geocode API
  slug: open-here-geocode-api
- collection_type: open
  name: HERE Geocoding & Search API v7 Autocomplete Lookup API
  slug: open-here-lookup-api
- collection_type: open
  name: HERE Geocoding & Search API v7 Autocomplete Reverse Geocode API
  slug: open-here-reverse-geocode-api
- collection_type: open
  name: HERE Geocoding & Search API v7
  slug: open-here
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/here-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/here-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/here-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heremaps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/here
- group: start
  title: ''
  type: Signup
  url: https://platform.here.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://platform.here.com/portal/
- group: commercial
  title: ''
  type: Plans
  url: https://www.here.com/get-started/pricing
- group: operate
  title: ''
  type: Support
  url: https://developer.here.com/help
- group: learn
  title: ''
  type: Tutorials
  url: https://developer.here.com/tutorials
- group: build
  title: ''
  type: Examples
  url: https://developer.here.com/examples
- group: company
  title: ''
  type: Blog
  url: https://www.here.com/company/blog?type=developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.here.com/documentation/changelog/index.html
- group: company
  title: ''
  type: Newsletter
  url: https://developer.here.com/newsletter
- group: other
  title: ''
  type: Knowledge
  url: https://knowledge.here.com/csm_kb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.here.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.here.com/privacy/policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.here.com/terms/serviceterms
created: 2023/11/13
description: As global mobility becomes increasingly connected, electrified and automated, HERE Technologies is leading the way to a safer, greener future. Our location platform is integrated into more than 160 million vehicles across the planet, using fresh and accurate data that we have been building for over 35 years - and continue to refresh daily. Our experience in mapmaking has made HERE one of the leading innovators in location technology and spatial intelligence.
finops:
- name: Here Finops
  service_category: API
  slug: here-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/here.png
layout: provider
modified: '2026-04-28'
name: HERE
nav: Providers
network: true
overview: 'HERE publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Autosuggest API, Browse API, and 4 more. Tagged areas include Location, Mapping, Maps, and Spatial.


  HERE''s developer surface includes authentication, signup flow, support, code examples, engineering blog, changelog, and 12 more developer resources.'
plans:
- name: Here Plans Pricing
  plan_count: 3
  slug: here-plans-pricing
random_paper: 122
rate_limits:
- limit_count: 5
  name: Here Rate Limits
  slug: here-rate-limits
score:
  band: thin
  composite: 37.7
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/here/refs/heads/main/screenshots/here-2026-06-20T182640.png
security:
- kind: authentication
  name: Here Authentication
  slug: here-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Here Domain Security
  slug: here-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: here
tags:
- Location
- Mapping
- Maps
- Spatial
---
