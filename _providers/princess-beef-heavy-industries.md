---
access_model:
  confidence: medium
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Princess Beef Heavy Industries Agentic Access
  operation_count: 6
  slug: princess-beef-heavy-industries-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: At Princess Beef Heavy Industries (or as we call it pb33f), we build beautifully designed heavy-duty and enterprise grade software for code hackers and ...
  name: Princess Beef Heavy Industries
  slug: princess-beef-heavy-industries
- baseURL: https://api.pb33f.io/wiretap/giftshop
  baseurl_source: spec
  description: product operations
  name: Princess Beef Heavy Industries Product API
  slug: princess-beef-heavy-industries-product-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Princess Beef Heavy Industries pb33f Giftshop API
  slug: open-princess-beef-heavy-industries-giftshop
- collection_type: open
  name: Princess Beef Heavy Industries pb33f Giftshop Product API
  slug: open-princess-beef-heavy-industries-product-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/princess-beef-heavy-industries-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/princess-beef-heavy-industries-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/princess-beef-heavy-industries-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pb33f
created: '2025-01-08'
description: At Princess Beef Heavy Industries (or as we call it pb33f), we build beautifully designed heavy-duty and enterprise grade software for code hackers and ...
finops:
- name: Princess Beef Heavy Industries Finops
  service_category: API
  slug: princess-beef-heavy-industries-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/princess-beef-heavy-industries.png
json_schemas:
- name: pb33f Giftshop Error
  property_count: 5
  slug: error
- name: pb33f Giftshop Product
  property_count: 7
  slug: product
jsonld:
- class_count: 0
  name: Princess Beef Heavy Industries Context
  property_count: 2
  slug: princess-beef-heavy-industries-context
layout: provider
modified: '2026-05-19'
name: Princess Beef Heavy Industries
nav: Providers
network: true
overview: 'Princess Beef Heavy Industries publishes 1 API on the [APIs.io](https://apis.io/) network: Product API. Tagged areas include Commerce, Documentation, Editors, Governance, and Platform.


  The Princess Beef Heavy Industries catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Princess Beef Heavy Industries'' developer surface includes authentication and 3 more developer resources.'
plans:
- name: Princess Beef Heavy Industries Plans Pricing
  plan_count: 3
  slug: princess-beef-heavy-industries-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Princess Beef Heavy Industries Rate Limits
  slug: princess-beef-heavy-industries-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Princess Beef Heavy Industries API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: princess-beef-heavy-industries-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 71.7
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/princess-beef-heavy-industries/refs/heads/main/screenshots/princess-beef-heavy-industries-2026-06-20T192117.png
security:
- kind: authentication
  name: Princess Beef Heavy Industries Authentication
  slug: princess-beef-heavy-industries-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Princess Beef Heavy Industries Domain Security
  slug: princess-beef-heavy-industries-domain-security
  summary_line: TLSv1.3
slug: princess-beef-heavy-industries
tags:
- Commerce
- Documentation
- Editors
- Governance
- Platform
- Product
- Rules
---
