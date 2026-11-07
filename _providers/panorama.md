---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Panorama Agentic Access
  operation_count: 7
  slug: panorama-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- description: Panorama XML/REST API for centralized network security management across Palo Alto Networks firewalls.
  name: Panorama API
  slug: panorama
- baseURL_template: https://{panorama_host}
  baseurl_source: spec_template
  description: The Panorama API API from Panorama — 1 operation(s) for panorama api.
  name: Panorama API
  slug: panorama-panorama-api-api
- baseURL_template: https://{panorama_host}
  baseurl_source: spec_template
  description: The REST API API from Panorama — 3 operation(s) for rest api.
  name: Panorama REST API
  slug: panorama-rest-api-api
artifact_total: 13
collections:
- collection_type: open
  name: Panorama Panorama API API
  slug: open-panorama-panorama-api-api
- collection_type: open
  name: Panorama Panorama API Restapi API
  slug: open-panorama-restapi-api
- collection_type: open
  name: Panorama API
  slug: open-panorama
common:
- group: commercial
  href: https://artifacts.apis.io/panorama/plans/panorama-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/panorama-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/panorama/rate-limits/panorama-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/panorama-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/panorama/finops/panorama-finops.yml
  title: ''
  type: FinOps
  url: finops/panorama-finops.yml
- group: other
  href: https://artifacts.apis.io/panorama/capabilities/panorama-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/panorama-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/panorama/agentic-access/panorama-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/panorama-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/panorama/security/panorama-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/panorama-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/panorama/authentication/panorama-authentication.yml
  title: ''
  type: Authentication
  url: authentication/panorama-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/panorama-ed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/panorama-education
- group: company
  title: ''
  type: Website
  url: https://www.paloaltonetworks.com/network-security/panorama
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paloaltonetworks.com/panorama
created: '2026-03-16'
description: Panorama is a centralized network security management platform by Palo Alto Networks that provides centralized policy management, device configuration, and logging across Palo Alto Networks firewalls and Prisma Access.
finops:
- has_sources: false
  method: generated
  name: Panorama Finops
  primary_unit: request
  service_category: API
  slug: panorama-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/panorama.png
layout: provider
modified: '2026-09-16'
name: Panorama
nav: Providers
network: true
overview: 'Panorama publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API, and 2 more. Tagged areas include Firewall Management, Network Security, and Palo Alto Networks.


  The Panorama catalog on APIs.io includes 1 Spectral governance ruleset.


  Panorama''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Panorama Plans Pricing
  plan_count: 3
  slug: panorama-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Panorama Rate Limits
  slug: panorama-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Panorama API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: panorama-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.5
    catalog_earned_first_party: 0.0
    catalog_gap: 77.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 42.2
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 23.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/panorama/panorama-2026-06-20T191341.png
security:
- kind: authentication
  name: Panorama Authentication
  slug: panorama-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Panorama Domain Security
  slug: panorama-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: panorama
tags:
- Firewall Management
- Network Security
- Palo Alto Networks
website: https://www.paloaltonetworks.com/network-security/panorama
---
