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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Food Facts Agentic Access
  operation_count: 7
  slug: open-food-facts-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Cgi API from Open Food Facts — 1 operation(s) for cgi.
  name: Open Food Facts Cgi API
  slug: open-food-facts-cgi-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Product API from Open Food Facts — 3 operation(s) for product.
  name: Open Food Facts Product API
  slug: open-food-facts-product-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Search API from Open Food Facts — 1 operation(s) for search.
  name: Open Food Facts Search API
  slug: open-food-facts-search-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Taxonomy API from Open Food Facts — 1 operation(s) for taxonomy.
  name: Open Food Facts Taxonomy API
  slug: open-food-facts-taxonomy-api
- baseURL: https://world.openfoodfacts.org
  baseurl_source: spec
  description: The Taxonomy Suggestions API from Open Food Facts — 1 operation(s) for taxonomy suggestions.
  name: Open Food Facts Taxonomy Suggestions API
  slug: open-food-facts-taxonomy-suggestions-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Food Facts Cgi API
  slug: open-open-food-facts-cgi-api
- collection_type: open
  name: Open Food Facts Cgi Product API
  slug: open-open-food-facts-product-api
- collection_type: open
  name: Open Food Facts Cgi Search API
  slug: open-open-food-facts-search-api
- collection_type: open
  name: Open Food Facts Cgi Taxonomy API
  slug: open-open-food-facts-taxonomy-api
- collection_type: open
  name: Open Food Facts Cgi Taxonomy Suggestions API
  slug: open-open-food-facts-taxonomy-suggestions-api
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
random_paper: 7
rate_limits:
- limit_count: 5
  name: Open Food Facts Rate Limits
  slug: open-food-facts-rate-limits
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.8
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 18.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
