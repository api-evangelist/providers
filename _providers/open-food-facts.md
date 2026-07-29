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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Food Facts Agentic Access
  operation_count: 7
  slug: open-food-facts-agentic-access
  summary_line: 7 operations
api_count: 5
apis:
- description: The Cgi API from Open Food Facts — 1 operation(s) for cgi.
  name: Open Food Facts Cgi API
  slug: open-food-facts-cgi-api
- description: The Product API from Open Food Facts — 3 operation(s) for product.
  name: Open Food Facts Product API
  slug: open-food-facts-product-api
- description: The Search API from Open Food Facts — 1 operation(s) for search.
  name: Open Food Facts Search API
  slug: open-food-facts-search-api
- description: The Taxonomy API from Open Food Facts — 1 operation(s) for taxonomy.
  name: Open Food Facts Taxonomy API
  slug: open-food-facts-taxonomy-api
- description: The Taxonomy Suggestions API from Open Food Facts — 1 operation(s) for taxonomy suggestions.
  name: Open Food Facts Taxonomy Suggestions API
  slug: open-food-facts-taxonomy-suggestions-api
artifact_total: 12
collections:
- collection_type: open
  name: Open Food Facts API
  slug: open-open-food-facts
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-food-facts-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-food-facts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-food-facts-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openfoodfacts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-food-facts
- group: company
  title: ''
  type: Blog
  url: https://blog.openfoodfacts.org/en/feed/
created: '2025-03-01'
description: Open Food Facts is a food products database made by everyone, for everyone. You can use it to make better food choices, and as it is open data, anyone can re-use it for any purpose.
finops:
- name: Open Food Facts Finops
  service_category: API
  slug: open-food-facts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-food-facts.png
layout: provider
modified: '2026-05-19'
name: Open Food Facts
nav: Providers
network: true
overview: 'Open Food Facts publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cgi API, Product API, Search API, and 2 more.


  Open Food Facts'' developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Open Food Facts Plans Pricing
  plan_count: 3
  slug: open-food-facts-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Open Food Facts Rate Limits
  slug: open-food-facts-rate-limits
score:
  band: thin
  composite: 30.6
  delta: -1.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.5
    developer_ergonomics: 2.2
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-food-facts/refs/heads/main/screenshots/open-food-facts-2026-06-20T190753.png
security:
- kind: domain-security
  name: Open Food Facts Domain Security
  slug: open-food-facts-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Open Food Facts Vulnerability Disclosure
  slug: open-food-facts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-food-facts
---
