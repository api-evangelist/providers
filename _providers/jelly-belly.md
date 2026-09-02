---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jelly Belly Agentic Access
  operation_count: 10
  slug: jelly-belly-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: The Jelly Belly Wiki API is a community-built, read-only REST API that provides detailed information about Jelly Belly beans, including flavor details, facts, milestones, and recipes. It is designed a
  name: Jelly Belly Wiki API
  slug: jelly-belly-wiki-api
- description: The Beans API from Jelly Belly — 2 operation(s) for beans.
  name: Jelly Belly Beans API
  slug: jelly-belly-beans-api
- description: The Combinations API from Jelly Belly — 2 operation(s) for combinations.
  name: Jelly Belly Combinations API
  slug: jelly-belly-combinations-api
- description: The Facts API from Jelly Belly — 2 operation(s) for facts.
  name: Jelly Belly Facts API
  slug: jelly-belly-facts-api
- description: The MileStones API from Jelly Belly — 2 operation(s) for milestones.
  name: Jelly Belly MileStones API
  slug: jelly-belly-milestones-api
- description: The Recipes API from Jelly Belly — 2 operation(s) for recipes.
  name: Jelly Belly Recipes API
  slug: jelly-belly-recipes-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jelly Belly Wiki Beans API
  slug: open-jelly-belly-beans-api
- collection_type: open
  name: Jelly Belly Wiki Beans Combinations API
  slug: open-jelly-belly-combinations-api
- collection_type: open
  name: Jelly Belly Wiki Beans Facts API
  slug: open-jelly-belly-facts-api
- collection_type: open
  name: Jelly Belly Wiki Beans MileStones API
  slug: open-jelly-belly-milestones-api
- collection_type: open
  name: Jelly Belly Wiki Beans Recipes API
  slug: open-jelly-belly-recipes-api
- collection_type: open
  name: Jelly Belly Wiki API
  slug: open-jelly-belly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jelly-belly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jelly-belly-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jelly-belly-candy-company
- group: company
  title: ''
  type: Website
  url: https://www.jellybelly.com/
- group: company
  title: ''
  type: About
  url: https://www.jellybelly.com/our-heritage
- group: other
  title: ''
  type: VisitorCenter
  url: https://www.jellybelly.com/visitor-center
- group: learn
  title: ''
  type: Recipes
  url: https://www.jellybelly.com/beanspiration
- group: other
  title: ''
  type: WhereToBuy
  url: https://www.jellybelly.com/where-to-buy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jellybelly.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jellybelly.com/terms-use
- group: other
  title: ''
  type: Accessibility
  url: https://www.jellybelly.com/accessibility
created: '2024-11-14'
description: Jelly Belly is the iconic American gourmet jelly bean candy company, owned by Ferrara Candy Company, known for its signature flavor assortments, themed collections, and historical association with American culture. This repository indexes the company's web properties and the community Jelly Belly Wiki API which catalogs Jelly Belly beans, flavors, recipes, facts, and milestones.
finops:
- name: Jelly Belly Finops
  service_category: API
  slug: jelly-belly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jelly-belly.png
layout: provider
modified: '2026-04-28'
name: Jelly Belly
nav: Providers
network: true
overview: Jelly Belly publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Beans API, Combinations API, Facts API, and 2 more. Tagged areas include Beans, Candy, Confectionery, Food, and Jelly Beans.
plans:
- name: Jelly Belly Plans Pricing
  plan_count: 3
  slug: jelly-belly-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Jelly Belly Rate Limits
  slug: jelly-belly-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 65.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 0.0
    contract_quality: 46.1
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jelly-belly/refs/heads/main/screenshots/jelly-belly-2026-06-20T183718.png
security:
- kind: domain-security
  name: Jelly Belly Domain Security
  slug: jelly-belly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jelly-belly
tags:
- Beans
- Candy
- Confectionery
- Food
- Jelly Beans
- Recipes
website: https://www.jellybelly.com/
---
