---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Affinity Agentic Access
  operation_count: 46
  slug: affinity-agentic-access
  summary_line: 46 operations · 4 acting
api_count: 1
apis:
- description: The legacy Affinity V1 API provides comprehensive read and write access to core CRM data including persons, organizations, opportunities, lists, notes, interactions, reminders, and webhooks. It uses H
  name: Affinity API V1
  slug: affinity-api-v1
- description: Operations about auths
  name: Affinity auth API
  slug: affinity-auth-api
- description: Operations about companies
  name: Affinity companies API
  slug: affinity-companies-api
- description: Operations about company merges
  name: Affinity companyMerges API
  slug: affinity-companymerges-api
- description: Operations about emails
  name: Affinity emails API
  slug: affinity-emails-api
- description: Operations about lists
  name: Affinity lists API
  slug: affinity-lists-api
- description: Operations about meetings
  name: Affinity meetings API
  slug: affinity-meetings-api
- description: Operations about notes
  name: Affinity notes API
  slug: affinity-notes-api
- description: Operations about opportunities
  name: Affinity opportunities API
  slug: affinity-opportunities-api
- description: Operations about person merges
  name: Affinity personMerges API
  slug: affinity-personmerges-api
- description: Operations about persons
  name: Affinity persons API
  slug: affinity-persons-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Affinity API v2 auth API
  slug: open-affinity-auth-api
- collection_type: open
  name: Affinity API v2 auth companies API
  slug: open-affinity-companies-api
- collection_type: open
  name: Affinity API v2 auth companyMerges API
  slug: open-affinity-companymerges-api
- collection_type: open
  name: Affinity API v2 auth emails API
  slug: open-affinity-emails-api
- collection_type: open
  name: Affinity API v2 auth lists API
  slug: open-affinity-lists-api
- collection_type: open
  name: Affinity API v2 auth meetings API
  slug: open-affinity-meetings-api
- collection_type: open
  name: Affinity API v2 auth notes API
  slug: open-affinity-notes-api
- collection_type: open
  name: Affinity API v2 auth opportunities API
  slug: open-affinity-opportunities-api
- collection_type: open
  name: Affinity API v2 auth personMerges API
  slug: open-affinity-personmerges-api
- collection_type: open
  name: Affinity API v2 auth persons API
  slug: open-affinity-persons-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/affinity-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/affinity-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affinity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/affinity-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.affinity.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.affinity.co/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/affinity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/project-affinity
- group: company
  title: ''
  type: Blog
  url: https://www.affinity.co/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.affinity.co/product/affinity-pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.affinity.co/
- group: other
  title: ''
  type: X
  url: https://x.com/affinity
- group: commercial
  title: ''
  type: Plans
  url: plans/affinity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/affinity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/affinity-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/affinity-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/affinity-context.jsonld
created: '2026-06-12'
description: 'Affinity is a relationship intelligence CRM built for private equity, venture capital, and investment banking teams. It provides a REST API that enables developers to manage contacts, organizations, opportunities, lists, notes, and relationship timelines derived from email and calendar activity. The API is available in two versions: a legacy V1 with full read/write capabilities for persons, companies, opportunities, notes, interactions, reminders, and webhooks, and a modern V2 RESTful interface designed for internal apps, automated workflows, and third-party integrations. API access is included in the Scale, Advanced, and Enterprise subscription tiers, with monthly call limits ranging from 100,000 to unlimited depending on the plan.'
examples:
- key_count: 24
  name: Affinity V2 Examples
  slug: affinity-v2-examples
finops:
- name: Affinity Finops
  service_category: ''
  slug: affinity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/affinity.png
json_schemas:
- name: Attendee
  property_count: 2
  slug: affinity-attendee
- name: CompanyData
  property_count: 3
  slug: affinity-companydata
- name: Field
  property_count: 5
  slug: affinity-field
- name: FieldValue
  property_count: 0
  slug: affinity-fieldvalue
- name: Grant
  property_count: 3
  slug: affinity-grant
- name: ListEntry
  property_count: 5
  slug: affinity-listentry
- name: Meeting
  property_count: 7
  slug: affinity-meeting
- name: notes.Note
  property_count: 0
  slug: affinity-note
- name: Opportunity
  property_count: 3
  slug: affinity-opportunity
- name: Pagination
  property_count: 2
  slug: affinity-pagination
- name: PersonData
  property_count: 5
  slug: affinity-persondata
- name: Tenant
  property_count: 3
  slug: affinity-tenant
- name: User
  property_count: 4
  slug: affinity-user
- name: WhoAmI
  property_count: 3
  slug: affinity-whoami
jsonld:
- class_count: 50
  name: Affinity Context
  property_count: 14
  slug: affinity-context
layout: provider
modified: '2026-06-12'
name: Affinity
nav: Providers
network: true
overview: 'Affinity publishes 10 APIs on the [APIs.io](https://apis.io/) network, including auth API, companies API, companyMerges API, and 7 more. Tagged areas include CRM, Relationship Intelligence, Private Equity, Venture Capital, and Contacts.


  The Affinity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Affinity''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Affinity Plans Pricing
  plan_count: 4
  slug: affinity-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Affinity Rate Limits
  slug: affinity-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Affinity API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: affinity-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 31.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 67.5
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/affinity/refs/heads/main/screenshots/affinity-2026-06-20T165626.png
security:
- kind: authentication
  name: Affinity Authentication
  slug: affinity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Affinity Domain Security
  slug: affinity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Affinity Trust Center
  slug: affinity-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: affinity
tags:
- CRM
- Relationship Intelligence
- Private Equity
- Venture Capital
- Contacts
- Organization
- Opportunities
- Deal Management
website: https://www.affinity.co/
---
