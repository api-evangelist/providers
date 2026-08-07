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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bizapi Agentic Access
  operation_count: 2
  slug: bizapi-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Search for business entity firmographic data
  name: BizAPI Company Search API
  slug: bizapi-company-search-api
artifact_total: 29
collections:
- collection_type: open
  name: BizAPI Business Intelligence API
  slug: open-bizapi-business-intelligence-api
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
  type: Signup
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
modified: '2026-05-19'
name: BizAPI
nav: Providers
network: true
overview: 'BizAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Company Search API. Tagged areas include Business Intelligence, Company Data, CRM, Firmographic Data, and NAICS.


  The BizAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BizAPI''s developer surface includes authentication, documentation, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Bizapi Plans Pricing
  plan_count: 3
  slug: bizapi-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Bizapi Rate Limits
  slug: bizapi-rate-limits
rules:
- name: BizAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bizapi-jsonschema-spectral-rules
- name: BizAPI API Rules
  rule_count: 35
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 17
  slug: bizapi-spectral-rules
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 79.1
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
