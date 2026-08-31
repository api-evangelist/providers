---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Uplead Agentic Access
  operation_count: 21
  slug: uplead-agentic-access
  summary_line: 21 operations · 11 acting
api_count: 1
apis:
- description: Account and credit management.
  name: UpLead Account API
  slug: uplead-account-api
- description: Combined person and company lookup.
  name: UpLead Combined API
  slug: uplead-combined-api
- description: Company search and enrichment operations.
  name: UpLead Company API
  slug: uplead-company-api
- description: Contact list management operations.
  name: UpLead Lists API
  slug: uplead-lists-api
- description: Person/contact search and enrichment operations.
  name: UpLead Person API
  slug: uplead-person-api
- description: Prospector search operations for discovering contacts.
  name: UpLead Prospector API
  slug: uplead-prospector-api
- description: Reference data lookups.
  name: UpLead Reference API
  slug: uplead-reference-api
- description: General search operations.
  name: UpLead Search API
  slug: uplead-search-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UpLead Account API
  slug: open-uplead-account-api
- collection_type: open
  name: UpLead Account Combined API
  slug: open-uplead-combined-api
- collection_type: open
  name: UpLead Account Company API
  slug: open-uplead-company-api
- collection_type: open
  name: UpLead Account Lists API
  slug: open-uplead-lists-api
- collection_type: open
  name: UpLead Account Person API
  slug: open-uplead-person-api
- collection_type: open
  name: UpLead Account Prospector API
  slug: open-uplead-prospector-api
- collection_type: open
  name: UpLead Account Reference API
  slug: open-uplead-reference-api
- collection_type: open
  name: UpLead Account Search API
  slug: open-uplead-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uplead-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uplead-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uplead-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uplead.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uplead.com/
- group: company
  title: ''
  type: Blog
  url: https://www.uplead.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uplead.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uplead.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uplead-com/
- group: other
  title: ''
  type: X
  url: https://x.com/UpLeadHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/uplead-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uplead-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uplead-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/uplead-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uplead-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uplead-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uplead-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uplead-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uplead-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uplead-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.uplead.com/en/collections/19646601-release-notes
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uplead-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.uplead.com/data-api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.uplead.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.uplead.com/getting-started-with-uplead/
- group: operate
  title: ''
  type: Support
  url: https://support.uplead.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.uplead.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uplead.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uplead.com/privacy/
created: '2026-06-13'
description: UpLead is a B2B contact and company data platform providing a REST API for searching leads, verifying emails, accessing company profiles, and enriching contact information. The API enables developers to look up verified contacts by email or name, search companies by domain or name, run prospector queries to find contacts by job title or function, and perform combined person-plus-company lookups in a single call. UpLead operates on a credit-based billing model where charges only apply when verified data is returned.
examples:
- key_count: 2
  name: Company Search Response
  slug: company-search-response
- key_count: 2
  name: Credits Response
  slug: credits-response
- key_count: 2
  name: Person Search Response
  slug: person-search-response
- key_count: 7
  name: Prospector Search Request
  slug: prospector-search-request
- key_count: 3
  name: Prospector Search Response
  slug: prospector-search-response
finops:
- name: Uplead Finops
  service_category: ''
  slug: uplead-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uplead.png
json_schemas:
- name: UpLead Company
  property_count: 32
  slug: company
- name: UpLead Contact List
  property_count: 3
  slug: list
- name: UpLead Person
  property_count: 20
  slug: person
jsonld:
- class_count: 42
  name: Uplead Context
  property_count: 13
  slug: uplead-context
layout: provider
modified: '2026-08-13'
name: UpLead
nav: Providers
network: true
overview: 'UpLead publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Combined API, Company API, and 5 more. Tagged areas include B2B, Lead Generation, Contact Data, Company Data, and Email Verification.


  The UpLead catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UpLead''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 23 more developer resources.'
plans:
- name: Uplead Plans Pricing
  plan_count: 6
  slug: uplead-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Uplead Rate Limits
  slug: uplead-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: UpLead API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uplead-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 27
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 14.4
    contract_quality: 62.1
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 14.4
    operational_transparency: 52.6
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uplead/refs/heads/main/screenshots/uplead-2026-06-20T200445.png
security:
- kind: authentication
  name: Uplead Authentication
  slug: uplead-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uplead Domain Security
  slug: uplead-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uplead
tags:
- B2B
- Lead Generation
- Contact Data
- Company Data
- Email Verification
- Data Enrichment
- Sales Intelligence
website: https://www.uplead.com/
---
