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
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bizapi Agentic Access
  operation_count: 2
  slug: bizapi-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Real-time business data append API. Submit a partial business record — company name and address, phone, website or DUNS number — and BizAPI matches it against the Dun & Bradstreet business database, r
  name: BizAPI Company Search API
  slug: bizapi-company-search-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BizAPI Business Intelligence API
  slug: open-bizapi-business-intelligence-api
- collection_type: open
  name: BizAPI Business Intelligence Company Search API
  slug: open-bizapi-company-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bizapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bizapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bizapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.naics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.naics.com/business-intelligence-api/
- group: start
  title: ''
  type: SignUp
  url: https://www.naics.com/bizapi-details/
- group: auth
  title: ''
  type: Authentication
  url: https://www.naics.com/business-intelligence-api/
- group: design
  title: ''
  type: SpectralRules
  url: rules/bizapi-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bizapi-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.naics.com/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.naics.com/business-intelligence-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.naics.com/wp-content/uploads/2021/09/BizAPI-V2-Documentation.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://www.naics.com/business-intelligence-api/bizapi-documents/
- group: build
  title: ''
  type: Postman
  url: https://www.naics.com/wp-content/uploads/2021/09/NAICS-BizAPI-V2-Examples.postman_collection.json_.zip
- group: operate
  title: ''
  type: Support
  url: https://www.naics.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.naics.com/data-layouts-pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.naics.com/privacypolicy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.naics.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/bizapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bizapi-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bizapi-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bizapi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bizapi-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bizapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bizapi-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bizapi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2025-02-24'
description: BizAPI is a real-time Business Intelligence API from the NAICS Association that provides firmographic data on over 220 million US and international business entities. It enables businesses to enrich CRM records, power customer acquisition workflows, and append NAICS codes, SIC codes, DUNS numbers, company details, sales volume, employee counts, and corporate hierarchy information to any business record via a simple REST API.
examples:
- key_count: 34
  name: Bizapi Company Example
  slug: bizapi-company-example
features:
- description: Returns live firmographic data on over 220 million US and international business entities in real time.
  name: Real-Time Firmographic Data
- description: Provides 6-digit NAICS codes and 4- and 8-digit SIC codes for industry classification of business entities.
  name: NAICS and SIC Classification
- description: Returns D&B DUNS numbers enabling universal business entity identification and credit data linkage.
  name: DUNS Number Lookup
- description: Exposes parent, domestic ultimate, and global ultimate company relationships with DUNS and name fields.
  name: Corporate Hierarchy
- description: Designed to integrate with CRMs, SFAs, and internal systems to append firmographic data to business records.
  name: CRM Enrichment
- description: Includes a /cosearchtest endpoint that returns fake data without consuming API credits for development and testing.
  name: Sandbox Test Endpoint
finops:
- name: Bizapi Finops
  service_category: API
  slug: bizapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bizapi.png
integrations:
- description: Integrate BizAPI with Salesforce CRM to auto-append firmographic data to account and lead records.
  name: Salesforce
- description: Enrich HubSpot company records with NAICS, SIC, DUNS, and financial indicators via BizAPI.
  name: HubSpot
- description: Append industry classification and company size data to Marketo lead records for segmentation and scoring.
  name: Marketo
- description: Connect BizAPI to Dynamics 365 to surface firmographic context on accounts and contacts.
  name: Microsoft Dynamics
json_schemas:
- name: BizAPI Company
  property_count: 34
  slug: bizapi-company
json_structures:
- name: Bizapi Company Structure
  property_count: 34
  slug: bizapi-company-structure
jsonld:
- class_count: 34
  name: Bizapi Context
  property_count: 0
  slug: bizapi-context
layout: provider
modified: '2026-08-14'
name: BizAPI
nav: Providers
network: true
overview: 'BizAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Company Search API. Tagged areas include Business Intelligence, Company Data, CRM, Firmographic Data, and NAICS.


  The BizAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BizAPI''s developer surface includes authentication, documentation, signup flow, engineering blog, API reference, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Bizapi Plans Pricing
  plan_count: 0
  slug: bizapi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Bizapi Rate Limits
  slug: bizapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BizAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bizapi-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  name: BizAPI API Rules
  rule_count: 35
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 17
  slug: bizapi-spectral-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 29
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 33.3
    contract_quality: 72.1
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 21.1
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bizapi/refs/heads/main/screenshots/bizapi-2026-06-20T173328.png
security:
- kind: authentication
  name: Bizapi Authentication
  slug: bizapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bizapi Domain Security
  slug: bizapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bizapi
tags:
- Business Intelligence
- Company Data
- CRM
- Firmographic Data
- NAICS
- SIC
use_cases:
- description: Append NAICS codes, DUNS numbers, employee counts, and sales volume to company records in CRM and SFA systems.
  name: CRM Data Enrichment
- description: Identify and qualify business prospects by searching firmographic data to match against target industry and size criteria.
  name: Customer Acquisition
- description: Analyze business landscapes by querying firmographic data across industries, geographies, and corporate hierarchies.
  name: Market Research
- description: Enrich inbound leads with firmographic attributes to power scoring models that prioritize high-value accounts.
  name: Lead Scoring
- description: Verify business identity, location, and corporate hierarchy for compliance and due diligence workflows.
  name: Compliance Verification
website: https://www.naics.com/
---
