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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rescuegroups Org Agentic Access
  operation_count: 12
  slug: rescuegroups-org-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 8
apis:
- description: Search and retrieve adoptable animal records.
  name: RescueGroups.org Animals API
  slug: rescuegroups-org-animals-api
- description: Obtain bearer tokens for authenticated access.
  name: RescueGroups.org Authentication API
  slug: rescuegroups-org-authentication-api
- description: Retrieve animal breed reference data.
  name: RescueGroups.org Breeds API
  slug: rescuegroups-org-breeds-api
- description: Retrieve animal color reference data.
  name: RescueGroups.org Colors API
  slug: rescuegroups-org-colors-api
- description: Search and retrieve rescue organization records.
  name: RescueGroups.org Organizations API
  slug: rescuegroups-org-organizations-api
- description: Retrieve animal pattern reference data.
  name: RescueGroups.org Patterns API
  slug: rescuegroups-org-patterns-api
- description: Manage organization pet lists.
  name: RescueGroups.org Pet Lists API
  slug: rescuegroups-org-pet-lists-api
- description: Retrieve animal species reference data.
  name: RescueGroups.org Species API
  slug: rescuegroups-org-species-api
artifact_total: 22
collections:
- collection_type: open
  name: RescueGroups.org API
  slug: open-rescuegroups-org
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rescuegroups-org-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rescuegroups-org-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rescuegroups-org-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rescuegroups-org
- group: company
  title: ''
  type: Website
  url: https://rescuegroups.org/
- group: docs
  title: ''
  type: Documentation
  url: https://userguide.rescuegroups.org/spaces/APIDG/pages/8192120/API+Developers+Guide+Home
- group: build
  title: ''
  type: PostmanCollection
  url: https://documenter.getpostman.com/view/60615/SWT5j1e4
- group: operate
  title: ''
  type: CommunityForum
  url: https://groups.google.com/a/rescuegroups.org/g/apidev
- group: auth
  title: ''
  type: Authentication
  url: https://userguide.rescuegroups.org/spaces/APIDG/pages/24053254/v5
- group: company
  title: ''
  type: About
  url: https://rescuegroups.org/about/
- group: company
  title: ''
  type: Blog
  url: https://rescuegroups.org/feed/
created: '2025-01-07'
description: RescueGroups.org provides the only updatable HTTP/JSON API for adoptable pet data, offering comprehensive search across animals, organizations, breeds, species, colors, and patterns with geodistance filtering. The API supports both public read-only access via API key and authenticated write access via bearer token, enabling rescue organizations to manage and share pet adoption data in real time.
examples:
- key_count: 4
  name: Rescuegroups Org Search Animals Example
  slug: rescuegroups-org-search-animals-example
finops:
- name: Rescuegroups Org Finops
  service_category: API
  slug: rescuegroups-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rescuegroups-org.png
json_schemas:
- name: RescueGroups.org Animal
  property_count: 4
  slug: rescuegroups-org-animal
- name: RescueGroups.org Organization
  property_count: 3
  slug: rescuegroups-org-organization
json_structures:
- name: Rescuegroups Org Animal Structure
  property_count: 0
  slug: rescuegroups-org-animal-structure
jsonld:
- class_count: 15
  name: Rescuegroups Org Context
  property_count: 0
  slug: rescuegroups-org-context
layout: provider
modified: '2026-05-19'
name: RescueGroups.org
nav: Providers
network: true
overview: 'RescueGroups.org publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Animals API, Authentication API, Breeds API, and 5 more. Tagged areas include Animals, Pet Adoption, Rescue, and Animal Welfare.


  The RescueGroups.org catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RescueGroups.org''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Rescuegroups Org Plans Pricing
  plan_count: 3
  slug: rescuegroups-org-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 5
  name: Rescuegroups Org Rate Limits
  slug: rescuegroups-org-rate-limits
rules:
- name: RescueGroups.org API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rescuegroups-org-jsonschema-spectral-rules
- name: RescueGroups.org API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 7
  slug: rescuegroups-org-rules
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 79.1
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/screenshots/rescuegroups-org-2026-06-20T192931.png
security:
- kind: authentication
  name: Rescuegroups Org Authentication
  slug: rescuegroups-org-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Rescuegroups Org Domain Security
  slug: rescuegroups-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rescuegroups-org
tags:
- Animals
- Pet Adoption
- Rescue
- Animal Welfare
website: https://rescuegroups.org/
---
