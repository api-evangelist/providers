---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Confident Lims Agentic Access
  operation_count: 45
  slug: confident-lims-agentic-access
  summary_line: 45 operations · 17 acting
api_count: 3
apis:
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: Client organization information
  name: Confident LIMS Client Info API
  slug: confident-lims-client-info-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: Client relationship management
  name: Confident LIMS Clients API
  slug: confident-lims-clients-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: Lab organization information
  name: Confident LIMS Lab Info API
  slug: confident-lims-lab-info-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: View associated labs
  name: Confident LIMS Labs API
  slug: confident-lims-labs-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: Order lifecycle state transitions
  name: Confident LIMS Order Status API
  slug: confident-lims-order-status-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: View orders and order details
  name: Confident LIMS Orders API
  slug: confident-lims-orders-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: Reference data for sample metadata
  name: Confident LIMS Reference Data API
  slug: confident-lims-reference-data-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: Upload sample images and documents
  name: Confident LIMS Sample Files API
  slug: confident-lims-sample-files-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: View samples and test results
  name: Confident LIMS Samples API
  slug: confident-lims-samples-api
- baseURL: https://api.confidentcannabis.com
  baseurl_source: declared
  description: Submit and manage test results
  name: Confident LIMS Test Results API
  slug: confident-lims-test-results-api
arazzos:
- description: A testing client confirms identity, lists recently changed orders, and pulls the finalized sample details for the first order (read-only client credentials).
  name: Confident LIMS — client results sync
  slug: confident-lims-client-results-sync
- description: A lab creates an order for a testing client, verifies it into the workflow, submits test results for a sample, attaches the COA, and completes the order.
  name: Confident LIMS — lab order to finalized results
  slug: confident-lims-lab-order-to-results
artifact_total: 32
asyncapis:
- description: ''
  name: Confident Lims Webhooks
  slug: confident-lims-webhooks
collections:
- collection_type: open
  name: Clients Client Info API
  slug: open-confident-lims-client-info-api
- collection_type: open
  name: Client Info Clients API
  slug: open-confident-lims-clients-api
- collection_type: open
  name: Clients Client Info Lab Info API
  slug: open-confident-lims-lab-info-api
- collection_type: open
  name: Clients Client Info Labs API
  slug: open-confident-lims-labs-api
- collection_type: open
  name: Clients Client Info Order Status API
  slug: open-confident-lims-order-status-api
- collection_type: open
  name: Clients Client Info Orders API
  slug: open-confident-lims-orders-api
- collection_type: open
  name: Clients Client Info Reference Data API
  slug: open-confident-lims-reference-data-api
- collection_type: open
  name: Clients Client Info Sample Files API
  slug: open-confident-lims-sample-files-api
- collection_type: open
  name: Clients Client Info Samples API
  slug: open-confident-lims-samples-api
- collection_type: open
  name: Clients Client Info Test Results API
  slug: open-confident-lims-test-results-api
common:
- group: other
  href: https://artifacts.apis.io/confident-lims/capabilities/confident-lims-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/confident-lims-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/confident-lims/plans/confident-lims-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/confident-lims-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.confidentlims.com/
- group: other
  href: https://artifacts.apis.io/confident-lims/overlays/confident-lims-clients-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confident-lims-clients-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://confidentlims.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://confidentlims.readme.io/reference
- group: docs
  title: ''
  type: APIReference
  url: https://confidentlims.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.confidentlims.com/products/api
- group: operate
  title: ''
  type: Support
  url: https://help.confidentlims.com/
- group: company
  title: ''
  type: Blog
  url: https://www.confidentlims.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.confidentcannabis.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confidentlims.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.confidentlims.com/register
- group: start
  title: ''
  type: Login
  url: https://accounts.confidentlims.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.confidentlims.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confidentlims.com/privacy
- group: auth
  href: https://artifacts.apis.io/confident-lims/conformance/confident-lims-conformance.yml
  title: ''
  type: Compliance
  url: conformance/confident-lims-conformance.yml
- group: auth
  href: https://artifacts.apis.io/confident-lims/authentication/confident-lims-authentication.yml
  title: ''
  type: Authentication
  url: authentication/confident-lims-authentication.yml
- group: design
  href: https://artifacts.apis.io/confident-lims/conventions/confident-lims-conventions.yml
  title: ''
  type: Conventions
  url: conventions/confident-lims-conventions.yml
- group: design
  href: https://artifacts.apis.io/confident-lims/errors/confident-lims-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/confident-lims-problem-types.yml
- group: design
  href: https://artifacts.apis.io/confident-lims/data-model/confident-lims-data-model.yml
  title: ''
  type: DataModel
  url: data-model/confident-lims-data-model.yml
- group: design
  href: https://artifacts.apis.io/confident-lims/lifecycle/confident-lims-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/confident-lims-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/confident-lims/conformance/confident-lims-conformance.yml
  title: ''
  type: Conformance
  url: conformance/confident-lims-conformance.yml
- group: agent
  href: https://artifacts.apis.io/confident-lims/mcp/confident-lims-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/confident-lims-mcp.yml
- group: agent
  href: https://artifacts.apis.io/confident-lims/llms/confident-lims-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/confident-lims-llms.txt
- group: design
  href: https://artifacts.apis.io/confident-lims/asyncapi/confident-lims-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/confident-lims-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/confident-lims/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/confident-lims/agentic-access/confident-lims-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/confident-lims-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/confident-lims/security/confident-lims-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/confident-lims-domain-security.yml
- group: design
  href: https://artifacts.apis.io/confident-lims/arazzo/confident-lims-lab-order-to-results.yml
  title: ''
  type: Arazzo
  url: arazzo/confident-lims-lab-order-to-results.yml
- group: design
  href: https://artifacts.apis.io/confident-lims/arazzo/confident-lims-client-results-sync.yml
  title: ''
  type: Arazzo
  url: arazzo/confident-lims-client-results-sync.yml
created: '2026-07-17'
description: Confident LIMS (CC Software LLC, formerly Confident Cannabis, founded 2015) is a cloud-based Laboratory Information Management System for high-velocity analytical testing labs and their testing clients. It manages samples from accession through workflow, results, and reporting, automates regulatory compliance (ISO 17025, TNI/NELAP, SOC 2, FDA 21 CFR Part 11), and gives clients a self-service ordering and results portal. It serves cannabis, food & beverage, agriculture, nutraceuticals, cosmetics, environmental, industrial chemicals, and oil & gas labs. The Confident Cannabis REST API (v0, api.confidentcannabis.com) exposes labs, clients, and shared reference data with API-key + HMAC-SHA256 request signing and result webhooks.
finops:
- has_sources: true
  method: derived
  name: Confident Lims Finops
  primary_unit: tier fee / month
  service_category: ''
  slug: confident-lims-finops
  template: false
image: https://files.readme.io/ebcaf628c1535f1f7354303ab5d660f8ee74c181042849f2f2954f5c025a3e1d-Brand_Symbol.svg
layout: provider
modified: '2026-07-18'
name: Confident LIMS
nav: Providers
network: true
overview: 'Confident LIMS publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Client Info API, Clients API, Lab Info API, and 7 more. Tagged areas include Company, LIMS, Laboratory Information Management, Analytical Testing, and Cannabis Testing.


  The Confident LIMS catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Confident LIMS''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Confident Lims Plans Pricing
  plan_count: 24
  slug: confident-lims-plans-pricing
- name: Confident Lims Price Estimates
  plan_count: 0
  slug: confident-lims-price-estimates
random_paper: 20
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 61.2
    developer_ergonomics: 58.9
    discoverability: 71.4
    operational_transparency: 13.2
  previous_composite: 50.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/confident-lims/confident-lims-2026-07-25T210248.png
security:
- kind: authentication
  name: Confident Lims Authentication
  slug: confident-lims-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Confident Lims Domain Security
  slug: confident-lims-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Onboard a testing client and create an order
  slug: confident-lims-create-order
- name: Retrieve your orders, samples, and results as a testing client
  slug: confident-lims-retrieve-client-results
- name: Submit lab test results for a sample
  slug: confident-lims-submit-test-results
slug: confident-lims
tags:
- Company
- LIMS
- Laboratory Information Management
- Analytical Testing
- Cannabis Testing
- Compliance
- Sample Management
- Lab Software
website: https://www.confidentlims.com/
---
